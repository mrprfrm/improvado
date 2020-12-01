from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cities.views import CityViewSet

router = DefaultRouter()
router.register('cities', CityViewSet, 'cities')

urlpatterns = [
    path('', include(router.urls))
]
