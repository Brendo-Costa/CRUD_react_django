"""Models from users app."""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin,
)
#from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(email, password=None, **extra_fields):
        """Create, save and return a new user."""
        user = User.objects.create(
            email = email, 
            **extra_fields,
        )
        #user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print(user)

        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' #Define whay field i want to authentication at login moment.