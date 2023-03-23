FROM python:3.8.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

#COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh

RUN pip install -r /code/requirements.txt

COPY . /code

ENV APP_ROOT=/code
RUN chmod -R u+x ${APP_ROOT} && \
    chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT}

#ENTRYPOINT ["/code/docker-entrypoint.sh"]
