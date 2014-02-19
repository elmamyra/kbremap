from PySide.QtGui import QIcon
import os.path

def get(name):
        return QIcon(os.path.join(__path__[0], "{}.svg".format(name)).decode('utf-8'))