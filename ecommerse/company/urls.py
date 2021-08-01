
from django.urls import path
from company.views.company import CompanyRegisterView, CompanyDetailView, CompanyUpdateView
# from apis.views import *

app_name = 'company'

urlpatterns = [
    path('add/', CompanyRegisterView.as_view(), name='company-add'),
    path('detail/<uuid:pk>/', CompanyDetailView.as_view(), name='company-detail'),
     path('update/<uuid:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    # path('logout/', logout_view, name='logout'),
    # path('register/',register_view,name='register'),
    # path('update/<uuid:id>/',update_view,name='update'),
    # path('detail/<uuid:id>/',user_detail_view,name='detail'),

]