# -*- coding: utf-8 -*-
from Xlib.display import Display as XDisplay
from Xlib import X, XK, error
from keysymdef import *

from keysData import keyGroups



class Display:
    CAPS_LOCK_DEFAULT, CAPS_LOCK_OLD = 0, 1
    def __init__(self):
        self._xdisplay = XDisplay()
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
    
    
    def text2keysym(self, text):
        return [self.char2keysym(char) for char in unicode(text)]
    
    
    def charFromModifier(self, keycode, shift=False, numLock=False, capsLock=False, altGr=False):
        char = ''
        groupStart = 4 if altGr else 0
        if not self.keycode2keysym(keycode, 1):
            return self.keycode2char(keycode, 0)
        elif numLock and self.isKeypadKeycode(keycode, groupStart + 1):
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
        
        
        

