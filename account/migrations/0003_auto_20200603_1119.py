# Generated by Django 3.0.6 on 2020-06-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name_p',
            field=models.CharField(default='', max_length=200, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name_p',
            field=models.CharField(default=' ', max_length=200, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
