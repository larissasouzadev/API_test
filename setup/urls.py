from django.urls import path,include
from setup import views 
from setup.views import  ClientAPIView
from setup.views import  CategoryAPIView
from setup.views import SalesAPIView
urlpatterns = [
    path('client_get/', ClientAPIView.as_view(), name='client_get/' ),
    path('client_get/<int:pk>/',ClientAPIView.as_view(),name='client_by_id'),
    path('client_post/',ClientAPIView.as_view(), name='client_post/'),
    path('category_get/', CategoryAPIView.as_view(), name='category_get/'),
    path('category_post/', CategoryAPIView.as_view(), name='category_post/'),
    path('sales_get/', SalesAPIView.as_view(), name='sales_get'),
    path('sales_post/', SalesAPIView.as_view(), name='sales_post'),

]
