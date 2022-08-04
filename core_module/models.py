from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
import uuid
from random import randint
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        # user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name           = models.CharField(verbose_name="Full name", max_length=20, null=True)
    unique_id                = models.UUIDField(verbose_name="Unique ID",unique=True, default=randint(100000,999999), editable=False, db_index=True)
    email               = models.EmailField( verbose_name="email", max_length=60, unique=True)
    is_email_verified   = models.BooleanField(default=False)
    username            = models.CharField(max_length=20, unique=True, null=True)
    address             = models.CharField(max_length=100, null=True)
    phone_number        = models.PositiveIntegerField(null=True)
    is_phone_verified   = models.BooleanField(default=False)

    joined_date   = models.DateTimeField(verbose_name="Joined date",auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name="Last Login", auto_now = True)
    is_admin      = models.BooleanField(default = False)
    is_active     = models.BooleanField(default = True)
    is_staff      = models.BooleanField(default = False)
    is_superuser  = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    required_fields = [
        'username',
        'full_name',
        'phone_number',
    ]

    objects = UserManager()

    def __str__(self):
        return f'{self.full_name} , {self.username}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    