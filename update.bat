git add .
git commit -m 'req'
git push origin master
git push heroku master
heroku run python manage.py migrate