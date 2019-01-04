import psycopg2
from flask import Flask

app = Flask(__name__)
# dbname='enco'
# try:
#     conn = psycopg2.connect(dbname=dbname, user='enco', host='localhost', password='enco')
#     app.logger.info ('Successfully connected to database %s ', dbname)
# except:
#     print ('I am unable to connect to the database')


def getConnectionPointsAll():
    stmt = "SELECT hostname, port from connectionpoints"
    cur = conn.cursor()
    cur.execute(stmt)
    rows = cur.fetchall()
    return rows
