Hotel DemandFlow (Producer–Consumer Demo)

A simple Django app where hotel staff create (produce) and fulfill (consume) customer demands.

Features
- Shared dashboard for all staff
- Add demand (Food, Cleaning, Maintenance, Billing, Room Service)
- Update status to In Progress or Completed
- Tracks creator and fulfiller

Quick start

1. Create and activate a virtual environment
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Apply migrations and create a superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the server
```bash
python manage.py runserver
```

5. Open the app
- Visit `http://127.0.0.1:8000/` for the dashboard (login required)
- Visit `http://127.0.0.1:8000/admin/` to manage users and demands

Notes
- All actions are manual to illustrate the Producer–Consumer concept.
- Beginner-friendly code: straightforward models, function-based views, and Bootstrap UI.







