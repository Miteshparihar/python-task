from rest_framework import serializers
from .models import *

class Bookserializers(serializers.Serializer):
    id = serializers.IntegerField(label="Enter ID :- ")
    title = serializers.CharField(max_length=200)
    author= serializers.CharField(max_length=200)
    lsbn=serializers.CharField(max_length=200)
    Publisher=serializers.CharField(max_length=200)




























































