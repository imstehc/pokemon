FROM python:3.7.4-slim-buster
ENV BASE_FOLDER /app

ENV DJANGO_PROJECT_NAME project
ARG INSTALLATION_DEPENDENCY_LIBS="gcc=4:8.3.0-1 python3-dev=3.7.3-1 libssl-dev libcups2-dev linux-libc-dev libpq-dev=11.7-0+deb10u1"
ARG RUNTIME_LIBS="cron authbind=2.1.2 libcups2 libxslt1.1=1.1.32-2.2~deb10u1 libxml2=2.9.4+dfsg1-7+b3 libpq5=11.7-0+deb10u1 cifs-utils=2:6.8-2 gettext"

RUN mkdir ${BASE_FOLDER}
WORKDIR ${BASE_FOLDER}

ADD Pipfile ${BASE_FOLDER}/
ADD Pipfile.lock ${BASE_FOLDER}/
ADD make_env.sh ${BASE_FOLDER}/
ADD requirements.txt ${BASE_FOLDER}/

ADD postgres_ready.py /

RUN apt-get update && \
    apt-get install -y $INSTALLATION_DEPENDENCY_LIBS && \
     apt-get install -y git && \
    apt autoremove -y && \
    apt-get install -y $RUNTIME_LIBS && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv run pip install pip && \
    pipenv install --deploy --system && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache && \
    apt-get remove --purge -y $INSTALLATION_DEPENDENCY_LIBS && \
    addgroup django && \
    adduser --system --no-create-home --disabled-password django && \
    adduser django django && \
    chown -R django:django ${BASE_FOLDER} && \
    chmod +x /postgres_ready.py && \
    touch /etc/authbind/byport/80 && \
    chown django /etc/authbind/byport/80 && \
    chmod 500 /etc/authbind/byport/80
