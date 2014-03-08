
from PySide.QtGui import *
from PySide.QtCore import Qt
from widgets import ShortcutWidget
from speedy_keyboard_app.Xtools import keyGroups
import os
from gtk import gdk
import mapping
from Xtools import display

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

        

class PageRemapping(PageBase):
    def __init__(self, dialog):
        PageBase.__init__(self)
        self.dialog = dialog
        self.menuButton = QPushButton(self.tr("Choose..."))
        self.layout.addWidget(self.menuButton)
        self.layout.addStretch(1)
        self.fillMenu()
#         self.char = ''
#         self.keyname = ''
        self.keysym = -1
        
    def fillMenu(self):
        menu = QMenu(self.menuButton)
        for group, data in keyGroups.keyGroups:
            m = menu.addMenu(group)
            for keyname, keysym, char_ in data:
                char, name = self.keysym2charAndName(keysym)
                a = m.addAction(u"{}  {}".format(char, name))
                a.setData(keysym)
                
        self.menuButton.setMenu(menu)
        menu.triggered.connect(self.slotMenu)
    
    def setMenuTitle(self, char, keyname):
        self.menuButton.setText(u"{}  {}".format(char, keyname))
    
    def slotMenu(self, act):
        self.menuButton.setText(act.text())
        self.keysym = act.data()
#         self.refreshMenuText()
        char = display.keysym2char(self.keysym)
        if char:
            self.dialog.textEvent.emit(char)
    
#     def keysym2charName(self, keysym):
#         name = gdk.keyval_name(keysym) or ""  # @UndefinedVariable
#         char = gdk.keyval_to_unicode(keysym)  # @UndefinedVariable
#         char = unichr(char) if char else ""
#         return char, name

    def keysym2charAndName(self, keysym):
        return display.keysym2char(keysym), display.keysym2name(keysym)

    def setData(self, data):
        char, name = self.keysym2charAndName(data)
        self.menuButton.setText(u"{}  {}".format(char, name))
#         self.keyname, self.char = data
#         self.refreshMenuText()
        
    def data(self):
        return self.keysym
    
    def isValid(self):
        return self.keysym != -1
    
    def errorMessage(self):
        return self.tr("You must choose a keysym.")
        
        
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
            
        
        
# class PageServer(PageBase):
#     def __init__(self, dialog):
#         PageBase.__init__(self)
#         self.dialog = dialog
#         self.combo = QComboBox()
#         self.layout.addWidget(self.combo)
#         self.li = (('media-playback-start', self.tr("Resume"), 'resume'),
#               ('media-playback-pause', self.tr("Pause"), 'pause'),
#               ('media-playback-stop', self.tr("Stop"), 'quit'),
#               ('sync', self.tr("synchronize"), 'update')
#               )
#               
#         for icon, name, data in self.li:
#             self.combo.addItem(icons.get(icon), name, data)
#         
#         self.action = None
#         self.combo.currentIndexChanged.connect(self.slotCombo)
#     
#     def start(self):
#         index = self.combo.currentIndex()
#         self.slotCombo(index)
#         
#         
#     def setData(self, data):
#         index = self.combo.findData(data)
#         self.combo.setCurrentIndex(index)
#         
#     def data(self):
#         index = self.combo.currentIndex()
#         return self.combo.itemData(index)
#     
#     def slotCombo(self, index):
#         iconName = self.li[index][0]
#         self.dialog.iconEvent.emit(iconName)
#         
            
        
    
    
        