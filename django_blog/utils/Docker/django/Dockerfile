FROM ubuntu:16.04
MAINTAINER MaoCat "maocatzk@gmail.com"
#源文件有问题?
#ADD sources.list /etc/apt/sources.list 
RUN apt-get update \
    && apt-get upgrade -y
RUN apt-get install -y \
    python3 \
    python3-pip \
    libpq-dev \
    python-dev \
    supervisor
WORKDIR /opt/webapps
EXPOSE 8001
CMD []
ENTRYPOINT ["/bin/bash"]
