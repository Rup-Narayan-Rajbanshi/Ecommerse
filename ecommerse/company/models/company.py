import os
import shortuuid
import uuid
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from commonapp.models.image import Image
from commonapp.models.category import Category
from account.models.user import User
from commonapp.models.address import Address
from helpers.validators import image_validator, phone_number_validator, is_numeric_value
from helpers.models import BaseModel
from helpers.constants import MAX_LENGTHS

class Company(BaseModel):
    name = models.CharField(max_length=MAX_LENGTHS['NAME'])
    address = models.ForeignKey(Address,on_delete=models.PROTECT, null=True, blank=False)
    opens_at = models.TimeField(null=True)
    closes_at = models.TimeField(null=True)
    logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,\
        related_name="company")
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT,\
        related_name="company", blank=True, null=True)
    images = GenericRelation(Image)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, \
        validators= [phone_number_validator, is_numeric_value])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_affiliate = models.BooleanField(default=False)
    service_charge = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    vat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    currency = models.CharField(max_length=10)
    invoice_counter = models.PositiveIntegerField(default=0, editable=False)
    description = models.TextField(blank=True, null=True)
    pan_number  = models.CharField(max_length=16, default='')

    class Meta:
        db_table = 'company'
        verbose_name_plural = "companies"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CompanyUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_user')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='company_user')
    is_staff = models.BooleanField(default=True)
    is_obsolete = models.BooleanField(default=False)

    class Meta:
        db_table = 'company_user'
        verbose_name_plural = 'company users'
        ordering = ['-created_at']

    def __str__(self):
        return self.user.full_name
