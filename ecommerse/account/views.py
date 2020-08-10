from django.contrib.auth import ( authenticate , get_user_model , login, logout )
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth.views import (
    PasswordChangeView
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from custom_decorators.decorators import *
from apis.views import *

# Create your views here.
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		login(request,user)

		return HttpResponseRedirect(reverse('home'))

	context = {'form':form}
	return render(request,'account/login.html',context=context)

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('account:login'))

def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user_category=form.cleaned_data.get('user_category')
		user.set_password(password)
		user.save()
		if user_category:
			user.groups.add(user_category)

		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)

		return HttpResponseRedirect(reverse('home'))

	context={
		'form':form,
		'form_title':"Register Now"
	}

	return render(request,'account/register.html',context=context)

@login_required
def update_view(request,id):
	instance = get_object_or_404(User,id=id)
	user_instance=UserDetail.objects.filter(user=instance).exists()
	if request.method =='POST':
		form = UpdateUserForm(request.POST, instance=instance)

		# check if user already has its associated userdetail object, if yes update it
		if user_instance == True:
			user_instance=get_object_or_404(UserDetail,user=instance)
			user_form=UserDetailForm(request.POST,instance=user_instance)
		else:
			# if no associated object, save new data
			user_form=UserDetailForm(request.POST)

		if form.is_valid() and user_form.is_valid():
			user=form.save(commit=False)
			user.save()

			user_form=user_form.save(commit=False)
			user_form.user=request.user
			user_form.save()

			return HttpResponseRedirect(reverse('home'))
	else:
		form = UpdateUserForm(instance=instance)

		# check if user already has userdetails
		if user_instance:
			user_instance=get_object_or_404(UserDetail,user=instance)
			print(instance)
			print(user_instance)
			user_form=UserDetailForm(instance=user_instance)
		else:
			# if user has no userdetaiils data open empty form
			user_form=UserDetailForm()

	context={
		'form':form,
		'user_form':user_form
	}
	return render(request,'account/register.html',context=context)

@login_required
def user_detail_view(request,id=None):
	user = get_object_or_404(User,id=id)
	user_detail=get_object_or_404(UserDetail,user=user)
	context={
		'user':user,
		'user_detail':user_detail
	}
	return render(request,'account/profile.html',context=context)



@method_decorator(login_required(), name = "dispatch")
class ChangePassword(PasswordChangeView):
  template_name = "account/register.html"
  success_url = reverse_lazy("home")
  extra_context = {
    "title": "Change Password",
    "form_title":"Change Password"
  }



# @method_decorator(login_required(), name = "dispatch")
# class UserAddView(CreateView,AjaxTemplateMixin):
# 	form_class = RegisterForm
# 	template_name = "account/register.html"

# 	def get_success_url(self):
# 		return reverse('home')

# 	def dispatch(self, request,*args, **kwargs):
# 		if not request.is_ajax():
# 			raise Http404()
# 		else:
# 			return super().dispatch(request,*args, **kwargs)


# 	def forms_valid(self, forms):
# 		user=forms.save(commit=False)
# 		password=forms.cleaned_data.get('password')
# 		user.set_password(password)
# 		user.save()

# 		new_user=authenticate(username=user.username,password=password)
# 		login(request,new_user)

# 		return HttpResponseRedirect(self.get_success_url())













