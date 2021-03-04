from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
    FormView,
    FormMixin,
    CreateView,
    UpdateView,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.db.models import Q
from .models import *
from product.models import *
from .forms import *
from custom_decorators.decorators import *
from mixins.mixin import *
import json


@method_decorator(login_required(), name = "dispatch")
class AddBrand(GroupRequiredMixin,CreateView):
    group_names = ['Shopkeeper']
    model = Brand
    form_class = BrandForm
    template_name = 'brand/add.html'

    def form_valid(self, forms):
        brand = forms.save(commit=False)
        brand.user = self.request.user
        brand.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('product:brand-list')


@method_decorator(login_required(), name="dispatch")
class BrandUpdate(UpdateView):
    group_names = ['Shopkeeper']
    model = Brand
    form_class = BrandForm
    template_name = 'brand/add.html'

    def get_success_url(self):
        return reverse('product:brand-list')


@method_decorator(login_required(), name="dispatch")
class BrandList(ListView):
    group_names = ['Shopkeeper']
    model = Brand
    template_name = 'brand/list.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.filter(user=self.request.user)
        return context


#********************** End Block : Brand *******************#


#********************** Block : Product *******************#
@group_required('Shopkeeper', 'login_url')
def ProductAdd(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST or None,request.FILES or None)
        if product_form.is_valid() or image_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            # code.interact(local = dict(globals(), **locals()))
            for img in request.FILES.getlist('image'):
                Images.objects.create(product=product, image=img)

            return HttpResponseRedirect(reverse('product:my-products'))
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()

    context={
        'product_form': product_form,
        'image_form': image_form,
        }

    return render(request, 'product/product_add.html', context=context)


@group_required('Shopkeeper','login_url')
def ProductUpdate(request, id=None):
    product_instance = get_object_or_404(Product,id=id,user=request.user)
    # Product.objects.get(id=id,user=request.user)
    image_instance = Images.objects.filter(product=product_instance)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product_instance)
        image_form = ProductImageForm(request.POST or None, request.FILES or None)
        if product_form.is_valid() or image_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            for img in request.FILES.getlist('image'):
                Images.objects.create(product=product, image=img)

            return HttpResponseRedirect(reverse('product:my-products'))
    else:
        product_form = ProductForm(instance=product_instance)
        image_form = ProductImageForm()

    context={
        'product_form':product_form,
        'image_form':image_form,
        'image_instance':image_instance,
        }

    return render(request, 'product/product_add.html', context=context)


@group_required('Shopkeeper','login_url')
def image_update(request,id=None): 
    image_instance = Images.objects.get(id=id)
    product = Product.objects.get(images=image_instance)
    form = ImageUpdateForm(request.POST or None,request.FILES or None, instance=image_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('product:update', args=[product.id]))
    else:
        form=ImageUpdateForm(instance=image_instance)
    context = {
        'form': form
    }
    return render(request, 'product/image_update.html', context=context)


@group_required('Shopkeeper', 'login_url')
def image_delete(request,id=None):
    image = get_object_or_404(Images, pk=id)
    product = Product.objects.get(images=image)
    image.delete()
    return HttpResponseRedirect(reverse('product:update', args=[product.id]))


class ProductDetail(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product/detail.html"


class ProductList(FormMixin, ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    form_class = FilterForm
    query = None
    category = None

    def dispatch(self, request, *args, **kwargs):
        try: 
            self.category = self.kwargs['pk']
        except:
            self.category = None
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # self.initial = self.query.copy()
        self.query = self.request.GET
        search_product = self.query.get('search-product')
        if len(self.query) > 0:
            if search_product:
                search = search_product.rsplit()# split every word of search in a list and apply filter to each word
                for i in search:
                    return self.model.objects.filter(
                        Q(product__icontains=i)|
                        Q(category__category__icontains=i)|
                        Q(model__model__icontains=i)|
                        Q(brand__brand__icontains=i)
                    ) 
            else:
                return self.filter()
        else:
            if self.category:
                return self.model.objects.filter(category = self.category)
            else:
                return self.model.objects.all()

    def filter(self):
        self.initial = self.query.copy()
        query = self.query
        cat = query.get("category")
        from_price = query.get("price_from")
        to_price = query.get("price_to")
        color = query.get("color")
        filters = {}

        if cat:
            filters['category'] = cat
        if from_price:
            filters['price__gte'] = int(from_price)
        if to_price:
            filters['price__lte'] = int(to_price)
        if color:
            filters['color'] = color
        return self.model.objects.filter(**filters)

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['product_categories'] = Category.objects.all()
        return context

class Home(FormMixin, ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    form_class = FilterForm
    query = None

    def get_queryset(self):
        self.query = self.request.GET
        search_product = self.query.get('search-product')
        if len(self.query) > 0:
            if search_product:
                search = search_product.rsplit()# split every word of search in a list and apply filter to each word
                for i in search:
                    return self.model.objects.filter(
                        Q(product__icontains=i)|
                        Q(category__category__icontains=i)|
                        Q(model__model__icontains=i)|
                        Q(brand__brand__icontains=i)
                    ) 
            else:
                return self.filter()
        else:
            return self.model.objects.all()

    def filter(self):
        self.initial = self.query.copy()
        query = self.query
        cat = query.get("category")
        from_price = query.get("price_from")
        to_price = query.get("price_to")
        color = query.get("color")

        return self.model.objects.filter(
            category=cat,
            price__gte=from_price,
            price__lte=to_price,
            color=color
        )

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['new_collections'] = Product.objects.filter(is_new_collection=True)
        return context

#********************** End Block : Product *******************#

#********************** Block : Order *******************#


class ProductOrderAdd(CreateView):
    model = ProductOrder
    form_class = ProductOrderForm 
    template_name = 'order/checkout.html'

    def get_success_url(self):
        return reverse('product:order-list')

    def form_valid(self, forms):
        order = forms.save(commit=False)
        order.product_json = json.loads(order.product_json)
        products = order.product_json
        total_price = 0
        for k, v in products.items():
            qty = int(v[0])
            rate_str = v[2]
            rate = int(rate_str[3:])
            price = rate * qty
            total_price = total_price + price

        order = Order.objects.create(status=Order.PENDING, created_by=self.request.user, total_price=total_price)

        for k, v in products.items():
            qty = int(v[0])
            rate_str = v[2]
            rate = int(rate_str[3:])
            product = Product.objects.get(id=int(k[2:]))
            price = rate*qty
            ProductOrder.objects.create(
                product=product,
                quantity=qty,
                total_price=price,
                order = order,
            )
        messages.success(self.request,"Thank You !. Your Order has been placed.")
        return HttpResponseRedirect(self.get_success_url())


class MyOrderList(ListView):
    model = Order
    template_name = 'order/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_orders'] = Order.objects.filter(created_by=self.request.user)
        return context


class MyOrderDetail(DetailView):
    model = Order
    template_name = 'order/order-detail.html'
    context_object_name = "my_orders_details"

    def get_context_data(self, *args, **kwargs):
        context = super(MyOrderDetail, self).get_context_data(*args, **kwargs)
        context['my_orders_detail'] = ProductOrder.objects.filter(order__id=self.kwargs['pk'])
        return context

# ********************** End Block : Order *******************#


# ********************** Block : Dashboard *******************#
@method_decorator(login_required(), name = "dispatch")
class Dashboard(GroupRequiredMixin,ListView):
    group_names=['Shopkeeper']
    model = Product
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(user=self.request.user)
        context['orders'] = ProductOrder.objects.filter(product__user=self.request.user)
        return context


@method_decorator(login_required(), name = "dispatch")
class MyProductList(GroupRequiredMixin, ListView):
    group_names = ['Shopkeeper']
    model = Product
    template_name = 'product/my_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(user=self.request.user)
        return context


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'order/contact.html'

    def form_valid(self,forms):
        forms.save()
        messages.success(self.request, "Message sent successfully.")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('product:contact')

def deliver(request,id=None):
    order = ProductOrder.objects.get(order_id=id)
    order.delivered = True
    order.save()

    return HttpResponseRedirect(reverse('dashboard'))

# Create your views here.
# class AddCategory(CreateView):
#     model = Category
#     fields = ('__all__')
#     template_name = 'category/add.html'

#     def get_success_url(self):
#         return reverse('product:category-list')



# class CategoryUpdate(UpdateView):
#     model = Category
#     fields = ('__all__')
#     template_name = 'category/add.html'

#     def get_success_url(self):
#         return reverse('product:category-list')



# class CategoryList(ListView):
#     model = Category
#     template_name = 'category/list.html'
#     context_object_name = 'categories'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#********************** End Block : Category *******************#


#********************** Block : Brand *******************#
# Create your views here.


# class ProductUpdate(UpdateView):
#     model = Product
#     fields = ('__all__')
#     template_name = 'category/add.html'

#     def get_success_url(self):
#         return reverse('product:list')


#********************** Block : Model *******************#
# Create your views here.
# @method_decorator(login_required(), name = "dispatch")
# class AddModel(CreateView):
#     group_names=['Shopkeeper']
#     model = Model
#     form_class=ModelForm
#     template_name = 'model/add.html'

#     def form_valid(self,forms):
#         model=forms.save(commit=False)
#         model.user=self.request.user
#         model.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse('product:model-list')


# @method_decorator(login_required(), name = "dispatch")
# class ModelUpdate(UpdateView):
#     group_names=['Shopkeeper']
#     model = Model
#     form_class=ModelForm
#     template_name = 'model/add.html'

#     def get_success_url(self):
#         return reverse('product:model-list')


# @method_decorator(login_required(), name = "dispatch")
# class ModelList(ListView):
#     group_names=['Shopkeeper']
#     model = Model
#     template_name = 'model/list.html'
#     # context_object_name = 'models'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['models']=Model.objects.filter(user=self.request.user)
#         return context


#********************** End Block : Model *******************#

#********************** Block : Color *******************#

# class AddColor(CreateView):
#     model = Color
#     fields = ('__all__')
#     template_name = 'category/add.html'

#     def get_success_url(self):
#         return reverse('product:color-list')


# class ColorUpdate(UpdateView):
#     model = Color
#     fields = ('__all__')
#     template_name = 'category/add.html'

#     def get_success_url(self):
#         return reverse('product:color-list')


# class ColorList(ListView):
#     model = Color
#     template_name = 'color/list.html'
#     context_object_name = 'colors'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#********************** End Block : Color *******************#

