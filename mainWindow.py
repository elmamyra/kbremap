#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *
from PySide.QtCore import *
from keyboardview import KeyboardView
from mapping import Mapping, MappingItem
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
        self._mapping = Mapping(settings.value('mapping', None))

    def setMenu(self):
        # action generator for actions added to search entry
        def act(text, slot, shortcut=None, icon=None):
            a = QAction(text, self, triggered=slot)
            self.addAction(a)
            a.setShortcutContext(Qt.WidgetWithChildrenShortcut)
            shortcut and a.setShortcut(QKeySequence(shortcut))
            icon and a.setIcon(icons.get(icon))
            return a
        
        menu = QMenuBar()
        #file menu
        menuFile = menu.addMenu(self.tr("&Fichier"))
        keyboardModel = menuFile.addMenu(self.tr("&keyboard model"))
        keyboardModel.triggered.connect(self.slotKeyboardModel)
        modList = ((self.tr('Generic 101'), 'generic_101'), 
                   (self.tr('Generic 102'), 'generic_102'),
                   (self.tr('Generic 104'), 'generic_104'),
                   (self.tr('Generic 105'), 'generic_105'),
                   ('TypeMatrix', 'typeMatrix'),
                   )
        self.modelActionGroup = ag = QActionGroup(self, exclusive=True)

        for title, name in modList:
            modAct = ag.addAction(QAction(title, self, checkable=True, checked=name==self.keyboardModel))
            modAct.setData(name)
            keyboardModel.addAction(modAct)
        
        a = act(self.tr("&Quit"), self.close, Qt.CTRL + Qt.Key_Q, 'application-exit')
        menuFile.addAction(a)
        
        #mapping menu
        menuMapping = menu.addMenu(self.tr("&Mapping"))
        a = act(self.tr("&New..."), self.slotNew, Qt.CTRL + Qt.Key_N, 'document-new')
        menuMapping.addAction(a)
        
        a = act(self.tr("&Save..."), self.slotSave, Qt.CTRL + Qt.Key_S, 'document-save')
        menuMapping.addAction(a)
        
        a = act(self.tr("&Rename..."), self.slotRename, Qt.CTRL + Qt.Key_R, 'go-jump')
        menuMapping.addAction(a)
        
        a = act(self.tr("&Delete"), self.slotDelete, Qt.CTRL + Qt.Key_D, 'edit-delete')
        menuMapping.addAction(a)
        
        menuMapping.addSeparator()
        
        a = act(self.tr("&Import..."), self.slotImport, Qt.CTRL + Qt.Key_I, 'folder-open')
        menuMapping.addAction(a)
        
        a = act(self.tr("E&xport..."), self.slotExport, Qt.CTRL + Qt.Key_I, 'document-save-as')
        menuMapping.addAction(a)
        
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
        
        self.keyboardEditor.keyDoubleClicked.connect(self.slotEditKey)
        
    def slotKeyboardModel(self, act):
        self.keyboardEditor.setModel(act.data())
    
    def slotEditKey(self, key):
        if not key.isModifier():
            dlg = dialogEditor.DialogEditor(self)
            dlg.exec_()
            
    def slotNew(self):
        print 'not implemented'
        
    def slotSave(self):
        print 'not implemented'
    
    def slotRename(self):
        print 'not implemented'
    
    def slotDelete(self):
        print 'not implemented'
    
    def slotImport(self):
        print 'not implemented'
        
    def slotExport(self):
        print 'not implemented'
    
    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())
        settings.setValue("keyboardModel", self.modelActionGroup.checkedAction().data())
        
        QMainWindow.closeEvent(self, event)
        
        
        