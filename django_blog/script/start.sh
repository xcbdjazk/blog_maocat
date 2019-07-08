#! /bin/bash
cd /opt/webapps/django_blog
pwd
pip3 install -r requirements.txt
python3 manage.py makemigrations backend
python3 manage.py migrate
#unlink /var/run/supervisor/supervisor.sock
#unlink /tmp/supervisor.sock
supervisord -c /opt/webapps/django_blog/utils/supervisord.conf
/usr/sbin/sshd -D