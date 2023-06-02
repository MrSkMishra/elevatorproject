from django.urls import path
from .views import (
    ElevatorViewSet,
    ElevatorSystemViewSet,
    ElevatorAssignmentViewSet,
    ElevatorStatusViewSet,
    NextDestinationFloorViewSet
)

elevator_list = ElevatorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

elevator_detail = ElevatorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

elevator_start = ElevatorViewSet.as_view({
    'post': 'start'
})



urlpatterns = [
    path('elevators/', elevator_list, name='elevator-list'),
    path('elevators/<int:pk>/', elevator_detail, name='elevator-detail'),
    path('elevators/<int:pk>/start/', elevator_start, name='elevator-start'),
    path('elevator-systems/', ElevatorSystemViewSet.as_view(), name='elevator-systems'),
]
