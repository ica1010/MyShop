# Generated by Django 5.0.6 on 2024-05-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.FileField(default="category.jgp", upload_to="category_image"),
        ),
    ]