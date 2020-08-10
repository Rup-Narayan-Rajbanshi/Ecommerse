from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from .models import *


class ProductOrderForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in self.fields:
	    	if field in ['product_json']:
	    		self.fields[field].widget.attrs.update({'type':'hidden', 'id':"product_json", 'value':""})
	class Meta:
		model = ProductOrder
		exclude = ('total_price','quantity','cansil','delivered','paid',)


class ProductForm(forms.ModelForm):
	# product_description = forms.CharField(strip=False, widget=forms.Textarea)
	class Meta:
		model=Product
		exclude=('user',)

class ModelForm(forms.ModelForm):
	class Meta:
		model=Model
		exclude=('user',)

class BrandForm(forms.ModelForm):
	class Meta:
		model=Brand
		exclude=('user',)

		
class ProductImageForm(forms.Form):
	image=MultiImageField(min_num=1, max_num=4, max_file_size=1024*1024*5,required=False)


class ImageUpdateForm(forms.ModelForm):
	class Meta:
		model=Images
		exclude=('product',)


class FilterForm(forms.Form):
	category=forms.ModelChoiceField(required=False,
							queryset = Category.objects.all(),
							label='Category',
							)
	price_from=forms.CharField(required=False,label='From ( Rs. )')
	price_to=forms.CharField(required=False,label='To ( Rs. )')
	color=forms.ModelChoiceField(required=False,
								queryset=Color.objects.all(),
								label='Color',
								)  
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control border-1'})


class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in self.fields:
	    	self.fields[field].label='' 
	    	if field in ['name']:
	    		self.fields[field].widget.attrs.update({'placeholder':'Name','class':'stext-111 cl2 plh3 size-116 p-l-62 p-r-30'})
	    	if field in ['email']:
	    		self.fields[field].widget.attrs.update({'placeholder':'Email','class':'stext-111 cl2 plh3 size-116 p-l-62 p-r-30'})
	    	if field in ['message']:
	    		self.fields[field].widget.attrs.update({'placeholder':'How can we help ?','class':'stext-111 cl2 plh3 size-200 p-l-62 p-r-30'})
	class Meta:
		model = Contact
		fields=('__all__')
