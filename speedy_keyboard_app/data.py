from PySide.QtGui import QColor
from PySide.QtCore import  QObject
from Xlib import X
from collections import namedtuple

ALT, CTRL, SHIFT, SUPER, NUM_LOCK, CAPS_LOCK, ALT_GR = range(7)

TEXT, LAUNCHER, SHORTCUT = range(3)

GR_TEXT, GR_ICON = range(2)

PORT = 22347

MODIFIER_MASK = {   
    ALT: X.Mod1Mask,
    CTRL: X.ControlMask,
    SHIFT: X.ShiftMask,
    SUPER: X.Mod4Mask,
    NUM_LOCK: X.Mod2Mask,
    CAPS_LOCK: X.LockMask,
    ALT_GR: X.Mod5Mask,
}

MODIFIER_KEYCODES = {
    64: ALT,
    37: CTRL,
    105: CTRL,
    50: SHIFT,
    62: SHIFT,
    133: SUPER,
    134: SUPER,
    77: NUM_LOCK,
    66: CAPS_LOCK,
    108: ALT_GR
}


t = namedtuple('t', 'title icon')

DATA_TYPE = {
            TEXT: t(QObject().tr("Text"), 'text'),
            LAUNCHER: t(QObject().tr("Launcher"), 'launcher'),
            SHORTCUT: t(QObject().tr("Shortcut"), 'shortcuts'),
            
            }

KEYBOARD_COLOR = {
    'border': QColor(128, 128, 128),
    'default': QColor(240, 240, 230),
    'content': QColor(210, 240, 215),
    'dead-key': QColor(220, 225, 210),
    'no-char': QColor(230, 225, 210),
    'not-used': QColor(200, 200, 200),
    'modifier-on': QColor(190, 210, 230),
    'modifier-off': QColor(225, 235, 230),
    'bg': QColor(230, 235, 230),
    'unused': QColor(192, 192, 192),
    'select': QColor(240, 210, 220)      
}


