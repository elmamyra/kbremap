
from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import QSettings, QSize, Signal, Qt
# import data
import icons
import os

class IconChooser(QToolButton):
    iconChanged = Signal()
    def __init__(self, parent=None):
        super(IconChooser, self).__init__(parent)
        self.setAcceptDrops(True)
        self.iconPath = ''
        self.setIconSize(QSize(32, 32))
        act = QAction(self,  triggered=self.slotTriggered)
        self.setDefaultAction(act)
        
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
            
    def dropEvent(self, e):
        mime = e.mimeData()
        text = str(mime.data('text/uri-list')).strip()
        path = text[7:]
        if os.path.exists(path):
            self.setIcon(path)
    
    def slotTriggered(self):
        iconPath = QSettings().value('iconPath', os.path.join('/usr', 'share', 'icons'))
        exts = ['*.'+str(ext) for ext in QImageReader.supportedImageFormats()]
        extStr = self.tr("Icon Files") + " ({})".format(' '.join(exts))
        iconFile = QFileDialog.getOpenFileName(self, self.tr("Icon"), iconPath, extStr)[0]
        if iconFile:
            QSettings().setValue('iconPath', os.path.dirname(iconFile))
            self.setIcon(iconFile)
            
    def getIcon(self):
        return self.defaultAction().data()
    
    def setIcon(self, icon):
        self.defaultAction().setIcon(icons.get(icon))
        self.defaultAction().setData(icon)
        self.iconChanged.emit()


class ShortcutWidget(QLineEdit):
    def __init__(self, parent=None):
        super(ShortcutWidget, self).__init__(parent)
        self.nativeKeycode = -1
        self.nativeModifiers = -1
        
        self.modList = [Qt.SHIFT, Qt.CTRL, Qt.ALT, Qt.META]
        self.modKeyList = [Qt.Key_Shift, Qt.Key_Control, Qt.Key_Alt, Qt.Key_Meta]

    def focusInEvent(self, event):
        self.grabKeyboard()
        QLineEdit.focusInEvent(self, event)
    
    
    def focusOutEvent(self, event):
        self.releaseKeyboard()
        QLineEdit.focusOutEvent(self, event)
        
        
    def keyPressEvent(self, event):
        key = event.key()
        modifiers = event.modifiers()
        if key not in (Qt.Key_NumLock, Qt.Key_AltGr):
            if modifiers and key not in self.modKeyList:
                seq = [mod for mod in self.modList if modifiers & mod]
                if key != -1:
                    seq.append(key)
                    if 1 < len(seq) <= 4:
                        keysText = QKeySequence(*seq).toString()
                        self.setText(keysText.replace('+, ', '+'))
                        self.nativeModifiers = event.nativeModifiers()
                        self.nativeKeycode = event.nativeScanCode()

    def setData(self, keycode, modifiers, text):
        self.nativeKeycode = keycode
        self.nativeModifiers = modifiers
        self.setText(text)
    
    def data(self):
        return self.nativeKeycode, self.nativeModifiers, self.text()


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