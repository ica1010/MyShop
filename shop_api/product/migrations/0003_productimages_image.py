# Generated by Django 5.0.6 on 2024-05-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productimages",
            name="image",
            field=models.FileField(default="product.jgp", upload_to="Product_image"),
        ),
    ]
