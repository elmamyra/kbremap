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
