### Welcome to vault security app!

 This app will allow you to track who is inside the vault and how long he has been there. Tired of your employees stealing from your vault? Do not hesitate, install this app immediately!

### Installation

You need `python3` to run this app.

Installation:
```
git clone # && cd django-orm-watching-storage
python -m venv venv && . ./venv/bin/activate
pip install -r requirements.txt
```

### Database credentials

Put your database credentials into `.env` file, like this:

```
DB_HOST='somehost'
DB_PORT='5434'
DB_NAME='db-name'
DB_USER='db-user'
DB_PASSWORD='db-password'
```

### Debug mode
To enable developoer mode add `DEBUG` key with any value to `.env` or use it ad environment variable when launching app.
```
DEBUG=1
```

### Run app!

Finally, if everything is done, you may enjoy your brand new shiny securety app!

Run it with command:

```
python manage.py runserver localhost:8000
```

Ofcourse you may want to run in on your desired host or port.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/). In this excersize i learned how to use django-orm models to get and filter data from database and how to run django server locally.
