#!/bin/bash
cd sites/apiMaster/apiMaster/tretas
git pull origin master
docker exec nodes sh -c "pip3 install -r /var/www/tretas/requeriments.txt"
docker exec nodes sh -c "/var/www/tretas/apimaster/manage.py migrate"
docker exec nodes sh -c "/var/www/tretas/apimaster/manage.py collectstatic --noinput"
docker exec nodes pkill python3.5
docker exec nodes sh -c "/var/www/tretas/apimaster/manage.py runserver 0.0.0.0:9001"
# docker exec -d nodes gunicorn --pythonpath /var/www clubsat.wsgi -b 0.0.0.0:8001
exit 0
