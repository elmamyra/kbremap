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

from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import Qt
from widgets import ShortcutWidget, SearchButton
import os
from kbremap_app import mapping, util, keyTools
import data as d


class PageBase(QWidget):
    def __init__(self, dialog=None):
        QWidget.__init__(self)
        self.dialog = dialog
        self._data = None
        self.layout = QHBoxLayout(self)
        
    def data(self):
        return None
    
    def isValid(self):
        return True
    
    def dialogHasIcon(self):
        if not self.dialog:
            return False
        return self.dialog.displayType() == d.GR_ICON and self.dialog.hasIcon()
    
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
    def __init__(self, dialog):
        PageBase.__init__(self, dialog)
        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(QLabel(self.tr("Text:")))
        self.layout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.slotTextChanged)
    
    def start(self):
        self.lineEdit.setFocus(Qt.OtherFocusReason)
    
    def data(self):
        return self.lineEdit.text()
    
    def setData(self, data):
        self.lineEdit.setText(data)
    
    def slotTextChanged(self, text):
        if not self.dialogHasIcon():
            self.dialog.textEvent.emit(text[:7])
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a text to send.")

    
class PageKey(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self, dialog)
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
        if not self.dialogHasIcon():
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
        PageBase.__init__(self, dialog)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setAcceptDrops(False)
        self.layout.addWidget(QLabel(self.tr("Command:")))
        self.layout.addWidget(self.lineEdit)
        self.setAcceptDrops(True)
        self.lineEdit.textChanged.connect(self.slotCommandChanged)
    
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
    
    def slotCommandChanged(self, text):
        if not self.dialogHasIcon():
            self.dialog.textEvent.emit(text[:7])
        
class PageShortcut(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self, dialog)
        self.shortcutWidget = ShortcutWidget()
        self.layout.addWidget(self.shortcutWidget)
        self.shortcutWidget.shortcutChanged.connect(self.slotShortcutChanged)
    
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
    
    def slotShortcutChanged(self):
        if not self.dialogHasIcon():
            self.dialog.textEvent.emit(self.shortcutWidget.text())


class PageLoad(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self, dialog)
        self.combo = QComboBox()
        self.layout.addWidget(self.combo)
        self.layout.addStretch(1)
        for name, title in mapping.getAllNamesAndTitles(True):
            self.combo.addItem(title, name)
            
        if not self.combo.count():
            self.combo.setDisabled(True)
    
        self.combo.currentIndexChanged[str].connect(self.slotCombo)
    
    def start(self):
        self.dialog.textEvent.emit(self.combo.currentText())
    
    def slotCombo(self, title):
        if not self.dialogHasIcon():
            self.dialog.textEvent.emit(self.combo.currentText())
    
    
    def setData(self, data):
        index = self.combo.findData(data)
        self.combo.setCurrentIndex(index)
        
    def data(self):
        index = self.combo.currentIndex()
        return self.combo.itemData(index)
            

        
    
    
        