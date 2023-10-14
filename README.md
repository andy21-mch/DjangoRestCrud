# Simple DRF CRUD

A simple Django REST Framework (DRF) CRUD project.

## Table of Contents

- [Simple DRF CRUD](#simple-drf-crud)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## Features

- Create, read, update, and delete operations (CRUD) for a resource using DRF.
- Authentication and authorization using token-based authentication.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.7 or higher)
- pip (package installer for Python)
- virtualenv (optional but recommended)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/simple-drf-crud.git
cd simple-drf-crud
```

Create and activate a virtual environment (optional but recommended):

```bash
virtualenv env or python3 -m venv myenv
source env/bin/activate  # for Unix/Linux
env\Scripts\activate  # for Windows
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Access the API at http://localhost:8000/api/ in your web browser.

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your forked repository.
Submit a pull request detailing your changes.
License
This project is licensed under the MIT License.
