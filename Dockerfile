FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

COPY ./app /owlvey/app
WORKDIR /owlvey

ENTRYPOINT ["python", "app/startup.py"]
