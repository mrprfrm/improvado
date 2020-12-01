import requests
from django.utils import timezone

from server.celery import app
from django.conf import settings


from cities.models import City
from .models import Series


@app.task()
def update_openweathermap_data():
    series_list = []
    for city in City.objects.all():
        url = f'{settings.OPENWEATHERMAP_URL}?q={city.name}&appid={settings.OPENWEATHERMAP_TOKEN}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            series = Series(source='open weather map',
                            temperature=data['main'].get('temp'),
                            timestamp=timezone.now(),
                            city=city)
            series_list.append(series)
    Series.objects.bulk_create(series_list, ignore_conflicts=True)
