FROM python:3.7

ARG requirements=requirements/prod.txt
ENV DJANGO_SETTINGS_MODULE=newtbase.settings.prod

RUN apt-get update && apt-get install -y ncbi-blast+

WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements/*.txt /app/requirements/
RUN pip install -r ${requirements}

# Now copy in our code, and run it
#ADD blastplus/ blastplus/
COPY newtbase newtbase
COPY static static
COPY manage.py /app/

RUN python manage.py collectstatic

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]