FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app
# Add current directory code to working directory
# ADD . /app/
# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# install environment dependencies
COPY requirements.txt /app/

# Install project dependencies
RUN pip install -r requirements.txt
COPY . /app/

