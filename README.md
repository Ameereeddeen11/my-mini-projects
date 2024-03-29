# My Recipe project
Firstly I want to say that this project is not finished yet. I will develop it by adding new features and technologies. <br>
This project is a web application for sharing recipes and also you can make recipes from AI with ingredients you have. You can also search for recipes from other websites. Now you can find <a href="https://your-recipe-61b00c24cb63.herokuapp.com/">here</a> it is deployed on Heroku server. Nowadays on my website, you can't generate recipes from AI<br>

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
3. Open the terminal and go to the directory with the project <br>
4. Clone this repository in GitHub <br>
5. Open the directory with the `recipe` project in the terminal <br>
6. Make a `.env` file and add your own secret key for AWS S3, OpenAI API key, and Secret key for Django app and database settings <br>
7. Then run the command `docker-compose up` <br>
8. Open your browser and go to the address `http://localhost:8000/` <br>

If you don't want to use Docker, you can run the project without Docker. <br>
1. Install Python3 on your PC or laptop <br>
2. Clone this repository in GitHub <br>
3. Open the directory with the `recipe` project in the terminal <br>
4. Create a virtual environment with the command `python3 -m venv venv` <br>
5. Activate virtual environment with the command `source venv/bin/activate` <br>
6. Install all requirements with the command `pip install -r requirements.txt` <br>
7. Make a `.env` file and add your own secret key for AWS S3, OpenAI API key, Secret key for Django app, Google API key, and database settings <br>
8. Run the command `python manage.py makemigrations` and then `python manage.py migrate` <br>
9. Run the command `python manage.py runserver` <br>
