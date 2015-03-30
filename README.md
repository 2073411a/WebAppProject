# WebAppProject - TetriVS

This is a Web Application made by Team A2 of Glasgow University Web Development course students. It is a free, open-source multi-player Tetris with scorekeeping and leaderboards.

To ensure that the application runs properly, please ensure you have a configuration that's as close to the requirements list in the requirements.txt as possible (slightly different versions might work but not necessarily).

After the application is cloned and requirements set, the application can be run from the terminal with the command:
python manage.py runserver
After that, with your browser, go to the address http://127.0.0.1:8000/. That's where the application will be run.

To flush the database (i.e all users, scores and etc) run the command:
python manage.py flush
However, after you do that, you'll have to make migrations and migrate with the following commands:
python manage.py makemigrations and python manage.py migrate

If you so wish, after flushing, you can repopulate the database with the population script given. For that just run the command:
python populate.py

The application can be tested with the following command:
python manage.py test Tetris

The following is the link to the deployed application in case you want to view the application straight-away:
http://tetrivs.pythonanywhere.com/
