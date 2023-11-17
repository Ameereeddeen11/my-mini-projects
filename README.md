# Welcome to my mini projects
Here you can checkout some of my mini projects such as My Recipes, my python bot for Telegram, frond-end of my school project.<br>
I will develope this repository by adding another own projects


# My Recipe project
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
7. Make a `.env` file and add your own secret key for AWS S3, OpenAI API key, Secret key for django app and database settings <br>
8. Run the command `python manage.py makemigrations` and then `python manage.py migrate` <br>
9. Run the command `python manage.py runserver` <br>

