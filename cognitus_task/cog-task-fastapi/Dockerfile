FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY docker-celery-entrypoint.sh /app

COPY . /app

ENV APP_ROOT=/app
RUN chmod -R u+x ${APP_ROOT} && \
 chgrp -R 0 ${APP_ROOT} && \
 chmod -R g=u ${APP_ROOT}

ENV PORT=8081


#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]