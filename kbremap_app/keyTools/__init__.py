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

# -*- coding: utf-8 -*-
from Xlib.display import Display
from Xlib import X, error
import Xlib
from collections import namedtuple
from gtk import gdk
import gtk
from subprocess import Popen, PIPE
from threading import Timer
from itertools import groupby
from operator import itemgetter


keyEvent = namedtuple('keyEvent', ['type', 'keycode', 'modMask'])

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

LEVEL_MOD = (0, X.ShiftMask, X.Mod5Mask, X.ShiftMask | X.Mod5Mask, X.ControlMask | X.Mod1Mask)

class KeyTools:
    KEY_PRESS = X.KeyPress
    KEY_RELEASE = X.KeyRelease
    def __init__(self):
        self._xdisplay = Display()
        self._xroot = self._xdisplay.screen().root
        self._clipboard = gtk.clipboard_get()
        self._clipPrimay = gtk.clipboard_get("PRIMARY")
        self._entryForPaste = 118, X.ShiftMask
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
    
    
    def filterGroup(self, entries):
        if entries:
            return [e for e in entries if e[-2] == self._group]
        return []
    
    
    def remapKey(self, keycode, keysyms):
        allKeysyms = list(self._xdisplay.get_keyboard_mapping(keycode, 1)[0])
        keysyms = keysyms + [0]*(4 - len(keysyms))
        allKeysyms[:2] = keysyms[:2]
        allKeysyms[4:6] = keysyms[2:]
        self._xdisplay.change_keyboard_mapping(keycode, [allKeysyms])
        self._xdisplay.sync()
    
    
    
    def resetMapping(self):
        try:
            process = Popen('setxkbmap -print -verbose 7'.split(), stdout=PIPE, stderr=PIPE)
        except OSError:
            print 'install setxkbmap'
        
        for line in process.stderr:
            print 'setxkbmap error: {}'.format(line)
        
        layout = variant = ''
        
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
            except OSError:
                print 'install setxkbmap'
                
            for line in process.stderr:
                print 'setxkbmap error: {}'.format(line)
    
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
    
    def keycode2entries(self, keycode):
        return self.filterGroup(self._keymap.get_entries_for_keycode(keycode))
    
    def keysym2entry(self, keysym):
        if not keysym:
            return None
        
        infos = self._keymap.get_entries_for_keyval(keysym)  # @UndefinedVariable
        if infos:
            for info in infos:
                keycode, group, level = info
                if group == self._group:
                    if level < len(LEVEL_MOD):
                        mod = LEVEL_MOD[level]
                        return keycode, mod
            
        return None
    
    def keysym2deadEntries(self, keysym):
        resp = ()
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
        
    
    def keycode2charsAndNames(self, keycode):
        entries = self.keycode2entries(keycode)
        chars = []
        names = []
        for entry in entries:
            chars.append(keysym2char(entry[0]))
            names.append(keysym2name(entry[0]))
            if len(chars) >= 4:
                break
        
        while not names[-1]:
            chars.pop(-1)
            names.pop(-1)
        return chars, names
    
    def keycode2keysyms(self, keycode):
        entries = self.keycode2entries(keycode)
        return [e[0] for e in entries][:4]
                
    def char2entries(self, char):
        keysym = gdk.unicode_to_keyval(ord(char))  # @UndefinedVariable
        if keysym:
            return self.keysym2deadEntries(keysym)
        
        return ()
    
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
    
        
    def grabKey(self, keycode, modMask):
        self._xroot.grab_key(keycode, modMask, 0, X.GrabModeAsync, X.GrabModeAsync)
        if not self.isKeypadKey(keycode) and not modMask & X.Mod2Mask:
            self._xroot.grab_key(keycode, modMask | X.Mod2Mask, 0, X.GrabModeAsync, X.GrabModeAsync)
            
    def ungrabKey(self, keycode, modMask):
        self._xroot.ungrab_key(keycode, modMask)
        if not self.isKeypadKey(keycode) and not modMask & X.Mod2Mask:
            self._xroot.ungrab_key(keycode, modMask | X.Mod2Mask)
    
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

    
    def slotClipboard(self, clipboard, text, backup):
        self.sendEntry(*self._entryForPaste)
        t = Timer(0.1, self.restoreClipboard, (backup,))
        t.start()
        
        
    def restoreClipboard(self, backup):
        self._clipboard.request_text(lambda a, b, c: None)
        if backup:
            self._clipboard.set_text(backup or '')
            self._clipPrimay.clear()
            self._clipboard.store()
     
    def sendText(self, text):
        backup = self._clipboard.wait_for_text()
        self._clipboard.set_text(text)
        self._clipPrimay.set_text(text)
        self._clipboard.request_text(self.slotClipboard, backup)
        self._clipboard.store()
        self._clipPrimay.store()
                
    def sendKeysym(self, keysym):
        entries = self.keysym2deadEntries(keysym)
        for entry in entries:
            self.sendEntry(*entry)
    
    def sendEntry(self, keycode, mod):
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

def name2keysym(name):
    return gdk.keyval_from_name(name)  # @UndefinedVariable

def keysym2name(keysym):
    try:
        return gdk.keyval_name(keysym) or ""  # @UndefinedVariable
    except:
        return ""

def keysym2char(keysym):
    char = gdk.keyval_to_unicode(keysym)  # @UndefinedVariable
    return unichr(char) if char else ""

def name2Char(name):
    char = name2unicode(name)
    if char:
        char = unichr(char)
        
    return char or ''

        

