# from django.contrib import admin
# from .models import *



# # Register your models here.
# admin.site.register(Category)
# admin.site.register(Brand)
# admin.site.register(Model)
# admin.site.register(Color)
# # admin.site.register(Product)
# admin.site.register(ProductColor)
# admin.site.register(ProductOrder)
# admin.site.register(Images)
# admin.site.register(Contact)



# class PostAdmin(admin.ModelAdmin):
#     list_display = ('product', 'size','price')

# class MyPost(Product):
#     class Meta:
#         proxy = True

# class MyPostAdmin(PostAdmin):
#     def get_queryset(self, request):
#         return self.model.objects.filter(user = request.user)


# admin.site.register(Product, PostAdmin)
# admin.site.register(MyPost, MyPostAdmin)





















# # from django import forms
# # from admin_reports import Report


# # class MyReportForm(forms.Form):
# #     from_date = forms.DateField(label="From")
# #     to_date = forms.DateField(label="To")


# # class MyReport(Report):
# #     form_class = MyReportForm

# #     def aggregate(self, from_date=None, to_date=None, **kwargs):
# #         # Write yout aggregation here
# #         a= "test"
# #         return a