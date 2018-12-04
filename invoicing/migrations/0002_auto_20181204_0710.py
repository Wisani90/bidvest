# Generated by Django 2.0.3 on 2018-12-04 07:10

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='billed_items',
        ),
        migrations.AddField(
            model_name='invoice',
            name='billed_items',
            field=jsonfield.fields.JSONField(default={}, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}),
            preserve_default=False,
        ),
    ]
