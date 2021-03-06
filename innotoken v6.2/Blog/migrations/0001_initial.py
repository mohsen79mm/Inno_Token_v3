# Generated by Django 3.1.3 on 2020-12-09 18:00

import Blog.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(null=True, upload_to=Blog.models.get_upload_path)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('url', models.CharField(max_length=150, unique=True, verbose_name='URL')),
                ('post_cat', models.ManyToManyField(to='Blog.post_category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
