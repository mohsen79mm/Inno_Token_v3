# Generated by Django 3.1.5 on 2021-01-23 21:50

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20210117_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuser',
            options={'permissions': (('can_add_service', 'Can added service'),)},
        ),
        migrations.AlterField(
            model_name='cuser',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=userprofile.models.get_upload_logo_path),
        ),
    ]
