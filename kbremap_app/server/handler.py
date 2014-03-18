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

import time
from kbremap_app import keyTools, mapping, cst
import threading
from subprocess import Popen, PIPE
import socket, sys

PORT = 22347

class Handler(object):
    def __init__(self, daemon):
        self.daemon = daemon
        self.log = daemon.log
        self.keyTools = keyTools.KeyTools()
        self.mapping = mapping.Mapping()
        self.running = True
        self.keyTools.resetMapping()
        
    def update(self):
        self.ungrabKeys()
        self.mapping = mapping.Mapping()
        self.mapping.loadCurrent()
        self.log.handler_('load mapping (%s)', self.mapping.title or 'none')
        self.restoreMap()
        self.grabKeys()
        self.remapKeys()
    
    def start(self):
        self.mapping.loadCurrent()
        self.log.handler_('start (%s)', self.mapping.title or 'none')
        self.grabKeys()
        self.remapKeys()
        th = threading.Thread(target=self.eventThread)
        th.start()
    
    def send(self, msg):        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((socket.gethostname(), PORT))
            s.send(msg)
            self.log.handler_('send: %s', msg)
        except socket.error, msg_:
            self.log.critical('handle connection failed: %s', msg_)
            
    def grabKeys(self, exceptType=()):
        self.log.handler_('grab keys')
        for item in self.mapping.shortcut:
            if item.type not in exceptType:
                self.keyTools.grabKey(item.keycode, item.modifiers)
                
    def ungrabKeys(self, exceptType=()):
        self.log.handler_('ungrab keys')
        for item in self.mapping.shortcut:
            if item.type not in exceptType:
                self.keyTools.ungrabKey(item.keycode, item.modifiers)
            
    def remapKeys(self):
        for item in self.mapping.remap:
            self.keyTools.remapKey(item.keycode, item.keysyms)
            
    def restoreMap(self):
        self.keyTools.resetMapping()
            
    def stop(self):
        self.running = False
        self.keyTools.resetMapping()
        
    def pause(self):
        self.ungrabKeys(exceptType=(cst.PAUSE,))
        self.restoreMap()
    
    def resume(self):
        self.grabKeys((cst.PAUSE,))
        self.remapKeys()
        
    def getMapping(self):
        return self.mapping
    
    def eventThread(self):
        while self.running:
            event = self.keyTools.nextKeyEvent()
            if event:
                modMask = self.keyTools.removeNumLockMask(event.keycode, event.modifiers)
                item = self.mapping.shortcut[event.keycode, modMask]
                if item:
                    self.log.handler_('item send: type=%s, data=%s', item.type, item.data)
                    if item.type == cst.TEXT:
                        self.keyTools.sendText(item.data)
                    elif item.type == cst.KEY:
                        self.keyTools.sendKeysym(item.data)
                    elif item.type == cst.SHORTCUT:
                        self.keyTools.sendEntry(item.data[0], item.data[1])
                    elif item.type == cst.COMMAND:
                        try:
                            Popen(item.data.split(), close_fds=True)
                        except OSError, msg:
                            self.log.warning('The command "%s" failed: %s', item.data, msg)
                            self.daemon.notify('The command <b>{}</b> failed'.format(item.data), True)
                    elif item.type == cst.PAUSE:
                        self.send('pause')
                    elif item.type == cst.STOP:
                        self.send('quit')
                    elif item.type == cst.LOAD:
                        self.ungrabKeys()
                        self.mapping.load(item.data)
                        self.mapping.save()
                        self.send('loaded {}'.format(item.data))
                        self.grabKeys()
                    elif item.type == cst.RUN_EDITOR:
                        try:
                            Popen([sys.argv[0], "-e"], close_fds=True)
                        except Exception, msg:
                            self.log.warning('Error launch editor: %s', msg)
                else:
                    self.log.handler_('no item for this entry: %s %s', event.keycode, hex(modMask))
                        
                    
            else:
                time.sleep(0.005)
        self.log.handler_('stopped')
    
        
        
        