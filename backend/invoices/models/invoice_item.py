from django.db import models
from django_extensions.db.models import TimeStampedModel

from invoices.models import Invoice
from users.models import User


class InvoiceItem(TimeStampedModel):
    invoice = models.ForeignKey(
        Invoice, related_name='invoice_items', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='invoice_items', on_delete=models.PROTECT,
    )

