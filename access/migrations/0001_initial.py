# Generated by Django 5.0.6 on 2024-06-21 04:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.UUID("777969c1-9974-4681-81dc-901024e784b5"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        db_index=True,
                        max_length=128,
                        null=True,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=128, verbose_name="Name"),
                ),
                ("password", models.CharField(max_length=128, verbose_name="Password")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user can access their account.",
                        verbose_name="Activate",
                    ),
                ),
                (
                    "is_admin",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this user can log into  admin pannel .",
                        verbose_name="Activate",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
