# -*- coding: utf-8 -*-
from Xlib.display import Display as XDisplay
from Xlib import X, XK, error
import Xlib
from keysymdef import *
from collections import namedtuple

from keysData import keyGroups


keyEvent = namedtuple('keyEvent', ['type', 'keycode', 'modifiers'])

class Display:
    CAPS_LOCK_DEFAULT, CAPS_LOCK_OLD = 0, 1
    KEY_PRESS = X.KeyPress
    KEY_RELEASE = X.KeyRelease
    def __init__(self):
        self._xdisplay = XDisplay()
        self._xroot = self._xdisplay.screen().root
        self._keysyms = {}
        self._groups = []
        self._char2keysym = {}
        self._name2char = {}
        self.caplockType = Display.CAPS_LOCK_DEFAULT
        self.addAllGroups()

        
    def keycode2keysym(self, keycode, index=0):
        return self._xdisplay.keycode_to_keysym(keycode, index)
    
    def keycode2char(self, keycode, index):
        keysym = self.keycode2keysym(keycode, index)
        return self.keysym2char(keysym, index)
    
    def keysym2char(self, keysym, index=0):
        data = self._keysyms.get(keysym)
        if data:
            if data.char:
                return data.char
            else:
                return data.name
        else:
            return self._tryFindChar(keysym)
        return ''
    
    def keycode2keysyms(self, keycode):
        return self._xdisplay.get_keyboard_mapping(keycode, 1)
    
    def keysym2keycodes(self, keysym):
        return self._xdisplay.keysym_to_keycodes(keysym)
    
    def keysym2name(self, keysym):
        if keysym in self._keysyms:
            return self._keysyms[keysym].name
        return ''
    
    def name2Char(self, name):
        return self._name2char.get(name, '')
    
    def char2keysym(self, char):
        return self._char2keysym.get(char, -1)
    
    def char2keycodes(self, char):
        keysym = self.char2keysym(char)
        keycodes = self.keysym2keycodes(keysym)
        if keycodes:
            keycode, modNum = keycodes[0]
            mod = {0: 0,
             1: X.ShiftMask,
             4: X.Mod5Mask,
             5: X.Mod5Mask | X.ShiftMask
             }.get(modNum, -1)
            if mod != -1:
                return keycode, mod
            
        return None, None 
    
    def text2keysym(self, text):
        return [self.char2keysym(char) for char in unicode(text)]
    
    
    def charFromModifier(self, keycode, shift=False, numLock=False, capsLock=False, altGr=False):
        char = ''
        groupStart = 4 if altGr else 0
        if not self.keycode2keysym(keycode, 1):
            return self.keycode2char(keycode, 0)
        elif numLock and self.isKeypadKeycode(keycode, groupStart+1):
            if (shift and capsLock) or (shift and not capsLock):
                groupId = 0
            elif (not shift and capsLock) or (not shift and not capsLock):
                groupId = 1
            char = self.keycode2char(keycode, groupStart+groupId)
        
        elif not shift and not capsLock:
            char = self.keycode2char(keycode, groupStart)
            
        elif not shift and capsLock:
            char1 = self.keycode2char(keycode, groupStart)
            char2 = self.keycode2char(keycode, groupStart+1)
            if self.caplockType == Display.CAPS_LOCK_DEFAULT:
                if char2.isdigit():
                    char = char2
                elif char1.islower():
                    char = char1.upper()
                else:
                    char = char1
            elif self.caplockType == Display.CAPS_LOCK_OLD:
                char = char1
                if char.islower():
                    char = char.upper()
                    
                
        elif shift and capsLock:
            char1 = self.keycode2char(keycode, groupStart)
            char2 = self.keycode2char(keycode, groupStart+1)
            if self.caplockType == Display.CAPS_LOCK_DEFAULT:
                if char2.isdigit() or char1.islower():
                    char = char1
                else:
                    char = char2
            elif self.caplockType == Display.CAPS_LOCK_OLD:
                char = self.keycode2char(keycode, groupStart+1)
                if char.islower():
                    char = char.upper()
                
        elif shift:
            char = self.keycode2char(keycode, groupStart+1)
                
        return char 
    
    
    def isKeypadKeycode(self, keycode, index):
        keysym = self.keycode2keysym(keycode, index)
        return 0xFF80 <= keysym <= 0xFFBD \
                or 0x11000000 <= keysym <= 0x1100FFFF
    
    
    def isKeypadKey(self, keycode):
        return keycode in (106, 163, 79, 80, 81, 83, 84, 85, 87, 88, 89,  90, 91, 82, 86, 104)
    
    def _tryFindChar(self, keysym):
        hexa = hex(keysym)
        if hexa[-1] == 'L':
            hexa = hexa[:-1]
        if len(hexa) == 9 and hexa[:5] == "0x100":
            return unichr(int(hexa[5:], 16))
        return ''
    
    def addGroup(self, group):
        for keysym, data in keyGroups[group].items():
            if data.char:
                self._char2keysym[data.char] = keysym
                self._name2char[data.name] = data.char
            self._keysyms[keysym] = data
        
        self._groups.append(group)
    
    def addGroups(self, groups):
        for group in groups:
            self.addGroup(group)
    
    def addAllGroups(self, exceptGroup=[]):
        self._groups = []
        self._char2keysym = {}
        self._name2char = {}
        for groupName in keyGroups:
            if groupName in exceptGroup:
                continue
            self.addGroup(groupName)
            
    def removeGroup(self, group):
        self._groups.remove(group)
        groups = self._keysymGroups[:]
        self._keysymGroups = []
        self._char2keysym = {}
        self._name2char = {}
        self.addGroups(groups)
        
    def groups(self):
        return self._groups
    
    def hasGroup(self, group):
        return group in self._groups
    
    def grabKey(self, keycode, modifiers):
        self._xroot.grab_key(keycode, modifiers, 0, X.GrabModeAsync, X.GrabModeAsync)
        if not self.isKeypadKey(keycode) and not modifiers & X.Mod2Mask:
            self._xroot.grab_key(keycode, modifiers | X.Mod2Mask, 0, X.GrabModeAsync, X.GrabModeAsync)
    
    def removeNumLock(self, keycode, modifiers):
        if not self.isKeypadKey(keycode) and modifiers & X.Mod2Mask:
            return modifiers ^ X.Mod2Mask
        
    
    def nextKeyEvent(self, typ=KEY_PRESS):
        if isinstance(typ, int):
            typ = (typ,)
        num = self._xdisplay.pending_events()
        if num:
            for _ in range(num):
                event = self._xdisplay.next_event()
                if event.type in typ:
                    return keyEvent(event.type, event.detail, event.state)
                self._xdisplay.allow_events(X.AsyncKeyboard, X.CurrentTime)
        return None

    
    def sendText(self, text):
        for char in text:
            keycode, mod = self.char2keycodes(char)
            self.pressKey(keycode, mod)
            self.releaseKey(keycode, mod)
        
#         self._xdisplay.sync()
            

    
    def pressKey(self, keycode, modifiers):
        window = self._xdisplay.get_input_focus()._data["focus"]
        evt = Xlib.protocol.event.KeyPress(  # @UndefinedVariable
            time = X.CurrentTime,
            root = self._xroot,
            window = window,
            same_screen = 0, child = Xlib.X.NONE,
            root_x = 0, root_y = 0, event_x = 0, event_y = 0,
            state = modifiers,
            detail = keycode
            )
        window.send_event(evt, propagate = True)
        
    def releaseKey(self, keycode, modifiers):
        window = self._xdisplay.get_input_focus()._data["focus"]
        evt = Xlib.protocol.event.KeyRelease(  # @UndefinedVariable
            time = X.CurrentTime,
            root = self._xroot,
            window = window,
            same_screen = 0, child = Xlib.X.NONE,
            root_x = 0, root_y = 0, event_x = 0, event_y = 0,
            state = modifiers,
            detail = keycode
            )
        window.send_event(evt, propagate = True)
        
#         self._xroot.grab_key(43, 0x14, 0, X.GrabModeAsync, X.GrabModeAsync)

        

        

