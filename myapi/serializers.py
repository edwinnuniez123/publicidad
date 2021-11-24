from rest_framework import serializers

from .models import Brand, Store, Deal

class BrandSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Brand
		fields = ('id','name', 'logo')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Store
		fields = ('id','brand', 'identifier', 'name', 'address')

class DealSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Deal
		fields = ('id','name', 'store', 'image', 'price')