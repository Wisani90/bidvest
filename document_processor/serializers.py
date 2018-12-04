from rest_framework import serializers
from django.contrib.auth.models import User

from document_processor.models import Profile, Billed, Item

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'


class BilledSerializer(serializers.ModelSerializer):
	class Meta:
		model = Billed
		fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'