
from PySide.QtCore import QSettings
import info
import random


class MappingItem:
    def __init__(self, keycode, mod, data):
        self._keycode = keycode
        self._mod = mod
        self._data = data


class Mapping:
    def __init__(self, name=''):
        self._name = ''
        self._title = ''
        self._mappingItems = []
        if name:
            self.load()
    
    def load(self):
        pass
    
    def create(self, title, from_=None):
        if from_:
            self.load(from_)
        else:
            self.clear()
            
        self._name = getUniqueName()
        self._title = title
    
    
    def __iter__(self):
        for item in self._mappingItems:
            yield item


def getUniqueName():
    names = QSettings(info.name, 'mappings').childGroups()
    while True:
        u = "n{0:06.0f}".format(random.random()*1000000)
        if u not in names:
            break
    return u