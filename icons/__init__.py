from PySide.QtGui import QIcon
import os.path

# print 'theme', QIcon.hasThemeIcon('application-exit')
# def keys(name):
#     path = os.path.join(__path__[0], "keys", "{}.svg".format(name))
#     return QIcon(path)
    
def get(name):
#     if QIcon.hasThemeIcon(name):
#         return QIcon.fromTheme(name)
#     else:
        return QIcon(os.path.join(__path__[0], "{}.svg".format(name)))