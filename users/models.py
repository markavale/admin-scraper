from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
# Validation
from django.core.validators import RegexValidator
from rest_framework.authtoken.models import Token
# import datetime # It could use for computing Age of users


# REGEX FOR STRING COMBINATIONS
USERNAME_REGEX = '^[a-za-z0-9]+$'
CP_NUMBER_REGEX = '^(09|\+639)\d{9}$'
NAME_REGEX = '^[a-zA-Z ]+$'

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric or contain numbers and lowercaps',
                           code='invalid_username'
                           )],
        unique=True
    )
    first_name              = models.CharField(max_length=255, blank=True, null=True)
    last_name               = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='default.jpg',
                              upload_to='avatar', null=True, blank=True)
    gender = models.CharField(
        max_length=10, blank=True, null=True, choices=GENDER_CHOICES, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    verified            = models.BooleanField(default=False)
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)
    admin               = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username            

    def get_total_user(self):
        return self.User.objects.all().count()

    def get_user_type(self):
        if self.admin:
            return "Admin"
        if self.staff:
            return "Staff"
        if self.active:
            return "User"

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    # def get_first_name(self):
    #     if self.first_name:
    #         return self.first_name
    #     return self.username

    # def get_last_name(self):
    #     if self.last_name:
    #         return self.last_name
    #     return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/default.jpg'

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    # @property
    # def is_active(self):
    #     return self.active
    
    @property
    def is_verified(self):
        return self.verified
