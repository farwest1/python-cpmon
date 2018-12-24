import socket
import requests
from flask import Flask

app = Flask(__name__)
conns = []

def checkConnectionPoints():
    # first update the connection points from the server
    global conns
    conns = updateConnectionPoints()
    app.logger.debug(str(conns))
    for conn in conns:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((conn["ip"],int(conn["port"])))
        conn['status'] = result
        app.logger.debug("Port status for %s: %d", conn["ip"], conn['status'])
    return 1


def updateConnectionPoints():
    app.logger.info("Get connectionpoints from Service")
    r =  requests.get('http://localhost:5000/connectionpoints')
    app.logger.debug (r.json())
    return r.json()
