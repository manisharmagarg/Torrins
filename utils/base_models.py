# Django imports
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    """
    All models extend from this model
    """
    created_by = models.ForeignKey(
        User,
        null=True, blank=True, 
        related_name='%(app_label)s_%(class)s_created_by',
        on_delete=models.SET_NULL
    )
    updated_by = models.ForeignKey(
        User,
        null=True, blank=True, 
        related_name='%(app_label)s_%(class)s_updated_by',
        on_delete=models.SET_NULL
    )
    deleted_by = models.ForeignKey(
        User,
        related_name='%(app_label)s_%(class)s_deleted_by',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True