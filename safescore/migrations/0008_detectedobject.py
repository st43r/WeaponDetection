# Generated by Django 4.2.6 on 2023-11-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("safescore", "0007_imagemodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="DetectedObject",
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
                ("track_id", models.IntegerField(unique=True)),
                ("image_path", models.CharField(max_length=255)),
            ],
        ),
    ]
