from django.contrib import admin
from commonapp.models.category import Category
from commonapp.models.address  import Address
# Register your models here.

admin.site.register(Category)
admin.site.register(Address)