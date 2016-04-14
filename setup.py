#!/usr/bin/env python

from setuptools import setup

setup(
    name='everyportland',
    version='0.0.1',
    description='every word but from portland',
    url='https://github.com/tpinecone/everyportland',
    author='pinecone',
    author_email='teriankoscik@gmail.com',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
    keywords='bots',
    packages=['everyportland'],
    install_requires = ['tweepy==3.4.0', 'inflect==0.2.5'],
    entry_points = {
          'console_scripts': [
              'everyportland  = everyportland.__init__:main'
          ]
    },
)
