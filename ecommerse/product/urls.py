from django.urls import path, include
from .views import *
from . import views
# from django.views.generic import TemplateView

app_name = 'product'

urlpatterns = [ 
#Brand
    path('brand/add/',AddBrand.as_view(),name='brand-add'),
    path('brand/<int:pk>/update/',BrandUpdate.as_view(),name='brand-update'),
    path('brand/list/',BrandList.as_view(),name='brand-list'),

#Product
    path('add/', ProductAdd,name='product-add'),
    path('<int:id>/update/', ProductUpdate,name='update'),
    path('list/', ProductList.as_view(), name='list'),
    path('category_list/<int:pk>/', ProductList.as_view(), name='category-list'),
    path('<int:pk>/detail/', ProductDetail.as_view(), name='detail'),

    path('my_list/', MyProductList.as_view(), name = 'my-products'),

#Order
    path('checkout/', ProductOrderAdd.as_view(), name='checkout'),
    path('order/list/', MyOrderList.as_view(), name='order-list'),
    path('order/<int:pk>/detail/', MyOrderDetail.as_view(), name='order-detail'),
    path('deliver/<int:id>/', deliver, name='deliver'),

#image
    path('image/<int:id>/update/', image_update, name='image-update'),
    path('image/<int:id>/delete/', image_delete, name='image-delete'),

#contact
    path('contact/', ContactView.as_view(), name='contact'),

# dashboard
#Category
    # path('category/add/',AddCategory.as_view(),name='category-add'),
    # path('category/<int:pk>/update/',CategoryUpdate.as_view(),name='category-update'),
    # path('category/list/',CategoryList.as_view(),name='category-list'),
#Model
    # path('model/add/',AddModel.as_view(),name='model-add'),
    # path('model/<int:pk>/update/',ModelUpdate.as_view(),name='model-update'),
    # path('model/list/',ModelList.as_view(),name='model-list'),

#Color
    # path('color/add/',AddColor.as_view(),name='color-add'),
    # path('color/<int:pk>/update/',ColorUpdate.as_view(),name='color-update'),
    # path('color/list/',ColorList.as_view(),name='color-list'),
]
