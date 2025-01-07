# Join Backend

Welcome to the backend repository for **Join**, a kanban-based project management tool. Join was created as an educational project during a web development bootcamp at the Developer Akademie.

## Overview

Join is designed to help users manage tasks and projects using the kanban methodology. While the frontend provides a visual interface, this repository contains only the backend, which powers the application's core functionality.

### Features
- RESTful API to manage tasks, contacts, and project data.
- SQLite database (not included in the repository, see `.gitignore`).
- Basic authentication for user login.
- API endpoints to handle CRUD operations for tasks and contacts.

## Requirements

To run the backend locally, ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/join-backend.git
   cd join-backend

2. Create a virtual environment and activate it:
  bash
  Code kopieren
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate

3. Install the dependencies:
  pip install -r requirements.txt

4.Apply database migrations:
  python manage.py migrate

5.Run the development server:
  python manage.py runserver

 ## Usage
 API Endpoints
 The backend provides the following endpoints:

 ## Tasks
 GET /tasks/: Fetch all tasks.
 POST /tasks/: Create a new task.
 PUT /tasks/<id>/: Update a task.
 DELETE /tasks/<id>/: Delete a task.

 ## Contacts
 GET /contacts/: Fetch all contacts.
 POST /contacts/: Create a new contact.
 PUT /contacts/<id>/: Update a contact.
 DELETE /contacts/<id>/: Delete a contact.

## Database
 The backend uses an SQLite database. The db.sqlite3 file is excluded from this repository for security reasons. To set up your own database, apply migrations as described above.

## Contributing
 This project is an educational exercise and is not intended for extensive business usage. Contributions are welcome, but please note this is not actively maintained.

## Contact
 For questions or feedback, feel free to contact us at: mail@kowalczyk-karol.de

 Enjoy using Join!
