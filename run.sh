service nginx start
gunicorn -w 2 -b 0.0.0.0:5000 -t 600 app:app 