# astronomy

# setup

1. generate github secrets for docker_user and docker_token
2. create a requirements.txt file
3. generate a .gitignore and .dockerignore file
4. add a Dockerfile to set up a docker image for running a python/django app
5. add docker-compose.yml to build the docker image
6. in the terminal run: docker-compose build    (to build the image)

# linting

to run the flake8 linting tool, in the terminal run:
docker-compose run --rm app sh -c "flake8"

# django project creation through docker compose

into the terminal enter:
docker-compose run --rm app sh -c "django-admin startproject app ."

# github actions

in .github/workflows/checks.yml there is a build pipeline that is defined. this runs
every time code is pushed to github and checks for linting and testing errors

# testing

to run tests in django project that uses docker, type this into the terminal:
docker-compose run --rm app sh -c "python manage.py test"