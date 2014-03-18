# This file is part of the kbremap project.
# Copyright (C) 2014 Nicolas Malarmey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
# contact: elmamyra@gmail.com

import socket
import select
from handler import Handler
from kbremap_app import util, info, logger, cst
import threading, sys
from subprocess import Popen, call
import pynotify

pynotify.init("Basic") 

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
            self.log.info('try connect server to port %s', cst.PORT)
            self.socket.bind((socket.gethostname(), cst.PORT))
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
        s.connect((socket.gethostname(), cst.PORT))
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
    
