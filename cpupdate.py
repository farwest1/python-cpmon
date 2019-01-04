from threading import Thread
import requests
from flask import Flask

dummyList = [{'ip':'192.168.2.11', 'port':'2376'}, {'ip':'192.168.2.103', 'port':'2376'}]

class Cpupdate(Thread):
    def __init__(self,event):
        Thread.__init__(self)
        self.stopped = event
        self.conns = []

    def run(self):
        while not self.stopped.wait(10):
            app.logger.debug("update connection points")
            self.conns = self.updateConnectionPoints()

    def updateConnectionPoints(self):
        # app.logger.info("Get connectionpoints from Service")
        # r =  requests.get('http://localhost:5000/connectionpoints')
        # app.logger.debug (r.json())
        # return r.json()

        return dummyList



app = Flask(__name__)
