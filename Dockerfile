# pull the official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

# The local execution needs its variables
# ENV SECRET_KEY ='+2(1l%n+@%(nm7en0_3k24wf7yix8!rxhq&)3i6#sp!e93*o33'
# ENV DEBUG = 1

# install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT