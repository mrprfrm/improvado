from django_filters import FilterSet, DateTimeFilter


class SeriesFilterSet(FilterSet):
    weather_time = DateTimeFilter(field_name='timestamp')
