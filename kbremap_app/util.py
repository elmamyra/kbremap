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

from PySide.QtGui import QColor
from PyQt4.QtCore import  QSettings, QSize
import client.data as d
from kbremap_app import info
import os
import weakref
import keyTools


def saveDialogSize(dialog, key, default=QSize()):
    """Makes the size of a QDialog persistent.
    
    Resizes a QDialog from the setting saved in QSettings().value(key),
    defaulting to the optionally specified default size, and stores the
    size of the dialog at its finished() signal.
    
    Call this method at the end of the dialog constructor, when its
    widgets are instantiated.
    
    """
    size = QSettings().value(key, default)
    if size:
        dialog.resize(size.toSize())
    dialogref = weakref.ref(dialog)
    def save():
        dialog = dialogref()
        if dialog:
            QSettings().setValue(key, dialog.size())
    dialog.finished.connect(save)

def str2bool(v):
    return v.lower() in ('true', '1')
 
def keyboardColors(name):
    return d.KEYBOARD_COLOR.get(name, QColor())

def configPath(fileName='mappings.xml'):
        configDir = os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser("~/.config")
        return os.path.join(configDir, info.name, fileName)

def keysym2text(keysym):
        text = ''
        name = keyTools.keysym2name(keysym)
        if name:
            char = keyTools.keysym2char(keysym)
            text = name
            if char and name != char:
                text = u'{} ({})'.format(text, char)
        return text


def isblank(s):
    """Return True if s is empty or whitespace only."""
    return not s or s.isspace()
 
def indentXML(elem, indent_string="    ", level=0):
    """Indent the XML in element.
    
    Text content that is already non-whitespace is not changed.
    
    """
    # based on http://effbot.org/zone/element-lib.htm#prettyprint
    i = "\n" + indent_string * level
    if len(elem):
        if isblank(elem.text):
            elem.text = i + indent_string
        if isblank(elem.tail):
            elem.tail = i
        for elem in elem:
            indentXML(elem, indent_string, level+1)
        if isblank(elem.tail):
            elem.tail = i
    else:
        if level and isblank(elem.tail):
            elem.tail = i
