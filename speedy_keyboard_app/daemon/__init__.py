import socket
import select
from handler import Handler
from .. import util
import threading, sys
import logging
from logging.handlers import RotatingFileHandler
from subprocess import Popen, call

PORT = 22347

class Signal(object):
    def __init__(self):
        self._slots = []
        
    
    def connect(self, slot):
        self._slots.append(slot)
    
    def emit(self, *args):
        for slot in self._slots:
            slot(*args)



class Daemon(object):
    def __init__(self):
        self.input = []
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.handler = Handler(self)
        self.log = logger()
        self.log.info('test')
        self._state = 'running'

    
    def connect(self, arg=None):
        try:
            self.socket.bind((socket.gethostname(), PORT))
            self.socket.listen(3)
            self.running = True
            self.input = [self.socket]
            self.handler.start()
            th = threading.Thread(target=self.start)
            th.start()
        except socket.error, msg:
            print 'The daemon is already started', msg
    
    
    @staticmethod
    def quit():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((socket.gethostname(), PORT))
            s.send('quit')
        except:
            print "The daemon is already closed"


    def start(self):
        while self.running:
            inputready, outputready, exceptready = select.select(self.input,[],[])
            for s in inputready: 
                if s == self.socket:
                    client, address = self.socket.accept()
                    self.input.append(client)
                else:
                    # handle all other sockets
                    data = s.recv(128)
                    print 'data', data
                    if not data:
                        s.close()
                        print 'client server close'
                        self.input.remove(s)
                    elif data == 'quit':
                        self.running = False
                        self.handler.stop()
                    elif data == 'update':
                        self.handler.update()
                    elif data == 'resume':
                        if self._state == 'paused':
                            self.handler.grabKeys()
                            self._state = 'running'
                            s.send('resume')
                        
                    elif data == 'pause':
                        if self._state == 'running':
                            self.handler.ungrabKeys()
                            self._state = 'paused'
                            s.send('pause')
                        else:
                            print "The daemon is already paused"
                        
                        
                        

        for client in self.input:
            client.close()
            

def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler(util.configPath('activity.log'), 'a', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    logger.addHandler(steam_handler)
    return logger

def _send(msg):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), PORT))
        s.send(msg)
        return True
    except:
        return False

def start():
    daemon = Daemon()
    daemon.connect()
    
def pause():
    if not _send('pause'):
        print "The daemon is closed"
        
def resume():
    if not _send('resume'):
        print "The daemon is closed"
    
def close():
    if not _send('quit'):
        print "The daemon is already closed"
    
