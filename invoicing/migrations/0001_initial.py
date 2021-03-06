# Generated by Django 2.0.3 on 2018-12-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document_processor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_invoiced', models.DateTimeField()),
                ('total', models.CharField(max_length=16)),
                ('vat', models.CharField(max_length=8)),
                ('billed_items', models.ManyToManyField(to='document_processor.Item')),
            ],
        ),
    ]
