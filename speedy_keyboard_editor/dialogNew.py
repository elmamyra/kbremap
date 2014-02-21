from PySide.QtGui import *
from PySide.QtCore import Qt
from mapping import getAllNamesAndTitles

class DialogNew(QDialog):
    def __init__(self, parent, currentName):
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
            if name != currentName:
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