#! /bin/bash
cd /opt/webapps/django_blog
pwd
pip3 install -r requirements.txt
supervisord -c utils/supervisord.conf