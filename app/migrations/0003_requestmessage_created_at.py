# Generated by Django 5.1.7 on 2025-03-17 07:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_requestmessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
