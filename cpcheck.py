import threading
import socket
import requests
from flask import Flask
import time

app = Flask(__name__)
#TODO: make this thread stoppable
class cpcheck(threading.Thread):

    def __init__ (self,ip,port,conn):
      threading.Thread.__init__(self)
      app.logger.debug("New Thread created for Address %s", ip)
      self.ip = ip
      self.port = port
      self.conn = conn



    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self.ip,int(self.port)))
        app.logger.debug("Result for Address %s: %s", self.ip, result)
        self._result = result

    def status():
        return self._result
