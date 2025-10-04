from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import serializers
from . import models

def test(request):
    return HttpResponse("Hi")

class ListUsers(APIView):

    @api_view(['GET'])
    def get(self, request={}, format=None):
        users = [user for user in models.User.objects.all()]
        print(users, "$$$$$$$$$$$$")
        user_serializer = serializers.UserSerializer(users, many=True)
        print(user_serializer.data)
        return Response(user_serializer.data)
