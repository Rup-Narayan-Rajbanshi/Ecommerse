from django.db import models
from helpers.models import BaseModel

class Address(BaseModel):
    country = models.CharField(max_length=30, default='', blank=True)
    state = models.CharField(max_length=30, default='', blank=True)
    district = models.CharField(max_length=30, default='', blank=True)
    city = models.CharField(max_length=30, default='', blank=True)
    address = models.CharField(max_length=30, default='', blank=True)
    zip_code = models.CharField(max_length=30, default='', blank=True)

    class Meta:
        db_table = 'address'

    def __str__(self):

        return self.city+" , "+ self.district +" , "+self.state 
