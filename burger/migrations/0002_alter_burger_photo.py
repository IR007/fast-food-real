# Generated by Django 5.0.4 on 2024-05-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burger',
            name='photo',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]
