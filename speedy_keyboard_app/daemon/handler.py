import time
from ..Xtools.display import Display
from .. import mapping
import threading
from subprocess import Popen, PIPE
from .. import data as d
from .. import logger
import socket, sys
# from speedy_keyboard_app import mainWindow
PORT = 22347

class Handler(object):
    def __init__(self, daemon):
        self.daemon = daemon
        self.log = logger.Logger('server')
        self.display = Display()
        self.mapping = mapping.Mapping()
        self.running = True
        self.display.resetMapping()
        
    def update(self):
        self.ungrabKeys()
        self.mapping = mapping.Mapping()
        self.mapping.loadCurrent()
        self.log.handler_('load mapping (%s)', self.mapping.title() or 'none')
        self.grabKeys()
    
    def start(self):
        self.mapping.loadCurrent()
        self.log.handler_('start (%s)', self.mapping.title() or 'none')
        self.grabKeys()
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
            
    def grabKeys(self, exceptType=-1):
        self.log.handler_('grab keys')
#         remapKeyList = []
        for item in self.mapping:
#             if item.type == d.REMAPPING:
#                 remapKeyList.append((item.keycode, item.modifiers, item.data))
#             self.display.remapKey(item.keycode, item.modifiers, item.data[0])
#             else:
            self.display.grabKey(item.keycode, item.modifiers)
                
#         self.display.remapKeys(remapKeyList)
            
    def ungrabKeys(self, exceptType=-1):
        self.log.handler_('ungrab keys')
        for item in self.mapping:
            self.display.ungrabKey(item.keycode, item.modifiers)
            
#         self.display.resetMapping()
        
    

#     def grabKey(self, item):
#         if item.type == d.REMAPPING:
#                 self.display.remapKey(item.keycode, item.modifiers, item.data[0])
#         else:
#             self.display.grabKey(item.keycode, item.modifiers)
#         
#     def ungrabKey(self, item):
#         self.display.ungrabKey(item.keycode, item.modifiers)
#             
#         
    
    
    def stop(self):
        self.running = False
        self.display.resetMapping()
        
    def pause(self):
        self.ungrabKeys(exceptType=(d.PAUSE,))
    
    def resume(self):
        self.grabKey((d.PAUSE,))
#         for item in self.mapping:
#             if item.type != d.PAUSE:
#                 self.grabKey(item)
    
    def eventThread(self):
        while self.running:
            event = self.display.nextKeyEvent()
            if event:
                modMask = self.display.removeNumLockMask(event.keycode, event.modifiers)
                item = self.mapping.getItem(event.keycode, modMask)
                if item:
                    self.log.handler_('item send: %s', item.type)
                    if item.type == d.TEXT:
                        self.display.sendText(item.data)
                    elif item.type == d.SHORTCUT:
                        self.display.sendKeycode(item.data[0], item.data[1])
                    elif item.type == d.COMMAND:
                        Popen(item.data.split(), close_fds=True)
                    elif item.type == d.REMAPPING:
                        self.display.remapTest(item.data)
                    elif item.type == d.PAUSE:
                        self.send('pause')
                    elif item.type == d.STOP:
                        self.send('quit')
                    elif item.type == d.LOAD:
                        self.ungrabKeys()
                        self.mapping.load(item.data)
                        self.mapping.save()
                        self.send('loaded {}'.format(item.data))
                        self.grabKeys()
                    elif item.type == d.RUN_EDITOR:
                        try:
                            Popen([sys.argv[0]], close_fds=True)
                        except Exception, msg:
                            self.log.warning('Error launch editor: %s', msg)
                else:
                    self.log.handler_('no item for this entry: %s %s', event.keycode, hex(modMask))
                        
                    
            else:
                time.sleep(0.005)
        self.log.handler_('stopped')
    
        
        
        