# Generated by Django 3.1.1 on 2020-11-12 12:36

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_acounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='details',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]