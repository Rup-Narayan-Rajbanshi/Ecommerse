# Generated by Django 3.0.4 on 2020-08-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200806_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='product_json',
            field=models.TextField(blank=True, null=True),
        ),
    ]
