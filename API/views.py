from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from Code import GenderIdentifier
# Create your views here.
from .serializers import FileSerializer
from .models import File
import os
import glob
import shutil


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class REST(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        def str_join(*args):
            return ''.join(map(str, args))
        gender_identifier = GenderIdentifier.GenderIdentifier("audio", "females.gmm", "males.gmm")
        winner=gender_identifier.process()
        shutil.rmtree('audio/')
        os.mkdir('audio/')
        if winner=='male':
            winner='Hombre'
        if winner=='female':
            winner='Mujer'
        data = {
            "edad":'Edad',
            "genero":winner
        }
        return Response(data)