
from PySide.QtCore import QSettings
import info
import random
import util
import xml.etree.ElementTree as ET
from operator import itemgetter
import unicodedata


class MappingItem:
    def __init__(self, keycode, modifiers, typ, data, displayType, displayValue):
        self.keycode = keycode
        self.modifiers = modifiers
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
        modifiers = int(elt.get('modifiers'), 16)
        typ = int(elt.get('type'))
        displayType = int(elt.get('displayType'))
        displayValue = elt.get('displayValue')
        
        return MappingItem(keycode, modifiers, typ, data, displayType, displayValue)
            
            
        
        
    def toXml(self):
        attrib = {'type': str(self.type),
                  'keycode': str(self.keycode), 
                  'modifiers': hex(self.modifiers),
                  'displayType': str(self.displayType),
                  'displayValue': unicode(self.displayValue)
                  }
        item = ET.Element('item', attrib)
        dataElt = ET.Element('data')
        data = self.data
        if not isinstance(data, (list, tuple)):
            data = (data,)
        for i, d in enumerate(data):
            dataSub = ET.Element('value'+str(i+1))
            if d is not None:
                dataSub.text = unicode(d)
                dataType = d.__class__.__name__
                dataSub.set('dataType', dataType) 
            dataElt.append(dataSub)
        item.append(dataElt)
        return item
        
    def __repr__(self):
        return "<mapping.MappingItem keycode={}, modifiers={}, type={}, data={}>"\
                    .format(self.keycode, hex(self.modifiers), self.type, self.data)


class Mapping:
    def __init__(self, name=''):
        self._name = ''
        self._title = ''
        self._mappingItems = {}
        if name:
            self.load(name)
    
    def name(self):
        return self._name
    
    def title(self):
        return self._title
    
    def setName(self, name):
        self._name = name
        
    def setTitle(self, title):
        self._title = title
        
    
    def addItem(self, item):
        self._mappingItems[(item.keycode, item.modifiers)] = item
        
    def getItem(self, keycode, modifiers):
        return self._mappingItems.get((keycode, modifiers))
    
    def popItemFromKey(self, keycode, modifiers):
        return self._mappingItems.pop((keycode, modifiers), None)
        
    def popItem(self, item):
        for k, v in self._mappingItems.items():
            if v == item:
                return self._mappingItems.pop(k)
        return None
    
    def loadCurrent(self):
        tree = self.loadTree()
        root = tree.getroot()
        currentElt = root.find("mapping[@isCurrent]")
        if currentElt is not None:
            self.load(currentElt.get('name'))
            return True
        return False
        
    
    def load(self, name):
        tree = self.loadTree()
        root = tree.getroot()
        mappingElt = root.find("mapping[@name='{}']".format(name))
        if mappingElt is not None:
            self._name = name
            self._title = mappingElt.get('title')
            currentElt = root.find("mapping[@isCurrent]")
            if currentElt is not None:
                currentElt.attrib.pop('isCurrent')
#             mappingElt.attrib.pop('isCurrent')
            mappingElt.set('isCurrent', 'true')
            self.write(tree)
            self._mappingItems = {}
            for itemElt in mappingElt:
                item = MappingItem.fromXml(itemElt)
                self._mappingItems[(item.keycode, item.modifiers)] = item
            return True
        return False
    
    def clearItems(self):
        self._mappingItems = {}
    
    def rename(self, title):
        self._title = title
        tree = self.loadTree()
        root = tree.getroot()
        mappingElt = root.find("mapping[@name='{}']".format(self._name))
        if mappingElt is not None:
            mappingElt.set('title', title)
            tree.write(util.configPath(), encoding="utf-8", xml_declaration=True)
    
    def write(self, tree):
        tree.write(util.configPath(), encoding="utf-8", xml_declaration=True)
    
    def delete(self):
        if self._name:
            tree = self.loadTree()
            root = tree.getroot()
            mappingElt = root.find("mapping[@name='{}']".format(self._name))
            if mappingElt is not None:
                root.remove(mappingElt)
                indent(root)
                tree.write(util.configPath(), encoding="utf-8", xml_declaration=True)
                self._name = ''
                self._title = ''
                self._mappingItems = {}
    
    def save(self):
        if self._name:
            tree = self.loadTree()
            root = tree.getroot()
            oldMapping = root.find("mapping[@name='{}']".format(self._name))
            if oldMapping is not None:
                root.remove(oldMapping)
            elt = self.toXml()
            elt.set('isCurrent', 'true')
            root.append(elt)
            indent(root)
            tree.write(util.configPath(), encoding="utf-8", xml_declaration=True)
    
    def isValid(self):
        return bool(self._name) and bool(self._title)
    
    
    def loadTree(self):
        configPath = util.configPath()
        try:
            tree = ET.parse(configPath)
        except:
            elt = ET.Element('mappingList', attrib={'version': '1.0'})
            tree = ET.ElementTree(elt)
        return tree
    
    def toXml(self):
        mappingElt = ET.Element('mapping', attrib={'name': self._name, 'title': self._title})
        for item in self._mappingItems.values():
            mappingElt.append(item.toXml())
            
        return mappingElt
        
        
    def settings(self):
        return QSettings(info.name, 'mappings')
    
    def create(self, title, from_=None):
        if from_:
            self.load(from_)
        else:
            self._mappingItems = {}
            
        self._name = getUniqueName()
        self._title = getUniqueTile(title)
    
    def iterEntries(self):
        for key in self._mappingItems:
            yield key
    
    def __getitem__(self, key):
        return self._mappingItems.get(key)
    
    def __iter__(self):
        for item in self._mappingItems.values():
            yield item
            
    

def isblank(s):
    """Return True if s is empty or whitespace only."""
    return not s or s.isspace()

def indent(elem, indent_string="    ", level=0):
    """Indent the XML in element.
    
    Text content that is already non-whitespace is not changed.
    
    """
    # based on http://effbot.org/zone/element-lib.htm#prettyprint
    i = "\n" + indent_string * level
    if len(elem):
        if isblank(elem.text):
            elem.text = i + indent_string
        if isblank(elem.tail):
            elem.tail = i
        for elem in elem:
            indent(elem, indent_string, level+1)
        if isblank(elem.tail):
            elem.tail = i
    else:
        if level and isblank(elem.tail):
            elem.tail = i

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
    
    
