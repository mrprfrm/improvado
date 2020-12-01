from rest_framework.generics import ListAPIView, get_object_or_404

from .filters import SeriesFilterSet
from .models import Series
from .serializers import SeriesSerializer


class SeriesListView(ListAPIView):
    filterset_class = SeriesFilterSet
    serializer_class = SeriesSerializer

    def get_queryset(self):
        return get_object_or_404(Series, city=self.kwargs.get('city_name'))
