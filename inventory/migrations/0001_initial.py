# Generated by Django 5.2 on 2025-04-18 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=20)),
                ("logo", models.ImageField(upload_to="brand_logo")),
                ("est_date", models.DateField()),
                ("tagline", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=120)),
                ("image", models.ImageField(upload_to="product_images/main")),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("description", models.TextField()),
                ("quantity", models.IntegerField()),
                ("added_on", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_on", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.brand",
                    ),
                ),
                ("category", models.ManyToManyField(to="inventory.category")),
                (
                    "suplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.supplierprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("image", models.ImageField(upload_to="product_images")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
        ),
    ]
