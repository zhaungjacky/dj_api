# Generated by Django 5.0.6 on 2024-06-21 04:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("access", "0002_alter_user_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("2326b6b5-b398-4fa2-a7e3-9c091ac859da"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="UUID",
            ),
        ),
    ]