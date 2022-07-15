from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, nickname, password=None):
        """
        Creates and saves a User with the given email,
        username(ID), name, date of birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an name')
        if not nickname:
            raise ValueError('Users must have an nickname')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password=None):
        """
        Creates and saves a superuser with the given email,
        username(ID), name, date of birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(verbose_name='name', max_length=40, null=False, blank=False)
    nickname = models.CharField(verbose_name='nickname', max_length=30, null=False, blank=False)
    thumbnail = models.CharField(max_length=256, default='default.jpg', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return self.nickname

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
        db_table = 'users'
