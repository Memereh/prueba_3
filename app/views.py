from msilib.schema import Class
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TIPO_PRODUCTO,PRODUCTO

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

class TipoProductoApi(APIView):
    def post(self,request):
        if("nombre" not in request.data):
            return Response({"response":"Faltan datos"})
        else:
            nombre = request.data.get("nombre")
            tipoObj = TIPO_PRODUCTO()
            tipoObj.descripcion = nombre
            tipoObj.save()
            return Response({"response":"Tipo producto guardado."})
    def get(self,request):
        lista = TIPO_PRODUCTO.objects.all().values()
        return Response(lista)
    def put(self,request):
        if("id_tipo" in request.data):
            id_tipo = request.data.get("id_tipo")
            try:
                tipoProducto = TIPO_PRODUCTO.objects.get(id_tipo_producto=id_tipo)
            except TIPO_PRODUCTO.DoesNotExist:
                return Response({"response":"Tipo de producto no existe"})
            tipoProducto.descripcion = request.data.get("nombre")
            tipoProducto.save()
            return Response({"response":"Tipo producto Actualizado"})
    def delete(self,request):
        id_tipo = request.data.get("id_tipo")
        try:
            tipoProducto = TIPO_PRODUCTO.objects.get(id_tipo_producto = id_tipo)
        except TIPO_PRODUCTO.DoesNotExist:
            return Response({"response":"tipo de producto no existe"})
        tipoProducto.delete()
        return Response({"response":"tipo de producto eliminado correctamente"})