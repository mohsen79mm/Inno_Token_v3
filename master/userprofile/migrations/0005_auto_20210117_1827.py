# Generated by Django 3.1.2 on 2021-01-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20210117_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='user_type',
            field=models.CharField(choices=[('کاربر', 'کاربر'), ('استارتاپ', 'استارتاپ'), ('خدمت دهنده', 'خدمت دهنده'), ('مرکز معرفی', 'مرکز معرفی')], default='کاربر', max_length=11),
        ),
    ]
