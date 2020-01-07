#stage 1
FROM python:3.8-alpine as builder
RUN apk add --virtual .build-dependencies \
            --no-cache \
            build-base \
            linux-headers
WORKDIR /opt/venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
#stage 2
FROM python:3.8-alpine
RUN apk add --no-cache pcre
WORKDIR /app
COPY . /app
COPY --from=builder /opt/venv /usr/local
RUN addgroup -S uwsgi && adduser -S -g uwsgi uwsgi; \
    rm -rf /var/cache/apk/*
USER uwsgi
CMD uwsgi --ini $PATH_WSGI