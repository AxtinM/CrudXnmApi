# Generated by Django 3.2.7 on 2021-09-30 11:44

import cyclecount.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=255, verbose_name='Content')),
                ('aile_num', models.IntegerField(verbose_name='Aile')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('bin', models.CharField(max_length=100, verbose_name='Bin')),
                ('last_scan', models.DateTimeField(auto_now=True, verbose_name='Last Scan')),
                ('first_scan', models.DateTimeField(auto_now_add=True, null=True, verbose_name='First Scan')),
                ('image', models.ImageField(blank=True, upload_to=cyclecount.models.image_location, verbose_name='Image')),
            ],
        ),
    ]
