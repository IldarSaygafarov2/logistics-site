# Generated by Django 5.1.7 on 2025-03-17 14:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_trackinfo_correlation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinfo',
            name='correlation_id',
            field=models.UUIDField(default=uuid.UUID('ed8172a9-3ce8-42f1-b116-37a13ac96e27')),
        ),
    ]
