# Generated by Django 5.0.6 on 2024-05-11 15:44

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_rename_add_at_cart_add_rename_update_at_cart_update_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="cid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefg1234",
                editable=False,
                length=16,
                max_length=40,
                prefix="Cart-",
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
