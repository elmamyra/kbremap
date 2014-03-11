
from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import Signal, QSettings
import util


class PreferenceDialog(QDialog):
    
    def __init__(self, parent, mItem=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("Preferences"))
        layout = QVBoxLayout(self)
        modelLayout = QHBoxLayout()
        settings = QSettings()
        #startup
        startupCheck = QCheckBox(self.tr("Launch at startup"))
        autoStart = util.str2bool(settings.value('autoStart', 'false'))
        startupCheck.setChecked(autoStart)
        startupCheck.stateChanged.connect(self.slotStartup)
        #auto update
        updateCheck = QCheckBox(self.tr("Automatically update the server"))
        autoUpdate = util.str2bool(settings.value('autoUpdate', 'true'))
        updateCheck.setChecked(autoUpdate)
        updateCheck.stateChanged.connect(self.slotAutoUpdate)
        #notiny
        notifyCheck = QCheckBox(self.tr("Show notification"))
        notify = parent.mapping().notify()
        notifyCheck.setChecked(notify)
        notifyCheck.stateChanged.connect(self.slotNotify)
        #model
        self.comboModel = QComboBox()
        modList = ((self.tr('Generic 101'), 'generic_101'), 
                   (self.tr('Generic 102'), 'generic_102'),
                   (self.tr('Generic 104'), 'generic_104'),
                   (self.tr('Generic 105'), 'generic_105'),
                   ('TypeMatrix', 'typeMatrix'),
                   )
        for title, name in modList:
            self.comboModel.addItem(title, name)
        
        
        currentModel = settings.value('keyboardModel', 'generic_105')
        index = self.comboModel.findData(currentModel)
        self.comboModel.setCurrentIndex(index)
        self.comboModel.currentIndexChanged.connect(self.slotModel)
        
        modelLayout.addWidget(QLabel(self.tr("keyboard model:")))
        modelLayout.addWidget(self.comboModel)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Close,
                                     rejected=self.reject)
        
        
        layout.addWidget(startupCheck)
        layout.addWidget(updateCheck)
        layout.addWidget(notifyCheck)
        layout.addLayout(modelLayout)
        layout.addWidget(util.Separator())
        layout.addWidget(buttonBox)
    
    
    def slotModel(self, index):
        model = self.comboModel.itemData(index)
        self.parent().modelChanged.emit(model)
        QSettings().setValue('keyboardModel', model)
        
    def slotStartup(self, state):
        state = bool(state)
        self.parent().autoStartChanged.emit(state)
        QSettings().setValue('autoStart', state)
        
    def slotAutoUpdate(self, state):
        state = bool(state)
        self.parent().autoUpdateChanged.emit(state)
        QSettings().setValue('autoUpdate', state)
        
    def slotNotify(self, val):
        state = bool(val)
        self.parent().notifyChanged.emit(state)
        mapping = self.parent().mapping()
        mapping.setNotify(state)
        mapping.save()
        
        
        
        