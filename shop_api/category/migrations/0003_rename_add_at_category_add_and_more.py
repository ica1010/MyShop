# Generated by Django 5.0.6 on 2024-05-10 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0002_category_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="add_at",
            new_name="add",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="update_at",
            new_name="update",
        ),
    ]