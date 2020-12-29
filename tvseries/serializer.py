from rest_framework import serializers

from tvseries.models import TvSeries


class TvSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvSeries
        fields = '__all__'
