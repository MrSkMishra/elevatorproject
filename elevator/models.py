from django.db import models
from django.utils import timezone



class Elevator(models.Model):
    elevator_number = models.IntegerField(unique=True)
    current_floor = models.IntegerField(default=0)
    destination_floor = models.IntegerField(blank=True, null=True)
    is_running = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return f'Elevator {self.elevator_number}'

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def open_door(self):
        self.is_door_open = True


    def direction(self,d):
        self.direction = d

    def close_door(self):
        self.is_door_open = False

    def start_running(self):
        self.is_running = True

    def stop_running(self):
        self.is_running = False

    def display_status(self):
        if self.is_running:
            status = f'Elevator {self.elevator_number} is moving'
        else:
            status = f'Elevator {self.elevator_number} is not running'
        if self.is_door_open:
            status += ' and the door is open'
        else:
            status += ' and the door is closed'
        status += f' at floor {self.current_floor}'
        return status

    def handle_requests(self, requests):
        if not requests:
            return

        destination_floors = [req['floor'] for req in requests]
        closest_floor = min(destination_floors, key=lambda floor: abs(floor - self.current_floor))
        self.destination_floor = closest_floor

        if closest_floor > self.current_floor:
            self.move_up()
        elif closest_floor < self.current_floor:
            self.move_down()
        else:
            self.stop_running()
            self.open_door()
            self.close_door()

            # Handle user requests at the current floor
            current_floor_requests = [req for req in requests if req['floor'] == self.current_floor]
            # Additional logic to handle the requests, e.g., process entering or exiting passengers

        self.save()

class ElevatorSystem(models.Model):
    elevators = models.ManyToManyField(Elevator)

    @property
    def total_elevators(self):
        return self.elevators.count()

    def __str__(self):
        return f'Elevator System with {self.total_elevators} elevators'


class ElevatorAssignment(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    assignment_time = models.DateTimeField(default=timezone.now)
    requested_floor = models.PositiveIntegerField()

    def __str__(self):
        return f"Elevator {self.elevator.elevator_number} assignment at floor {self.requested_floor}"