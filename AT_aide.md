docker build .
docker-compose up
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

git add .
git commit -am "le 16/08/2023 après correction du gethub sécurity ."
git log
git push origin 
git branch
git checkout "nom de la  brance"
git branch " nom branche"
docker login -u athabti
docker login -u athabti -p dckr_pat_A3UO7w8lg7bW-W1OkBdQHkdWOZs