#FROM python:3.7.2-alpine3.8
#COPY . /app
#EXPOSE 5000
#RUN pip install -r ./app/requirements.txt
#ENTRYPOINT ["python", "./app/app/startup.py"]

FROM python:3.7-alpine as builder
#FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt ./requirements.txt
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install --install-option="--prefix=/install" -r requirements.txt; \
	apk del .build-deps;

#RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM python:3.7-alpine
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
EXPOSE 5555
RUN addgroup -S uwsgi && adduser -S -g uwsgi uwsgi
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers
USER uwsgi
CMD uwsgi --ini uwsgi.ini
#CMD flask run --host=0.0.0.0
#ENTRYPOINT ["python", "./app/startup.py"]
#CMD ["gunicorn", "-w 4", "main:app"]
#CMD gunicorn --bind=0.0.0.0:8000 "app.startup:home()"