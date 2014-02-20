

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
            self.currentType = -1
            self.stackedWid.setCurrentWidget(self.pageEmpty)
        
        
        menu.triggered.connect(self.slotTypeChanged)
    
    def load(self, mItem):
        pass
    
    def accept(self):
        page = self.stackedWid.currentWidget()
        if self.currentType == -1:
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
        self.data = self.currentType, page.data(), self.displayType, self.displayValue
        self.done(QDialog.Accepted)
    
    def getData(self):
        return self.data
    
    def slotTypeChanged(self, act):
        self.stackedWid.setCurrentWidget(self.typeToPage.get(act.data()) or self.pageEmpty)
        self.typeButton.setText(act.text())
        self.typeButton.setIcon(act.icon())
        self.currentType = act.data()
