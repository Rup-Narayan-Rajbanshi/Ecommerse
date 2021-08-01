from helpers.models import BaseModel
from django.db import models
from django.core.validators import FileExtensionValidator

class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    icon = models.FileField(upload_to='icons/', validators=[FileExtensionValidator(allowed_extensions=['svg'])],\
                            null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = "categories"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
