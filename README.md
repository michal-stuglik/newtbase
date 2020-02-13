### NewtBase

The [NewtBase](http://newtbase.eko.uj.edu.pl/) site repository. 
It contains genomic resources obtained through transcriptome sequencing of the Lissotriton montandoni/vulgaris newts and tools (web Blast+) to mine resources with external sequences.


[![Code Health](https://landscape.io/github/michal-stuglik/newtbase/master/landscape.svg?style=flat)](https://landscape.io/github/michal-stuglik/newtbase/master)
[![Build Status](https://travis-ci.org/michal-stuglik/newtbase.svg?branch=master)](https://travis-ci.org/michal-stuglik/newtbase)
[![Code Climate](https://codeclimate.com/github/michal-stuglik/newtbase/badges/gpa.svg)](https://codeclimate.com/github/michal-stuglik/newtbase)
    

### Notes ###
Install, setup, management by project: newtbase-ansible

## on start

### db schema migration
```shell script
docker exec newtbase-web python3 manage.py migrate
```

### db restore (on host)
```shell script
docker exec newtbase-db /usr/bin/pg_restore --if-exists --clean --dbname=newtbase --single-transaction --username=newtbase --host=localhost --port=5432 /newtbase-data/newtbase.dump
```
