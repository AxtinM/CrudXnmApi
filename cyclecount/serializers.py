from rest_framework import serializers
from .models import StockModel


# cleaning and processing data, to work with python data-types
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockModel
        fields = ['id', 'content', 'aile_num', 'level', 'bin',
         'last_scan', 'first_scan', 'image']