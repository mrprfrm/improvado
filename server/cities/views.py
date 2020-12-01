from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django_filters import utils
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING, FORMAT_DATETIME
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from weather.filters import SeriesFilterSet
from weather.models import Series
from .models import City
from .serializers import CitySerializer, CityRetrieveSerializer


@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(
                      manual_parameters=[
                          Parameter(name='weather_time',
                                    in_=IN_QUERY,
                                    type=TYPE_STRING,
                                    format=FORMAT_DATETIME)]))
class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'city_name'
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CityRetrieveSerializer
        return CitySerializer

    def filter_queryset(self, queryset):
        series = Series.objects.all()
        filterset = SeriesFilterSet(self.request.GET, queryset=series)

        if not filterset.is_valid():
            raise utils.translate_validation(filterset.errors)

        return queryset.prefetch_related(Prefetch('series', queryset=filterset.qs))
