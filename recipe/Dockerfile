# OS python which include python in it
FROM python:3

# create folder in container
WORKDIR /app

# envirament
ENV PYTHONUNBUFFERED=1

# copy the requirements.txt file to docker image
COPY requirements.txt requirements.txt

# install all tool from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the recipe project in my directory
COPY . .

# expose the post the recipe project development server will use
EXPOSE 8000
