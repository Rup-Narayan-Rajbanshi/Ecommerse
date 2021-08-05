from django.contrib import admin
from company.models.company import Company, CompanyUser

from django.contrib.auth.models import Group

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if obj.pk:
            if obj.is_verified == True:
                company_user = CompanyUser.objects.filter(company=obj).first().update(is_active=True)
                user = company_user.user
                owner_group, _ = Group.objects.get_or_create(name='owner')
                user.group.add(owner_group)
                user.save()

        super().save_model(request, obj, form, change)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyUser)
