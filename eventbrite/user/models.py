from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'gender', 'city', 'country']

    

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_permissions_set'
    )

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    DISCOUNT_ID=models.IntegerField()
                              
    INTERESTS_ID=list()
    EVENT_CREATED=list()
    TICKETS_ID=list()
    FOLLOWERS=list()

  
    
    
class Interests(models.Model):
  ID=models.IntegerField()
  TYPE=models.CharField(max_length=20)
  Name=models.CharField(max_length=20)
  user_id=models.IntegerField()
  sub_category_id=models.IntegerField()