from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
class UserView(APIView):
    def get(self, request):
        users = User.objects.order_by('id').filter(is_superuser=False)
        result = UserDetailsSerializer(users, many=True).data
        return Response({'ok': True, "members": result}, status=status.HTTP_200_OK)