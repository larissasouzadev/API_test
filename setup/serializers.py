from rest_framework import serializers
from setup import models
from setup.models import Client, Category, Sales
#  serializers 
class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'