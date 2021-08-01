from django.contrib import admin
from company.models.company import Company, CompanyUser

# Register your models here.
admin.site.register(Company)

admin.site.register(CompanyUser)
