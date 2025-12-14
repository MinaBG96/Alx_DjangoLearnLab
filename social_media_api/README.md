# Social Media API

## Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Authentication
- POST /api/accounts/register/
- POST /api/accounts/login/
- GET /api/accounts/profile/

## User Model
Custom user with:
- bio
- profile_picture
- followers system

token = 'd0672f96e359fe5a6a3d013b7452dc4074770c17'