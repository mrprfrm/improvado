import itertools

from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class CityRetrieveSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()

    def get_weather(self, obj):
        groups = itertools.groupby(obj.series.all(), key=lambda itm: itm.source)
        for source, group in groups:
            yield {
                source: [
                    {"temperature": itm.temperature, "timestamp": itm.timestamp}
                    for itm in group
                ]
            }

    class Meta:
        model = City
        fields = ['name', 'weather']
