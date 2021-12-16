from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status

from rest_framework.response import Response

from .serializers import BrandSerializer, StoreSerializer, DealSerializer, UserSerializer, User_storeSerializer
from .models import Brand, Store, Deal, User, User_store


class BrandViewSet(viewsets.ModelViewSet):
	queryset = Brand.objects.all().order_by('name')
	serializer_class = BrandSerializer

class StoreViewSet(viewsets.ModelViewSet):
	queryset = Store.objects.all().order_by('name')
	serializer_class = StoreSerializer

class DealViewSet(viewsets.ModelViewSet):
	queryset = Deal.objects.all().order_by('name')
	serializer_class = DealSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('email')
	serializer_class = UserSerializer

class User_storeViewSet(viewsets.ModelViewSet):
	queryset = User_store.objects.all().order_by('user')
	serializer_class = User_storeSerializer
	"""
	print ("suscritos a la tienda")

	def list(self, request):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")

	def create(self, request):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")


	def retrieve(self, request, pk=None):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")


	def update(self, request, pk=None):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")


	def partial_update(self, request, pk=None):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")


	def destroy(self, request, pk=None):
		print("suscritos a la tienda")
		return Response("suscritos a la tienda")

    """
