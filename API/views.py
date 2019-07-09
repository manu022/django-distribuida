from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class REST(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        def str_join(*args):
            return ''.join(map(str, args))
        
        data = {
            "edad":'Hola',
            "genero":'Chao'
        }
        return Response(data)