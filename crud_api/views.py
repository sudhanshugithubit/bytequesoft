from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from crud_api.models import*
from crud_api.serializers import*


class Categoryviewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Categoryserializer
    



class Brandviewset(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=Brandserializer


class Itemsviewset(viewsets.ModelViewSet):
    queryset=Items.objects.all()
    serializer_class=Itemsserializer


    def retrieve(self, request,pk=None):
        queryset=Items.objects.all()
        item=get_object_or_404(queryset,pk=pk)
        serializer=Itemsserializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer=Itemsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Item is created")

        return Response(serializer.errors)    

    def update(self,request,pk=None):
        queryset=Items.objects.get(pk=pk)
        serializer=Itemsserializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Item is Updated")
        return Response(serializer.errors)    


    def destroy(self, request,pk=None):
        queryset=Items.objects.get(pk=pk)
        queryset.delete()
        return Response("Item is Deleted ")    



    


