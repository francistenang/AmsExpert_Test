FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /var/www/amexpert/Database_project/project/
ENV STATIC_URL /data_base_/static
ENV STATIC_PATH /var/www/amexpert/Database_project/project/data_base_/static
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP run.py
ENV FLASK_ENV development
ENV FLASK_DEBUG True
ENV DB_DRIVER=postgres
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_USERNAME=postgres
ENV DB_PASSWORD=1234
ENV DB_DBNAME=amexpert
COPY . ./requirements.txt /var/www/amexpert/Database_project/project/
RUN pip install -r ./requirements.txt

COPY . ./docker-entrypoint.sh /var/www/amexpert/Database_project/project/

EXPOSE 5000
RUN ["chmod", "+x", "./docker-entrypoint.sh"]
RUN FLASK_DEBUG=FALSE
RUN flask_env=production
RUN FLASK_APP=run.py
ENTRYPOINT ["./docker-entrypoint.sh"]
