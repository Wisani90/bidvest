# Generated by Django 2.0.3 on 2018-12-04 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0004_auto_20181204_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_invoiced',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
