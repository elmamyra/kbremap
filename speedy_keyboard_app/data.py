from PySide.QtGui import QColor
from PySide.QtCore import  QObject
from collections import namedtuple

TEXT, COMMAND, SHORTCUT, REMAPPING = range(4)

GR_TEXT, GR_ICON = range(2)

PORT = 22347

t = namedtuple('t', 'title icon')

DATA_TYPE = {
            TEXT: t(QObject().tr("Text"), 'text'),
            COMMAND: t(QObject().tr("Command"), 'utilities-terminal'),
            SHORTCUT: t(QObject().tr("Shortcut"), 'shortcuts'),
            REMAPPING: t(QObject().tr("Remapping"), 'keys'),
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



