from rest_framework import serializers
from crud_api import*
from crud_api.models import Brand, Category, Items

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields="__all__"
      


class Brandserializer(serializers.ModelSerializer):    
    class Meta:
        model=Brand
        fields="__all__"


class Itemsserializer(serializers.ModelSerializer):
    class Meta:
        model=Items    
        fields="__all__"