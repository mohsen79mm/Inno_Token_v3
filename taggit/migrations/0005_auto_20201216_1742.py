# Generated by Django 3.1.3 on 2020-12-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_auto_20201216_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
