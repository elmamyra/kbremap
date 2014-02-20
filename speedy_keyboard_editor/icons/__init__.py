from PySide.QtGui import QIcon
from PySide.QtCore import QDir
import os.path

QDir.setSearchPaths("icons", [__path__[0].decode('utf-8')])

def get(name):
        return QIcon('icons:{}.svg'.format(name))