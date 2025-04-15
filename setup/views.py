from django.shortcuts import render
from django.http import JsonResponse
import rest_framework
from rest_framework import serializers
from setup import serializers
from setup.serializers import ClientSerializers, CategorySerializers, SaleSerializers
from rest_framework import status
from setup import models
from setup.models import Client, Category, Sales
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


# class APIVIEW using the CBV method
class ClientAPIView(APIView):
    # it may process one by one get(client)
    def get(self, request): 
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(status=status.HTTP_200_OK)

    # it may process one by one post(client)
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
# # it may process one by one get(category)
class CategoryAPIView(APIView):
    pass
 # it may process one by one post(category)
  # it may process one by one get(Sales)
   # it may process one by one post(sales)