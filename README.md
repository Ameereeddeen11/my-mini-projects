# My Recipe project
Firstly I want to say that this project is not finished yet. I will develope it by adding new features and techlogies. <br>
This project is a web application for sharing recipes and also you can make recipe from AI with ingredients you have. You can also search recipes from other websites. <br>

## Features
- Python 3.11  & Django 4.2.3
- Install via Docker or Pip
- I use PostgreSQL database
- Static files are in AWS S3
- I use API's such as OpenAI API, Google API
- Styling with Bootstrap 5
- I dry forms with crispy forms

## How to run the project with Docker or without Docker
If you want to run the project My Recipe on your PC or laptop, you can use Docker. <br>
1. Install Docker on your PC or laptop <br>
2. Clone this repository in DockerHub https://hub.docker.com/r/amiriddin/recipe-django <br>
3. Open terminal and go to the directory with the project <br>
4. Clone this repository in GitHub <br>
5. Open directory with the `recipe` project in terminal <br>
6. Make a `.env` file and add your own secret key for AWS S3, OpenAI API key, Secret key for django app and database settings <br>
7. Then run the command `docker-compose up` <br>
8. Open your browser and go to the address `http://localhost:8000/` <br>

If you don't want to use Docker, you can run the project without Docker. <br>
1. Install Python3 on your PC or laptop <br>
2. Clone this repository in GitHub <br>
3. Open directory with the `recipe` project in terminal <br>
4. Create virtual environment with the command `python3 -m venv venv` <br>
5. Activate virtual environment with the command `source venv/bin/activate` <br>
6. Install all requirements with the command `pip install -r requirements.txt` <br>
7. Make a `.env` file and add your own secret key for AWS S3, OpenAI API key, Secret key for django app, Google API key and database settings <br>
8. Run the command `python manage.py makemigrations` and then `python manage.py migrate` <br>
9. Run the command `python manage.py runserver` <br>
