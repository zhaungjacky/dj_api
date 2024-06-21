# Generated by Django 5.0.6 on 2024-06-21 04:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("access", "0003_alter_user_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("40393a33-2224-46d8-9a14-4a18eca793d4"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="UUID",
            ),
        ),
    ]
