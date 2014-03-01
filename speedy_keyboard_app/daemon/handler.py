from ..Xtools import display
from .. import mapping
import threading
from subprocess import Popen, PIPE
import time, os, sys
from .. import data as d

class Signal(object):
    def __init__(self):
        self._slots = []
        
    
    def connect(self, slot):
        self._slots.append(slot)
    
    def emit(self, *args):
        for slot in self._slots:
            slot(*args)


class Handler(object):
    testSig = Signal()
    def __init__(self, daemon):
        self.daemon = daemon
        self.display = display.Display()
        self.mapping = mapping.Mapping()
        self.running = True
        self.display.resetMapping()
        
    def update(self):
        self.ungrabKeys()
        self.mapping = mapping.Mapping()
        self.mapping.loadCurrent()
        self.grabKeys()
    
    def start(self):
        self.mapping.loadCurrent()
        self.grabKeys()
        th = threading.Thread(target=self.eventThread)
        th.start()
    
    def grabKeys(self):
        for item in self.mapping:
            if item.type == d.REMAPPING:
                self.display.remapKey(item.keycode, item.modifiers, item.data[0])
            else:
                self.display.grabKey(item.keycode, item.modifiers)
            
    def ungrabKeys(self):
        for keycode, modifiers in self.mapping.iterKey():
            self.display.ungrabKey(keycode, modifiers)
            
        self.display.resetMapping()
    

    def stop(self):
        self.running = False
        self.display.resetMapping()
    
    def eventThread(self):
        while self.running:
            event = self.display.nextKeyEvent()
            if event:
                item = self.mapping.getItem(event.keycode, event.modifiers)
                if not item:
                    modifiers = self.display.removeNumLockMask(event.keycode, event.modifiers)
                    item = self.mapping.getItem(event.keycode, modifiers)
                if item:
                    if item.type == d.TEXT:
                        self.display.sendText(item.data[0])
                    elif item.type == d.SHORTCUT:
                        self.display.sendKeycode(item.data[0], item.data[1])
                    elif item.type == d.COMMAND:
                        Popen(item.data.split(), close_fds=True)
                        
                    
            else:
                time.sleep(0.005)
    