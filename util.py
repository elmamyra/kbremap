from PySide.QtGui import QColor, QFrame
from PyQt4.QtCore import  QSettings, QSize, Qt
import data as d
import weakref


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

class Separator(QFrame):
    def __init__(self, *args, **kwargs):
        QFrame.__init__(self, *args, **kwargs)
        self.setLineWidth(1)
        self.setMidLineWidth(0)
        self.setOrientation(Qt.Horizontal)
        
    def setOrientation(self, orientation):
        if orientation == Qt.Vertical:
            self.setFrameShape(QFrame.VLine)
            self.setFrameShadow(QFrame.Sunken)
            self.setMinimumSize(2, 0)
        else:
            self.setFrameShape(QFrame.HLine)
            self.setFrameShadow(QFrame.Sunken)
            self.setMinimumSize(0, 2)
        self.updateGeometry()
        
    def orientation(self):
        return Qt.Vertical if self.frameStyle() & QFrame.VLine == QFrame.VLine else Qt.Horizontal

    
def modXmask(mod):
    return d.MODIFIER_MASK.get(mod, -1)

def keycodeMod(keycode):
    return d.MODIFIER_KEYCODES.get(keycode, -1)

def keyboardColors(name):
    return d.KEYBOARD_COLOR.get(name, QColor())



