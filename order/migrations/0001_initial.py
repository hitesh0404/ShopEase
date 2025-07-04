# Generated by Django 5.2 on 2025-04-18 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Order placed", "Order placed"),
                            ("Order Confirmed", "Order Confirmed"),
                            ("Order processing", "Order processing"),
                            ("Dispatched", "Dispatched"),
                            ("In Transit", "In Transit"),
                            ("Out for delivery", "Out for delivery"),
                            ("Delivered", "Delivered"),
                            ("cancelled", "cancelled"),
                            ("pending", "pending"),
                            ("Completed", "Completed"),
                            ("refunded", "refunded"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "delivery_charge",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("order_amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Completed", "Completed"),
                            ("Rejected", "Rejected"),
                            ("Processing", "Processing"),
                        ],
                        max_length=20,
                    ),
                ),
                ("pickup_date", models.DateField()),
                ("delivery_date", models.DateField()),
                (
                    "Shipping_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="account.address",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="account.customerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderDetails",
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
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="order.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="inventory.product",
                    ),
                ),
            ],
        ),
    ]
