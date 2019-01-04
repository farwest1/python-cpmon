import requests
import connectivity as conn
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import cpmondb



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Bernd!"

@app.route("/add/<int:add>")
def calc(add):
    return str(add + add)

@app.route("/enco/test")
def testEnco():
    URL = 'http://google.com'
    r = requests.get(URL)
    return r.text

#TODO: ensure that this servers only GET requests
# @app.route("/connectionpoints", methods=['GET'])
# def getConnectionPoints():
#     connections = []
#     rows = cpmondb.getConnectionPointsAll()
#     for row in rows:
#         conn = {
#             "ip": row[0],
#             "port":str(row[1])
#         }
#         connections.append(conn)
#
#     jresp = jsonify(connections)
#     app.logger.debug(jresp)
#     return (jresp, 200, {"Content-Type": 'application/json'})

@app.route("/management/health")
def healthCheck():
    filtered = "True" if( request.args.get('exampleCheck1')) else "False"

    #first set the headers
    my_headers = {"X-Config":"blabla"}
    conn.checkConnectionPoints()
    app.logger.debug(str(conn.conns))
    return render_template('hello.html', conns=conn.conns, filtered=filtered), 200, my_headers


if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000)) 
app.run(host='0.0.0.0', port=port, debug=True)
