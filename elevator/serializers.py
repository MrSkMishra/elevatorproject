from rest_framework import serializers
from .models import *


class ElevatorSerializer(serializers.ModelSerializer):
    direction = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    is_running = serializers.BooleanField(read_only=True)
    is_door_open = serializers.BooleanField(read_only=True)

    def get_direction(self, obj):
        if obj.is_running:
            if obj.destination_floor > obj.current_floor:
                return 'up'
            elif obj.destination_floor < obj.current_floor:
                return 'down'
        return None

    def get_status(self, obj):
        if obj.is_running:
            return f'Elevator {obj.elevator_number} is running'
        else:
            return f'Elevator {obj.elevator_number} is not running'

    class Meta:
        model = Elevator
        fields = ['id', 'elevator_number', 'current_floor', 'destination_floor', 'direction', 'status', 'is_running', 'is_door_open']

class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = '__all__'

class ElevatorAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorAssignment
        fields = '__all__'


class ElevatorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['id', 'elevator_number', 'current_floor', 'destination_floor', 'is_running', 'is_door_open', 'is_working']


class NextDestinationFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['id', 'destination_floor']