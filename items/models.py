from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(100)],
    )
    description = models.TextField(
        max_length=1000,
        validators=[MaxLengthValidator(1000)],
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
