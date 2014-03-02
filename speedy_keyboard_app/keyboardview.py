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
from Xtools import display
from mapping import MappingItem
import keyboardmodel
import dialogEditor
import util
import data as d
import icons
import os
import time


class KeyBase(QGraphicsRectItem):
    def __init__(self, scene, keycode):
        QGraphicsRectItem.__init__(self, scene=scene)
        self.setAcceptHoverEvents(True)
        self.keyRound = 4
        self._keycode = keycode
        self.content = None
        self._color = QColor()
        self._mItem = None
        self._isUsed = True
        self._isKeypadKey = False
        self._modifier = 0
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
        return bool(self._modifier)
    
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
            self._mItem = None
    
    def setColor(self, colorName):
        self._color = util.keyboardColors(colorName)
        self.updateColor(self._color)
        
    def updateColor(self, color, colorRadius=0x333333, forceShadow=False):
        w = self.rect().width()
        h = self.rect().height()
        gradient = QRadialGradient(w/6, h/6, max(w, h)*1.2 , w/2, h/2)
        gradient.setColorAt(0, self._color);
        gradient.setColorAt(0.8, QColor(color.rgb() - colorRadius))
        brush = QBrush(gradient)
        self.setBrush(brush)
        
    def setMItemTooltip(self):
        if self._mItem:
            t = self._mItem.type
            data = self._mItem.data
            name = d.DATA_TYPE[t].title
            val = ''
            if t == d.TEXT:
                val = u'{}<br/>use {}'.format(data[0], self.tr('clipboard') if data[1] else self.tr('system'))
            elif t == d.SHORTCUT:
                val = data[2]
            elif t == d.REMAPPING:
                val = u"<b>{}</b> {}".format(data[1], data[0])
            else:
                val = data
            
            tooltip = u'<b>{}</b><br/>{}'.format(name, val)
            
            self.setToolTip(tooltip)
    
    def pixmap(self):
        if self._mItem:
            if self._mItem.displayType == d.GR_ICON:
                pix = self.content.pixmap()
            else:
                fontMetric = QFontMetrics(self.content.font())
                rect = fontMetric.tightBoundingRect(self.content.toPlainText())
                size = rect.size()
                pix = QPixmap(size)
                pix.fill(Qt.transparent)
                painter = QPainter(pix)
                painter.setFont(self.content.font())
                x = -rect.x() + (size.width() - rect.width())/2
                y = -rect.y() + (size.height() - rect.height())/2
                painter.drawText(x, y, self.content.toPlainText())
                painter.end()
            return pix
        return None
    
    def select(self):
        self.updateColor(QColor(self._color.rgb() + 0x0E0E0E), 0x222222)
        
#         
    def restoreColor(self):
        self.updateColor(self._color)
    
    def setSize(self, w, h):
        self.setRect(0, 0, w, h)
        minSize = min(w, h)
        self.keyRound = minSize/10.0
        pen = self.pen()
        pen.setWidth(minSize/20.0)
        self.setPen(pen)
    
    def getCenter(self, rect):
        x = (self.rect().width() - rect.width()) / 2
        y = (self.rect().height() - rect.height()) / 2
        return QPointF(x, y)
    
    def setText(self, text, tooltip='', elide=True):
        size = self.view().keySize()
        if len(text) == 1:
            self.font.setPixelSize(int(size/2))
        elif len(text) == 2:
            self.font.setPixelSize(int(size/2.5))
        elif len(text) == 3:
            self.font.setPixelSize(int(size/3))
        else:
            self.font.setPixelSize(int(size/4))
        
        self.setToolTip('')
        if elide:
            metric = QFontMetrics(self.font)
            textWidth = metric.width(text)
            self.setToolTip(text if textWidth >= size-2 else '')
            text = metric.elidedText(text, Qt.ElideRight, size-2)
        
            
        self.clear()
        self.content = QGraphicsTextItem(text, self)
        
        self.content.setFont(self.font)
        self.content.setPos(self.getCenter(self.content.boundingRect()))

        
    def setIcon(self, iconName, tooltip='', sizeCoef = 0.5, isPath=False):
        self.clear()
        icon = icons.get(iconName) 
        size = int(self.view().keySize()*sizeCoef)
        pix = icon.pixmap(size, size)
        self.content = QGraphicsPixmapItem(pix, self)
        self.content.setPos(self.getCenter(self.content.boundingRect()))
        self.setToolTip(tooltip)
    
    def setMitem(self, mItem):
        val = mItem.displayValue
        if mItem.displayType == d.GR_TEXT:
            self.setText(val)
        else:
            self.setIcon(val, sizeCoef=0.8, isPath=True)
        self._mItem = mItem
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
        if self.isUsed():
            self.view().keyReleased.emit(event.scenePos())
        else:
            event.ignore()
        
    def mouseMoveEvent(self, event):
        if self.isUsed() and self._mItem:
            self.view().keyMove.emit(event.scenePos())
        else:
            event.ignore()
    
    def hoverEnterEvent(self, event):
        if self.isUsed():
            self.updateColor(QColor(self._color.rgb() + 0x0E0E0E), 0x222222, True)
#             self.setBrush(QColor(clr))
#             self.effect.setColor(QColor(self._color.rgb() - 0x5A5A5A))
#             self.effect.setEnabled(True)
            
        
    def hoverLeaveEvent(self, event):
        if self.isUsed():
            self.restoreColor()
#             self.setBrush(self._color)
#             self.effect.setColor(QColor(self._color.rgb() - 0x7F7F7F))
    
    def view(self):
        return self.scene().views()[0]

    def contextMenuEvent(self, event):
        self.view().keyContext.emit(self, event.screenPos())
    
class Key(KeyBase):
    def __init__(self, scene, keycode):
        KeyBase.__init__(self, scene, keycode)
    
    def paint(self, painter, opt, widget):
        painter.setPen(self.pen())
        painter.setBrush(self.brush())
        painter.drawRoundedRect(self.rect(), self.keyRound, self.keyRound)
       
        

class ReturnKey(KeyBase):
    def __init__(self, scene, keycode):
        KeyBase.__init__(self, scene, keycode)
        self.infoSize = None
    
    def setInfoSize(self, *infoSize):
        self.infoSize = infoSize
    
    def paint(self, painter, opt, widget):
        painter.setPen(self.pen())
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
    keyPressed = Signal(KeyBase)
    keyReleased = Signal(KeyBase)
    modifierPressed = Signal(int)
    keyDoubleClicked = Signal(KeyBase)
    keyModified = Signal()
    keyContext = Signal(Key, QPoint)
    keyMove = Signal(QPointF)
    resized = Signal()
    def __init__(self, parent, mainWindow):
        super(KeyboardView, self).__init__(parent)
        self.mainWindow = mainWindow
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)
#         self.setBackgroundBrush(util.keyboardColors('bg'))
        self.setMinimumSize(400, 180)
        self.setScene(QGraphicsScene(self))
        self.display = display.Display()
        self._keys = []
        self._modifierKeys = []
        self._space = 5.0
        self._keySize = 40.0
        self.model = ()
        self._currentModifier = self.display.numMask()
        self.currentPressed = None
        self.currentHover = None
        
        self.keyDoubleClicked.connect(self.slotEditKey)
        self.modifierPressed.connect(self.slotModifierPressed)
        self.keyReleased.connect(self.slotKeyReleased)
        self.keyMove.connect(self.slotKeyMove)
        self.keyContext.connect(self.slotContext)

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
                    
                if self.display.isModifier(keycode):
                    key.setModifier(self.display.getModMask(keycode))
                    self._modifierKeys.append(key)
                    
                if self.display.isKeypadKey(keycode):
                    key.setIsKeypadKey(True)
                
                if info == km.EMPTY:
                    key.setIsUsed(False)
                self._keys.append(key)
                addY = coef[2]*si+1 if len(coef) == 3 else 0
                key.setPos(x, y+addY)
                x += w + sp
            y += si + sp
            x = 0
    
    def loadLayout(self):
        for key in self._keys:
            self.loadKey(key)
            
            
    def loadKey(self, key):
        if not key.isUsed():
            key.setColor('not-used')
            return
        key.clear()
        char, name = self.display.keycode2char(key.keycode(), self._currentModifier)
        keycode = key.keycode()
        mods = self.display.removeNumLockMask(keycode, self._currentModifier)
        item = self.mapping()[keycode, mods]
        if item:
            key.setMitem(item)
        else:
            if char:
                key.setText(char)
            elif name:
                if name in ('Shift_L', 'Shift_R'):
                    key.setIcon('arrow-shift')
                elif name in ('Control_L', 'Control_R'):
                    key.setText('Ctrl')
                elif name in ('Alt_L', 'Alt_R'):
                    key.setText('Alt')
                elif name == 'ISO_Level3_Shift':
                    key.setText('Art Gr'),
                elif name in ('Super_L', 'Super_R'):
                    key.setIcon('linux')
                elif name == 'BackSpace':
                    key.setIcon('backspace', 'backspace')
                elif name in ('Tab', 'ISO_Left_Tab'):
                    key.setIcon('tab', 'Tabulation')
                elif name in ('Up', 'KP_Up'):
                    key.setIcon('arrow-up', 'Up')
                elif name in ('Left', 'KP_Left'):
                    key.setIcon('arrow-left', 'Left')
                elif name in ('Right', 'KP_Right'):
                    key.setIcon('arrow-right', 'Right')
                elif name in ('Down', 'KP_Down'):
                    key.setIcon('arrow-down', 'Down')
                elif name in ('Return', 'KP_Enter'):
                    key.setIcon('arrow-return', 'Return')
                elif name in 'Menu':
                    key.setIcon('dropmenu', 'Menu')
                elif name.startswith('KP_'):
                    key.setText(name[3:].replace('_', '\n'), name, False)
                elif name.lower() == 'dead_circumflex':
                    key.setText(u"\u005E")
                elif name.lower() == 'dead_acute':
                    key.setText(u"\u00B4")
                elif name.lower() == 'dead_abovering':
                    key.setText(u"\u00B0")
                elif name.lower() in ('dead_tilde', 'dead_perispomeni'):
                    key.setText(u"\u007E")
                elif name == 'dead_belowcomma':
                    key.setText(u"\u00B8")
                elif name == 'dead_horn':
                    key.setText(u"\u031b")
                elif name == 'dead_hook':
                    key.setText(u"\u0309")
                elif name == 'dead_belowdot':
                    key.setText(u"\u0323")
                elif name.lower().startswith('dead_'):
                    key.setText(display.name2Char(name[5:].lower()))
                elif name in ('Page_Up', 'Page_Down', 'Num_Lock', 'Caps_Lock'):
                    key.setText(name.replace('_', '\n'), elide=False)
                elif name == 'voidSymbol':
                    name = char = ''
                else:
                    key.setText(name.replace('_', ' '))
            
            if key.isModifier():
                key.setColor("modifier-on" if self._currentModifier & key.modifier() else "modifier-off")
            elif not char and name:
                key.setColor('special-key')
            elif char:
                key.setColor('default')
            else:
                key.setColor('no-char')
#             else:
#                 key.setColor('default')
                
                
#                 len(name) > 1:
#                 key.setColor('dead-key')
                
#             elif char.lower().startswith('dead_'):
#                 key.setColor('dead-key')
            
#     
    
    def mapping(self):
        return self.mainWindow.mapping()
    
    def slotModifierPressed(self, mod):
        self.toggleModifier(mod)
        self.loadLayout()
        
    def toggleModifier(self, mod):
        if self._currentModifier & mod:
            self._currentModifier ^= mod
        else:
            self._currentModifier |= mod
        
    
    def slotEditKey(self, key):
        if key.isModifier():
            return
        
        dlg = dialogEditor.DialogEditor(self, key.mItem())
        if dlg.exec_():
            item = MappingItem(key.keycode(), self.display.removeNumLockMask(key.keycode(), self._currentModifier), *dlg.getData())
            self.mapping().addItem(item)
            key.setMitem(item)
            self.keyModified.emit()
        
    
    def slotKeyReleased(self, pos):
        key = self.keyAt(pos)
        if self.currentPressed and key and key.isUsed() and not key.isModifier():
            sourceMItem = self.mapping().popItem(self.currentPressed)
            sourceModifiers = sourceMItem.modifiers
            sourceKeycode = sourceMItem.keycode
            cibleKey = key
            modMask = self.display.removeNumLockMask(cibleKey.keycode(), self._currentModifier)
            cibleMItem = self.mapping().popItemFromKey(cibleKey.keycode(), modMask)
            newCibleMItem = sourceMItem
            newCibleMItem.keycode = cibleKey.keycode()
            newCibleMItem.modifiers = modMask
            self.mapping().addItem(newCibleMItem)
            
            if cibleMItem:
                newSourceMItem = cibleMItem
                newSourceMItem.keycode = sourceKeycode
                newSourceMItem.modifiers = sourceModifiers
                self.mapping().addItem(newSourceMItem)
                
            self.loadLayout()
            self.keyModified.emit()
            
            
        self.currentPressed = None
        if self.currentHover:
            self.currentHover.restoreColor()
            self.currentHover = None
        self.setCursor(Qt.ArrowCursor)
    
    def slotKeyMove(self, pos):
        key = self.keyAt(pos)
        if self.currentPressed:
            if self.currentHover != key:
                if self.currentHover:
                    self.currentHover.restoreColor()
                if key and key.isUsed() and not key.isModifier():
                    key.select()
                    self.currentHover = key
                    
        elif key:
            pix = key.pixmap()
            if pix:
                self.setCursor(QCursor(pix))
                self.currentPressed = key.mItem()
                self.currentHover = key
    
    def slotContext(self, key, pos):
        menu = QMenu()
        editAction = QAction(icons.get('document-edit'), self.tr("Edit..."), self)
        deleteAction = QAction(icons.get('list-remove'), self.tr("Remove"), self)
        menu.addAction(editAction)
        if key.mItem():
            menu.addAction(deleteAction)

        act = menu.exec_(pos)
        if act == editAction:
            self.keyDoubleClicked.emit(key)
        elif act == deleteAction:
            if key.mItem():
                self.mapping().popItem(key.mItem())
                key.clear()
                self.keyModified.emit()
                self.loadKey(key)
                
        
    def keyAt(self, pos):
        key = self.scene().itemAt(pos)
        if key and not isinstance(key, KeyBase):
            key = key.parentItem()
        return key
        
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
    
    def updateSize(self):
        if not self.model:
            return
        size = self.viewport().size()
        if size is None:
            size = self.viewport().size()
        w = max(size.width(), self.minimumWidth())
        h = max(size.height(), self.minimumHeight())
        margin = 10
        self._space = w / 300.0
        hKey = (w-self._space*self.hNumKey-margin) / (self.hNumKey)
        vKey = (h-self._space*self.vNumKey-margin) / (self.vNumKey)
        self._keySize = min(hKey, vKey)
        wScene = self.hNumKey*(self._keySize+self._space) - self._space
        hScene= self.vNumKey*(self._keySize+self._space) - self._space
        self.scene().setSceneRect(0, 0, wScene, hScene)
        gradient = QLinearGradient(0, 0, 0, h)
        gradient.setColorAt(0, QColor(util.keyboardColors('bg').rgb() - 0x202020))
        gradient.setColorAt(1, util.keyboardColors('bg'));
        self.setBackgroundBrush(QBrush(gradient))
        
        
        self.drawKey()
        self.loadLayout()
    
    def keyPressEvent(self, event):
        keycode = event.nativeScanCode()
        if keycode in self.display.modifiersKeycodeList():
            mod = self.display.getModMask(keycode)
            self.modifierPressed.emit(mod)
                
                
    def resizeEvent(self, event):
        self.updateSize()
