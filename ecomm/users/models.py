import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True)