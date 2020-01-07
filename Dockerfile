FROM python:3.8-alpine as builder
RUN apk add --virtual .build-dependencies \
            --no-cache \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre
WORKDIR /opt/venv
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre
WORKDIR /app
COPY . /app
COPY --from=builder /opt/venv /usr/local

ENV PATH="/app:$PATH"
RUN addgroup -S uwsgi && adduser -S -g uwsgi uwsgi; \
    apk del .build-dependencies && rm -rf /var/cache/apk/*
USER uwsgi
CMD uwsgi --ini $PATH_WSGI