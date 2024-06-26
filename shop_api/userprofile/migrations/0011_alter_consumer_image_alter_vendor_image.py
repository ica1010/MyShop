# Generated by Django 5.0.6 on 2024-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0010_rename_add_at_consumer_add_rename_add_at_vendor_add"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumer",
            name="image",
            field=models.FileField(
                default="./default_Profile.png", upload_to="media/profile"
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="image",
            field=models.FileField(
                default="./default_Profile.png", upload_to="media/profile"
            ),
        ),
    ]
