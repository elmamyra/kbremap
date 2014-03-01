# -*- coding: utf-8 -*-
from Xlib.display import Display as XDisplay
from Xlib import X, error
import Xlib
# from keysymdef import *
from collections import namedtuple
from gtk import gdk
# from speedy_keyboard_app.Xtools.keysDataback import keyGroups
from subprocess import Popen, PIPE


keyEvent = namedtuple('keyEvent', ['type', 'keycode', 'modifiers'])

DEAD_KEYS = (
    'grave',
    'acute',
    'circumflex',
    'tilde',
    'macron',
    'breve',
    'abovedot',
    'diaeresis',
    'ring',
    'doubleacute',
    'caron',
    'cedilla',
    'ogonek',
    'belowdot',
    'hook',
    'horn',
    'stroke',
    'schwa',
    'SCHWA',
)

LEVEL_MOD = (0, X.ShiftMask, X.Mod5Mask, X.ShiftMask | X.Mod5Mask)

class Display:
    KEY_PRESS = X.KeyPress
    KEY_RELEASE = X.KeyRelease
    def __init__(self):
        self._xdisplay = XDisplay()
        self._xroot = self._xdisplay.screen().root
        self._group = 0
        self.loadModifiers()
        self._keymap = gdk.keymap_get_default()  # @UndefinedVariable
        
    def loadModifiers(self):
        self._modifiers = []
        self._modifierList = []
        for key in self._xdisplay.get_modifier_mapping():
            li = [k for k in key if k]
            #for altgr key
            if 92 in li:
                li.append(108)
            self._modifierList += li
            self._modifiers.append(li)
    
    
    def remapKey(self, keycode, modMask, newKeysym):
        oldKeysym = self.entry2name(keycode, modMask)
        process = Popen('xmodmap -e "keysym {} = {}"'.format(oldKeysym, newKeysym), shell=True, stdout=PIPE, stderr=PIPE)
        for line in process.stderr:
            if not line:
                break
            print 'remapKey error:', line
    
    def resetMapping(self):
        try:
            process = Popen('setxkbmap -print -verbose 7'.split(), stdout=PIPE, stderr=PIPE)
        except OSError:
            print 'resetMappig error: install setxkbmap'
            
        layout = variant = ''
        for line in process.stderr:
            if line:
                print 'resetMappig error:', line
            else:
                break
        
        for line in process.stdout:
            line = line.rstrip()
            if line == '':
                break
            
            if line.startswith('layout:'):
                layout = line.split()[1]
            elif line.startswith('variant:'):
                variant = line.split()[1]
                break
                
        command = ['setxkbmap']
        if layout:
            command += ['-layout', layout]
                   
        if variant:
            command += ['-variant', variant]
        if layout or command:
            try:
                process = Popen(command, stdout=PIPE, stderr=PIPE)
            except:
                print 'resetMappig error: command: {}'.format(' '.join(command))
    
    def isModifier(self, keycode):
        return keycode in self._modifierList
    
    def getModMask(self, keycode):
        for i, mods in enumerate(self._modifiers):
            if keycode in mods:
                return 2**i
            
        return 0
    
    def modifiersKeycodeList(self):
        return self._modifierList
    
    def numMask(self):
        return X.Mod2Mask
    
    def keycode2char(self, keycode, mods, group=0):
        char = ''
        name = ''
        info = self._keymap.translate_keyboard_state(keycode, mods, group)
        if info:
            keysym = info[0]
            char = gdk.keyval_to_unicode(keysym)  # @UndefinedVariable
            if char:
                char = unichr(char)
            name = gdk.keyval_name(keysym)  # @UndefinedVariable
            
        return char or '', name or ''
    
    def removeNumLockMask(self, keycode, mod):
        if not self.isKeypadKey(keycode) and mod & X.Mod2Mask:
            return mod ^ X.Mod2Mask
        
        return mod
     
    def entry2keysym(self, keycode, modMask):
        info = self._keymap.translate_keyboard_state(keycode, modMask, self._group)
        if info:
            return info[0]
        
        return None
        
    def entry2name(self, keycode, modMask):
        keysym = self.entry2keysym(keycode, modMask)
        if keysym is not None:
            return gdk.keyval_name(keysym)  # @UndefinedVariable
        
        return None
    
    def keysym2entry(self, keysym):
        infos = self._keymap.get_entries_for_keyval(keysym)
        if infos:
            for info in infos:
                if info[1] == 0:
                    keycode = info[0]
                    mod = LEVEL_MOD[info[2]]
                    return keycode, mod
            
        return None
    
    def char2keycodes(self, char):
        resp = ()
        keysym = gdk.unicode_to_keyval(ord(char))  # @UndefinedVariable
        if keysym:
            entry = self.keysym2entry(keysym)
            if entry:
                keycode, mod = entry
                resp = ((keycode, mod), )
        
        if not resp:
            deadKeys = self.findWithDeadKey(keysym)
            if deadKeys:
                keyKeysym, deadKeysym = deadKeys
                keyKeycodes = self.keysym2entry(keyKeysym)
                deadKeycodes = self.keysym2entry(deadKeysym)
                if keyKeycodes and deadKeycodes:
                    keyKeycode, keyMod = keyKeycodes
                    deadKeycode, deadMod = deadKeycodes
                    resp = ((deadKeycode, deadMod), (keyKeycode, keyMod))
              
        return resp
    
    def findWithDeadKey(self, keysym):
        name = gdk.keyval_name(keysym)  # @UndefinedVariable
        for deadName in DEAD_KEYS:
            if name.endswith(deadName):
                keyName = name[:-len(deadName)]
                deadName = {'ring': 'abovering', 
                           'schwa': 'small_schwa', 
                           'SCHWA': 'capital_schwa'}.get(deadName, deadName)
                deadName = 'dead_' + deadName
                keyKeysym = gdk.keyval_from_name(keyName)  # @UndefinedVariable
                deadSym = gdk.keyval_from_name(deadName)  # @UndefinedVariable
                return keyKeysym, deadSym
        return None
            
    
    def isKeypadKey(self, keycode):
        entry = self._keymap.get_entries_for_keycode(keycode)
        if entry:
            for info in entry:
                if info[2] == self._group:
                    name = gdk.keyval_name(info[0])  # @UndefinedVariable
                    if name and name.startswith('KP_'):
                        return True
                    
        return False
    
        
    def grabKey(self, keycode, modifiers):
        self._xroot.grab_key(keycode, modifiers, 0, X.GrabModeAsync, X.GrabModeAsync)
        if not self.isKeypadKey(keycode) and not modifiers & X.Mod2Mask:
            self._xroot.grab_key(keycode, modifiers | X.Mod2Mask, 0, X.GrabModeAsync, X.GrabModeAsync)
            
    def ungrabKey(self, keycode, modifiers):
        self._xroot.ungrab_key(keycode, modifiers)
        if not self.isKeypadKey(keycode) and not modifiers & X.Mod2Mask:
            self._xroot.ungrab_key(keycode, modifiers | X.Mod2Mask)
    
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
            for keycode, mod in self.char2keycodes(char):
                self.sendKeycode(keycode, mod)
                
                
    def sendKeycode(self, keycode, mod):
        self.pressKey(keycode, mod)
        self.releaseKey(keycode, mod)
    
    def pressKey(self, keycode, modMask):
        window = self._xdisplay.get_input_focus()._data["focus"]
        evt = Xlib.protocol.event.KeyPress(  # @UndefinedVariable
            time = X.CurrentTime,
            root = self._xroot,
            window = window,
            same_screen = 0, child = Xlib.X.NONE,
            root_x = 0, root_y = 0, event_x = 0, event_y = 0,
            state = modMask,
            detail = keycode
            )
        window.send_event(evt, propagate = True)
        
    def releaseKey(self, keycode, modMask):
        window = self._xdisplay.get_input_focus()._data["focus"]
        evt = Xlib.protocol.event.KeyRelease(  # @UndefinedVariable
            time = X.CurrentTime,
            root = self._xroot,
            window = window,
            same_screen = 0, child = Xlib.X.NONE,
            root_x = 0, root_y = 0, event_x = 0, event_y = 0,
            state = modMask,
            detail = keycode
            )
        window.send_event(evt, propagate = True)
        
        
def name2unicode(name):
    keysym = gdk.keyval_from_name(name)  # @UndefinedVariable
    return gdk.keyval_to_unicode(keysym)  # @UndefinedVariable
    

def name2Char(name):
    char = name2unicode(name)
    if char:
        char = unichr(char)
        
    return char or ''

        

