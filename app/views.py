from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ApiRespuesta(APIView):
    def get(self,request):
        nombre = request.GET.get("nombre")
        return Response({"response":"Hola "+nombre})
    def post(self,request):
        if ("nombre" not in request.data):
            return Response({"response":"Faltan datos"})
        nombre = request.data.get("nombre")
        return Response({"response":"Hola "+nombre})