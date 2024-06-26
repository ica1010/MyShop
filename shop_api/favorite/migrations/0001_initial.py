# Generated by Django 5.0.6 on 2024-05-09 13:13

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0002_initial"),
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "fid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=16,
                        max_length=40,
                        prefix="Fav-",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("add_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userprofile.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FavoriteItem",
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
                ("add_at", models.DateTimeField(auto_now_add=True)),
                (
                    "Favorite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="favorite.favorite",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]
