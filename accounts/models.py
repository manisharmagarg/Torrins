from django.db import models
from uuid import uuid4

# # Django imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# # Local imports
from .managers import UserManager
import datetime
# from utils.base_model import BaseModel
# # Create your models here.


class Role(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True
    )
    guard_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'role'


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=64, blank=False, null=True)
    last_name = models.CharField(_('last name'), max_length=64, blank=False, null=True)
    email = models.EmailField(_('email address'), max_length=256, unique=True)
    phone = models.CharField(_('phone no'), max_length=100, blank=False, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    email_verified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    two_factor_code = models.CharField(_('two factor code'), max_length=100, blank=False, null=True)
    two_factor_expires_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_verified = models.IntegerField(null=True, blank=True)
    two_factor_secret = models.TextField(_('two factor code'), blank=False, null=True)
    two_factor_recovery_code = models.TextField(_('two factor code'), blank=False, null=True)
    remember_toke = models.CharField(_('two factor code'), max_length=100, blank=False, null=True)
    
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(_('deleted'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['date_joined',]

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
