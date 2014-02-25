#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import * # @UnusedWildImport
from keyboardview import KeyboardView
from dialogNew import DialogNew
import mapping
import icons
import info
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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
        menuFile = menu.addMenu(self.tr("Fichier"))
        
        
        #mapping menu
#         menuMapping = menu.addMenu(self.tr("Mapping"))
        self.newAction = act(self.tr("New..."), self.slotNew, Qt.Key_N, 'document-new')
        menuFile.addAction(self.newAction)
        
        self.loadMenu = menuFile.addMenu(self.tr("Load"))
        self.fillLoadMenu()
        
        self.saveAction = act(self.tr("Save"), self.slotSave, Qt.Key_S, 'document-save')
        menuFile.addAction(self.saveAction)
        
        self.renameAction = act(self.tr("Rename..."), self.slotRename, Qt.Key_R, 'go-jump')
        menuFile.addAction(self.renameAction)
        
        self.clearAction = act(self.tr("Clear"), self.slotClear, Qt.Key_C, 'edit-clear')
        menuFile.addAction(self.clearAction)
        
        self.deleteAction = act(self.tr("Delete"), self.slotDelete, Qt.Key_D, 'edit-delete')
        menuFile.addAction(self.deleteAction)
        
        menuFile.addSeparator()
        
        self.importAction = act(self.tr("Import..."), self.slotImport, Qt.Key_I, 'folder-open')
        menuFile.addAction(self.importAction)
        
        self.exportAction = act(self.tr("Export..."), self.slotExport, Qt.Key_X, 'document-save-as')
        menuFile.addAction(self.exportAction)
        
        menuFile.addSeparator()
        
        keyboardModel = menuFile.addMenu(self.tr("keyboard model"))
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
        
        menuFile.addSeparator()
        
        a = act(self.tr("Quit"), self.close, Qt.Key_Q, 'application-exit')
        menuFile.addAction(a)
        
        
        self.setMenuBar(menu)
        self.enableAction()
        self.saveAction.setDisabled(True)
    
    def enableAction(self):
        val = self._mapping.isValid()
        for act in (self.renameAction, self.deleteAction, self.exportAction):
            act.setEnabled(val)
    
    def updateTitle(self):
        mappingTitle = self._mapping.title() or self.tr("Untitled")
        modified = "[{}]".format(self.tr("Modified")) if self._isModified else ""
        title = ' '.join((mappingTitle, modified, '-', info.name))
        self.setWindowTitle(title)
    
    def fillLoadMenu(self):
        m = self.loadMenu
        m.clear()
        
        self.mappingActionGroup = ag = QActionGroup(self, exclusive=True)
        
        for name, title in mapping.getAllNamesAndTitles():
            act = ag.addAction(QAction(title, self, checkable=True, checked=name==self._mapping.name()))
            act.setData(name)
            m.addAction(act)
        ag.triggered.connect(self.slotLoad)
        m.setEnabled(bool(ag.actions()))
    
    def mapping(self):   
        return self._mapping
        
        
    def slotKeyboardModel(self, act):
        self.keyboardEditor.setModel(act.data())
    
    def slotModified(self):
        if not self._isModified:
            self._isModified = True
            self.saveAction.setEnabled(True)
            self.updateTitle()

    def slotNew(self):
        if self._isModified:
            resp = self.saveDialog()
            if resp == QMessageBox.Cancel:
                return
            
            if resp == QMessageBox.Save:
                self.saveAction.trigger()
                
        dlg = DialogNew(self, self._mapping.name())
        if dlg.exec_():
            title, from_ = dlg.getData()
            self._mapping.create(title, from_)
            self._mapping.save()
            self._isModified = False
            self.updateTitle()
            self.keyboardEditor.loadLayout()
            self.enableAction()
            self.fillLoadMenu()
        
    def load(self, name):
        self._mapping.load(name)
        self._isModified = False
        self.enableAction()
        self.updateTitle()
        self.keyboardEditor.loadLayout()
    
    def saveDialog(self):
        title = self.tr("Close mapping")
        name = self._mapping.title() or self.tr("Untitled")
        mess = self.tr("The mapping \"{name}\" has been modified.<br/>\
            Do you want to save your changes or discard them?").format(name=name)
        buttons = QMessageBox.Discard | QMessageBox.Cancel | QMessageBox.Save
        return QMessageBox.question(self, title, mess, buttons=buttons)
        
    
    def slotLoad(self, act):
        if self._isModified:
            resp = self.saveDialog()
        
            if resp == QMessageBox.Cancel:
                prevAction = filter(lambda a: a.data() == self._mapping.name(), 
                                    self.mappingActionGroup.actions())[0]
                prevAction.setChecked(True)
                return
            
            if resp == QMessageBox.Save:
                self.saveAction.trigger()
        
        self.load(act.data())
    
    
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
        self.saveAction.setDisabled(True)
        self.updateTitle()
        
    def slotRename(self):
        newName, isOk = QInputDialog.getText(self, self.tr("Rename"), self.tr("Enter the new name"))
        if isOk:
            self._mapping.rename(newName)
            self.fillLoadMenu()
            self.updateTitle()
    
    def slotClear(self):
        if self._mapping.isValid():
            mess = self.tr("do you really want delete all items?").format(name=self._mapping.title())
            resp = QMessageBox.question(self, self.tr("Warning"), mess, QMessageBox.Yes, QMessageBox.No)
            if resp == QMessageBox.No:
                return
            
            self._mapping.clear()
            self._isModified = True
            self.keyboardEditor.loadLayout()
            self.updateTitle()
        
    def slotDelete(self):
        if self._mapping.isValid():
            mess = self.tr("do you really want delete this \
                        layout <b>{name}</b> and all its items?").format(name=self._mapping.title())
            resp = QMessageBox.question(self, self.tr("Warning"), mess, QMessageBox.Yes, QMessageBox.No)
            if resp == QMessageBox.No:
                return
            
            self._mapping.delete()
            self._isModified = False
            self.enableAction()
            self.updateTitle()
            self.keyboardEditor.loadLayout()
            self.fillLoadMenu()
            
    def slotImport(self):
        print 'not implemented'
        
    def slotExport(self):
        print 'not implemented'
    
    def closeEvent(self, event):
        if self._isModified:
            resp = self.saveDialog()
            if resp == QMessageBox.Cancel:
                return
            
            if resp == QMessageBox.Save:
                self.saveAction.trigger()
        
        settings = QSettings()
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("windowState", self.saveState())
        settings.setValue("keyboardModel", self.modelActionGroup.checkedAction().data())
        if self._mapping.isValid():
            settings.setValue('mapping', self._mapping.name())
        
        QMainWindow.closeEvent(self, event)
        
def start():
    app = QApplication(sys.argv)
    locale = QLocale.system().name()
    translator=QTranslator ()
    translator.load("qt_" + locale,   
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    QApplication.setApplicationName(info.name)
    QApplication.setApplicationVersion(info.version)
    QApplication.setOrganizationName(info.name)
    QApplication.setOrganizationDomain(info.domain)
    win = MainWindow()
    sys.exit(app.exec_())
        