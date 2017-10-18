from rest_framework import serializers
from .models import Coinlist


class CoinlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Coinlist
        fields = ('id', 'name', 'nick', 'ammount', 'worth', 'roi', 'logo', 'nodecount', 'coinslocked', 'sharetime', 'price', 'mcap', 'weekcoins', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')