

"""
Dialog to add or edit a key.
"""

from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import Signal
from keyTools import keyGroups
from pageEditor import *  # @UnusedWildImport
from widgets import IconChooser, Separator
import data as d
import icons


        
class KeysymPicker(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        layout = QHBoxLayout(self)
        layout.setSpacing(2)
        menuButton = QToolButton()
        menuButton.setText('...')
        menuButton.setPopupMode(QToolButton.InstantPopup)
        searchButton = SearchButton()
        self.lineEdit = QLineEdit()
        self.label = QLabel()
        self.label.setMinimumWidth(150)
        self.lineEdit.setFixedWidth(100)
        self.lineEdit.setValidator(HexValidator(self))
        
        layout.addWidget(menuButton)
        layout.addWidget(searchButton)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label, 1)
        self._keysym = 0
        
        menu = QMenu(self)
        keysymList = []
        for group, data in keyGroups.groups:
            m = menu.addMenu(group)
            for keysym in data:
                a = m.addAction(util.keysym2text(keysym))
                a.setData(keysym)
                keysymList.append(keysym)
                
        searchButton.setKeysyms(keysymList)        
        
        menuButton.setMenu(menu)
        menu.triggered.connect(self.slotMenu)
        searchButton.keysymSelected.connect(self.slotSearch)
        self.lineEdit.textChanged.connect(self.slotKeysymChanged)
    
    def _setLineEditText(self, keysym):
        self.lineEdit.setText('0x{0:04X}'.format(keysym) if keysym else '')
        
    def slotMenu(self, act):
        self.setKeysym(act.data())
        
    def slotKeysymChanged(self, text):
        if self.isValid():
            self.updateLabel()
        else:
            self.label.setText(self.tr("Invalid"))
        
    def slotSearch(self, keysym):    
        self.setKeysym(keysym)
            
    def keysym(self):
        text = self.lineEdit.text()
        if not text:
            return 0x0
        try:
            return int(text, 16)
        except:
            return None
    
    def updateLabel(self):
        keysym = self.keysym()
        name = keyTools.keysym2name(keysym)
        if name:
            char = keyTools.keysym2char(keysym)
            label = name
            if char:
                label = u'{} ({})'.format(label, char)
            self.label.setText(label)
        else:
            self.label.setText('')
            
    def setFocus_(self):
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        
    def isValid(self):
        keysym = self.keysym()
        if keysym == 0:
            return True
        if keysym is not None:
            name = keyTools.keysym2name(keysym)
            if name:
                return True
        return False
    
    def setKeysym(self, keysym):
        self._keysym = keysym
        self._setLineEditText(keysym)
        self.updateLabel()
    

class HexValidator(QValidator):
    def __init__(self, parent):
        QValidator.__init__(self, parent)
        
    def validate(self, text, pos):
        if not text:
            return QValidator.Acceptable, text
            
        text = '0x' + filter(lambda c: c.upper() in "ABCDEF0123456789", text[2:]).upper()
        return QValidator.Acceptable, text


class TextLineEdit(QLineEdit):
    focusIn = Signal()
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        
    def focusInEvent(self, event):
        self.focusIn.emit()
        
        QLineEdit.focusInEvent(self, event)


class RemappingDialog(QDialog):
    def __init__(self, parent, keycode, keysyms=None):
        super(RemappingDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("remapping editor"))
        layout = QVBoxLayout(self)
        if not keysyms:
            keysyms = parent.keyTools().keycode2keysyms(keycode)
        self.keysymPickers = []
        for i in range(4):
            keysymPicker = KeysymPicker(self)
            self.keysymPickers.append(keysymPicker)
            if len(keysyms) > i:
                keysymPicker.setKeysym(keysyms[i])
            layout.addWidget(keysymPicker)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok,
                                     rejected=self.reject, accepted=self.accept)
        
        layout.addStretch(1)
        layout.addWidget(Separator())
        layout.addWidget(buttonBox)
    
    def invalid(self):
        for i, pick in enumerate(self.keysymPickers):
            if not pick.isValid():
                return i
            
        return -1
    
    def accept(self):
        invalid = self.invalid()
        if invalid != -1:
            QMessageBox.warning(self, 'Incorrect value', 'Keysym values sont incorrect.')
            self.keysymPickers[invalid].setFocus_()
            return
        
        self.done(True)
    
    def keysyms(self):
        return [pick.keysym() for pick in self.keysymPickers]
            
        
        
class ShortcutDialog(QDialog):
    textEvent = Signal(unicode)
    iconEvent = Signal(str)
    def __init__(self, parent, mItem=None):
        super(ShortcutDialog, self).__init__(parent)
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
        self.textLineEdit = TextLineEdit()
        self.iconChooser = IconChooser()
        
        
        layoutGroupBox.addRow(self.radioIcon, self.iconChooser)
        layoutGroupBox.addRow(self.radioText, self.textLineEdit)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok,
                                     rejected=self.reject, accepted=self.accept)
        
        layout.addLayout(top)
        layout.addWidget(self.stackedWid)
        layout.addWidget(displayGroupBox)
        layout.addStretch(1)
        layout.addWidget(Separator())
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        
        
        menuList = (d.TEXT, d.KEY, d.COMMAND, d.SHORTCUT, -1, d.LOAD, d.PAUSE, d.STOP, d.RUN_EDITOR)
        #fill the menu
        for typ in menuList:
            if typ != -1:
                title, iconName = d.DATA_TYPE[typ]
                self.typeChooser.addItem(icons.get(iconName), title, typ)
            else:
                self.typeChooser.insertSeparator(self.typeChooser.count())
        
        self.typeToPage = {d.TEXT: PageText(),
                           d.KEY: PageKey(self),
                           d.COMMAND: PageCommand(self),
                           d.SHORTCUT: PageShortcut(),
                            d.LOAD: PageLoad(self)
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
        
        self.iconChooser.iconChanged.connect(self.radioIcon.click)
        self.textLineEdit.focusIn.connect(self.radioText.click)
        self.typeChooser.activated.connect(self.slotTypeChanged)
        self.textEvent.connect(self.slotTextEvent)
        self.iconEvent.connect(self.slotIconEvent)
    
    def load(self, mItem):
        typ = mItem.type
        page = self.typeToPage.get(typ, self.pageEmpty)
        page.setData(mItem.data)
        self.stackedWid.setCurrentWidget(page)
        page.start()
        self.typeChooser.setCurrentIndex(self.typeChooser.findData(typ))
        if mItem.displayType == d.GR_TEXT:
            self.radioText.setChecked(True)
            self.textLineEdit.setText(mItem.displayValue)
        else:
            self.radioIcon.setChecked(True)
            self.iconChooser.setIcon(mItem.displayValue)
    
    def accept(self):
        page = self.stackedWid.currentWidget()
        index = self.typeChooser.currentIndex()
        typ = self.typeChooser.itemData(index)
        if  index == -1:
            QMessageBox.warning(self, self.tr("Warning"), self.tr("You must select a type of key."))
            return
        
        if not page.isValid():
            QMessageBox.warning(self, self.tr("Warning"), page.errorMessage())
            return
        self.displayType = d.GR_ICON if self.radioIcon.isChecked() else d.GR_TEXT
        self.displayValue = self.iconChooser.getIcon() if self.displayType == d.GR_ICON else self.textLineEdit.text()
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
        page = self.typeToPage.get(typ, self.pageEmpty)
        if isinstance(page, PageEmpty):
            self.iconChooser.setIcon(d.DATA_TYPE[typ].icon)
        
        self.stackedWid.setCurrentWidget(page)
        page.start()
        
    def slotTextEvent(self, text):
        self.textLineEdit.setText(text)
        self.radioText.setChecked(True)
        
    def slotIconEvent(self, iconFile):
        self.iconChooser.setIcon(iconFile)
        self.radioIcon.setChecked(True)
        
        
