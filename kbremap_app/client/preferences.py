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
from PySide.QtCore import QSettings
from kbremap_app import util
from widgets import Separator
import os
import __main__
from kbremap_app import info

class PreferenceDialog(QDialog):
    
    def __init__(self, parent, mItem=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("Preferences"))
        layout = QVBoxLayout(self)
        modelLayout = QHBoxLayout()
        settings = QSettings()
        #startup
        startupCheck = QCheckBox(self.tr("Launch at startup"))
        autoStart = os.path.exists(os.path.join(util.configDir, 'autostart', 'kpremap-server.desktop'))
        startupCheck.setChecked(autoStart)
        startupCheck.stateChanged.connect(self.slotAutoStart)
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
        layout.addWidget(Separator())
        layout.addWidget(buttonBox)
    
    
    def slotModel(self, index):
        model = self.comboModel.itemData(index)
        self.parent().modelChanged.emit(model)
        QSettings().setValue('keyboardModel', model)
    
    def slotAutoStart(self, val):
        print __main__.__file__
        configDir = os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser('~/.config/')
        autoStartPath = os.path.join(configDir, 'autostart')
        filePath = os.path.join(autoStartPath, 'kpremap-server.desktop')
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
        
        
        
        