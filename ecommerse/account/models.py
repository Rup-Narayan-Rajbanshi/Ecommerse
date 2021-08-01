# from django.conf import settings
# from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import Group

# from helpers.models import BaseModel
# from helpers.choices import GENDER_CHOICES
# from helpers.constants import DEFAULTS, MAX_LENGTHS
# from helpers.validators import name_validator, is_alphabetic, is_numeric_value


# class UserManager(BaseUserManager):
#     def _create_user(self, first_name, middle_name, last_name, email, phone_number,\
#         password, is_active=True, is_staff=False, is_admin=False):
#         if not first_name:
#             raise ValueError(_("User must have a First name."))

#         if not last_name:
#             raise ValueError(_("User must have a Last name."))

#         if not email:
#             raise ValueError(_("Users must have email address."))

#         if not phone_number:
#             raise ValueError(_("Users must have Phone Number."))

#         if not password:
#             raise ValueError(_("User must have a password."))

#         user_obj = self.model(
#             email=email.lower()
#         )
#         user_obj.first_name = first_name
#         user_obj.middle_name = middle_name
#         user_obj.last_name = last_name
#         user_obj.phone_number = phone_number
#         user_obj.staff = is_staff
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.set_password(password)
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_user(self, first_name, middle_name, last_name, email,\
#         phone_number, password=None):
#         return self._create_user(first_name, middle_name, last_name,\
#             email, phone_number, password)

#     def create_superuser(self, first_name, middle_name, last_name, email,\
#         phone_number, password=None):
#         user = self._create_user(first_name, middle_name, last_name,\
#             email, phone_number, password, is_staff=True, is_admin=True)
#         # assign admin as group
#         user_group, _ = Group.objects.get_or_create(name='user')
#         admin_group, _ = Group.objects.get_or_create(name='admin')
#         user.group.add(user_group, admin_group)
#         user.save()
#         return user


# class User(AbstractBaseUser, BaseModel):
#     first_name = models.CharField(max_length=MAX_LENGTHS['NAME'], validators=[name_validator, is_alphabetic])
#     middle_name = models.CharField(max_length=MAX_LENGTHS['NAME'], validators=[name_validator, is_alphabetic],\
# 									 blank=True, null=False, default = '')
#     last_name = models.CharField(max_length=MAX_LENGTHS['NAME'], validators=[name_validator, is_alphabetic])
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
#     email = models.EmailField(max_length=MAX_LENGTHS['EMAIL'], unique=True)
#     phone_number = models.CharField(max_length=MAX_LENGTHS['PHONE_NUMBER'], unique=True, validators=[is_numeric_value])
#     image = models.ImageField(upload_to='profile/', blank=False, null=True)
#     admin = models.BooleanField(default=False)
#     staff = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     is_obsolete = models.BooleanField(default=False)
#     dob = models.DateField(null=True, blank=True)
#     group = models.ManyToManyField(Group)

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

#     objects = UserManager()

#     class Meta:
#         db_table = 'user'
#         ordering = ['-created_at']
    
#     def __str__(self):
#         return self.full_name

#     def save(self, *args, **kwargs):
#         return super(User, self).save(*args, **kwargs)

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     def to_representation(self, request=None):
#         if self:
#             image = url_builder(self.image, request)
#             return {
#                 "id": self.id,
#                 "first_name": self.first_name,
#                 "middle_name": self.middle_name,
#                 "last_name": self.last_name,
#                 "image": image,
#                 "email": self.email
#             }
#         return None

#     @property
#     def full_name(self):
#         return "%s %s %s" %(self.first_name,self.middle_name, self.last_name)

#     @property
#     def is_staff(self):
#         return self.staff
    
#     @property
#     def is_superuser(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active

