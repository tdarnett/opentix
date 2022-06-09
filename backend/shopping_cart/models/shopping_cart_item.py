from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import User


class ShoppingCartItem(TimeStampedModel):
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='cart_items', on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
