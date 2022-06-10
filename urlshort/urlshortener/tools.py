import random
import string
from django.conf import settings


def createRandomLink():
    """
    Creates a random string with the predetermined size
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(settings.SIZE))
