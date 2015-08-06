# newtbase
Newtbase website repository


### Install


1.  BioPython:

        pip install biopython

2.  Python-PostgreSQL Database Adapter:

        pip install psycopg2

3.  django-blastplus:

        pip install django-blastplus

3.  Blast DB setup e.g. :

        makeblastdb -in reference_helveticus.fa -dbtype nucl -parse_seqids -hash_index

### Update

1.  NewtBase:

        git xxx

2.  django-blastplus:

        pip install --upgrade django-blastplus

3.  update/reload static files:

        python manage.py collectstatic

4.  WWW server restart e.g. :

        sudo service apache2 restart

