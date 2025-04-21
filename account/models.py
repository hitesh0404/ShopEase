from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.forms import ValidationError

# -----------------------------
# Validators and Choices
# -----------------------------

gender_choice = [
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Other"),
    ('NA', "Prefer not to say"),
]

title_choice = [
    ('H', 'Home'),
    ('W', 'Work'),
    ('O', 'Office'),
]

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
)

# -----------------------------
# Custom User Model
# -----------------------------

class User(AbstractUser):         # login Register    Pass hashing
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.user_type})"

# -----------------------------
# Customer Profile
# -----------------------------
from datetime import datetime
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime(2025, 4, 15, 11, 2,50, 29600))
    gender = models.CharField(max_length=2, choices=gender_choice)
    phone = models.CharField(max_length=17, validators=[phone_validator])

    def __str__(self):
        return f"Customer: {self.user.username}"

# -----------------------------
# Supplier Profile
# -----------------------------

class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    est_date = models.DateField()
    tagline = models.CharField(max_length=50)

    def __str__(self):
        return f"Supplier: {self.user.username}"

# -----------------------------
# Contact Details
# -----------------------------

class ContactDetails(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT, related_name='contacts')
    phone = models.CharField(max_length=17, validators=[phone_validator])

    def __str__(self):
        return f"{self.phone} ({self.supplier.user.username})"

# -----------------------------
# Address Model
# -----------------------------

class Address(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT, null=True, blank=True, related_name='addresses')
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT, null=True, blank=True, related_name='addresses')
    title = models.CharField(max_length=1, choices=title_choice)
    block_number = models.CharField(max_length=5)
    building_name = models.CharField(max_length=20)
    street = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return f"{self.get_title_display()} - {self.city}"

