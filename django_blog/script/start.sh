#! /bin/bash
cd /opt/webapps/django_blog
pwd
pip3 install -r requirements.txt
#unlink /var/run/supervisor/supervisor.sock
#unlink /tmp/supervisor.sock
supervisord -c /opt/webapps/django_blog/utils/supervisord.conf