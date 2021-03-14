# Generated by Django 3.1.7 on 2021-03-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_auto_20210314_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]