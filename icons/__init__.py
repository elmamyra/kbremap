from PySide.QtGui import QIcon
import os.path

print __path__
def keys(cat, name):
    path = os.path.join(__path__[0], "keys", cat, "{}.svg".format(name))
    return QIcon(path)
    
def app(name):
    if QIcon.hasThemeIcon(name):
        return QIcon.fromTheme(name)
    else:
        return QIcon(os.path.join(__path__[0], "{}.svg".format(name)))