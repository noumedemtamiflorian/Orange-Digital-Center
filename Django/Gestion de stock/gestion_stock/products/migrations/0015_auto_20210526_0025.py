# Generated by Django 3.2.3 on 2021-05-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(max_length=255, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(max_length=255, upload_to='images'),
        ),
    ]
