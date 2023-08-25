from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class VehicleSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSize
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer()
    size = VehicleSizeSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    vehicle = VehicleSerializer()
    class Meta:
        model = Rental
        fields = '__all__'

class RentalRateSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer()
    size = VehicleSizeSerializer()

    class Meta:
        model = RentalRate
        fields = '__all__'

class RentalStationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = RentalStation
        fields = '__all__'

class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleAtRentalStation
        fields = '__all__'
