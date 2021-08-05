from django.contrib import admin
from django import forms
from account.models.user import User
# # Register your models here.

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    # def clean_password(self):
    #     from django.contrib.auth.hashers import make_password
    #     password = self.cleaned_data.get('password')
    #     password = make_password(password)
    #     return password


class AdminUser(admin.ModelAdmin):
    form = UserAdminForm

admin.site.register(User, AdminUser)