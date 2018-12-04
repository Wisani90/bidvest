from rest_framework import generics
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from invoicing.models import Invoice
from invoicing.serializers import InvoiceSerializer

from document_processor.utils import render_to_pdf
from document_processor.views import GeneratePdf
from document_processor.models import Profile, Billed
# from document_processor.serializers import ProfileSeriliazer, BilledSerializer
from document_processor.serializers import ProfileSerializer, BilledSerializer, ItemSerializer, UserSerializer


class InvoiceListCreate(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetail(APIView):
    model = Invoice
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # import pdb
        # pdb.set_trace()
        # invoice = self.get_object(pk)
        invoice = Invoice.objects.get(id=pk)
        serializer = InvoiceSerializer(invoice)

        if request.GET.get('show', None) == 'pdf':
            # api/invoicing/invoice/1/?show=pdf
            context = serializer.data
            try:
                context.update({
                    'profile': ProfileSerializer(Profile.objects.get(id=serializer.data.get('billed_to'))).data,
                    'company': BilledSerializer(Billed.objects.get(id=serializer.data.get('billed'))).data
                })
            except Exception as e:
                print(e)

            pdf = render_to_pdf('invoice.html', context_dict=context)
        
            return HttpResponse(pdf, content_type='application/pdf')
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(self.model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)