import bottle
import json
import psycopg2

from bottle import route, run, response
from requests import ConnectionError

app_v1 = bottle.Bottle()

def _get_connection():
    try:
        conn = psycopg2.connect("dbname='mootiro' user='postgres' host='localhost' password='postgres'")
        return conn.cursor()

    except:
        print "Erro ao se conectar a base de dados"

@app_v1.route("/organizations")
def get_organizations():
    query = _get_connection()
    query.execute("SELECT * from organization_organization")
    org = query.fetchall()
    return org

bottle.mount('/v1', app_v1)

def _standalone(port=8000):
    run(host='localhost', port=port)