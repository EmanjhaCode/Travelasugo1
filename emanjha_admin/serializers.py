from rest_framework import serializers
from .models import Facilities, Activities, Categories, Location_add, Usa_state

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('id','name','image','history')


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('id','name','image','history')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('id','name','image','history')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location_add
        fields = ('id','name','city','state','country','zipcode','address','logitude','latitude','overview','category',
        'facility','activity','thumbnail1','thumbnail2','thumbnail3','other1','other2','other3')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usa_state
        fields = ('id','name','api_url')
