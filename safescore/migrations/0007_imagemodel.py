# Generated by Django 4.2.6 on 2023-11-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("safescore", "0006_delete_rtsplink_rename_file_video_video_file_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("image", models.ImageField(upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
