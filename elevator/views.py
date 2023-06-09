from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Elevator, ElevatorSystem
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status




class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=['get'])
    def list_elevators(self, request):
        elevators = self.get_queryset()
        serializer = self.get_serializer(elevators, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        elevator = self.get_object()
        direction = request.data.get('direction', 'up')
        if elevator.is_running:
            message = f'Elevator {elevator.elevator_number} is already running'
        else:
            elevator.start_running()
            elevator.move_direction(direction)
            message = f'Elevator {elevator.elevator_number} started running {direction}'
        serializer = self.get_serializer(elevator)
        response_data = {
            'message': message,
            'elevator': serializer.data
        }
        return Response(response_data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except ValidationError as e:
            if 'elevator_number' in e.detail:
                error_message = f"Elevator with elevator number {request.data['elevator_number']} already exists."
                return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# class ElevatorViewSet(viewsets.ModelViewSet):
#     queryset = Elevator.objects.all()
#     serializer_class = ElevatorSerializer

#     @action(detail=True, methods=['post'])
#     def elefetch(selfa, request, pk=None):
#         elevator = selfa.filter_queryset(selfa.get_queryset())
#         serializer = selfa.get_serializer(elevator, many=True)
#         return Response(serializer.data)
    
#     # @action(detail=True, methods=['post'])
#     # def start(selfa, request, pk=None):
#     #     elevator = selfa.get_object()
#     #     elevator.start_running()
#     #     elevator.dir('up')
#     #     serializer = selfa.get_serializer(elevator)
#     #     return Response(serializer.data)

#     @action(detail=False, methods=['get'])
#     def list_elevators(self, request):
#         elevators = self.get_queryset()
#         serializer = self.get_serializer(elevators, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=['post'])
#     def direction(selfa, request, pk=None):
#         elevator = selfa.get_object()
#         elevator.direction()
#         serializer = selfa.get_serializer(elevator)
#         return Response(serializer.data)

# class ElevatorSystemViewSet(viewsets.ModelViewSet):
#     queryset = ElevatorSystem.objects.all()
#     serializer_class = ElevatorSystemSerializer








class ElevatorSystemViewSet(APIView):
    def get(self, request, format=None):
        elevator_systems = ElevatorSystem.objects.all()
        serializer = ElevatorSystemSerializer(elevator_systems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ElevatorSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElevatorAssignmentViewSet(viewsets.ViewSet):
    def list(self, request):
        assignments = ElevatorAssignment.objects.all()
        serializer = ElevatorAssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        assignment = ElevatorAssignment.objects.get(pk=pk)
        serializer = ElevatorAssignmentSerializer(assignment)
        return Response(serializer.data)

    def create(self, request):
        serializer = ElevatorAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        assignment = ElevatorAssignment.objects.get(pk=pk)
        serializer = ElevatorAssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ElevatorStatusViewSet(viewsets.ViewSet):
    def retrieve(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(id=elevator_id)
            serializer = ElevatorStatusSerializer(elevator)
            return Response(serializer.data)
        except Elevator.DoesNotExist:
            return Response({"detail": "Elevator not found."}, status=404)


class NextDestinationFloorViewSet(viewsets.ViewSet):
    def retrieve(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(id=elevator_id)
            serializer = NextDestinationFloorSerializer(elevator)
            return Response(serializer.data)
        except Elevator.DoesNotExist:
            return Response({"detail": "Elevator not found."}, status=404)