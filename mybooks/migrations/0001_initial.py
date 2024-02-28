# Generated by Django 5.0.2 on 2024-02-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.TextField(max_length=100)),
                ("password", models.TextField(max_length=100)),
            ],
        ),
    ]
