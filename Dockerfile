FROM python:3.9-buster
RUN apt update && apt install -y --no-install-recommends \
    git \
    ffmpeg \
    curl \
    cron \
    mime-support \
    nginx \
    nginx-extras 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata &&\
    TZ=Asia/Taipei &&\
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone &&\
    dpkg-reconfigure -f noninteractive tzdata 
RUN pip install flask==1.1.2 \
    jinja2==2.11.3 \
    markupsafe==1.1.1 \
    itsdangerous==1.1.0 \
    flask_sqlalchemy \
    flask_marshmallow \
    flask_bcrypt \
    flask_cors==3.0.10 \
    imageio==2.9.0 \
    tqdm==4.60.0 \
    Werkzeug==1.0.1 \
    pymysql \
    gunicorn
RUN mkdir /var/log/gunicorn
ADD ./ /imageApi
WORKDIR /imageApi
# RUN cp -r /imageApi/frontend/build /usr/share/nginx/imageApi
# RUN cp /imageApi/nginx.conf /etc/nginx/conf.d/default.conf
# RUN cp /imageApi/nginx.conf /etc/nginx/sites-available/default
RUN cp /imageApi/nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT sh run.sh