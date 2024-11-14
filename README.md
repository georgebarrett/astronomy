# astronomy

# docker

generate a token
apply user and token to repo secrets
verify token in docker desktop 'personal access tokens'
Dockerfile created
docker-compose.yml created

this is the terminal command for how docker and django will be used together:
docker-compose run --rm app sh -c "python manage.py collectstatic"

# linting 

using flake8

for linting errors, enter into the terminal:
docker-compose run --rm app sh -c "flake8"

# testing

docker-compose run --rm app sh -c "python manage.py test"
