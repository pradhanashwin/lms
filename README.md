Library Management System
This project is developed using Django web framwork.gi 

## Project structure

```bash
lms
├── books
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── all.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── form.css
│   │   │   ├── index.css
│   │   │   └── style.css
│   │   ├── icon
│   │   │   ├── LICENSE.txt
│   │   │   ├── css
│   │   │   │   └── all.css
│   │   ├── images
│   │   └── js
│   │       ├── add_book.js
│   │       ├── add_book_issue.js
│   │       ├── bootstrap.min.js
│   │       ├── jquery.min.js
│   │       └── view_books.js
│   ├── templates
│   │   ├── add_book_issue.html
│   │   ├── add_new_book.html
│   │   ├── add_new_individual.html
│   │   ├── base.html
│   │   ├── edit_individual_data.html
│   │   ├── index.html
│   │   ├── issue_records.html
│   │   ├── show_individuals.html
│   │   ├── view_book_record.html
│   │   └── view_books.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── deploy
│   ├── Dockerfile
│   └── docker-compose.yml
├── lms
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   └── book_images
│       └── image-20240315-080337.png
├── readme.md
└── requirements.tx
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory or rename
`example.env` to `.env` and place all
environment variables here

An example of .env file:
```bash
SECRET_KEY=foo
DB_ENGINE=django.db.backends.postgresql
DB_NAME=lms
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

**Attention:** Please make sure to set up the required environment variables or configuration files before running the application. Failure to provide these settings may result in errors during application startup.

## Installation

### Using virtual environment
**Create a virtual environment and install dependencies using Conda**

1. Create a New Conda Environment:

   Open your terminal or command prompt and use the following command to create a new Conda environment. Replace `myenv` with the name you'd like to give to your environment.

   ```shell
   conda create --name lms_env python=3.9
   ```

   This command will create a new Conda environment named `lms_env` and use Python 3.9.

2. Activate the Conda Environment**:

   Once the environment is created, activate it using the following command:

   ```shell
   conda activate lms_env
   ```

   Replace `lms_env` with the name of your Conda environment.

After you activated the enviroment install the dependencies.

```bash
pip install -r requirements.txt
```

create the database with the same name in the environment file
```shell
   psql postgres
   create database "lms";
   \q
   ```
after quiting the psql run following commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver   
``` 

This will start the server on the configured host.


### Using Docker
Need to figure out static file using docker
You can start the project with Docker using the following command:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```
This command will start the server on port 8000.


### Running tests
In the directory where there is migrate.py run 
```bash
python manage.py test   
``` 
