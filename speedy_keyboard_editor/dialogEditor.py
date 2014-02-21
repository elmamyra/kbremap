

"""
Dialog to add or edit a key.
"""

from PySide.QtGui import *
from PySide.QtCore import Qt
from pageEditor import *
import util
import data as d
import icons





class DialogEditor(QDialog):
    def __init__(self, parent, mItem=None):
        super(DialogEditor, self).__init__(parent)
        self.setWindowTitle(self.tr("key editor"))
        layout = QVBoxLayout()
        top = QHBoxLayout()
        self.typeChooser = QComboBox()
        top.addWidget(QLabel(self.tr("Type:")))
        top.addWidget(self.typeChooser)
        top.addStretch(1)
        
        self.stackedWid = QStackedWidget()
        
        displayGroupBox = QGroupBox(self.tr("Display"))
        layoutGroupBox = QFormLayout(displayGroupBox)
        layoutGroupBox.setFormAlignment(Qt.AlignHCenter|Qt.AlignLeft)
        self.radioIcon = QRadioButton(self.tr("Icon:"), checked=True)
        self.radioText = QRadioButton(self.tr("text:"))
        self.textLineEdit = QLineEdit()
        self.iconChooser = IconChooser()
        
        
        
        layoutGroupBox.addRow(self.radioIcon, self.iconChooser)
        layoutGroupBox.addRow(self.radioText, self.textLineEdit)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok,
                                     rejected=self.reject, accepted=self.accept)
        
        layout.addLayout(top)
        layout.addWidget(self.stackedWid)
        layout.addWidget(displayGroupBox)
        layout.addStretch(1)
        layout.addWidget(util.Separator())
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        
        
        menuList = (d.TEXT, d.LAUNCHER, d.SHORTCUT)
        #fill the menu
        for typ in menuList:
            title, iconName = d.DATA_TYPE[typ]
            self.typeChooser.addItem(icons.get(iconName), title, typ)
        
        self.typeToPage = {d.TEXT: PageText(),
                           d.LAUNCHER: PageLauncher(),
                           d.SHORTCUT: PageShortcut()
                        }
        
        for page in self.typeToPage.values():
            self.stackedWid.addWidget(page)
        
        self.pageEmpty = PageEmpty()
        self.stackedWid.addWidget(self.pageEmpty)
        
        if mItem is not None:
            self.load(mItem)
        else:
            self.typeChooser.setCurrentIndex(-1)
            self.stackedWid.setCurrentWidget(self.pageEmpty)
        
        
        self.typeChooser.activated.connect(self.slotTypeChanged)
    
    def load(self, mItem):
        typ = mItem.type
        page = self.typeToPage.get(typ, self.pageEmpty)
        page.setData(mItem.data)
        self.stackedWid.setCurrentWidget(page)
        
    
    def accept(self):
        page = self.stackedWid.currentWidget()
        typ = self.typeChooser.currentIndex()
        if  typ == -1:
            QMessageBox.warning(self, self.tr("Warning"), self.tr("You must select a type of key."))
            return
        
        if not page.isValid():
            QMessageBox.warning(self, self.tr("Warning"), page.errorMessage())
            return
        self.displayType = d.GR_ICON if self.radioIcon.isChecked() else d.GR_TEXT
        self.displayValue = self.iconChooser.iconFile() if self.displayType == d.GR_ICON else self.textLineEdit.text()
        if not self.displayValue:
            if self.displayType == d.GR_ICON:
                mess = self.tr("You must select an icon")
            else:
                mess = self.tr("You must enter a text")
            QMessageBox.warning(self, self.tr("Warning"), mess)
            return
        self.data = typ, page.data(), self.displayType, self.displayValue
        self.done(QDialog.Accepted)
    
    def getData(self):
        return self.data
    
    def slotTypeChanged(self, index):
        typ = self.typeChooser.itemData(index)
        self.stackedWid.setCurrentWidget(self.typeToPage.get(typ) or self.pageEmpty)
