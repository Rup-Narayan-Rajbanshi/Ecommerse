import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import os

from helpers.models import BaseModel

class Image(BaseModel):

    def get_upload_path(self, filename):
        return '{}/{}'.format(self.content_type, filename)

    image = models.ImageField(upload_to=get_upload_path)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'image'
        ordering = ['-created_at']

    def __str__(self):
        return os.path.basename(self.image.name)
