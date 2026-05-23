# pdf_project (uploaded copy)

This folder contains a copy of the `pdf_project` Django example (PDF keyword search + highlight).

Files included: minimal core files required to run the project locally (manage.py, project package, `pdfapp` app, templates).

Notes:
- This is a copy placed in the `projects/pdf_project` folder inside the repository for sharing.
- Exclude large or environment-specific files such as virtual environments and the SQLite database.

To run locally:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
