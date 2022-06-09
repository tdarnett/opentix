from django.db import models


class ShoppingCartStatus(models.Model):
    (STATUS_PENDING, STATUS_PAYED) = (1, 2)
    STATUSES = {
        STATUS_PENDING: {
            'name': 'Pending'
        },
        STATUS_PAYED: {
            'name': 'Pending'
        }
    }

    status = models.IntegerField(choices=STATUSES, default=STATUS_PENDING, editable=False)

    class Meta:
        abstract = True
