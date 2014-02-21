
from PySide.QtGui import *
from PySide.QtCore import QSettings, QSize, Signal
import icons
import os

class IconChooser(QToolButton):
    iconChanged = Signal()
    def __init__(self, parent=None):
        super(IconChooser, self).__init__(parent)
        self.iconPath = ''
        self.setIconSize(QSize(32, 32))
        act = QAction(self,  triggered=self.slotTriggered)
        self.setDefaultAction(act)
        
        
    def slotTriggered(self):
        iconPath = QSettings().value('icon-path', os.path.join('/usr', 'share', 'icons'))
        exts = ['*.'+str(ext) for ext in QImageWriter.supportedImageFormats()]
        extStr = self.tr("Icon Files") + " ({})".format(' '.join(exts))
        iconFile = QFileDialog.getOpenFileName(self, self.tr("Icon"), iconPath, extStr)[0]
        if iconFile:
            self.setIconFile(iconFile)
            self.iconChanged.emit()
            
    def getIconName(self):
        return self.defaultAction().data()
    
    def setIcon(self, icon):
        self.defaultAction().setIcon(icons.get(icon))
        self.defaultAction().setData(icon)
