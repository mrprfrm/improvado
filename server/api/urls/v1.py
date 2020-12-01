from django.urls import path

from cities.views import CityListCreateView
from weather.views import SeriesListView

urlpatterns = [
    path('cities', CityListCreateView.as_view(), name='cities'),
    path('cities/<str:city_name>', SeriesListView.as_view(), name='series')
]
