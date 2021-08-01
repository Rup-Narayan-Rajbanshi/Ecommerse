# Generated by Django 2.0.8 on 2021-07-27 06:50

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to='icons/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])])),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'category',
                'ordering': ['-created_at'],
            },
        ),
    ]