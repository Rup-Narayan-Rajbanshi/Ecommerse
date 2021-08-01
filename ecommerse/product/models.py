# from django.db import models
# from django.conf import settings

# # Create your models here.
# class Category(models.Model):
# 	category=models.CharField(max_length=250)
# 	image=models.ImageField(upload_to="category_images/",
# 				            null=True, 
# 				            blank=True
# 				           	)
# 	text=models.CharField(max_length=250,null=True,blank=True)

# 	def __str__(self):
# 		return self.category

# class Brand(models.Model):
# 	user=models.ForeignKey(settings.AUTH_USER_MODEL,
# 							on_delete=models.CASCADE,
# 							related_name='brand',
# 							related_query_name='brands',
# 							null=True,
# 							blank=True
# 							)
# 	brand=models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.brand

# class Model(models.Model):
# 	user=models.ForeignKey(settings.AUTH_USER_MODEL,
# 							on_delete=models.CASCADE,
# 							related_name='model',
# 							related_query_name='models',
# 							null=True,
# 							blank=True
# 							)
# 	model=models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.model

# class Color(models.Model):
# 	color=models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.color

# class Product(models.Model):
# 	M="M"
# 	F="F"
# 	A="A"

# 	GENDER_CHOICES = (
# 	(M, "male"),
# 	(F, "female"),
# 	(A,"All"),
# 		)

# 	S="S"
# 	M="M"
# 	L="L"
# 	XL="XL"

# 	SIZE_CHOICES = (
# 	(S,"small"),
# 	(M, "medium"),
# 	(L, "large"),
# 	(XL,"xtra large"),
# 		)

# 	user=models.ForeignKey(settings.AUTH_USER_MODEL,
# 							on_delete=models.CASCADE,
# 							related_name='product',
# 							related_query_name='products',
# 							null=True,
# 							blank=True
# 							)
# 	category=models.ForeignKey(Category,
# 							on_delete=models.CASCADE,
# 							related_name='product',
# 							related_query_name='products',
# 							null=True,
# 							)
# 	brand=models.ForeignKey(Brand,
# 						on_delete=models.CASCADE,
# 						related_name='product',
# 						related_query_name='products',
# 						null=True,
# 						)
# 	model=models.ForeignKey(Model,
# 						on_delete=models.CASCADE,
# 						related_name='product',
# 						related_query_name='products',
# 						null=True
# 						)
# 	gender=models.CharField(
# 			    choices = GENDER_CHOICES,
# 			    max_length = 3,
# 			    default = A,
# 			  )
# 	product = models.CharField(max_length=300)
# 	color = models.ManyToManyField(Color,through='ProductColor')
# 	size = models.CharField(choices = SIZE_CHOICES,
# 						    max_length = 10,
# 						    default = M,
# 						    )

# 	price = models.IntegerField()
# 	description = models.TextField(null=True)
# 	new_collection = models.BooleanField(default=False)
# 	text1 = models.CharField(max_length=250,null=True,blank=True)
# 	text2 = models.CharField(max_length=250,null=True,blank=True)

# 	def __str__(self):
# 		return self.product

# class Images(models.Model):
# 	product=models.ForeignKey(Product,
# 					on_delete=models.CASCADE,
# 					related_name='image',
# 					related_query_name='images',
# 					null=True,
# 					)
# 	image=models.FileField(upload_to="product_images/",null=True, blank=True)

# class ProductColor(models.Model):
#     product = models.ForeignKey(Product,
#     					on_delete=models.CASCADE,
#     					null=True,
#     					)
#     color = models.ForeignKey(Color,
#     					on_delete=models.CASCADE,
#     					null=True,
#     					)



# class ProductOrder(models.Model):
# 	order_id=models.AutoField(primary_key=True)
# 	user=models.ForeignKey(settings.AUTH_USER_MODEL,
# 							on_delete=models.CASCADE,
# 							related_name='order',
# 							related_query_name='orders',
# 							null=True,
# 							blank=True
# 							)
# 	product=models.ForeignKey(Product,
# 						on_delete=models.CASCADE,
# 						related_name='order',
# 						related_query_name='orders',
# 						null=True,
# 						blank=True,
# 						)
# 	product_json=models.TextField(null=True,blank=True)
# 	name=models.CharField(max_length=250)
# 	address=models.CharField(max_length=250)
# 	ph_no=models.IntegerField()
# 	quantity = models.IntegerField()
# 	total_price=models.IntegerField()
# 	cansil=models.BooleanField(default=False)
# 	delivered=models.BooleanField(default=False)
# 	paid=models.BooleanField(default=False)

# class Contact(models.Model):
# 	name=models.CharField(max_length=250)
# 	email=models.EmailField()
# 	message=models.TextField()

# 	def __str__(self):
# 		return self.name