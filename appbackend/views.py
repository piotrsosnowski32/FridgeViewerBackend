from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from typing import Dict
from . import serializers
from . import models


def test(request):
    return HttpResponse("Hi")

class Users(APIView):
    def get(self, request, id: int = None):
        if id == None:     
            users = [user for user in models.User.objects.all()]
        else: 
            users = models.User.objects.filter(id=id)
            
        user_serializer = serializers.UserSerializer(users, many=True)
        return Response(user_serializer.data)

    def post(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Categories(APIView): 
    def get(self, request, id: int = None):
        if id == None:     
            categories = [category for category in models.Category.objects.all()]
        else: 
            categories = models.Category.objects.filter(id=id)
            
        category_serializer = serializers.CategorySerializer(categories, many=True)
        return Response(category_serializer.data)

    def post(self, request):
        category_serializer = serializers.CategorySerializer(data=request.data)
        
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_201_CREATED)

        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Products(APIView): 
    def get(self, request, id: int = None):
        if id == None:     
            products = [product for product in models.Product.objects.all()]
        else: 
            products = models.Category.objects.filter(id=id)
            
        product_serializer = serializers.ProductSerializer(products, many=True)
        return Response(product_serializer.data)

    def post(self, request):
        product_serializer = serializers.ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        