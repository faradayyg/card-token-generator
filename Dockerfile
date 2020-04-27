FROM python:3
COPY ./supervisord.conf /etc/supervisord.conf
ADD . /var/www
WORKDIR /var/www
RUN apt update
RUN apt install -y supervisor
RUN pip install -r requirements.txt
RUN touch /dev/shm/supervisor.sock
RUN easy_install gunicorn
RUN touch /var/log/gunicorn.log