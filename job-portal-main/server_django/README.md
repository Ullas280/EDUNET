Django backend for Job Portal

Quick setup (Windows PowerShell):

1. Create and activate virtualenv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill DB credentials (or run `docker-compose up -d` to start MySQL service)

4. Run migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional)

```powershell
python manage.py createsuperuser
```

6. Run server

```powershell
python manage.py runserver 8000
```

API endpoints (replace host/port as needed):
- POST /api/v1/user/register
- POST /api/v1/user/login
- POST /api/v1/user/logout

Notes:
- The login endpoint sets a cookie named `token` containing the JWT access token (HttpOnly).
- Update your frontend `VITE_BACKEND_URL` to `http://localhost:8000` in `Client/.env` or `Client/src/utils/constant.js`.
