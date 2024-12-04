from rest_framework import viewsets
from .models import Calculation 
from .serializers import CalculationSerializer


# Create your views here.
class CalculationViewSet(viewsets.ModelViewSet):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer