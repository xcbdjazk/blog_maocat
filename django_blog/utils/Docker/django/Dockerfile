FROM ubuntu:16.04
MAINTAINER MaoCat "maocatzk@gmail.com"
#源文件有问题?
#ADD sources.list /etc/apt/sources.list
WORKDIR /home
RUN mkdir -p /root/.pip
ADD pip.conf /root/.pip/pip.conf

RUN apt-get update \
    && apt-get upgrade -y
RUN apt-get install -y \
    python3 \
    python3-pip \
    libpq-dev \
    python-dev \
    supervisor \
    openssh-server
RUN mkdir -p /var/run/sshd
WORKDIR /opt/webapps
EXPOSE 8001
#ENTRYPOINT ["/bin/bash", "django_blog/script/start.sh"]

#CMD ["/bin/bash"]
CMD ["/usr/sbin/sshd", "-D"]