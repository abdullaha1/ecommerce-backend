from django.db import models
import uuid


class Base(models.Model):
    """
    This model will b used as a base model for all classes
    """
    id = models.UUIDField(unique=True, default=uuid.uuid4,primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="%(class)s_updated_by"
    )

    class Meta:
        abstract = True