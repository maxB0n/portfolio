# 🚀 Deploying Your Django Portfolio
### GitHub + Railway (Free Hosting)

---

## STEP 1 — Set Up Your Local Environment

Open a terminal in your project folder (`portfolio_site/`).

```bash
# Create the virtual environment
python -m venv .venv

# Activate it (Windows PowerShell)
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Test locally — visit http://127.0.0.1:8000
python manage.py runserver
```

✅ You should see your portfolio at `http://127.0.0.1:8000`

---

## STEP 2 — Push to GitHub

### 2a. Create a new GitHub repo
1. Go to **github.com** → click **New Repository**
2. Name it `portfolio` (or anything you want)
3. Set it to **Public** (required for free Railway hosting)
4. Do **NOT** check "Add README" — your folder already has files
5. Click **Create Repository**

### 2b. Initialize Git and push

```bash
# In your portfolio_site/ folder:
git init
git add .
git commit -m "Initial commit: Django portfolio"

# Connect to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
git branch -M main
git push -u origin main
```

✅ Refresh GitHub — you should see all your files

---

## STEP 3 — Deploy to Railway (Free Hosting)

Railway gives you a free hobby plan with a public URL. No credit card needed.

### 3a. Sign up & connect
1. Go to **railway.app** → click **Login with GitHub**
2. Authorize Railway to access your GitHub account

### 3b. Create a new project
1. Click **New Project**
2. Select **Deploy from GitHub repo**
3. Choose your `portfolio` repository
4. Railway will detect it's a Python project automatically

### 3c. Add environment variables
In your Railway project dashboard:
1. Click your service → **Variables** tab
2. Add these variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | (generate one — see below) |
| `DEBUG` | `False` |
| `DJANGO_SETTINGS_MODULE` | `config.settings` |

**To generate a SECRET_KEY**, run this in your terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and paste it as the `SECRET_KEY` value.

### 3d. Run migrations on Railway
In Railway dashboard → your service → **Shell** tab:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 3e. Get your public URL
1. Go to your service → **Settings** tab
2. Under **Networking** → click **Generate Domain**
3. Railway gives you a free URL like `portfolio-production-abc1.up.railway.app`

✅ Your portfolio is live on the internet!

---

## STEP 4 — Updating Your Site

Every time you make changes:

```bash
# Stage your changes
git add .

# Commit with a description
git commit -m "Update project descriptions"

# Push to GitHub
git push
```

Railway automatically detects the push and **redeploys** your site within ~2 minutes. No extra steps.

---

## TROUBLESHOOTING

**Static files not loading on Railway?**
Make sure `whitenoise` is in `requirements.txt` and `MIDDLEWARE` in settings. Run `collectstatic` again.

**"DisallowedHost" error?**
Check that `ALLOWED_HOSTS = ['*']` is set in `settings.py` (already done in your version).

**Migrations error?**
Run `python manage.py makemigrations portfolio` then `python manage.py migrate` again.

**Check Railway logs:**
Railway dashboard → your service → **Logs** tab. This shows you exactly what's failing.

---

## PROJECT STRUCTURE (for reference)

```
portfolio_site/
├── config/
│   ├── __init__.py
│   ├── settings.py      ← Django configuration
│   ├── urls.py          ← Root URL router
│   └── wsgi.py          ← Production server entry point
├── portfolio/
│   ├── templates/
│   │   └── portfolio/
│   │       └── index.html   ← Your HTML template (DTL)
│   ├── __init__.py
│   ├── admin.py         ← Register models for /admin
│   ├── models.py        ← Database schemas (Project, Skill)
│   ├── urls.py          ← App URL patterns
│   └── views.py         ← Logic: assembles context, renders template
├── .gitignore           ← Excludes .venv, db.sqlite3, etc.
├── manage.py            ← Django management CLI
├── Procfile             ← Tells Railway to use gunicorn
└── requirements.txt     ← Python dependencies
```

---

*Built for Maximilian C. Bonilla — NYU Tandon School of Engineering*
