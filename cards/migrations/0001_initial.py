# Generated by Django 4.1.7 on 2023-03-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("question", models.CharField(max_length=100)),
                ("answer", models.TextField(max_length=1000)),
                (
                    "box",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
