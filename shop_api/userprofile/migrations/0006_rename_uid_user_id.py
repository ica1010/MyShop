# Generated by Django 5.0.6 on 2024-05-09 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0005_alter_user_uid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="uid",
            new_name="id",
        ),
    ]