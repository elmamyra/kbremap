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
    'border': QColor(50, 50, 50),
    'default': QColor(240, 240, 230),
    'content': QColor(205, 235, 205),
    'special-key': QColor(210, 215, 200),
    'no-char': QColor(220, 215, 200),
    'not-used': QColor(200, 200, 200),
    'modifier-on': QColor(180, 200, 240),
    'modifier-off': QColor(220, 235, 240),
    'bg': QColor(100, 110, 110),
    'unused': QColor(192, 192, 192),
}



