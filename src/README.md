# django-celery-video-merger
start redis server on ubuntu console:
```
sudo service redis-server start
redis-server
```

run a secondary console in project virtual environment and run:
```
cd src
celery worker -A config --loglevel=info
```
stop redis server
```
Ctrl + c
sudo service redis-server stop
```
