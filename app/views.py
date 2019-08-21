from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .ser import *
class VerView(mixins.CreateModelMixin,GenericViewSet):
    queryset = Verycode.objects.all()
    serializer_class = VerCodeSer

class RegView(mixins.CreateModelMixin,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegSer

class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = LogSer
    def create(self,request):
        ser = LogSer(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data)
        return Response(ser.errors)