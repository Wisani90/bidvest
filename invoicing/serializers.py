from rest_framework import serializers
    
from invoicing.models import Invoice
from document_processor.models import Profile, Billed
from document_processor.serializers import ProfileSerializer, BilledSerializer

from django.utils import timezone

import json
 

class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        result = super(DateTimeFieldWihTZ, self).to_representation(value)
        return result.timestamp()

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        converted = datetime.fromtimestamp(float('%s' % value))
        return super(DateTimeFieldWihTZ, self).to_representation(converted)


class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date_invoiced = serializers.DateTimeField()

    billed_to = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Profile.objects.all())

    billed = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Billed.objects.all())

    billed_items = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id', 'billed_items', 'date_invoiced','tax','total', 
            'vat_no','client_name', 'street_address' ,
            'address', 'billed_to', 'billed')

    def get_billed_to(self, obj):
        qs = obj.billed_to.all()
        return ProfileSerializer(obj.billed_to.all(), read_only=True).data

    def get_billed(self, obj):
        s = obj.billed.all()
        return BilledSerializer(obj.billed.all(), read_only=True).data

    def get_billed_items(self, obj):  
        # qs = [ json.loads(i) for i in obj.billed_items]
        # qs = [ json.loads(i) for i in obj.billed_items]
        return obj.billed_items

    # def date(self, o):
    #     if isinstance(o, datetime.datetime):
    #         return o.__str__()

    # date_invoiced = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')