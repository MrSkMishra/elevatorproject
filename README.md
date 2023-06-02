# elevatorproject
# Elevator System API Documentation

## Introduction
This project provides an API for managing elevator systems and performing elevator operations. It allows users to create, retrieve, update, and delete elevators, elevator systems, and elevator assignments. Additionally, it provides endpoints to start an elevator, retrieve elevator status, and get the next destination floor.

## Thought Process
The main goal of this project is to design and implement a flexible and scalable API for managing elevator systems. Here's an overview of the thought process behind the project:

1. Understand the Requirements: Analyze the requirements and functionalities of the elevator system API, including elevator management, system management, elevator assignments, and status retrieval.

2. Design the API Architecture: Choose an appropriate architecture for the API. In this project, the chosen architecture is the Django REST Framework, which provides powerful tools and abstractions for building RESTful APIs.

3. Database Modeling: Design the database schema to store information about elevators, elevator systems, elevator assignments, and destinations. Use Django's object-relational mapping (ORM) to define models and their relationships.

4. API Endpoint Design: Define the API endpoints based on the requirements and functionalities. Determine the URL patterns, HTTP methods, and corresponding view classes for each endpoint.

5. Implement View Classes: Create view classes using Django REST Framework's viewsets and APIView classes. Implement the necessary methods for handling CRUD operations, additional actions, and retrieving specific information.

6. Serializer Implementation: Develop serializers to convert model instances to JSON representations and vice versa. Define fields, relationships, and validation rules in the serializers.

7. Write Unit Tests: Create unit tests to ensure the correctness and reliability of the API. Test each endpoint, view class, and serializer to cover different scenarios and edge cases.

8. Documentation: Provide clear and comprehensive documentation to help users understand the API's functionality, endpoints, serializers, and setup instructions.

9. Code Review and Refactoring: Review the code for readability, maintainability, and adherence to best practices. Refactor the code if necessary to improve its structure and performance.

10. Deployment and Testing: Deploy the API to a server or hosting platform. Test the API endpoints using tools like Postman or cURL to verify their functionality and validate the API contracts.

## Design Decisions
- **Choice of Architecture:** The Django REST Framework was chosen as the architecture for this API project due to its robust features, scalability, and ease of development. It provides built-in support for handling CRUD operations, authentication, serialization, and URL routing.

- **Repository File Structure:** The repository follows a standard Django project structure, with separate directories for the main application, tests, static files, and configuration files. This structure allows for better organization and maintainability of the codebase.

- **Database Modeling:** The database modeling is based on the requirements of the elevator system API. The models represent entities such as Elevator, ElevatorSystem, ElevatorAssignment, and Destination. Relationships between these models are defined using Django's ORM.

- **Plugins or Libraries Used:** The project utilizes the Django REST Framework for building the API, which includes various libraries and plugins for authentication, serialization, and viewsets. The Django ORM is used for database interactions. Additionally, the project may include other libraries as per the specific requirements, such as the `django-cors-headers` library for handling CORS headers.

## API Contracts

### Elevator Endpoints
- `GET /elevators/`: Retrieves a list of all elevators or creates a new elevator.
- `GET /elevators/<int:pk>/`: Retrieves a specific elevator or updates and deletes the elevator.
- `POST /elevators/<int:pk>/start/`: Starts a specific elevator and sets its direction.
- `GET /elevators/list_elevators/`: Retrieves a list of all elevators.

### Elevator System Endpoints
- `GET /elevator-systems/`: Retrieves a list of all elevator systems or creates a new elevator system.
- `POST /elevator-systems/`: Creates a new elevator system.
- `GET /elevator-systems/<int:pk>/`: Retrieves a specific elevator system or updates and deletes the elevator system.

### Elevator Assignment Endpoints
- `GET /elevator-assignments/`: Retrieves a list of all elevator assignments or creates a new elevator assignment.
- `GET /elevator-assignments/<int:pk>/`: Retrieves a specific elevator assignment or updates and deletes the elevator assignment.

### Elevator Status Endpoint
- `GET /elevator-status/<int:elevator_id>/`: Retrieves the status of a specific elevator.

### Next Destination Floor Endpoint
- `GET /elevator-next-destination/<int:elevator_id>/`: Retrieves the next destination floor for a specific elevator.

## Setup, Deployment, and Testing

### Prerequisites
- Python 3.x
- Django 3.x
- Django REST Framework 3.x

### Installation Steps
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create and activate a virtual environment (optional but recommended).
4. Install the project dependencies using the command: `pip install -r requirements.txt`.
5. Configure the database settings in the project's `settings.py` file.
6. Run the database migrations using the command: `python manage.py migrate`.
7. Start the development server with the command: `python manage.py runserver`.

### Testing the API
1. Ensure the development server is running.
2. Open a web browser or use an API testing tool like Postman.
3. Make requests to the API endpoints mentioned in the API contracts section.
4. Validate the responses and ensure the API functions as expected.
5. You can also run the unit tests by executing the command: `python manage.py test`.

## Acknowledgments
The Elevator System API project was developed using the Django framework and the Django REST Framework. We would like to acknowledge the contributions of the Django and Django REST Framework communities for providing excellent documentation, resources, and support. Additionally, we would like to thank the reviewers and contributors who have provided valuable feedback and suggestions.

