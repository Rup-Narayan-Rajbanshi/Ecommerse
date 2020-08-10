# Generated by Django 3.0.4 on 2020-08-05 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200803_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='product_json',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', related_query_name='orders', to='product.Product'),
            preserve_default=False,
        ),
    ]