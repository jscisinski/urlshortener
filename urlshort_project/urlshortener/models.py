from django.db import models, transaction
from psycopg2._psycopg import IntegrityError

from .tools import createRandomLink


class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return self.short_url

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        # https://docs.djangoproject.com/en/3.2/ref/models/instances/#customizing-model-loading
        # if self._state.adding is True is a new instance - must set shorten link
        if self._state.adding is True:
            counter = 0
            while True:
                counter += 1
                if counter > 1000:
                    raise RuntimeError('Cannot set campaign_octi_id.')
                try:
                    self.short_url = createRandomLink()
                    with transaction.atomic():
                        super().save(*args, **kwargs)
                    break
                except IntegrityError as e:
                    # 23505 is exact error if we have same short link generated
                    if e.__cause__.diag.sqlstate == '23505':
                        continue
                    else:
                        raise e
        else:
            super().save(*args, **kwargs)
