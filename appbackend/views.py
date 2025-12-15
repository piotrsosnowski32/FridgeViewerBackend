from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from . import models


class Users(APIView):
    """
    Request users from database.
    Post users data to database.
    """
    def get(self, request, id: int = None):
        if not id:
            users = models.User.objects.all()
            user_serializer = serializers.UserSerializer(users, many=True)
        else:
            users = get_object_or_404(models.User, id=id)
            user_serializer = serializers.UserSerializer(users)

        return Response(user_serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id: int = None):
        if not id:
            return Response(data={'message': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = get_object_or_404(models.User, id=id)
            user_serializer = serializers.UserSerializer(user, data=request.data, partial=True)

            if user_serializer.is_valid():
                user_serializer.save()

        return Response(data={'message': 'User updated successfully.'}, status=status.HTTP_201_CREATED)
    
    
class Categories(APIView): 
    def get(self, request, id: int = None):
        if not id:
            categories = models.Category.objects.all()
            category_serializer = serializers.CategorySerializer(categories, many=True)
        else: 
            categories = get_object_or_404(models.Category, id=id)
            category_serializer = serializers.CategorySerializer(categories)

        return Response(category_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_serializer = serializers.CategorySerializer(data=request.data)
        
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)

        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id: int = None):
        if not id:
            return Response(data={'message': 'Category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            category = get_object_or_404(models.Category, id=id)
            category_serializer = serializers.CategorySerializer(category, data=request.data, partial=True)

            if category_serializer.is_valid():
                category_serializer.save()

        return Response(data={'message': 'Category updated successfully.'}, status=status.HTTP_200_OK)
    
class Products(APIView): 
    def get(self, request, id: int = None):
        if not id:
            products = models.Product.objects.filter(is_active=True).order_by('expiry_date')
            product_serializer = serializers.ProductSerializer(products, many=True)
        else: 
            products = get_object_or_404(models.Product, id=id)
            product_serializer = serializers.ProductSerializer(products)

        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = serializers.ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id: int = None):
        if not id:
            return Response(data={'message':'Product does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            product = get_object_or_404(models.Product, id=id)
            product_serializer = serializers.ProductSerializer(product, data=request.data, partial=True)

            if product_serializer.is_valid():
                product_serializer.save()

        return Response(data={'message':'Product updated successfully.'}, status=status.HTTP_200_OK)
        