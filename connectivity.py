import socket
import requests
from flask import Flask
from flask import appcontext_tearing_down
from cpcheck import cpcheck
from threading import Event
from cpupdate import Cpupdate





def checkConnectionPoints():
    # first update the connection points from the server
    global conns
    probes = []

    app.logger.debug(str(conns))

    conns = thread.conns

    for conn in conns:
        # Create a new thread, store a refernece to an array and start the thread
        current = cpcheck(conn['ip'], int(conn['port']), conn)
        probes.append(current)
        current.start()


    for p in probes:
        p.join()
        app.logger.debug("Status for Address (%s:%s): %d", p.ip, p.port, p._result)

        # Store status in array
        p.conn['status'] = p._result

def stopCpupdate(sender, **extra):
    app.logger.debug("Stop update thread")
    stopFlag.set()

app = Flask(__name__)
app.logger.info("initialize module connectivity.py")
appcontext_tearing_down.connect(stopCpupdate, app)

stopFlag = Event()
thread = Cpupdate(stopFlag)
thread.start()

conns = []
