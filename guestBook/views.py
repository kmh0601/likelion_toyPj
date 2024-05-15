from django.shortcuts import render

from .serializers import guestBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import Http404
from guestBook.models import *

class guestBookList(APIView):
    serializer_class = guestBookSerializer
    
    def post(self, request, format=None):
        serializer = guestBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, format=None):
        guestBooks = GuestBook.objects.all()
        serializer = guestBookSerializer(guestBooks, many = True)
        return Response(serializer.data)

class guestBookDetail(APIView):

	def get(self, request, id):
		guestBook =  get_object_or_404(GuestBook,id=id)
		serializer = guestBookSerializer(guestBook)
		return Response(serializer.data)
	
	def put(self, request, id):
		guestBook = get_object_or_404(GuestBook,id=id)
		serializer = guestBookSerializer(guestBook, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, id):
		guestBook = get_object_or_404(GuestBook, id=id)
		serializer = guestBookSerializer(guestBook, data=request.data)
		serializer.check_object_permissions(self.request, guestBook)
		guestBook.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
