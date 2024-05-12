# Generated by Django 5.0.4 on 2024-05-06 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0002_alter_burger_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='raw_response',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='successful',
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='burger.order'),
        ),
    ]