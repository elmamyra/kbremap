#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import * # @UnusedWildImport
from keyboardview import KeyboardView
from dialogNew import DialogNew
import network
import mapping
import data as cst
import icons
import info
import os, sys
from subprocess import Popen
import __main__
import dbus
PORT = 45691

class MainWindow(QMainWindow):
    updated = Signal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.action = Action(self)
#         self.setWindowState(Qt.WindowActive)

        
        centralWidget = QWidget(self)
        layout = QVBoxLayout(centralWidget)
        self.keyboardEditor = KeyboardView(centralWidget, self)
        self.keyboardEditor.setFocus()
        layout.addWidget(self.keyboardEditor)
        self.setCentralWidget(centralWidget)
        self.readSettings()
        self.setMenu()
        self.setToolBar()
#         self.fillLoadMenu()
        QApplication.setWindowIcon(icons.get('speedy-keyboard'))
        
        
        self.network = network.Network(self)
        
        self.updateTitle()
        self.action.daemonPauseAction.setEnabled(False)
        self.action.daemonStopAction.setEnabled(False)
        self.action.syncAction.setEnabled(False)
        self._serverState = "stopped"
        self.setStateLabel("stopped")
        

        self.keyboardEditor.keyModified.connect(self.slotModified)
        self.network.messageReceived.connect(self.slotMessageReceived)
        self.network.serverClosed.connect(self.slotServerClosed)
        self.network.connect_()
        self.show()
    
    
    
    def slotMessageReceived(self, msg):
        if msg == 'updated':
            self.setStateLabel(msg, 2)
            self.keyboardEditor.loadLayout()
        if msg.startswith('loaded'):
            self._mapping.load(msg.split()[1])
            self.keyboardEditor.loadLayout()
            self.updateTitle()
            self.setStateLabel('loaded {}'.format(self._mapping.title()), 2)
        elif msg.startswith('state'):
            self.action.daemonPauseAction.blockSignals(True)
            state = msg.split()[1]
            if state == 'paused':
                self.action.daemonPauseAction.setChecked(True)
                self.applyEnabled(False, True, True, True)
                self._serverState = 'paused'
            elif state == 'running':
                self.action.daemonPauseAction.setChecked(False)
                self._serverState = 'running'
                self.applyEnabled(False, True, True, True)
            self.action.daemonPauseAction.blockSignals(False)
            self.setStateLabel()
            
    def slotServerClosed(self):
        self._serverState = 'closed'
        self.applyEnabled(True, False, False, False)
        self.action.daemonPauseAction.setChecked(False)
        self.setStateLabel()
        

    
    def applyEnabled(self, start, stop, pause, sync):
        a = self.action
        a.daemonStartAction.setEnabled(start)
        a.daemonStopAction.setEnabled(stop)
        a.daemonPauseAction.setEnabled(pause)
        a.syncAction.setEnabled(sync)
    
    
    def setStateLabel(self, state='', secs=0):
        state = state or self._serverState
        self.labelState.setText(self.tr("Server state: <b>{}</b>").format(state))
        if secs:
            QTimer.singleShot(int(secs*1000), self.setStateLabel)
    
    def readSettings(self):
        settings = QSettings()
        if settings.allKeys():
            self.restoreGeometry(settings.value('geometry'))
            self.restoreState(settings.value('windowState'))
        else:
            self.resize(920, 340)
        
        
        self.keyboardModel = settings.value('keyboardModel', 'generic_105')
        self.keyboardEditor.setModel(self.keyboardModel)
        mode = int(settings.value('mode', cst.SHORTCUT_MODE))
        for act in self.action.modeGroupAction.actions():
            if act.data() == mode:
                act.setChecked(True)
                break
        
        self._mapping = mapping.Mapping()
        self._mapping.loadCurrent()
        if not self._mapping.isValid():
            self.keyboardEditor.setEnabled(False)
            
        self.keyboardEditor.setMode(mode)
        self.keyboardEditor.loadLayout()
        
        self.action.loadAction.setEnabled(bool(mapping.getAllNames()))
        autoStart = {'true': True, 'false': False}[settings.value('autoStart', 'false')]
        self.action.autoStartAction.setChecked(autoStart)
        
    def setMenu(self):
        a = self.action
        menu = QMenuBar()
        #file menu
        menuFile = menu.addMenu(self.tr("Fichier"))
        menuFile.addAction(a.newAction)
        menuFile.addMenu(a.loadMenu)
        menuFile.addAction(a.renameAction)
#         menuFile.addAction(a.clearAction)
        menuFile.addAction(a.deleteAction)
        menuFile.addSeparator()
        menuFile.addAction(a.importAction)
        menuFile.addAction(a.exportAction)
        
        menuFile.addSeparator()
        
#         keyboardModel = menuFile.addMenu(self.tr("keyboard model"))
#         keyboardModel.triggered.connect(self.slotKeyboardModel)
#         modList = ((self.tr('Generic 101'), 'generic_101'), 
#                    (self.tr('Generic 102'), 'generic_102'),
#                    (self.tr('Generic 104'), 'generic_104'),
#                    (self.tr('Generic 105'), 'generic_105'),
#                    ('TypeMatrix', 'typeMatrix'),
#                    )
#         self.modelActionGroup = ag = QActionGroup(self, exclusive=True)

#         for title, name in modList:
#             modAct = ag.addAction(QAction(title, self, checkable=True, checked=name==self.keyboardModel))
#             modAct.setData(name)
#             keyboardModel.addAction(modAct)
        
        menuFile.addSeparator()
        
        menuFile.addAction(a.quitAction)
        
        menuServer = menu.addMenu(self.tr("Server"))
        
        menuServer.addAction(a.daemonStartAction)
        menuServer.addAction(a.daemonPauseAction)
        menuServer.addAction(a.daemonStopAction)
        menuServer.addAction(a.syncAction)
        menuServer.addSeparator()
        menuServer.addAction(a.autoStartAction)
        
        menuKeyboard = menu.addMenu(self.tr("Keyboard"))
        keyboardModel = menuKeyboard.addMenu(self.tr("keyboard model"))
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
            
        menuMode = menuKeyboard.addMenu(self.tr("Mode"))
        menuMode.addAction(a.shortcutModeAction)
        menuMode.addAction(a.remappingModeAction)
        self.setMenuBar(menu)
        self.enableAction()
    
    def setToolBar(self):
        a = self.action
        toolBar = self.addToolBar(self.tr('Tool bar'))
        toolBar.setIconSize(QSize(20, 20))
        toolBar.setObjectName('mainToolBar')
        loadTool = QToolButton()
        loadTool.setMenu(a.loadMenu)
        loadTool.setDefaultAction(a.loadAction)
        loadTool.setPopupMode(QToolButton.InstantPopup)
        self.labelState = QLabel()
         
        toolBar.addAction(a.newAction)
        toolBar.addWidget(loadTool)
        toolBar.addSeparator()
        toolBar.addAction(a.daemonStartAction)
        toolBar.addAction(a.daemonPauseAction)
        toolBar.addAction(a.daemonStopAction)
        toolBar.addAction(a.syncAction)
        toolBar.addSeparator()
        toolBar.addAction(a.shortcutModeAction)
        toolBar.addAction(a.remappingModeAction)
        toolBar.addSeparator()
        toolBar.addWidget(self.labelState)
        
        
    def enableAction(self):
        val = self._mapping.isValid()
        a = self.action
        for act in (a.renameAction, a.deleteAction, a.exportAction):
            act.setEnabled(val)
    
    def updateTitle(self):
        mappingTitle = self._mapping.title or self.tr("Untitled")
        title = ' '.join((mappingTitle, '-', info.name))
        self.setWindowTitle(title)
    
    def fillLoadMenu(self):
        m = self.action.loadMenu
        m.clear()
        
        self.mappingActionGroup = ag = QActionGroup(self, exclusive=True)
        
        for name, title in mapping.getAllNamesAndTitles():
            act = ag.addAction(QAction(title, self, checkable=True, checked=name==self._mapping.name))
            act.setData(name)
            m.addAction(act)
        ag.triggered.connect(self.slotLoad)
        m.setEnabled(bool(ag.actions()))
        self.action.loadAction.setEnabled(bool(ag.actions()))
    
    def mapping(self):   
        return self._mapping
        
    
    
    def slotKeyboardModel(self, act):
        self.keyboardEditor.setModel(act.data())
    
    def slotModified(self):
#         self.network.send('update')
        QTimer.singleShot(500, lambda: self.network.send('update'))
#         self.save()

    def slotNew(self):
        dlg = DialogNew(self)
        if dlg.exec_():
            title, from_ = dlg.getData()
            self._mapping.create(title, from_)
            self._mapping.save()
            self.updateTitle()
            self.enableAction()
            self.keyboardEditor.setEnabled(True)
            self.fillLoadMenu()
            self.keyboardEditor.loadLayout()
        
    def load(self, name):
        self._mapping.load(name)
        self.enableAction()
        self.updateTitle()
        self.keyboardEditor.setEnabled(True)
        
    def slotLoad(self, act):
        self.load(act.data())
        self.keyboardEditor.loadLayout()
    
#     def save(self):
#         self._mapping.save()
        
    def slotRename(self):
        newName, isOk = QInputDialog.getText(self, self.tr("Rename"), self.tr("Enter the new name"))
        if isOk:
            self._mapping.rename(newName)
            self.updateTitle()
    
#     def slotClear(self):
#         if self._mapping.isValid():
#             mess = self.tr("do you really want delete all items?").format(name=self._mapping.title)
#             resp = QMessageBox.question(self, self.tr("Warning"), mess, QMessageBox.Yes, QMessageBox.No)
#             if resp == QMessageBox.No:
#                 return
#             
#             self._mapping.clearItems()
#             self.keyboardEditor.loadLayout()
#             self.save()
        
    def slotDelete(self):
        if self._mapping.isValid():
            mess = self.tr("do you really want delete this \
                        layout <b>{name}</b> and all its items?").format(name=self._mapping.title)
            resp = QMessageBox.question(self, self.tr("Warning"), mess, QMessageBox.Yes, QMessageBox.No)
            if resp == QMessageBox.No:
                return
            
            self._mapping.delete()
            self.enableAction()
            self.updateTitle()
            self.fillLoadMenu()
            self.keyboardEditor.setDisabled(True)
            self.keyboardEditor.loadLayout()
            
    def slotImport(self):
        print 'not implemented'
        
    def slotExport(self):
        print 'not implemented'
    
    def slotDeamonStart(self):
        if not self.network.isConnected():
            Popen([sys.argv[0], '-s'], close_fds=True)
            
            
    def slotDeamonStop(self):
        self.network.send('quit')
        
    def slotDeamonPause(self, val):
        self.network.send('pause')
        
    def slotSync(self):
        self.network.send('update')
#         self.updated.emit()
        
        
    def slotAutoStart(self, val):
        configPath = os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser('~/.config/')
        autoStartPath = os.path.join(configPath, 'autostart')
        filePath = os.path.join(autoStartPath, 'speedy-keyboard-server.desktop')
        if val:
            path = __main__.__file__
            text = "[Desktop Entry]\n"
            text += "Type=Application\n"
            text += "Exec={} -s\n".format(path)
            text += "Icon={}.svg\n".format(path)
            text += "Name={}\n".format(info.name)
            text += "Comment={} server\n".format(info.name)
            if not os.path.exists(autoStartPath):
                os.makedirs(autoStartPath)
                
            with open(filePath, 'w') as f:
                f.write(text)
        else:
            if os.path.exists(filePath):
                os.remove(filePath)
    
    def slotModeChanged(self, act):
        self.keyboardEditor.setMode(act.data())
        self.keyboardEditor.loadLayout()
    
    def currentMode(self):
        return self.action.modeGroupAction.checkedAction().data()
    
    def closeEvent(self, event):
        self.network.stop()
        s = QSettings()
        s.setValue("geometry", self.saveGeometry())
        s.setValue("windowState", self.saveState())
        s.setValue("keyboardModel", self.modelActionGroup.checkedAction().data())
        s.setValue("mode", self.currentMode())
#         if self._mapping.isValid():
#             s.setValue('mapping', self._mapping.name())
            
        s.setValue('autoStart', self.action.autoStartAction.isChecked())
        
        QMainWindow.closeEvent(self, event)

class Action(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        def act(text, slot, shortcut=None, icon=None):
            a = QAction(text, parent, triggered=slot)
#             parent.addAction(a)
            a.setShortcutContext(Qt.WidgetWithChildrenShortcut)
            shortcut and a.setShortcut(QKeySequence(shortcut))
            icon and a.setIcon(icons.get(icon))
            return a
        
        self.loadAction = QAction(icons.get('document-open'), self.tr('Load'), parent)
        self.loadMenu = QMenu(self.tr('Load'))
        self.loadMenu.setActiveAction(self.loadAction)
        self.loadMenu.setIcon(icons.get('document-open'))
        self.loadMenu.aboutToShow.connect(parent.fillLoadMenu)
        
        self.newAction = act(self.tr("New..."), parent.slotNew, Qt.Key_N, 'document-new')
        self.renameAction = act(self.tr("Rename..."), parent.slotRename, Qt.Key_R, 'go-jump')
#         self.clearAction = act(self.tr("Clear"), parent.slotClear, Qt.Key_C, 'edit-clear')
        self.deleteAction = act(self.tr("Delete"), parent.slotDelete, Qt.Key_D, 'edit-delete')
        self.importAction = act(self.tr("Import..."), parent.slotImport, Qt.Key_I, 'folder-open')
        self.exportAction = act(self.tr("Export..."), parent.slotExport, Qt.Key_X, 'document-save-as')
        self.quitAction = act(self.tr("Quit"), parent.close, Qt.Key_Q, 'application-exit')
        
        self.daemonStartAction = act(self.tr("Start"), parent.slotDeamonStart, None, 'media-playback-start')
        self.daemonPauseAction = QAction(icons.get('media-playback-pause'), self.tr("Pause/Resume"), parent)
        self.daemonPauseAction.setCheckable(True)
        self.daemonPauseAction.toggled.connect(parent.slotDeamonPause)
        self.daemonStopAction = act(self.tr("Stop"), parent.slotDeamonStop, None, 'media-playback-stop')
        self.syncAction = act(self.tr("Synchronize"), parent.slotSync, None, 'sync')
        self.autoStartAction = QAction(icons.get('gears-sticker'), self.tr("Launch at startup"), parent)
        self.autoStartAction.setCheckable(True)
        self.autoStartAction.toggled.connect(parent.slotAutoStart)
        self.modeGroupAction = mg = QActionGroup(parent)
        self.modeGroupAction.triggered.connect(parent.slotModeChanged)
        self.shortcutModeAction = mg.addAction(icons.get('shortcuts'), self.tr("Shortcut"))
        self.shortcutModeAction.setCheckable(True)
        self.shortcutModeAction.setData(cst.SHORTCUT_MODE)
        self.remappingModeAction = mg.addAction(icons.get('keys'), self.tr("Remapping"))
        self.remappingModeAction.setCheckable(True)
        self.remappingModeAction.setData(cst.REMAPPING_MODE)

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
    MainWindow()
    sys.exit(app.exec_())
    
        