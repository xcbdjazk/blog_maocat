FROM ubuntu:16.04
MAINTAINER MaoCat "maocatzk@gmail.com"
#源文件有问题?
#ADD sources.list /etc/apt/sources.list


RUN apt-get update \
    && apt-get upgrade -y
WORKDIR /home
RUN apt-get install -y nodejs \
    nodejs-legacy \
    npm
RUN apt-get install -y wget
RUN npm install n -g
RUN  n stable
RUN npm install npm@latest -g
WORKDIR /opt/webapps/django_blog/frontend
RUN node -v
#ENTRYPOINT ["/bin/bash", "django_blog/script/start.sh"]

CMD ["/bin/bash"]
