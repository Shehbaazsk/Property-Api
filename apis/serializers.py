from rest_framework import serializers
from .models import State,City,Property


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state']  


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city',]


class PropertySerializer(serializers.ModelSerializer):
    state = StateSerializer()
    city = CitySerializer()

    class Meta:
        model = Property
        fields = ['id','name','address','city','state']

    def create(self,validated_data):
        state = validated_data.pop('state')
        state_obj, created= State.objects.get_or_create(**state)
        city = validated_data.pop('city')
        city_obj, created = City.objects.get_or_create(state=state_obj,**city)
        property=Property.objects.create(city=city_obj,state=state_obj,**validated_data)
        return property
    
    def update(self,instance,validated_data):
        state = validated_data.pop('state')
        stateobj, created = State.objects.get_or_create(**state)
        city = validated_data.pop('city')
        cityobj, created = City.objects.get_or_create(state=stateobj,**city)
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.city=cityobj
        instance.state = stateobj
        instance.save()
        return instance

class CityListSerializer(serializers.ModelSerializer):
    state = StateSerializer()
    class Meta:
        model = City
        fields = ['city','state']

