# encoding: utf-8

import bottle
import psycopg2

from bottle import route, run

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
    query.close()

    results = []
    for item in org:
        results.append(str(item).strip())

    return results

bottle.mount('/v1', app_v1)

def _standalone(port=8000):
    run(host='localhost', port=port)