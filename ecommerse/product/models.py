from django.db import models
from django.conf import settings

from helpers.choices import GENDER_CHOICES, SIZE_CHOICES, GENDER, SIZE, ORDER_STATUS_CHOICES, ORDER_STATUS
from helpers.models import BaseModel

# Create your models here.

class Color(models.Model):
	color=models.CharField(max_length=250)

	def __str__(self):
		return self.color

class Product(BaseModel):
	category=models.ForeignKey(Category,
							on_delete=models.CASCADE,
							related_name='product',
							related_query_name='products',
							null=True,
							)
	company=models.ForeignKey(Company,
						on_delete=models.CASCADE,
						related_name='product',
						related_query_name='products',
						)

	gender_choice=models.CharField(
			    choices = GENDER_CHOICES,
			    max_length = 10,
			    default = GENDER['ALL'],
			  )

	name = models.CharField(max_length=300)
	color = models.ManyToManyField(Color,through='ProductColor')
	size = models.CharField(choices = SIZE_CHOICES,
						    max_length = 10,
						    default = SIZE['MEDIUM'],
						    )

	price = models.IntegerField()
	description = models.TextField(null=True, blank=True)
	new_collection = models.BooleanField(default=False)
    tags = models.CharField(max_length=250,blank=True,null=True)
	text1 = models.CharField(max_length=250,null=True,blank=True)
	text2 = models.CharField(max_length=250,null=True,blank=True)

	def __str__(self):
		return self.product

# class Images(models.Model):
# 	product=models.ForeignKey(Product,
# 					on_delete=models.CASCADE,
# 					related_name='image',
# 					related_query_name='images',
# 					null=True,
# 					)
# 	image=models.FileField(upload_to="product_images/",null=True, blank=True)

class ProductColor(models.Model):
    product = models.ForeignKey(Product,
    					on_delete=models.CASCADE,
    					null=True,
    					)
    color = models.ForeignKey(Color,
    					on_delete=models.CASCADE,
    					null=True,
    					)



class ProductOrder(BaseModel):
	user=models.ForeignKey(User,
							on_delete=models.CASCADE,
							related_name='order',
							related_query_name='orders',
							null=True,
							blank=True
							)
	product=models.ForeignKey(Product,
						on_delete=models.CASCADE,
						related_name='order',
						related_query_name='orders',
						null=True,
						blank=True,
						)
	product_json=models.TextField(null=True,blank=True)
	price=models.IntegerField()
    status = models.CharField(choices = ORDER_STATUS_CHOICES,
						    max_length = 10,
						    default = ORDER_STATUS['NEW_ORDER'],)
	# cansil=models.BooleanField(default=False)
	# delivered=models.BooleanField(default=False)
	# paid=models.BooleanField(default=False)

class Contact(models.Model):
	name=models.CharField(max_length=250)
	email=models.EmailField()
	message=models.TextField()

	def __str__(self):
		return self.name