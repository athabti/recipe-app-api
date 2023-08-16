docker build .
docker-compose up
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

git add .
