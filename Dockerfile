FROM python:3.12-slim as build

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libpq-dev

COPY appserver /usr/local/bin/appserver
COPY --from=build /opt/docker-image /opt/docker-image

WORKDIR /app

COPY . /app

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install virtualenv && \
    python3 -m virtualenv venv && \
    . venv/bin/activate && \
    python3 -m pip install wheel && \
    python3 -m pip install -r requirements.txt

EXPOSE 8000

RUN python3 -m pip install flask flask-sqlalchemy marshmallow flask-paginate psycopg2-binary


CMD ["python3", "app.py"]
