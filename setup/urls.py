from django.urls import path,include
from setup import views 
from setup.views import  ClientAPIView
urlpatterns = [
    path('client_get/', ClientAPIView.as_view(), name='client_get/' ),
    path('client_post/',ClientAPIView.as_view(), name='client_post/'),
]
