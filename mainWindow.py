#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *
from PySide.QtCore import *
from keyboardview import KeyboardView
from mapping import Mapping
import icons
import dialogEditor
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.shift = self.altGr = self.numLock = self.capsLock = False
        self.ctrl = self.alt = self.super = False
        self.readSettings()
        self.setMenu()
        self.initUI()
        self.shift = True
        self.show()
    
    def readSettings(self):
        settings = QSettings()
        if settings.allKeys():
            self.restoreGeometry(settings.value('geometry'))
            self.restoreState(settings.value('windowState'))
        else:
            self.resize(1000, 260)
            
        self.keyboardModel = settings.value('keyboardModel', 'generic_105')
        self._mapping = Mapping()
        
    
    def setMenu(self):
        menu = QMenuBar()
        menuFichier = menu.addMenu(self.tr("Fichier"))
        keyboardModel = menuFichier.addMenu(self.tr("keyboard model"))
        keyboardModel.triggered.connect(self.slotKeyboardModel)
        modList = ((self.tr('Generic 101'), 'generic_101'), 
                   (self.tr('Generic 102'), 'generic_102'),
                   (self.tr('Generic 104'), 'generic_104'),
                   (self.tr('Generic 105'), 'generic_105'),
                   ('TypeMatrix', 'typeMatrix'),
                   )
        self.modelActionGroup = ag = QActionGroup(self, exclusive=True)

        for title, name in modList:
            act = ag.addAction(QAction(title, self, checkable=True, checked=name==self.keyboardModel))
            act.setData(name)
            keyboardModel.addAction(act)
            
            
        
        quit_ = menuFichier.addAction(self.tr("Quit"), self.close)
        quit_.setIcon(icons.get('application-exit'))
        self.setMenuBar(menu)
    
    def findItem(self, keycode, modId):
        return None
    
    
    def initUI(self):
        self.setWindowTitle('Speedy keyboard')
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'speedy-keyboard.svg').decode('utf-8')))
        centralWidget = QWidget(self)
        layout = QVBoxLayout(centralWidget)
        self.keyboardEditor = KeyboardView(centralWidget)
        self.keyboardEditor.setModel(self.keyboardModel)
        layout.addWidget(self.keyboardEditor)
        self.setCentralWidget(centralWidget)
        
        self.keyboardEditor.keyDoubleClicked.connect(self.SlotEditKey)
        
    def slotKeyboardModel(self, act):
        self.keyboardEditor.setModel(act.data())
    
    def SlotEditKey(self, key):
        if not key.isModifier():
            dlg = dialogEditor.DialogEditor(self)
            dlg.exec_()
    
    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())
        settings.setValue("keyboardModel", self.modelActionGroup.checkedAction().data())
        
        QMainWindow.closeEvent(self, event)
        
        
        