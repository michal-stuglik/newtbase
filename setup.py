import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='newtbase',
    version='1.0.0',
    packages=['newtbase'],
    include_package_data=True,
    license='GPL v.2 License',
    description='A web app (Django) with genomic resources obtained through transcriptome sequencing of the \ '
                'Lissotriton montandoni/vulgaris newts.',
    long_description=README,
    url='https://github.com/michal-stuglik/newtbase',
    author='Michal Stuglik',
    author_email='michal@codelabs.info',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
