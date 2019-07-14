from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from http.client import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer

# Create your views here.

class REST(APIView, BaseHTTPRequestHandler):
    authentication_classes = []
    permission_classes = []

    def _send_cors_headers(self):
      """ Sets headers required for CORS """
      self.send_header("Access-Control-Allow-Origin", "*")

    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def get(self, request, format=None):
        def str_join(*args):
            return ''.join(map(str, args))
        
        data = {
            "edad":'Hola',
            "genero":'Chao'
        }
        return Response(data)