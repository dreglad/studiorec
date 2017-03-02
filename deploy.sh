#!/bin/bash

echo "Primero dry-run:"

rsync -avz -n --delete --no-perms --no-owner --no-group --exclude "*/__pycache__" --exclude "data/static" --exclude "*/.DS_Store" --exclude ".vagrant/" --exclude "*/local_settings.py" --exclude "*.pyc" ./ root@studiorec.openmultimedia.biz:/vagrant

echo "CUALQUIER TECLA PARA EJECUTAR"
read

rsync -avz --delete --no-perms --no-owner --no-group --exclude "*/__pycache__" --exclude "data/static" --exclude "*/.DS_Store" --exclude ".vagrant/" --exclude "*/local_settings.py" --exclude "*.pyc" ./ root@studiorec.openmultimedia.biz:/vagrant

ssh root@studiorec.openmultimedia.biz "chown -R nginx:nginx /vagrant && /etc/init.d/uwsgi reload"
