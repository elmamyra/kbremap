
from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import Qt
from widgets import ShortcutWidget, SearchButton
import os
from kbremap import mapping, util, keyTools

class PageBase(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self._data = None
        self.layout = QHBoxLayout(self)
        
    def data(self):
        return None
    
    def isValid(self):
        return True
    
    def setData(self, data):
        pass
    
    def start(self):
        pass
    
    def errorMessage(self):
        return ''
    
class PageEmpty(PageBase):
    def __init__(self):
        PageBase.__init__(self)


class PageText(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(QLabel(self.tr("Text:")))
        self.layout.addWidget(self.lineEdit)
    
    def start(self):
        self.lineEdit.setFocus(Qt.OtherFocusReason)
    
    def data(self):
        return self.lineEdit.text()
    
    def setData(self, data):
        self.lineEdit.setText(data)
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a text to send.")

    
class PageKey(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self)
        self.dialog = dialog
        self._keysym = 0
        ktools = keyTools.KeyTools()
        menu = QMenu(self)
        self.menuButton = QPushButton()
        searchButton = SearchButton()
        self.menuButton.setText(self.tr("Choose..."))
        keysyms = []
        for group, data in keyTools.keyGroups.groups:
            m = QMenu(group)#menu.addMenu(group)
            for keysym in data:
                if ktools.keysym2deadEntries(keysym):
                    a = m.addAction(util.keysym2text(keysym))
                    a.setData(keysym)
                    keysyms.append(keysym)
                    
            if not m.isEmpty():
                menu.addMenu(m)
            
        searchButton.setKeysyms(keysyms)
        self.menuButton.setMenu(menu)
        self.layout.setSpacing(2)
        self.layout.addWidget(self.menuButton)
        self.layout.addWidget(searchButton)
        self.layout.addStretch(1)

        menu.triggered.connect(self.slotMenu)
        searchButton.keysymSelected.connect(self.slotSearch)
        
    def slotMenu(self, act):
        self._keysym = act.data()
        self.updateButtonText()
    
    def updateButtonText(self):
        self.menuButton.setText(util.keysym2text(self._keysym))
        text = keyTools.keysym2char(self._keysym) or keyTools.keysym2name(self._keysym)[:5]
        self.dialog.textEvent.emit(text)
    
    def slotSearch(self, keysym):
        self._keysym = keysym
        self.updateButtonText()
    
    def setData(self, data):
        self._keysym = data
        self.updateButtonText()
        
    def data(self):
        return self._keysym
    
    def isValid(self):
        return self._keysym != 0
    
    def errorMessage(self):
        return self.tr("You must select a key.")
  
    
class PageCommand(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self)
        self.dialog = dialog
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setAcceptDrops(False)
        self.layout.addWidget(QLabel(self.tr("Command:")))
        self.layout.addWidget(self.lineEdit)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
             
        else:
            e.ignore() 

    def start(self):
        self.lineEdit.setFocus(Qt.OtherFocusReason)

    def dropEvent(self, e):
        mime = e.mimeData()
        text = str(mime.data('text/plain')).strip()
        path = text[7:]
        if os.path.exists(path) and os.path.splitext(path)[1] == '.desktop':
            with open(path) as f:
                command = ''
                icon = ''
                for line in f:
                    if line.startswith('Exec='):
                        command = line.split('=')[1]
                    if line.startswith('Icon='):
                        icon = line.split('=')[1]
                
                self.lineEdit.setText(command.strip())
                self.dialog.iconEvent.emit(icon.strip())
        else:
            self.lineEdit.setText(text)
        
    def data(self):
        return self.lineEdit.text()
    
    def setData(self, data):
        self.lineEdit.setText(data)
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a command.")   
    
        
class PageShortcut(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.shortcutWidget = ShortcutWidget()
        self.layout.addWidget(self.shortcutWidget)
    
    def start(self):
        self.shortcutWidget.setFocus(Qt.OtherFocusReason)
        
    def data(self):
        return self.shortcutWidget.data()
    
    def setData(self, data):
        self.shortcutWidget.setData(*data)
        
    def isValid(self):
        return bool(self.shortcutWidget.text())
    
    def errorMessage(self):
        return self.tr("You must enter a shortcut.")   
        


class PageLoad(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self)
        self.combo = QComboBox()
        self.layout.addWidget(self.combo)
        for name, title in mapping.getAllNamesAndTitles(True):
            self.combo.addItem(title, name)
            
    def setData(self, data):
        index = self.combo.findData(data)
        self.combo.setCurrentIndex(index)
        
    def data(self):
        index = self.combo.currentIndex()
        return self.combo.itemData(index)
            

        
    
    
        