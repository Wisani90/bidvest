from django.db import models
from jsonfield import JSONField
from django.utils import timezone

import collections

from document_processor.models import Profile, Billed, Item
# Create your models here.

class Invoice(models.Model):

    
    billed_items = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
    date_invoiced = models.DateTimeField(auto_now_add=True)
    tax = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=7)
    total = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=7)
    vat_no = models.CharField(max_length=8)

    client_name = models.CharField(max_length=32)
    street_address = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    billed_to = models.ForeignKey(Profile, related_name='billed_to', on_delete=models.CASCADE, null=True)
    billed = models.ForeignKey(Billed, related_name='billed', on_delete=models.CASCADE, null=True)

    def calculate_total(self):

        return

    def generate_invoice(self):

        return
