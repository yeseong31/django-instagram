from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, name, date_of_birth, password=None):
        """
        Creates and saves a User with the given email,
        username(ID), name, date of birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an user ID')
        if not name:
            raise ValueError('Users must have an name')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email,
        username(ID), name, date of birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=username,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name='user ID', max_length=30, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(verbose_name='name', max_length=40, null=False, blank=False)
    date_of_birth = models.DateField()
    thumbnail = models.CharField(max_length=256, default='default_profile.jpg', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'date_of_birth']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'user'
