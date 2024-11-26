from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import ugettext_lazy as _
# for phone_number field

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        
        email = self.normalize_email(email)
        
        new_user = self.model(email=email, **extra_fields)
        
        new_user.set_password(password)
        
        new_user.save()
        
        return new_user
        
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff as True."))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser as True."))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser must have is_active as True."))
        
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length = 70, unique=True)
    # install phone number fields with this command pip install "django-phonenumber-field[phonenumbers]" and then add it to the installed apps
    phone_number = PhoneNumberField(null=False, unique=True) # use your country code
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f'<User {self.email}'
    
