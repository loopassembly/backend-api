# Generated by Django 4.0 on 2022-01-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_hotel_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='password',
            field=models.CharField(default='admin@123', max_length=50, verbose_name='password'),
        ),
    ]
