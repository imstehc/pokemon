FROM registry.gitlab.com/syeriwon/study-projects/pokemon-base:1.0

ADD . ${BASE_FOLDER}

RUN cd ${BASE_FOLDER} && python manage.py collectstatic --noinput -v 3
