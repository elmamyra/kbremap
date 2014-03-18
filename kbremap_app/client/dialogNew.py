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
from kbremap_app.mapping import getAllNamesAndTitles

class DialogNew(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowTitle(self.tr("New mapping"))
        layout = QVBoxLayout() 
        self.setLayout(layout)
        self.lineEdit = QLineEdit()
        center = QFormLayout()
        self.comboFrom = QComboBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        center.setLabelAlignment(Qt.AlignRight)
        center.addRow(QLabel(self.tr("Name:")), self.lineEdit)
        center.addRow(QLabel(self.tr("inherited from:")), self.comboFrom)
        
        layout.addLayout(center)
        layout.addWidget(buttonBox)
        
        
        self.comboFrom.addItem('', None)
        for name, title in getAllNamesAndTitles():
            self.comboFrom.addItem(title, name)
        
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
    
    def accept(self):
        if not self.lineEdit.text():
            QMessageBox.warning(self, self.tr("Warning"), self.tr("You must enter name."))
        else:
            self.done(QDialog.Accepted)
        
    def getData(self):
        title = self.lineEdit.text()
        from_ = self.comboFrom.itemData(self.comboFrom.currentIndex())
        return title, from_