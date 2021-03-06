__author__ = 'root'


import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.txt')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=['desenvolvimento'],
    include_package_data=True,
    # license='BSD License',  # example license
    description='Site para DACOM UTFPR-CM.',
    long_description=README,
    url='https://www.example.com/',
    author='Humberto Gonçalves',
    author_email='humberto.g.moreira@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)