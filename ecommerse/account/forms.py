from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from account.models.user import User
# User = get_user_model()

class UserLoginForm(forms.Form):
	phone_number = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	# email = forms.EmailField()

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in self.fields:
	    	self.fields[field].widget.attrs.update({'class':'input100'})
	
	def clean(self, *args, **kwargs):
		phone_number = self.cleaned_data.get('phone_number')
		password = self.cleaned_data.get('password')
		# email = self.cleaned_data.get('email')
		user = authenticate(phone_number=phone_number,password=password)
		print("passed form")

		if not user:
			raise forms.ValidationError('The user doesnot exist')
		if not user.check_password(password):
			raise forms.ValidationError('The password is incorrect')
		if not user.is_active:
			raise forms.ValidationError('The user is not active')


class RegisterForm(forms.ModelForm):
	confirm_password=forms.CharField(label='Confirm Password')
	# user_category=forms.ModelChoiceField(queryset = Group.objects.all(),
	# 							        required = False,
	# 							        label='User Category',
	# 							        )
	class Meta:
		model = User
		fields = [
			'first_name',
			'middle_name',
			'last_name',
			'email',
			'phone_number',
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
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			'email',
			'phone_number',
			'dob',
			'image',
			]


class UserDetailForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("__all__")











