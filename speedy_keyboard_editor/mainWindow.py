#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import * # @UnusedWildImport
from keyboardview import KeyboardView
import mapping
import icons
import info

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
#         self.shift = self.altGr = self.numLock = self.capsLock = False
#         self.ctrl = self.alt = self.super = False
        self._isModified = False
        self.readSettings()
        self.setMenu()
        
        QApplication.setWindowIcon(icons.get('speedy-keyboard'))
        centralWidget = QWidget(self)
        layout = QVBoxLayout(centralWidget)
        self.keyboardEditor = KeyboardView(centralWidget, self)
        self.keyboardEditor.setModel(self.keyboardModel)
        layout.addWidget(self.keyboardEditor)
        self.setCentralWidget(centralWidget)
        self.updateTitle()
#         self.shift = True

        self.keyboardEditor.keyModified.connect(self.slotModified)
        self.show()
    
    def readSettings(self):
        settings = QSettings()
        if settings.allKeys():
            self.restoreGeometry(settings.value('geometry'))
            self.restoreState(settings.value('windowState'))
        else:
            self.resize(1000, 260)
            
        self.keyboardModel = settings.value('keyboardModel', 'generic_105')
        self._mapping = mapping.Mapping(settings.value('mapping', None))

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
    
#     def findItem(self, keycode, modId):
#         return None
    
    def updateTitle(self):
        mappingTitle = self._mapping.title() or self.tr("Untitled")
        modified = "[{}]".format(self.tr("Modified")) if self._isModified else ""
        title = ' '.join((mappingTitle, modified, '-', info.name))
        self.setWindowTitle(title)
    
    def mapping(self):   
        return self._mapping
        
        
    def slotKeyboardModel(self, act):
        self.keyboardEditor.setModel(act.data())
    
    def slotModified(self):
        if not self._isModified:
            self._isModified = True
            self.updateTitle()

    def slotNew(self):
        print 'not implemented'
        
    def slotSave(self):
        if not self._mapping.isValid():
            title, isOk = QInputDialog.getText(self, self.tr("mapping name"), 
                                               self.tr("Enter a name for this mapping"))
            if isOk and title:
                title = mapping.getUniqueTile(title)
                self._mapping.setName(mapping.getUniqueName())
                self._mapping.setTitle(title)
                self.save()
        else:
            self.save()
    
    def save(self):
        self._mapping.save()
        self._isModified = False
        self.updateTitle()
        
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
        if self._mapping.isValid():
            settings.setValue('mapping', self._mapping.name())
        
        QMainWindow.closeEvent(self, event)
        
        
        