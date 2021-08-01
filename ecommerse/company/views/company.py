from company.models.company import Company
from company.forms import CompanyRegisterForm, CompanyUpdateForm

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
    FormView, 
    FormMixin,
    CreateView,
    UpdateView,
)
from django.views.generic import DetailView, ListView

# Create your views here.        
class CompanyRegisterView(CreateView):
    model = Company
    form_class = CompanyRegisterForm
    template_name = 'company/add.html'

    def get_success_url(self):
        return reverse('company:company-detail', kwargs={'pk': self.object.pk})

    


class CompanyDetailView(DetailView):
    model = Company
    context_object_name = "company"
    template_name = 'company/detail.html'


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    template_name = 'company/update.html'

    def get_success_url(self):
        return reverse('company:company-detail', kwargs={'pk': self.object.pk})



# class CategoryList(ListView):
#     model = Category
#     template_name = 'category/list.html'
#     context_object_name = 'categories'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context