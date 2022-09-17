FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/dj_blog

COPY ./requirements.txt /usr/src/dj_blog/requirements.txt

RUN  pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/dj_blog


#CMD ["python", "manage.py", "runserver", "0.0.0.0:9088" ]