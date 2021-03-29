from rest_framework import serializers
from .models import SearchEngineUser,SearchHistory

class SearchEngineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchEngineUser
        fields = '__all__'


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'