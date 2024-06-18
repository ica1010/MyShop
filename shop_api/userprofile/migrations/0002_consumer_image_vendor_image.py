# Generated by Django 5.0.6 on 2024-05-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="consumer",
            name="image",
            field=models.FileField(
                default="./default_Profile.png", upload_to="profile"
            ),
        ),
        migrations.AddField(
            model_name="vendor",
            name="image",
            field=models.FileField(
                default="./default_Profile.png", upload_to="profile"
            ),
        ),
    ]