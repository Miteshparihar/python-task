from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status
from django.http import Http404
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class Booklistview(APIView):
    serializers_class = Bookserializers
    def get(self,request,pk=None):
        all_books=Book.objects.all().values()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",all_books)
        return Response({'msg':'List of all books ', 'book':all_books})
    
    def post(self,request,pk=None):
        serializer_class=Bookserializers
        book_class=Bookserializers(data=request.data)
        if(book_class.is_valid()):
            Book.objects.create(
                id=book_class.data['id'],
                title=book_class.data['title'],
                author=book_class.data['author'],
                lsbn=book_class.data['lsbn'],
                Publisher=book_class.data['Publisher'],
            )
        book=Book.objects.all().filter(id=request.data['id']).values()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",book)
        return Response({'msg':'data insert','book':book})
    
    def delete(self,request,pk):
        book=Book.objects.get(id=pk)
        book.delete()
        return Response({'msg':'Data deleted !!!!'})
    
    def put(self,request,pk):
        serializer = Bookserializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            data['id'] = pk
            d = Book(**data).save()
            serializer =Bookserializers(d)
            return Response(serializer.data, status=status.HTTP_200_OK)