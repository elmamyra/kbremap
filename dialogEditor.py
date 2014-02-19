

"""
Dialog to add or edit a key.
"""

from PySide.QtGui import *
from PySide.QtCore import QSize, Qt, QSettings
import os
import util
import data as d
import icons


class IconButton(QToolButton):
    def __init__(self, parent=None):
        super(IconButton, self).__init__(parent)
        self.iconPath = ''
        act = QAction(self,  triggered=self.slotTriggered)
        self.setDefaultAction(act)
        
    def slotTriggered(self):
        iconPath = QSettings().value('icon-path', os.path.join('/usr', 'share', 'icons'))
        exts = ['*.'+str(ext) for ext in QImageWriter.supportedImageFormats()]
        extStr = self.tr("Icon Files") + " ({})".format(' '.join(exts))
        iconFile = QFileDialog.getOpenFileName(self, self.tr("Icon"), iconPath, extStr)[0]
        if iconFile:
            self.defaultAction().setIcon(QIcon(iconFile))
            self.defaultAction().setData(iconFile)
            
    def iconFile(self):
        return self.defaultAction().data()

class DialogEditor(QDialog):
    def __init__(self, parent):
        super(DialogEditor, self).__init__(parent)
        self.setWindowTitle(self.tr("key editor"))
        layout = QVBoxLayout()
        top = QHBoxLayout()
        self.typeButton = QPushButton()
        top.addWidget(QLabel(self.tr("Type:")))
        top.addWidget(self.typeButton)
        top.addStretch(1)
        
        self.stackedWid = QStackedWidget()
        
        displayGroupBox = QGroupBox(self.tr("Display"))
        layoutGroupBox = QFormLayout(displayGroupBox)
        layoutGroupBox.setFormAlignment(Qt.AlignHCenter|Qt.AlignLeft)
        self.radioIcon = QRadioButton(self.tr("Icon:"), checked=True)
        self.radioText = QRadioButton(self.tr("text:"))
        self.iconButton = IconButton()
        self.textLineEdit = QLineEdit()
        
        self.iconButton.setIconSize(QSize(32, 32))
        
        layoutGroupBox.addRow(self.radioIcon, self.iconButton)
        layoutGroupBox.addRow(self.radioText, self.textLineEdit)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok,
                                     rejected=self.reject, accepted=self.accept)
        
        layout.addLayout(top)
        layout.addWidget(self.stackedWid)
        layout.addWidget(displayGroupBox)
        layout.addWidget(util.Separator())
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        
        
        dataMenu = {
            d.TEXT: (self.tr("Text"), 'text'),
            d.LAUNCHER: (self.tr("Launcher"), 'launcher'),
            d.SHORTCUT: (self.tr("Shortcut"), 'shortcuts'),
            
            }
        
        menuList = (d.TEXT, d.LAUNCHER, d.SHORTCUT)
        #fill the menu
        menu = QMenu(self.typeButton)
        for typ in menuList:
            title, iconName = dataMenu[typ]
            menu.addAction(icons.get(iconName), title).setData(typ)
            
        self.typeButton.setMenu(menu)
        
        menu.triggered.connect(self.slotTypeChanged)
        
    def slotTypeChanged(self, act):
        self.typeButton.setText(act.text())
        self.typeButton.setIcon(act.icon())
