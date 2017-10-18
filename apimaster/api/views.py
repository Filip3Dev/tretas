from django.shortcuts import render
from rest_framework import generics
from .serializers import CoinlistSerializer
from .models import Coinlist

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Coinlist.objects.all()
    serializer_class = CoinlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Coinlist.objects.all()
    serializer_class = CoinlistSerializer