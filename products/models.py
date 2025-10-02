from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    icon_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="subcategories",
        on_delete=models.CASCADE,
        )
    
    def __str__(self):
        return self.name
    
class Maker(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    class Currency(models.TextChoices):
        USD = "USD", _("US Dollar")
        EUR = "EUR", _("Euro")
        GBP = "GBP", _("British Pound")
        JPY = "JPY", _("Japanese Yen")
        INR = "INR", _("Indian Rupee")
    
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=512)

    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD,
    )

    variation_products_ids = PostgresFields.ArrayField(
        models.IntegerField(blank=True, null=True),
        blank=True,
        default=list,
    )

    def __str__(self):
        return f"{self.title} - {self.subtitle} - {self.maker}"