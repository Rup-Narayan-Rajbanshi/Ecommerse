from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from .models import *
User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in self.fields:
	    	self.fields[field].widget.attrs.update({'class':'input100'})
	
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username,password=password)

		if not user:
			raise forms.ValidationError('The user doesnot exist')
		if not user.check_password(password):
			raise forms.ValidationError('The password is incorrect')
		if not user.is_active:
			raise forms.ValidationError('The user is not active')


class RegisterForm(forms.ModelForm):
	confirm_password=forms.CharField(label='Confirm Password')
	user_category=forms.ModelChoiceField(queryset = Group.objects.all(),
								        required = False,
								        label='User Category',
								        )
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'user_category',
			'password',
			'confirm_password',
			]

	def clean(self,*args,**kwargs):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError('Password must match')

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			]

class UserDetailForm(forms.ModelForm):
	class Meta:
		model = UserDetail
		exclude=('user',)











