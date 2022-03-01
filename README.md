# Cinema ticket

## Startup guide

1. clone

```
git clone this repo
cd cinema
```

2. virtualenv

```
virtualenv -p python3 venv
source venv/bin/activate
```

3. local settings

```
cp main_app/.env.example main_app/.evn
vim main_app/.env
```

4. requirements

```
pip install -r requirements/dev.txt
npm install
```

5. DB and initial data

```
python manage.py migrate
python manage.py import_fake_data
```

6. run server

```
python manage.py runserver
```

7. login credential
```
username: admin
email: admin@example.com
password: asdfqwer
```
