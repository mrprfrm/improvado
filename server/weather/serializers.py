from rest_framework import serializers

class SeriesListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        pass


class SeriesSerializer(serializers.Serializer):
    class Meta:
        list_serializer_class = SeriesListSerializer
