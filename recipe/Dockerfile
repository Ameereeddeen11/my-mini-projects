# OS python which include python in it
FROM python:3

# create folder in container
WORKDIR /app

# copy the requirements.txt file to docker image
COPY requirements.txt /app/

# install all tool from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the recipe project in my directory
COPY . /app/

# expose the post the recipe project development server will use
EXPOSE 8000

# comand for running project
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]