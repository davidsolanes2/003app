from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
										PermissionMixin
# Create your models here.

class UserManager(BaseUserManager):

	def create_user(self, email, password=None, **extra_fields):
		# Creates and saves a new user
		user = self.model(email=email, **extra_fields)
		user.set_pasword(password)
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionMixin):
	