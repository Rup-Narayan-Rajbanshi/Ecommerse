from django.db import models
from django.conf import settings


# Create your models here.

class UserDetail(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.CASCADE,
							related_name='user_detail',
							related_query_name='user_details'
							)
	phone_no=models.IntegerField()
	address=models.CharField(max_length=1000)
	landmark=models.CharField(max_length=250,null=True,blank=True)

	def __str__(self):
		return self.user.username
