

# pdf_Search_Keywords

A small Django example that lets users upload a PDF, search for a keyword, and highlights matching text in the PDF preview using pdf.js.

## Features
- Upload PDFs via web form
- Search PDF text for a keyword (case-insensitive)
- Client-side rendering and highlighting using pdf.js
- Auto-scrolls preview to first match
- Minimal Bootstrap-based responsive UI

## Requirements
- Python 3.10+ (tested with 3.12)
- Django 5.2.12
- A browser with JavaScript enabled (pdf.js for rendering)

## Install (local)
1. Create and activate a virtual environment:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Apply migrations:
```powershell
python manage.py migrate
```

4. Create a superuser (optional):
```powershell
python manage.py createsuperuser
```

## Run
```powershell
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser.

## Usage
- Use the form to upload a PDF and enter a keyword.
- The page will render the PDF and highlight occurrences of the keyword.
- Results are client-side (pdf.js); only uploaded files are stored in MEDIA_ROOT.

## Project structure (high-level)
- manage.py — Django CLI entry
- media/pdf_project/ — original project package (settings, urls, wsgi)
- pdfapp/ — app with models, views, templates
- projects/pdf_project/ — bundled copy for sharing
- media/documents/ — uploaded PDFs (MEDIA_ROOT)

## Notes & recommendations
- Add a `.gitignore` to exclude venv, db.sqlite3, and large uploaded files:
  ```
  venv/
  db.sqlite3
  media/documents/
  __pycache__/
  ```
- For production, serve media files via a proper media server and disable `DEBUG`.
- Replace `SECRET_KEY` in settings.py before deploying.

## output link - https://drive.google.com/file/d/1wzSEKDEIO5a7Sdca4DwqK31IkjUXCGwo/view?usp=sharing
