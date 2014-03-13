import socket
import select
from handler import Handler
from .. import util
from .. import logger
import threading, sys
from subprocess import Popen, call
from .. import info
import pynotify

pynotify.init("Basic")
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
    def __init__(self, debug=False):
        self.input = []
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.log = logger.Logger('server', debug=debug)
        self.handler = Handler(self)
        self._notify = pynotify.Notification('', '')
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
            self.notify('server started')
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
                        self.sendState(s)
                    elif data.startswith('change-notify'):
                        val = util.str2bool(data.split()[1])
                        self.handler.getMapping().setNotify(val)

        for client in self.input:
            client.close()
        
        self.notify('server closed')
        self.log.info('server closed')
        
    def notify(self, msg, warning=False):
        icon = 'dialog-warning' if warning else ''
        if self.handler.getMapping().notify():
            self._notify.close()
            self._notify.update(info.name, msg, icon)
            self._notify.show()
    
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
            self.notify('server paused')
        else:
            self.handler.resume()
            self._state = 'running'
            self.log.info('server resumed')
            self.sendState()
            self.notify('server resumed')
            
    def quit_(self):
        self.running = False
        self.handler.stop()
    
    def sendState(self, client=None):
        self.send('state {}'.format(self._state), client)
    
    def send(self, msg, client=None):
        text = '{} data sended : {}'
        if client:
            self.log.send(text.format(client.getpeername()[1], msg))
            client.send(msg)
        else:
            for s in self.input:
                if s != self.socket:
                    self.log.send(text.format(s.getpeername()[1], msg))
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
        print ' the server is not responding: {}'.format(msg)
        return
    if msg.startswith('state'):
        state = msg.split()[1]
        if state == 'paused':
            print 'the server is paused'
        elif state == 'running':
            print 'the server is resumed'
    elif msg == 'quit':
        print 'the server is off'

def start(debug=False):
    daemon = Daemon(debug)
    msg = daemon.connect()
    if msg:
        print 'connection failed: {}'.format(msg)
        print 'The server is probably already started'
    
    
def pause():
    _send('pause')
    
    
def close():
    _send('quit')
    
