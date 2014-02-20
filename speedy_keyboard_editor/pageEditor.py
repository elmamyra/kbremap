
from PySide.QtGui import *
from widgets import IconChooser


class PageBase(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self._data = None
#         super(PageBase, self).__init__()
#         self.dialog = dialog
        self.layout = QHBoxLayout(self)
#         self.setLayout(self.layout)
        
    def data(self):
        return None
    
    def isValid(self):
        return False
    
    def setData(self, data):
        pass
    
    def errorMessage(self):
        return ''
    
class PageEmpty(PageBase):
    def __init__(self):
        PageBase.__init__(self)
#         self._data = None
#         
#     def setData(self, data):
#         self._data = data
#         
#     def data(self):
#         return self._data

class PageText(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.lineEdit = QLineEdit(self)
        self.checkClipboard = QCheckBox(self.tr("Use clipboard"))
        
        self.layout.addWidget(QLabel(self.tr("Text:")))
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.checkClipboard)
    
    def data(self):
        return (self.lineEdit.text(), self.checkClipboard.isChecked())
    
    def setData(self, data):
        text, clipboard = data
        self.lineEdit.setText(text)
        self.checkClipboard.setChecked(clipboard)
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a text to send.")
    
    
class PageLauncher(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(QLabel(self.tr("Command:")))
        self.layout.addWidget(self.lineEdit)
    
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
        self.layout.addWidget(QLabel("TODO"))
        
    def errorMessage(self):
        return self.tr("You must enter a valid shortcut.")   
        
        
        