

"""
Dialog to add or edit a key.
"""

from PySide.QtGui import *
from PySide.QtCore import *
import util

class DialogEditor(QDialog):
    def __init__(self, parent):
        super(DialogEditor, self).__init__(parent)
        layout = QVBoxLayout()
        
        top = QHBoxLayout()
        self.typeButton = QPushButton()
        top.addWidget(QLabel(self.tr("Type:")))
        top.addWidget(self.typeButton)
        top.addStretch(1)
        self.stackedWid = QStackedWidget()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        
        layout.addLayout(top)
        layout.addWidget(self.stackedWid)
        layout.addWidget(util.Separator())
        layout.addWidget(buttonBox)
        self.setLayout(layout)