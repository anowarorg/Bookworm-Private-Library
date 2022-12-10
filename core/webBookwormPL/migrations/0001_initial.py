# Generated by Django 4.1.1 on 2022-12-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookList",
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
                ("title", models.CharField(max_length=100)),
                ("author_name", models.EmailField(max_length=100)),
                ("genre", models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
