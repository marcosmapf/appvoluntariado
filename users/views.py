from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

class UserLoginConfirmation(APIView):

    def get(self, request, format=None):
        content = {
            'status': 'Your access request was permitted'
        }
        return Response(content)