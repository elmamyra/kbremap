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

import random
from kbremap_app import util
import xml.etree.ElementTree as ET
import unicodedata


class ShortcutItem:
    def __init__(self, keycode, modMask, typ, data, displayType, displayValue):
        self.keycode = keycode
        self.modMask = modMask
        self.type = typ
        self.data = data
        self.displayType = displayType
        self.displayValue = displayValue
    
    @staticmethod
    def fromXml(elt):
        dataElt = elt.find('data')
        data = []
        for valElt in dataElt:
            valText = valElt.text
            dataType = valElt.get('dataType')
            if valText is None:
                val = None
            elif dataType == 'bool':
                val = valText == 'True'
            else:
                val = eval('{}({})'.format(dataType, 'valText'))
                
            data.append(val)
        if len(data) == 1:
            data = data[0]
        keycode = int(elt.get('keycode'))
        modMask = int(elt.get('modMask'), 16)
        typ = int(elt.get('type'))
        displayType = int(elt.get('displayType'))
        displayValue = elt.get('displayValue')
        
        return ShortcutItem(keycode, modMask, typ, data, displayType, displayValue)
            
            
        
        
    def toXml(self):
        attrib = {'type': str(self.type),
                  'keycode': str(self.keycode), 
                  'modMask': hex(self.modMask),
                  'displayType': str(self.displayType),
                  'displayValue': unicode(self.displayValue)
                  }
        item = ET.Element('shortcutItem', attrib)
        dataElt = ET.Element('data')
        data = self.data
        if not isinstance(data, (list, tuple)):
            data = (data,)
        for d in data:
            dataSub = ET.Element('value')
            if d is not None:
                dataSub.text = unicode(d)
                dataType = d.__class__.__name__
                dataSub.set('dataType', dataType) 
            dataElt.append(dataSub)
        item.append(dataElt)
        return item
        
    def __repr__(self):
        return "<mapping.ShortcutItem keycode={}, modMask={}, type={}, data={}>"\
                    .format(self.keycode, hex(self.modMask), self.type, self.data)


class RemapItem:
    def __init__(self, keycode, keysyms=[]):
        self.keycode = keycode
        self.keysyms = keysyms
        
    @staticmethod
    def fromXml(elt):
        keycode = int(elt.get('keycode'))
        keysyms = []
        for k in elt:
            keysyms.append(int(k.text, 16))
        
        return RemapItem(keycode, keysyms)
            
    
    def toXml(self):
        elt = ET.Element('remappingItem', {'keycode': str(self.keycode)})
        for keysym in self.keysyms:
            keyElt = ET.Element('keysym')
            keyElt.text = hex(keysym)
            elt.append(keyElt)
        return elt
    
    def __getitem__(self, index):
        return self.keysyms[index]
    
    def __len__(self):
        return len(self.keysyms)
    
    def __repr__(self):
        return "<mapping.RemapItem keycode={}, keysym={}>"\
                    .format(self.keycode, ', '.join(map(str, self.keysyms)))

class SubMappingBase:
    def __init__(self, parent):
        self._parent = parent
        self._items = {}
        
    def clear(self):
        self._items = {}
        
    def getItem(self, key):
        return self._items.get(key)
        
    def toXml(self):
        elt = ET.Element(self.tag)
        for item in self._items.values():
            elt.append(item.toXml())
        return elt
    
    def setItems(self, items):
        self._items = items
    
    def fromXml(self, elt):
        self._items = {}
        for item in elt:
            self.addItem(self.itemClass.fromXml(item))
        return self
    
    def save(self):
        if self._parent.name:
            tree = loadTree()
            root = tree.getroot()
            mapping = root.find("mapping[@name='{}']".format(self._parent.name))
            if mapping is None:
                mapping = self._parent.emptyXmlMapping()
                root.append(mapping)
            subMapping = mapping.find(self.tag)
            if subMapping is not None:
                mapping.remove(subMapping)
            
            elt = self.toXml()
            mapping.append(elt)
            util.indentXML(root)
            writeTree(tree)
            
    def popItemFromKey(self, key):
        return self._items.pop(key, None)
        
    def popItem(self, item):
        for k, v in self._items.items():
            if v == item:
                return self._items.pop(k)
        return None
    
    def __getitem__(self, key):
        return self._items.get(key)
    
    def __iter__(self):
        for item in self._items.values():
            yield item
    
    
class ShortcutSubMapping(SubMappingBase):
    tag = 'shortcuts'
    itemClass = ShortcutItem
    def __init__(self, parent):
        SubMappingBase.__init__(self, parent)
        pass
    
    def addItem(self, item):
        self._items[(item.keycode, item.modMask)] = item
        
    
            
    

class RemapSubMapping(SubMappingBase):
    tag = 'remapping'
    itemClass = RemapItem
    def __init__(self, parent):
        SubMappingBase.__init__(self, parent)
        pass
    
    def addItem(self, item):
        self._items[item.keycode] = item
        
    
    

class Mapping:
    def __init__(self, name=''):
        self.name = ''
        self.title = ''
        self._notify = False
        self.shortcut = ShortcutSubMapping(self)
        self.remap = RemapSubMapping(self)
        if name:
            self.load(name)
    
    def create(self, title, from_=None):
        self.clear()
        if from_:
            self.load(from_)
            
        self.name = getUniqueName()
        self.title = getUniqueTile(title)
        
    
    def save(self):
        if self.name:
            tree = loadTree()
            root = tree.getroot()
            root.set('notify', str(self._notify).lower())
            oldMapping = root.find("mapping[@name='{}']".format(self.name))
            if oldMapping is not None:
                root.remove(oldMapping)
            elt = self.toXml()
            self.setIsCurrent(root, elt)
            root.append(elt)
            util.indentXML(root)
            writeTree(tree)
    
    def toXml(self):
        elt = self.emptyXmlMapping()
        elt.append(self.shortcut.toXml())
        elt.append(self.remap.toXml())
        return elt
    
    def clear(self):
        self.name = ''
        self.title = ''
        self.shortcut.clear()
        self.remap.clear()
    
    def notify(self):
        return self._notify
    
    def setNotify(self, val):
        self._notify = val
    
    def loadCurrent(self):
        tree = loadTree()
        if not tree:
            return False
        root = tree.getroot()
        currentElt = root.find("mapping[@isCurrent]")
        if currentElt is not None:
            return self.load(currentElt.get('name'))
        return False
            
    def load(self, name):
        tree = loadTree()
        if not tree:
            return False
        root = tree.getroot()
        self._notify = {'true': True, 'false': False}.get(root.get('notify'), False)
        mappingElt = root.find("mapping[@name='{}']".format(name))
        if mappingElt is not None:
            self.name = name
            self.title = mappingElt.get('title')
            self.setIsCurrent(root, mappingElt)
            writeTree(tree)
            self.shortcut.fromXml(mappingElt.find(ShortcutSubMapping.tag))
            self.remap.fromXml(mappingElt.find(RemapSubMapping.tag))
            return True
        return False
    
    def setIsCurrent(self, root, elt):
        for e in root.findall("mapping[@isCurrent]"):
            e.attrib.pop('isCurrent')
            
        elt.set('isCurrent', 'true')
    
    def emptyXmlMapping(self):
        return ET.Element('mapping', attrib={'name': self.name, 'title': self.title})
    
    def rename(self, title):
        self.title = title
        tree = loadTree()
        root = tree.getroot()
        mappingElt = root.find("mapping[@name='{}']".format(self.name))
        if mappingElt is not None:
            mappingElt.set('title', title)
            writeTree(tree)
            
    def delete(self):
        if self.name:
            tree = loadTree()
            root = tree.getroot()
            mappingElt = root.find("mapping[@name='{}']".format(self.name))
            if mappingElt is not None:
                root.remove(mappingElt)
#                 indent(root)
                writeTree(tree)
                self.clear()
                
    def isValid(self):
        return bool(self.name) and bool(self.title)
    
    

def writeTree(tree):
    tree.write(util.configPath(), encoding="utf-8", xml_declaration=True)

def loadTree():
    configPath = util.configPath()
    try:
        tree = ET.parse(configPath)
    except ET.ParseError, err:
        if err.code == 3:
            elt = ET.Element('mappingList', attrib={'notify': 'true', 'version': '1.0'})
            tree = ET.ElementTree(elt)
        else:
            return None
    return tree     
    
            
    


def _getAll(attr):
    configPath = util.configPath()
    try:
        root = ET.parse(configPath).getroot()
        return [elt.attrib[attr] for elt in root]
    except:
        return []
    return []

def getAllNames():
    return _getAll('name')

def getAllTitles():
    return _getAll('title')

def getAllNamesAndTitles(exceptCurrent=False):
    configPath = util.configPath()
    try:
        root = ET.parse(configPath).getroot()
        val = []
        for elt in root:
            if exceptCurrent and elt.get('isCurrent'):
                continue
             
            val.append((elt.attrib['name'], elt.attrib['title']))
        return sorted(val, key=lambda v: removeAccents(unicode(v[1].lower())))
    
    except:
        return []
    
def removeAccents(text):
    nkfd_form = unicodedata.normalize('NFKD', text)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii

def getUniqueName():
    names = getAllNames()
    while True:
        u = "n{0:06.0f}".format(random.random()*1000000)
        if u not in names:
            break
    return u

def getUniqueTile(title):
    titles = getAllTitles()
    newTitle = title
    i = 2
    while newTitle in titles:
        newTitle = "{}-{}".format(title, i)
        i += 1
        
    return newTitle
    
    
