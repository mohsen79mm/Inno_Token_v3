# Generated by Django 3.1.3 on 2020-11-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20201130_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
