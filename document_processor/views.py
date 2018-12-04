from rest_framework import generics
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
from django.contrib.auth.models import User


from document_processor.models import Profile, Billed, Item
from document_processor.serializers import ProfileSerializer, BilledSerializer, ItemSerializer, UserSerializer
from document_processor.utils import render_to_pdf

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BilledListCreate(generics.ListCreateAPIView):
    queryset = Billed.objects.all()
    serializer_class = BilledSerializer


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Billed.objects.all()
    serializer_class = ItemSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()

        pdf = render_to_pdf('invoice.html')

        return HttpResponse(pdf, content_type='application/pdf')