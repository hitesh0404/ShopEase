# Generated by Django 5.2 on 2025-04-18 04:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("order", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "razorpay_order_id",
                    models.CharField(blank=True, default="default", max_length=25),
                ),
                (
                    "razorpay_payment_id",
                    models.CharField(blank=True, default="default", max_length=25),
                ),
                (
                    "payment_signature",
                    models.CharField(blank=True, default="default", max_length=128),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("COMPLETED", "COMPLETED"),
                            ("FAILED", "FAILED"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("RAZORPAY", "RAZORPAY"),
                            ("COD", "COD"),
                            ("KARMA_WALLET", "KARMA_WALLET"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="order.order"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
