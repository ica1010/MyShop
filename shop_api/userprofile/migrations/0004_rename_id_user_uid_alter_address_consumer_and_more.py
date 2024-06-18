# Generated by Django 5.0.6 on 2024-05-09 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0003_address"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="id",
            new_name="uid",
        ),
        migrations.AlterField(
            model_name="address",
            name="consumer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consumer",
                to="userprofile.consumer",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vendor",
                to="userprofile.vendor",
            ),
        ),
    ]