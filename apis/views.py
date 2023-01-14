from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,ListAPIView
from .serializers import PropertySerializer,CityListSerializer
from .models import Property,City
from rest_framework import filters
from django.db.models import Q

# Create your views here.


class PropertyListCreateAPIView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^city__city']

    def get_queryset(self):
        queryset = Property.objects.all()
        id  = self.request.query_params.get('id',None)
        if id:
            property = Property.objects.get(id=id)
            queryset = Property.objects.filter(Q(id=id)|Q(city=property.city))
        return queryset
    

class PropertyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^state__state','state__id']
