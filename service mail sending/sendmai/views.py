from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response
from .models import mail
from .serializer import mail_serializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def mail_post(request):
    #post
    if request.method=='POST':
        serializer = mail_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
