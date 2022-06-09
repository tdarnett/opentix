from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import User


class Invoice(TimeStampedModel):
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='invoices', on_delete=models.PROTECT,
    )
