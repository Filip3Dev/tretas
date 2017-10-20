from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CoinlistSerializer, DetailsSerializer
from .models import Coinlist, Details

class CoinlistViewSet(viewsets.ModelViewSet):

    queryset = Coinlist.objects.all()
    serializer_class = CoinlistSerializer

class DetailsViewSet(viewsets.ModelViewSet):

    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
