# Generated by Django 4.2.6 on 2023-10-29 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("safescore", "0002_csvreport_delete_csvfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
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
                ("title", models.CharField(max_length=255)),
                ("report_file", models.FileField(upload_to="reports/")),
            ],
        ),
        migrations.CreateModel(
            name="Analytics",
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
                ("date", models.DateField()),
                ("tree", models.IntegerField()),
                ("glass", models.IntegerField()),
                ("plastic", models.IntegerField()),
                ("metal", models.IntegerField()),
                (
                    "csv_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="safescore.csvreport",
                    ),
                ),
            ],
        ),
    ]
