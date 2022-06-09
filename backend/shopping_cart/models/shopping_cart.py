from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import User


class ShoppingCart(TimeStampedModel):
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='carts', on_delete=models.PROTECT,
    )
