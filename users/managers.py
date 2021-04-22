from django.contrib.auth.models import BaseUserManager
from django.db.models import Q
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            username=username, 
            email = self.normalize_email(email)
            )
        user.set_password(password)  # change user password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, staff=True, admin=True, password=None):
        user = self.model(
            username=username,
            email= self.normalize_email(email),
            password=password,
        )
        # user.active = active
        user.admin = admin
        user.staff = staff
        user.set_password(password)
        user.save(using=self._db)
        return user
