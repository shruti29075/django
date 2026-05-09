# Todo App Manager
<img width="1917" height="972" alt="image" src="https://github.com/user-attachments/assets/1e950a1c-3e6a-49af-9fe8-c175e9a787d9" />


A Django-based To-Do list web application with user authentication, task management, and file upload support.

## Features

- User registration and login
- Logout support
- Add tasks with a title, completed status, and optional document upload
- View only your own tasks after login
- Delete tasks
- Toggle task completion status
- Responsive UI for desktop and mobile

## Tech Stack

- Python
- Django
- SQLite
- HTML, CSS

## Project Structure

```text
todo-app manager/
|-- manage.py
|-- db.sqlite3
|-- README.md
|-- .gitignore
|-- todo/
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   `-- templates/todo/
|       |-- login.html
|       |-- register.html
|       `-- task_list.html
`-- todo_project/
    |-- settings.py
    |-- urls.py
    |-- asgi.py
    `-- wsgi.py
```

## Main Pages

- `/register/` - Create a new account
- `/login/` - Login page
- `/` - Task dashboard
- `/logout/` - Logout action

## Setup Instructions

1. Open the project folder:

```powershell
cd "c:\Users\Shlok\OneDrive\Desktop\Django\Projects\To-Do list Web application\todo-app manager"
```

2. Activate the virtual environment if you have one:

```powershell
..\venv\Scripts\Activate.ps1
```

3. Install dependencies if needed:

```powershell
pip install django
```

4. Apply migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:

```powershell
python manage.py runserver
```

6. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Notes

- Each user can only see their own tasks.
- Uploaded documents are stored under `media/documents/`.
- The app uses SQLite for local development.

## Future Improvements

- Edit task feature
- Task due dates
- Search and filter tasks
- Better dashboard analytics
- Deployment support for production
