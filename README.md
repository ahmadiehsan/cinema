# TODO (ehsan) update this file

# Cinema ticket!

# quick start

```
git clone this repo
cd cinema

virtualenv -p python3 venv
source venv/bin/activate

cp main_app/.env.example main_app/.evn
vim main_app/.env

pip install -r requirements/dev.txt
python manage.py npminstall
python manage.py migrate
python manage.py initialize
python manage.py runserver
```
