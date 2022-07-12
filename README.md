[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# My-website

My personal portfolio which presents some of my github projects as well as my resume and technical skills.

## Local testing

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

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

#### Tests unitaires

```bash
d /path/to/my-website
source venv/bin/activate
python manage.py test
```

## Mise en place de l'intégration et déploiement continu (Pipeline CI/CD)

### Les étapes du Pipeline CI/CD 

### 1) unittest-and-linter 
CircleCi créer un environnement virtuel, installe les dépendances du project et éxécute l'ensemble des tests unitaires de l'application puis, CircleCI lance flake8 pour vérifier la confomité du code selon les règles PEP8 définit dans le fichier setup.cfg.
Si les tests réussissent CircleCi passe au job suivant, sinon l'éxécution s'arrête puis CircleCi renvoie la cause de l'echec.
Cette étape ne filtre pas les branches, elle sera éxécutée lors de chaque commit sur une branche du repository GitHub.

Vous pouvez éxécuter ces étapes avec une container docker en local.
- Ouvrez un terminal et déplacez vous dans le répertoire racine du project
- Lancer la commande `docker build --tag app_name:latest .` 
- Ouvrez Docker desktop, cliquez sur images puis lancez le container créee avec le bouton run
- Allez dans containers/app et ouvrez le terminal CLI du container
- Tapez les commandes suivantes: <br>
    `python manage.py test` <br>
    `flake8 --max-line-length=99` <br>

### 2) build-and-push-docker-image
CircleCi crée un container docker à partir du fichier Dockerfile du projet puis, 
une fois l'image créee elle est publiée sur le compte Docker Hub assigné.
Cette étape s'éxécute uniquement pour les commits faite sur la branche `main` du repository GitHub.

Pour faire la même chose en local.
- Ouvrez un terminal et déplacez vous dans le répertoire racine contenant le fichier Dockerfile
- Tapez les commandes suivantes : <br>
    `docker login -u DOCKERHUB_USER -p DOCKERHUB_PASS` <br>
    `docker build -t DOCKERHUB_USER/oc_lettings:lastest .` <br>
    `docker push DOCKERHUB_USER/oc_lettings:lastest` <br>

### 3) deploy-on-heroku
CircleCi fait la liaison avec le compte heroku grâce à l'API Key puis, procède à la configuration de l'environemment de production en mentionnant les valeurs des variables SECRET_KEY, HEROKU_APP_NAME pour identifier l'application, DEBUG, et dsn pour Sentry. <br>
Une fois la configuration finit, une image et créee à partir de Dockerfile puis deployée sur heroku en production.<br>Cette étape s'éxécute uniquement pour les commits faite sur la branche `main` du repository GitHub.
<br>

Pour faire la même chose manuellement.
Tout d'abord veillez à enregistrer les variables SECRET_KEY, DEBUG, dsn dans le fichier .env
du projet puis, suivez les étapes suivantes:
- Ouvrez un terminal et déplacez vous dans le répertoire racine contenant le fichier Dockerfile
- Tapez les commandes suivantes : <br>
    `heroku container:login` <br>
    `heroku container:push web --app NOM_APP_HEROKU` <br>
    `heroku container:release --app NOM_APP_HEROKU web` <br>

#### Lancer l'application en local
Si vous souhaitez éxécuter votre application en local avec une image docker, suivez les étapes suivantes: <br>
- Pour récupérer une image existant depuis Docker Hub <br>
    `docker pull DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>
    `docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>
- Pour une image existante dans Docker desktop <br>
    `docker run --name IMAGE_NAME -d -p PORT:PORT DOCKERHUB_USER/IMAGE_NAME:TAG_IMAGE` <br>

### Contact
Pour tout autre question contactez-moi par mail : mavamalonga.alpha@gmail.com