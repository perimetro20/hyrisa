# Generated by Django 2.0.4 on 2018-07-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20180717_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=155, verbose_name='Marca'),
        ),
    ]
