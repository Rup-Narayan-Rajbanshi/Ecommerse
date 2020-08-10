# Generated by Django 3.0.4 on 2020-08-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=1000)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('ph_no', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('cansil', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
