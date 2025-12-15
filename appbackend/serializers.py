from appbackend.models import User, Category, Product
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'fridge_id']
        validators = [UniqueTogetherValidator(queryset=User.objects.all(), fields=['email'])]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        validators = [UniqueTogetherValidator(queryset=Category.objects.all(), fields=['name'])]
     
                
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        validators = [UniqueTogetherValidator(queryset=Product.objects.all(), fields=['name'])]
                               