# Generated by Django 5.0.6 on 2024-06-21 04:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("access", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("d18b1fd5-3392-4d8f-9526-f4eb63fe4cad"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="UUID",
            ),
        ),
    ]
