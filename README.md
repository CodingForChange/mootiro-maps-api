API for Mootiro Maps
======================

A public API for Mootiro Maps.

Requirements for developer enviroment
---------------------------------------------
* Python 2.7
* iPython (recommended)

Requirements for the Python enviroment
-----------------------

The API dependencies are listed in requirements.txt file.

* bottle
* psycopg2

Installing and configuring the sample database
-------------------------------------------------

Before you run the API, you must have to install and configure a local database. For this project we used the PostgreSQL and you can find a sample database in the folder "samples".

If you are using a debian-like operating system, do the commands bellow to install the PostgreSQL:

    $ sudo apt-get install postgresql

To configure PostgreSQL correctly to use do:

    $ sudo su postgres
    $ createuser your_user
    $ createdb your_db
    $ exit
    $ sudo su postgres -c psql
    postgres=# alter role your_user with encrypted password 'your_pass';

And to import the sample file, do:

    $ psql -d mootiro -f /path/to/dbsample.sql

Running API on localhost:8000
--------------------------------

    $ ipython -i PostmonServer.py
    >> _standalone()

If you want to run the API in another port, just put a parameter in the _standalone call.


        Copyright [2013] [Coding for Change]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.