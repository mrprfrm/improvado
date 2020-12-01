from rest_framework.generics import ListCreateAPIView

from .models import City
from .serializers import CitySerializer


class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
