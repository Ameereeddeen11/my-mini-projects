# Welcome to my mini projects
Here you can checkout some of my mini projects such as Recipes, my python bot to Telegram, frond-end of my school project.<br>
I will develope this repository by adding another own projects


# Recipe project
If you want to run the project Recipe to your computer. You can use docker. 
1. Clone the repository 
2. In your directory of your Command Line run the docker compose by using command: <strong>docker-compose run --rm app django-admin startproject main .</strong>
<br>It will create database and folder <strong>.mysql_data </strong> in your directory <br>
The resent why you have to run this command <strong>docker-compose run --rm app django-admin startproject main .</strong> is when I dockerized the project I have all most done the project. 
If you don't do this step it will show the error that says it can't connect to database. 
3. Then write the command: <strong>docker-compose up</strong> <br>
It will run Recipe project 
4. Open your browser and write this host: <strong>127.0.0.0:8000</strong>
5. It will show you "This page don't found" so after host write path /recipe/ That means you have to write this: <strong>127.0.0.0:8000/recipe/ 