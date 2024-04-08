# base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /app

# copy the pipfiles
COPY Pipfile /app/
COPY Pipfile.lock /app/

# install pipenv
RUN pip install pipenv

# install deps
RUN pipenv install
RUN pipenv install fastapi uvicorn

# copy other files
COPY . /app/

# expose port
EXPOSE 8000

# run the server
CMD [ "pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]