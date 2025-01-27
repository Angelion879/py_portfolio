# Generated by Django 5.1.5 on 2025-01-27 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images')),
                ('body', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.language')),
            ],
        ),
    ]
