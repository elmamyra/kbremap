# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2012 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
Base class of graphic keyboard.
"""


from PySide.QtCore import *
from PySide.QtGui import *
#from . import util
#from . import data
from Xtools.display import Display
from mapping import MappingItem
import keyboardmodel
import dialogEditor
import util
import data as d
import icons
import time


class KeyBase(QGraphicsRectItem):
    def __init__(self, scene, keycode):
        QGraphicsRectItem.__init__(self, scene=scene)
        self.setAcceptHoverEvents(True)
        self.keyRound = 4
        self._keycode = keycode
        self.content = None
#         self._rect = QRectF()
        self._color = QColor()
        self._mItem = None
        self._isUsed = True
        self._isKeypadKey = False
        self._modifier = -1
        self.font = QFont()
        pen = QPen(util.keyboardColors('border'))
        pen.setWidth(2)
        self.setPen(pen)
        self.tr = QObject().tr
        
    def keycode(self):
        return self._keycode
    
    def mItem(self):
        return self._mItem
    
    def modifier(self):
        return self._modifier
    
    def setModifier(self, mod):
        self._modifier = mod
    
    def isModifier(self):
        return self._modifier != -1
    
    def setIsUsed(self, val):
        self._isUsed = val
        val and self.setColor('not-used')
        
    def isUsed(self):
        return self._isUsed
    
    def setIsKeypadKey(self, val):
        self._isKeypadKey = val
        
    def isKeypadKey(self):
        return self._isKeypadKey
    
    def clear(self):
        if self.content:
            self.scene().removeItem(self.content)
            self.content = None
    
    def setColor(self, colorName):
        self._color = util.keyboardColors(colorName)
        self.setBrush(self._color)
        
    def setMItemTooltip(self):
        if self._mItem:
            t = self._mItem.type
            data = self._mItem.data
            name = d.DATA_TYPE[t].title
            val = ''
            if t == d.TEXT:
                val = '{}<br/>use {}'.format(data[0], self.tr('clipboard') if data[1] else self.tr('system'))
                
            tooltip = u'<b>{}</b><br/>{}'.format(name, val)
            self.setToolTip(tooltip)
    
    def select(self):
        self.setBrush(util.keyboardColors('select'))
        
#     def hover(self):
#         clr = self._color.rgb() + 0x0E0E0E
#         self.setBrush(QColor(clr))
#         
#     def restoreColor(self):
#         self.setBrush(self._color)
    
    def setSize(self, w, h):
#         self._rect.setRect(0, 0, w, h)
        self.setRect(0, 0, w, h)
    
    def getCenter(self, rect):
        x = (self.rect().width() - rect.width()) / 2
        y = (self.rect().height() - rect.height()) / 2
        return QPointF(x, y)
    
    def setText(self, text):
        size = int(self.view().keySize()/2)
        if len(text) > 1:
            size = int(self.view().keySize()/4)
#         self._mItem = None
        self.clear()
            
        self.content = QGraphicsTextItem(text, self)
        self.font.setPixelSize(size)
        self.content.setFont(self.font)
        self.content.setPos(self.getCenter(self.content.boundingRect()))
        self.setToolTip('')
        
    def setIcon(self, iconName, tooltip='', sizeCoef = 0.5, isPath=False):
        self.clear()
        icon = QIcon(iconName) if isPath else icons.get(iconName) 
        size = int(self.view().keySize()*sizeCoef)
        pix = icon.pixmap(size, size)
        self.content = QGraphicsPixmapItem(pix, self)
        self.content.setPos(self.getCenter(self.content.boundingRect()))
        self.setToolTip(tooltip)
    
    def setMappingItem(self, mItem):
        self._mItem = mItem
        val = mItem.displayValue
        if mItem.displayType == d.GR_TEXT:
            pass
        self.setText(val) if mItem.displayType == d.GR_TEXT else self.setIcon(val, isPath=True) #@NoEffect
        self.setColor('content')
        self.setMItemTooltip()
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.isModifier():
                self.view().modifierPressed.emit(self._modifier)
            else:
                self.view().keyPressed.emit(self)
        else:
            event.ignore()
        
    def mouseDoubleClickEvent(self, event):
        if self.isUsed():
            if event.buttons() == Qt.LeftButton:
                self.view().keyDoubleClicked.emit(self)
            else:
                event.ignore()
        else:
            event.ignore()
  
    def mouseReleaseEvent(self, event):
        if self.isUsed() and event.buttons() == Qt.LeftButton:
            self.view().keyReleased.emit(event.scenePos())
        else:
            event.ignore()
        
    def mouseMoveEvent(self, event):
        if self.isUsed():
            self.view().keyMove.emit(event.scenePos())
        else:
            event.ignore()
    
    def hoverEnterEvent(self, event):
        if self.isUsed():
            clr = self._color.rgb() + 0x0E0E0E
            self.setBrush(QColor(clr))
#         self.view().keyHover.emit(self)
        
    def hoverLeaveEvent(self, event):
        if self.isUsed():
            self.setBrush(self._color)
#         self.view().keyLeave.emit(self)
    
    def view(self):
        return self.scene().views()[0]

    def contextMenuEvent(self, event):
        self.view().keyContext.emit(self, event.screenPos())
    
class Key(KeyBase):
    def __init__(self, scene, keycode):
        KeyBase.__init__(self, scene, keycode)
    
    def paint(self, painter, opt, widget):
        painter.setBrush(self.brush())
        painter.drawRoundedRect(self.rect(), self.keyRound, self.keyRound)
       
        

class ReturnKey(KeyBase):
    def __init__(self, scene, keycode):
        KeyBase.__init__(self, scene, keycode)
        self.infoSize = None
    
    def setInfoSize(self, *infoSize):
        self.infoSize = infoSize
    
    def paint(self, painter, opt, widget):
        painter.setBrush(self.brush())
        w1, w2, space, size = self.infoSize
        path = QPainterPath()

        round_ = self.keyRound * 2
        path.moveTo(round_/2, 0)
        path.arcTo(w1 - round_, 0, round_, round_, 90, -90)
        path.arcTo(w1-round_, size*2+space-round_, round_, round_, 0, -90)
        path.arcTo(w1-w2, size*2+space-round_, round_, round_, -90, -90)
        path.arcTo(w1-w2-round_, size, round_, round_, 0, 90)
        path.arcTo(0, size-round_, round_, round_, -90, -90)
        path.arcTo(0, 0, round_, round_, 180, -90)
        painter.drawPath(path)

        

class KeyboardView(QGraphicsView):
    """ """
    keyPressed = Signal(Key)
    keyReleased = Signal(QPointF)
    modifierPressed = Signal(int)
    keyDoubleClicked = Signal(Key)
    keyModified = Signal()
#     keyContext = Signal(Key, QPoint)
    keyMove = Signal(QPointF)
#     keyHover = Signal(Key)
#     keyLeave = Signal(Key)
    resized = Signal()
    def __init__(self, parent, mainWindow):
        super(KeyboardView, self).__init__(parent)
        self.mainWindow = mainWindow
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)
        self.setBackgroundBrush(util.keyboardColors('bg'))
        self.setMinimumSize(400, 180)
        self.setScene(QGraphicsScene(self))
        self.display = Display()
        self._keys = []
        self._modifierKeys = []
        self._space = 4.0
        self._keySize = 40.0
        self.model = ()
        self._modifierStates = {}
        self.currentPressed = None
        for mod in d.ALT, d.CTRL, d.SHIFT, d.SUPER, d.NUM_LOCK, d.CAPS_LOCK, d.ALT_GR:
            self._modifierStates[mod] = False
        self._modifierStates[d.NUM_LOCK] = True
        
        self.keyDoubleClicked.connect(self.slotEditKey)
        self.modifierPressed.connect(self.slotModifierPressed)
#         self.keyPressed.connect(self.slotKeyPressed)
        self.keyReleased.connect(self.slotKeyReleased)
        self.keyMove.connect(self.slotKeyMove)
    
    def drawKey(self):
        self.scene().clear()
        self._keys = []
        self._modifierKeys = []
        km = keyboardmodel
        x = y = 0
        si = self._keySize
        sp = self._space
        for line in self.model[1:]:
            for data in line:
                keycode, coef = data[:2]
                info = data[2] if len(data) == 3 else None
                w = si*coef[0] + sp*(coef[0]-1)
                h = si*coef[1] + sp*(coef[1]-1)
                if info == km.SPACE:
                    x += w + sp
                    continue
                
                if info == km.RETURN:
                    key = ReturnKey(self.scene(), keycode)
                    w2 = si*5.0/4 + sp*(5.0/4-1)
                    key.setInfoSize(w, w2, sp, si)
                    self._keys.append(key)
                else:
                    key = Key(self.scene(), keycode)
                key.setSize(w, h)
                    
                mod = util.keycodeMod(keycode)
                if mod != -1:
                    key.setModifier(mod)
                    self._modifierKeys.append(key)
                    
                if self.display.isKeypadKey(keycode):
                    key.setIsKeypadKey(True)
                
                if info == km.EMPTY:
                    key.setIsUsed(False)
                self._keys.append(key)
                addY = coef[2]*si+1 if len(coef) == 3 else 0
                key.setPos(x, y+addY)
                x += w + sp
#                 key.keyDoubleClicked.connect(self.slotEditKey)
#                 key.modifierPressed.connect(self.slotModifierPressed)
            y += si + sp
            x = 0
    
    def loadLayout(self):
        for key in self.keys():
            char = self.display.charFromModifier(key.keycode(), *self.usefulModifier())
            item = self.mapping()[(key.keycode(), self.modifier2hexa(key.isKeypadKey()))]
            
            if item:
                key.setMappingItem(item)
            else:
                if not char:
                    firstChar = self.display.charFromModifier(key.keycode())
                    for k in ('BackSpace', 'Tab', 'Num_Lock'):
                        if k == firstChar:
                            char = k
                            break
                    else:
                        key.clear()
                
#                 if not key.isUsed():
#                     key.setColor('not-used')
#                     continue
                 
                if key.isModifier():
                    meth, val = {
                        d.ALT: (key.setText, 'Alt'),
                        d.CTRL: (key.setText, 'Ctrl'),
                        d.SHIFT: (key.setIcon, 'arrow-shift'),
                        d.SUPER: (key.setIcon, 'linux'),
                        d.NUM_LOCK: (key.setText, 'Num\nLock'),
                        d.CAPS_LOCK: (key.setText, 'Caps\nLock'),
                        d.ALT_GR: (key.setText, 'Art Gr'),
                    }[key.modifier()]
                    meth(val)
                        
                elif len(char) > 1:
                    if char == 'BackSpace':
                        key.setIcon('backspace', 'backspace')
                    elif char in ('Tab', 'ISO_Left_Tab'):
                        key.setIcon('tab', 'Tabulation')
                    elif char in ('Up', 'KP_Up'):
                        key.setIcon('arrow-up', 'Up')
                    elif char in ('Left', 'KP_Left'):
                        key.setIcon('arrow-left', 'Left')
                    elif char in ('Right', 'KP_Right'):
                        key.setIcon('arrow-right', 'Right')
                    elif char in ('Down', 'KP_Down'):
                        key.setIcon('arrow-down', 'Down')
                    elif char in ('Return', 'KP_Enter'):
                        key.setIcon('arrow-return', 'Return')
                    elif char in 'Menu':
                        key.setIcon('dropmenu', 'Menu')
                    elif char == 'KP_Divide':
                        key.setText('/')
                    elif char == 'KP_Multiply':
                        key.setText('*')
                    elif char == 'KP_Subtract':
                        key.setText('-')
                    elif char == 'KP_Add':
                        key.setText('+')
                    elif char.startswith('KP_') and char[-1].isdigit():
                        key.setText(char[-1])
                    elif char.startswith('KP_'):
                        key.setText(char[3:].replace('_', '\n'))
                    elif char in ('L1', 'L2'):
                        key.setText(char.replace('L', 'F1'))
                    elif char.lower() == 'dead_circumflex':
                        key.setText(u"\u005E")
                    elif char.lower() == 'dead_acute':
                        key.setText(u"\u00B4")
                    elif char.lower() == 'dead_abovering':
                        key.setText(u"\u00B0")
                    elif char.lower() in ('dead_tilde', 'dead_perispomeni'):
                        key.setText(u"\u007E")
                    elif char == 'dead_belowcomma':
                        key.setText(u"\u00B8")
                    elif char == 'dead_horn':
                        key.setText(u"\u031b")
                    elif char == 'dead_hook':
                        key.setText(u"\u0309")
                    elif char == 'dead_belowdot':
                        key.setText(u"\u0323")
                    elif char.lower().startswith('dead_'):
                        key.setText(self.display.name2Char(char[5:].lower()))
                    else:
                        key.setText(char.replace("_", "\n"))
                
                else:
                    key.setText(char)
                
                if key.isModifier():
                    key.setColor("modifier-on" if self._modifierStates[key.modifier()] else "modifier-off")
                elif not char:
                    key.setColor('no-char')
                    
                elif char.lower().startswith('dead_'):
                    key.setColor('dead-key')
                else:
                    key.setColor('default')
    
    def mapping(self):
        return self.mainWindow.mapping()
    
    def slotModifierPressed(self, mod):
        self._modifierStates[mod] = not self._modifierStates[mod]
        for k in self._modifierKeys:
            if k.modifier() == mod:
                k.setColor("modifier-on" if self._modifierStates[mod] else "modifier-off")
        
        self.loadLayout()
    
    def slotEditKey(self, key):
        if not key.isModifier():
            dlg = dialogEditor.DialogEditor(self)
            if dlg.exec_():
                print 'key', key.isKeypadKey()
                item = MappingItem(key.keycode(), self.modifier2hexa(key.isKeypadKey()), *dlg.getData())
                self.mapping().addItem(item)
                key.setMappingItem(item)
                self.keyModified.emit()
    
    def slotKeyMove(self, pos):
        key = self.keyAt(pos)
        if self.currentPressed:
            pass
        
#     def slotKeyPressed(self, pos):
#         print pos
        
    def slotKeyReleased(self, pos):
        print pos
        
    
    def usefulModifier(self):
        li = (d.SHIFT, d.NUM_LOCK, d.CAPS_LOCK, d.ALT_GR)
        return [self._modifierStates[mod] for mod in li]
    
    def setModel(self, model):
        self.model = keyboardmodel.keyboardModels[model]
        self.hNumKey, self.vNumKey = self.model[0]
        if self.isVisible():
            self.updateSize()
            self.loadLayout()
    
    def keys(self):
        return self._keys
    
    def keySize(self):
        return self._keySize
    
    def modifier2hexa(self, includeNumLock=False):
        modState = 0
        for modId, modMask in d.MODIFIER_MASK.items():
            if self._modifierStates[modId]:
                if modId == d.NUM_LOCK:
                    if includeNumLock:
                        modState |= modMask
                else:
                    modState |= modMask
        return modState

#     def findKeyByChar(self, char):
#         for k in self._keys:
#             if k.char() and k.char() == char:
#                 return k
#         return None
    
    def updateSize(self):
        if not self.model:
            return
        size = self.viewport().size()
        if size is None:
            size = self.viewport().size()
        w = size.width()
        h = size.height()
        margin = 10
        hKey = (w-self._space*self.hNumKey-margin) / (self.hNumKey)
        vKey = (h-self._space*self.vNumKey-margin) / (self.vNumKey)
        self._keySize = min(hKey, vKey)
        wScene = self.hNumKey*(self._keySize+self._space) - self._space
        hScene= self.vNumKey*(self._keySize+self._space) - self._space
        self.scene().setSceneRect(0, 0, wScene, hScene)
        self.drawKey()
        self.loadLayout()
    
    def resizeEvent(self, event):
        self.updateSize()
        