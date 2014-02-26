from ..Xtools import display
from .. import mapping
import threading
import time
from .. import data as d

class Handler(object):
    def __init__(self):
        self.display = display.Display()
#         self.root = self.display.screen().root
#         self.root.grab_key(38, 0x0, 0, X.GrabModeAsync, X.GrabModeAsync)
        self.mapping = mapping.Mapping()
        self.running = True
        self.mapping.loadCurrent()
        self.grabKeys()
        th = threading.Thread(target=self.eventThread)
        th.start()
        
    def grabKeys(self):
#         self.display.grabKey(38, 0)
#         return
        for keycode, modifiers in self.mapping.iterKey():
#             print keycode, modifiers
            self.display.grabKey(keycode, modifiers)
            
    def stop(self):
        self.running = False
    
    def eventThread(self):
        while self.running:
#             print 'before'
            event = self.display.nextKeyEvent()
            if event:
                print event
                item = self.mapping.getItem(event.keycode, event.modifiers)
                if not item:
                    modifiers = self.display.removeNumLock(event.keycode, event.modifiers)
                    item = self.mapping.getItem(event.keycode, modifiers)
                if item:
                    print item
                    if item.type == d.TEXT:
                        self.display.sendText(item.data[0])
                    
#                 print 'event thread', event
            else:
                time.sleep(0.05)
#             self.display.allow_events(X.ReplayKeyboard, X.CurrentTime)
#             self.display.sync()
    