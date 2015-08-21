NewtBase
========

The NewtBase site repository (http://newtbase.eko.uj.edu.pl/). It contains genomic resources obtained through transcriptome sequencing of the Lissotriton montandoni/vulgaris newts
and tools (web Blast+) to mine resources with external sequences.



[![Code Health](https://landscape.io/github/michal-stuglik/newtbase/master/landscape.svg?style=flat)](https://landscape.io/github/michal-stuglik/newtbase/master)
[![Build Status](https://travis-ci.org/michal-stuglik/newtbase.svg?branch=master)](https://travis-ci.org/michal-stuglik/newtbase)
[![Code Climate](https://codeclimate.com/github/michal-stuglik/newtbase/badges/gpa.svg)](https://codeclimate.com/github/michal-stuglik/newtbase)
    

Requirements
------------

####  Python 2.7

####   pip & virtualenv (optional)

    sudo apt-get install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv


####   Django 1.7-1.8

    pip install django


####   Python-PostgreSQL Database Adapter

    (e.g. with pip) pip install psycopg2


#### BioPython

    (e.g. with pip) pip install biopython


####  django-blastplus:

    pip install django-blastplus


Installation
------------


1.  Clone site

    git clone https://github.com/michal-stuglik/newtbase.git


2.  Collect static files

    python manage.py collectstatic

3.  Setup database

    to be complemented ...


4.  Setup server WWW

    to be complemented ...




Update
------

    to be complemented ...



