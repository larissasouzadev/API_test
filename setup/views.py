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
from rest_framework.permissions import AllowAny

# it may process one by one get(client)
class ClientAPIView(APIView):
    permission_classes = [AllowAny]
    def get( self,request): 
        if request.method =="GET":
            queryset = Client.objects.all()
            serializer = ClientSerializers(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # it may process one by one post(client)

    def post(self, request):
        if request.method =="POST":
             serializer = ClientSerializers(data=request.data)
             if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
                
# it may process one by one get(category)

 # it may process one by one post(category)
  # it may process one by one get(Sales)
   # it may process one by one post(sales)