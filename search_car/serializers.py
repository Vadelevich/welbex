from rest_framework import serializers

from search_car.models import Location, Car, Cargo
from search_car.seach_task import search_to_miles, search_delivery
from search_car.validators import ValidateNumber


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['id', ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id', ]
        validators = [
            ValidateNumber(field='number'),
        ]


class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id', ]
        validators = [
            ValidateNumber(field='number'),
        ]


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class CargoListSerializer(serializers.ModelSerializer):
    count_car = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            'pick_up',
            'delivery',
            'weight',
            'count_car',
        )

    def get_count_car(self, instance):
        """ Количество ближайших машин до груза ( =< 450 миль)) """
        search_to_miles(instance)
        return instance.count


class CargoRetrieveSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            'pick_up',
            'delivery',
            'weight',
            'description',
            'description',
            'number'
        )

    def get_number(self, instance):
        """  список номеров ВСЕХ машин с расстоянием до выбранного груза """
        search_delivery(instance)
        return instance.number
