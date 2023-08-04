# Pull base imange
FROM python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABALE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

# Set Work Directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Coyp project
COPY . code

