import socket
import select
from handler import Handler
from .. import util
from .. import logger
import threading, sys
from subprocess import Popen, call
from .. import info

PORT = 22347

# class Signal(object):
#     def __init__(self):
#         self._slots = []
#         
#     
#     def connect(self, slot):
#         self._slots.append(slot)
#     
#     def emit(self, *args):
#         for slot in self._slots:
#             slot(*args)



class Daemon(object):
    def __init__(self):
        self.input = []
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.log = logger.Logger('server')
        self.handler = Handler(self)
        self._state = 'running'
        
    
    def connect(self, arg=None):
        try:
            self.log.info('try connect server to port %s', PORT)
            self.socket.bind((socket.gethostname(), PORT))
            self.log.info('server started')
            self.socket.listen(3)
            self.running = True
            self.input = [self.socket]
            self.handler.start()
            th = threading.Thread(target=self.start)
            th.start()
            return ''
        except socket.error, msg:
            self.log.warning('connection failed: %s', str(msg))
            return msg
        
    def getLogger(self):
        return self.log

    def start(self):
        while self.running:
            inputready, outputready, exceptready = select.select(self.input,[],[])
            for s in inputready: 
                if s == self.socket:
                    client, address = self.socket.accept()
                    self.input.append(client)
                    self.log.info('%s client connected', address[1])
                else:
                    # handle all other sockets
                    try:
                        data = s.recv(128)
                    except socket.error, msg:
                        self.log.error('receive error: %s', msg)
                        continue
                        
                    self.log.recv('%s %s', address[1], data)
                    if not data:
                        s.close()
                        self.log.info('%s client closed', address[1])
                        self.input.remove(s)
                    elif data == 'update':
                        self.update()
                    elif data.startswith('loaded'):
                        self.send(data)
                    elif data == 'quit':
                        self.quit_()
                    elif data == 'pause':
                        self.pause()
                    elif data == 'send-state':
                        self.sendState()

        for client in self.input:
            client.close()
        
        self.log.info('server closed')
    
    def update(self):
        self.handler.update()
        self.log.action('updated')
        self.send('updated')
        
    def pause(self):
        if self._state == 'running':
            self.handler.pause()
            self._state = 'paused'
            self.log.action('server paused')
            self.sendState()
        else:
            self.handler.resume()
            self._state = 'running'
            self.log.info('server resumed')
            self.sendState()
            
    def quit_(self):
        self.running = False
        self.handler.stop()
    
    def sendState(self):
        self.send('state {}'.format(self._state))
    
    def send(self, msg):
        for s in self.input:
            if s != self.socket:
                self.log.send('{} data sended : {}'.format(s.getpeername()[1], msg))
                s.send(msg)
            

def _send(msg):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), PORT))
        s.settimeout(1)
        s.send(msg)
    except socket.error, msg:
        print 'connection failed: {}'.format(msg)
        print 'The server is probably off'
        print 'run "{} -s" to start'.format(info.name)
        return
    
    try:
        msg = s.recv(128)
    except socket.error, msg:
        print 'receive error: {}'.format(msg)
        return
    if msg.startswith('state'):
        state = msg.split()[1]
        if state == 'paused':
            print 'the server is paused'
        elif state == 'running':
            print 'the server is resumed'
    elif msg == 'quit':
        print 'the server is off'

def start():
    daemon = Daemon()
    msg = daemon.connect()
    if msg:
        print 'connection failed: {}'.format(msg)
        print 'The server is probably already started'
    
    
def pause():
    _send('pause')
    
    
        
# def resume():
#     _send('resume')
    
    
def close():
    _send('quit')
    
