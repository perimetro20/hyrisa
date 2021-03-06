# Generated by Django 2.0.4 on 2018-07-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
