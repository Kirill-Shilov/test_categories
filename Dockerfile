FROM python:3.9
WORKDIR /code
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_EMAIL=example@example.com
ENV DJANGO_SUPERUSER_USERNAME=admin
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
