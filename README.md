# Family Tree Concept

## Overview

The Family Tree Concept project is designed to manage and visualize relationships between family members. It includes functionality for adding members, defining relationships, and querying paths between members.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.11 or later
- pip (Python package installer)
- Virtual environment (recommended)
- mysql

### Installation

1. **Clone the repository:**

   
   git clone  https://github.com/hfsvv/family_tree.git  -b feature/family-shortest-path


2. **Set up a virtual environment::**


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install dependencies::**

pip install -r requirements.txt
Running the Project
Apply database migrations:


python manage.py migrate family_app

3. **Start the development server::**


python manage.py runserver
The server will be available at http://127.0.0.1:8000/.


4. **Running Test Cases::**


Run tests with coverage:


coverage run manage.py test
coverage report
coverage html
The HTML coverage report will be available in the htmlcov directory.


4. **JWT Token Generation::**

JWT Token Generation
You can generate a JWT token using a custom Django management command. This is useful for authentication and authorization purposes.



python manage.py generate_token
{'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsImV4cCI6MTcyNDk5MDI1NH0.LHjiw7stxw7-kGTYfQd8E7HimciVgbQ5tewlni0nxMA'}


5. **JWT Token in header::**


{
    "Authorization":"Bearer {{token}}"
}


6. **Postman Collection::**

A Postman collection for testing the API endpoints is available in the repository. You can find file Family.postman_collection.json. Import this collection into Postman to easily test and interact with the API endpoints.



7. **sample env**

DB_NAME = 'family'
DB_USER = 'root'
DB_PASSWORD = '****'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'