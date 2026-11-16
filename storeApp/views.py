from django.shortcuts import render
from rest_framework import authentication,permissions
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

from .models import ProductModel
from .serializers import ProductSerializer

class ProductCreateListView(CreateAPIView,ListAPIView):
    serializer_class=ProductSerializer

    def get_queryset(self):
        return ProductModel.objects.all()

    filter_backends=[SearchFilter,OrderingFilter]

    search_fields=["name"]
    Ordering_fields=["stock","created_at"]
    
class ProductUpdateDeleteRetrieve(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    serializer_class=ProductSerializer
    lookup_url_kwarg="id"
    
    def get_queryset(self):
            return ProductModel.objects.all()
     
    
