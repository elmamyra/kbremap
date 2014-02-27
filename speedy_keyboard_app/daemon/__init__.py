import socket
import select
from .. import  data as d
from handler import Handler
import threading, sys
import Queue
import time
from subprocess import Popen, call

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
        self._state = 'running'

    
    def connect(self, arg=None):
        try:
            self.socket.bind((socket.gethostname(), d.PORT))
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
            s.connect((socket.gethostname(), d.PORT))
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
                        with open('log.txt', 'w') as f:
                            f.write('client server close')
                        print 'client server close'
                        self.input.remove(s)
                    elif data == 'quit':
                        print 'quit'
#                         self.queue.put('quit')
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
                        
                        
                        

        for client in self.input:
            client.close()
            

def start():
    daemon = Daemon()
    daemon.connect()
    
def close():
    Daemon.quit()
    
# start()