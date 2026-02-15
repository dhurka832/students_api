## **Student Management System**

A **Student Management System** built with **Django REST Framework** for the backend and **Bootstrap-based frontend** for displaying student records.
This system allows administrators to manage student information efficiently with full CRUD operations via a RESTful API.

- - -

## **Features**

- Add, view, update, and delete **student records**.

- RESTful API endpoints for managing **students** using **serializers and API views**.

- **Bootstrap-based frontend** for user-friendly display of student data.

- - -

## **Requirements** 
    - Python and Django
    - Django REST Framework
    - Python packages: 
       - djangorestframework
       - django-crispy-forms
       - crispy-bootstrap5

- - -

## **API Endpoints**

| Method | Endpoint                           | Description              |
| ------ | ---------------------------------- | ------------------------ |
| GET    | `api/v1/students/`                 | List all students        |
| POST   | `api/v1/students/create/`          | Create a new student     |
| GET    | `api/v1/students/<int:pk>/`        | Retrieve a student by ID |
| PUT    | `api/v1/students/update/<int:pk>/` | Update a student by ID   |
| DELETE | `api/v1/students/delete/<int:pk>/` | Delete a student by ID   |

- - - 

## **Screenshots**

<img width="1920" height="1020" alt="students_api" src="https://github.com/user-attachments/assets/d4c1f569-fdcb-4c52-9285-a5749cb2c966" />
