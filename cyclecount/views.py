from .serializers import StockSerializer
from rest_framework import viewsets
from .models import StockModel

# Create your views here.


class StockView(viewsets.ModelViewSet):
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer
