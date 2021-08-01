
from django.urls import path
from .views import *
from apis.views import *

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register_view,name='register'),
    path('update/<uuid:id>/',update_view,name='update'),
    path('detail/<uuid:id>/',user_detail_view,name='detail'),

#     path('password/change/',ChangePassword.as_view(),name='password-change'),
#     # path('add/',UserAddView.as_view(),name='add'),
]