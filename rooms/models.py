from django.db import models
from core import models as core_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()