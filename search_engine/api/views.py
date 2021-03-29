from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SearchEngineUserSerializer,SearchHistorySerializer
from .models import SearchEngineUser,SearchHistory




@api_view(['GET'])
def user_view(request):
    print(request.query_params.get('search'))
    user = SearchEngineUser.objects.all()
    serializer=SearchEngineUserSerializer(user,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def keyword_view(request):
    history = SearchHistory.objects.all()
    serializer = SearchHistorySerializer(history,many=True)
    return Response(serializer.data)