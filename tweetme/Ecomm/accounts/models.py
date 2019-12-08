# from django.db import models
# from django.contrib.auth.models import (AbstractUser,BaseUserManager)
# from django.contrib.auth.mixins import PermissionRequiredMixin
#
# # Create your models here.
# class Myusermanager(BaseUserManager):
#     def create_user(self,email,username,password=None,is_staff=True,is_admin=False,is_active=True):
#         if not email:
#             raise ValueError("User must have email")
#         if not password:
#             raise ValueError("user must have password")
#         if not username:
#             raise ValueError("user must have username")
#
#         # email = self.normalize_email(email),
#         user_obj = self.model(
#             email=self.normalize_email(email)
#         )
#         user_obj.username=username
#         user_obj.set_password(password)  # change user password
#         user_obj.staff = is_staff
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.save(using=self._db)
#         return user_obj
#
#     def create_staff(self,email,username,password=None):
#         user=self.create_user(email,
#             username=username,
#             password=password,
#             is_staff=True
#         )
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self,email,username,password=None):
#         user=self.create_user(
#             username,
#             email,
#             password=password,
#             is_staff=True,
#             is_admin=True
#         )
#         user.save(using=self._db)
#         return user
#
#
# class Myuser(AbstractUser):
#     username    =models.CharField(max_length=155,unique=True,verbose_name='Username')
#     email       =models.EmailField(max_length=155,unique=True)
#     active      =models.BooleanField(default=True)
#     staff       =models.BooleanField(default=False)
#     admin       =models.BooleanField(default=False)
#     timestamp   =models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD ="email"
#     REQUIRED_FIELDS = ['username',]
#
#     objects = Myusermanager()
#
#
#     def __str__(self):
#         return str(self.username)
#
#     def get_fullname(self):
#         return str(self.username)
#
#     def get_shortname(self):
#         return str(self.username)
#
#     def has_perm(self,perm,obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#
#     @property
#     def is_staff(self):
#         return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
#
#     @property
#     def is_active(self):
#         return self.active
#
# #
# #
# # # from django.db import models
# # # from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # #
# # #
# # # class MyAccountManager(BaseUserManager):
# # # 	def create_user(self, email, username, password=None):
# # # 		if not email:
# # # 			raise ValueError('Users must have an email address')
# # # 		if not username:
# # # 			raise ValueError('Users must have a username')
# # #
# # # 		user = self.model(
# # # 			email=self.normalize_email(email),
# # # 			username=username,
# # # 		)
# # #
# # # 		user.set_password(password)
# # # 		user.save(using=self._db)
# # # 		return user
# # #
# # #
# # # 	def create_staff(self, email, username, password):
# # # 		user = self.create_user(
# # # 			email=self.normalize_email(email),
# # # 			password=password,
# # # 			username=username,
# # # 		)
# # # 		user.is_admin = True
# # # 		user.is_staff = True
# # # 		user.is_superuser = False
# # # 		user.save(using=self._db)
# # # 		return user
# # #
# # # 	def create_superuser(self, email, username, password):
# # # 		user = self.create_user(
# # # 			email=self.normalize_email(email),
# # # 			password=password,
# # # 			username=username,
# # # 		)
# # # 		user.is_admin = True
# # # 		user.is_staff = True
# # # 		user.is_superuser = True
# # # 		user.save(using=self._db)
# # # 		return user
# # #
# # #
# # # class Account(AbstractBaseUser):
# # # 	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
# # # 	username 				= models.CharField(max_length=30, unique=True)
# # # 	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
# # # 	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
# # # 	is_admin				= models.BooleanField(default=False)
# # # 	is_active				= models.BooleanField(default=True)
# # # 	is_staff				= models.BooleanField(default=False)
# # # 	is_superuser			= models.BooleanField(default=False)
# # #
# # #
# # # 	USERNAME_FIELD = 'email'
# # # 	REQUIRED_FIELDS = ['username']
# # #
# # # 	objects = MyAccountManager()
# # #
# # # 	def __str__(self):
# # # 		return self.email
# # #
# # # 	# For checking permissions. to keep it simple all admin have ALL permissons
# # # 	def has_perm(self, perm, obj=None):
# # # 		return self.is_admin
# # #
# # # 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# # # 	def has_module_perms(self, app_label):
# # # 		return True
# #
# #
# #
