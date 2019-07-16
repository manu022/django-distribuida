from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from Code import GenderIdentifier
# Create your views here.


class REST(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        def str_join(*args):
            return ''.join(map(str, args))
        gender_identifier = GenderIdentifier.GenderIdentifier("audio", "females.gmm", "males.gmm")
        winner=gender_identifier.process()
        if winner=='male':
            winner='Hombre'
        if winner=='female':
            winner='Mujer'
        data = {
            "edad":'Edad',
            "genero":winner
        }
        return Response(data)