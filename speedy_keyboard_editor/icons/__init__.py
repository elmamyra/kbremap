from PySide.QtGui import QIcon
from PySide.QtCore import QDir, QFile
import os.path



QDir.setSearchPaths("icons", [__path__[0].decode('utf-8')])



def get(name):
    if QFile('icons:{}.svg'.format(name)).exists():
        return QIcon('icons:{}.svg'.format(name))
    
    if QIcon.hasThemeIcon(name):
        return QIcon.fromTheme(name)
    
    if os.path.exists(name):
        return QIcon(name)
    
    return QIcon()