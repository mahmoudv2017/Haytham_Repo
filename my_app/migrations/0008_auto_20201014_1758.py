# Generated by Django 3.1.1 on 2020-10-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20201014_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='gpu',
            field=models.CharField(blank=True, max_length=67),
        ),
        migrations.AlterField(
            model_name='products',
            name='ram',
            field=models.CharField(blank=True, max_length=83),
        ),
    ]