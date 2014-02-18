#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide.QtGui import *
from PySide.QtCore import *


class Tray(QSystemTrayIcon):
    def __init__(self, parent):
        super(Tray, self).__init__(parent)
        self.activated.connect(self.slotActived)
        self.initUI()
        
    
    def initUI(self):
        self.setIcon(QIcon("keyboard-icon.png"))
        self.setToolTip("Speedy keyboard")
        self.show()
        
    def slotActived(self, reason):
        self.parent().show()
        print "actif"
        
        
