# Generated by Django 3.1.3 on 2021-01-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20210111_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(default='service_defult.png', upload_to='logo/'),
        ),
    ]