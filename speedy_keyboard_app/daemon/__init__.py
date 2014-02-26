import socket
import select
# from ..Xtools import display
from .. import  data as d
from handler import Handler
import threading, sys
import Queue
import time

class Daemon(object):
    def __init__(self):
        self.conns = []
        self._isAlive = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.handler = Handler()
        self.mainSocket = None

    
    def connect(self, arg=None):
        try:
            self.socket.bind((socket.gethostname(), d.PORT))
            self.socket.listen(3)
            self.start()
        except socket.error:
            print 'The daemon is already started'
    
    @staticmethod
    def quit():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((socket.gethostname(), d.PORT))
            s.send('quit')
        except:
            print "The daemon is already closed"


    def close(self):
        self._isAlive = False

    def start(self):
        ct = None
        while True:
            try:
                client, addr = self.socket.accept()
                data = client.recv(128)
                if data == 'quit':
                    if ct:
                        ct.stop()
                    self.handler.stop()
                    break
                elif data == 'mainwindow':
                    self.mainSocket = client
                    ct = ProcessThread(client)
                    ct.start()
            except KeyboardInterrupt:
                print "Stop."
                break
            except socket.error, msg:
                print "Socket error! %s" % msg
                break
            

    
class ProcessThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.conn.setblocking(0)
        
        self.running = True
        self.q = Queue.Queue()
        
    def add(self, data):
        self.q.put(data)
        
    def stop(self):
        self.running = False
     
     
    def run(self):
        while self.running:
            try:
                msg = self.conn.recv(128)
                if msg == 'quit':
                    Daemon.quit()
                    break
                    
            except Exception as e:
                pass
            time.sleep(0.05)
        self.conn.close()  


def start():
    daemon = Daemon()
    daemon.connect()
    
def close():
    Daemon.quit()
    
# start()