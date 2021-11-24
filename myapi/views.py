from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BrandSerializer, StoreSerializer, DealSerializer
from .models import Brand, Store, Deal


class BrandViewSet(viewsets.ModelViewSet):
	queryset = Brand.objects.all().order_by('name')
	serializer_class = BrandSerializer

class StoreViewSet(viewsets.ModelViewSet):
	queryset = Store.objects.all().order_by('name')
	serializer_class = StoreSerializer

class DealViewSet(viewsets.ModelViewSet):
	queryset = Deal.objects.all().order_by('name')
	serializer_class = DealSerializer
