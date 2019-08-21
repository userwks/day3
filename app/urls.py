from app import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
rou = DefaultRouter()
rou.register('ver',views.VerView,basename='v'),
rou.register('reg',views.RegView,basename='r'),
rou.register('login',views.LoginView,basename='l'),
urlpatterns = [
    path('',include(rou.urls))
]
