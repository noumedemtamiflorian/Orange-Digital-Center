# Generated by Django 3.2.3 on 2021-05-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produits',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
