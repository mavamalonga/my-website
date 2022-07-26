[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# My-website

My personal portfolio which presents some of my github projects as well as my resume and technical skills.

## Local testing

### Creating Virtual environment and downloading the program:

You need Python 3 (tested on 3.10), git and venv installed on your machine.

Open a terminal and navigate into the folder you want My-website CRM to be downloaded, and run the following commands:

* On Linux or macOS:
```bash
git clone https://github.com/mavamalonga/my-website
cd my-website
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

* On Windows:
```bash
git clone https://github.com/mavamalonga/my-website
cd EpicEvents
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Initiate SQlite database

Open a terminal and navigate into the root of the project (i.e. the folder where is situated manage.py) , and run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### Create a superuser (administrator)

Open a terminal and navigate into the root of the project (i.e. the folder where is situated manage.py) , and run the following command:

```bash
python manage.py createsuperuser
```

You will be prompted an email, first and last name, and a password. That's it, the superuser is created !

### Run My-website CRM

Open a terminal and navigate into the root of the project (i.e. same folder than manager.py), and run the following command:

```bash
python manage.py runserver
```

The admin page will be accessible at http://127.0.0.1:8000/admin.
You can then login with previously created superuser email and password.
It is now possible to populate the database, with some sales or support team members (don't forget to assign roles).

API will be accessible (with Postman for example) at http://127.0.0.1:8000 .

#### Linting

```bash 
cd /path/to/my-website
source venv/bin/activate
flake8
```

#### Unit tests

```bash
d /path/to/my-website
source venv/bin/activate
python manage.py test
```

## Implementation of integration and continuous deployment (CI/CD Pipeline)

### The stages of the CI/CD Pipeline  

### 1) unittest-and-linter 
CircleCi creates a virtual environment, installs the project dependencies and runs all the unit tests for the application. CircleCi then runs flake8 to check the consistency of the code according to the PEP8 rules defined in the setup.cfg file.
If the tests are successful CircleCi moves on to the next job, otherwise the execution stops and CircleCi returns the cause of the failure.
This step does not filter the branches, it will be executed at each commit on a branch of the GitHub repository.

```bash
python manage.py test
flake8 --max-line-length=99
```

### 2) build-and-push-docker-image
CircleCi creates a docker container from the project's Dockerfile and then, 
once the image is created it is published on the assigned Docker Hub account.
This step is only performed for commits made on the `main` branch of the GitHub repository.

```bash 
docker login -u DOCKERHUB_USER -p DOCKERHUB_PASS
docker build -t DOCKERHUB_USER/oc_lettings:lastest .
docker push DOCKERHUB_USER/oc_lettings:lastest
```

### 3) deploy-on-heroku
CircleCi makes the connection with the heroku account thanks to the Key API then, proceeds to the configuration of the production environment by mentioning the values of the variables SECRET_KEY, HEROKU_APP_NAME to identify the application, DEBUG, and dsn for Sentry. <br>
Once the configuration is finished, an image is created from Dockerfile and then deployed to heroku in production.<br>This step only executes for commits made on the `main` branch of the GitHub repository.
<br>

```bash
heroku container:login
heroku container:push web --app NOM_APP_HEROKU
heroku container:release --app NOM_APP_HEROKU web
```

#### Local testing with Docker

- To retrieve an existing image from Docker Hub <br>
```bash
docker pull DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE
docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE
```

- For an existing image in Docker desktop <br>
```bash
docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE
```

### API Documentation

<table>
    <tr>
        <th>API endpoint</th>
        <th>HTTP method</th>
        <th>URI</th>
    </tr>
    <tr>
        <td>Get the list of projects</td>
        <td>GET</td>
        <td>api/project/</td>
    </tr>
    <tr>
        <td>Get a single project</td>
        <td>GET</td>
        <td>api/project/{id}/</td>
    </tr>
    <tr>
        <td>Get the list of badges</td>
        <td>GET</td>
        <td>api/badge/</td>
    </tr>
    <tr>
        <td>Get a single badge</td>
        <td>GET</td>
        <td>api/badge/{id}/</td>
    </tr>
    <tr>
        <td>Get the list of tasks</td>
        <td>GET</td>
        <td>api/task/</td>
    </tr>
    <tr>
        <td>Get a single task</td>
        <td>GET</td>
        <td>api/task/{id}/</td>
    </tr>
</table>

### Contact
For any other questions contact me by email :
mavamalonga.alpha@gmail.com