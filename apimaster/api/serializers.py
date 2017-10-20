from rest_framework import serializers
from .models import Coinlist, Details



class CoinlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coinlist
        fields = ('id', 'name', 'nick', 'ammount', 'worth', 'roi', 'logo', 'price', 'weekcoins', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class DetailsSerializer(serializers.ModelSerializer):
    data = CoinlistSerializer(many=False)

    class Meta:
        model = Details
        fields = ('data', 'nodesconf', 'bootstrap', 'nodecount', 'coinslocked', 'sharetime', 'mcap')
