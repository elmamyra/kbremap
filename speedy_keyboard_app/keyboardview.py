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
from mapping import ShortcutItem, RemapItem
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
        self._shortcutItem = None
        self._remapItem = None
        self._isUsed = True
        self._isKeypadKey = False
        self._modifier = 0
        self._mode = d.SHORTCUT_MODE
        self.font = QFont()
        pen = QPen(util.keyboardColors('border'))
        pen.setWidth(2)
        self.setPen(pen)
        self.tr = QObject().tr
        
    def setEnabled_(self, val):
        if val:
            self.restoreColor()
        else:
            self.updateColor(QColor(80, 80, 80), 0x3A3A3A)
        
        
    def keycode(self):
        return self._keycode
    
    def shortcutItem(self):
        return self._shortcutItem
    
    def remapItem(self):
        return self._remapItem
    
    def modifier(self):
        return self._modifier
    
    def setModifier(self, mod):
        self._modifier = mod
    
    def isModifier(self):
        return bool(self._modifier)
    
    def unused(self):
        self._isUsed = False
        self.noSymbol()
        
    def noSymbol(self):
        self.setColor('not-used')
        self.setEnabled(False)
        self.setToolTip(self.tr('no symbol'))
        
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
            self._shortcutItem = None
            self._remapItem = None
        self.setEnabled(True)
#             self.setAcceptHoverEvents(True)
#             self.setAcceptedMouseButtons(Qt.LeftButton | Qt.RightButton)
        self.setToolTip('')
#             print self.isEnabled()
    
    def setColor(self, colorName):
        self._color = util.keyboardColors(colorName)
        self.updateColor(self._color)
        
    def updateColor(self, color, colorRadius=0x333333):
        w = self.rect().width()
        h = self.rect().height()
        gradient = QRadialGradient(w/6, h/6, max(w, h)*1.2 , w/2, h/2)
        gradient.setColorAt(0, color);
        gradient.setColorAt(0.8, QColor(color.rgb() - colorRadius))
        brush = QBrush(gradient)
        self.setBrush(brush)
        
    def setMItemTooltip(self):
        return
        if self._mItem:
            t = self._mItem.type
            data = self._mItem.data
            name = d.DATA_TYPE[t].title
            val = ''
            if t == d.TEXT:
                pass
#                 val = u'{}<br/>use {}'.format(data[0], self.tr('clipboard') if data[1] else self.tr('system'))
            elif t == d.SHORTCUT:
                val = data[2]
            elif t == d.REMAPPING:
                char = display.keysym2char(data)
                name = display.keysym2name(data)
                val = u"<b>{}</b> {}".format(char, name)
            else:
                val = data
            
            tooltip = u'<b>{}</b><br/>{}'.format(name, val)
            
            self.setToolTip(tooltip)
    
    def pixmap(self):
        pix = None
        if self._shortcutItem:
            if self._shortcutItem.displayType == d.GR_ICON:
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
        
        elif self._remapItem:
            pix = self.content.pixmap()
        return pix
    
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
    
    def setMapChars(self, chars, names):
        size = self.rect().size().toSize()
        standartSize = self.view().keySize()
        hmargin = int(standartSize / 15.0)
        vmargin = int(size.height() / 7.0)
        metric = QFontMetrics(self.font)
        pix = QPixmap(size)
        pix.fill(Qt.transparent)
        painter = QPainter(pix)
        painter.setFont(self.font)
        painter.setPen(self.pen())
        
        def getPos(i, rect):
            return QPoint(*((hmargin, size.height() - vmargin),
                        (hmargin, rect.height() + vmargin),
                        (size.width()/2 , size.height() - vmargin),
                        (size.width()/2 , rect.height() + vmargin))[i])
        
        if len(chars) == 1:
            self.font.setPixelSize(standartSize / 4.5)
            metric = QFontMetrics(self.font)
            char = metric.elidedText(chars[0] or names[0], Qt.ElideRight, size.width()- hmargin*2)
            rect = metric.tightBoundingRect(char)
            posX = (size.width() - rect.width()) / 2
            posY = (size.height() + rect.height()) / 2
            painter.setFont(self.font)
            painter.drawText(QPoint(posX, posY), char)
        elif len(chars) == 2:
            self.font.setPixelSize(standartSize / 5)
            metric = QFontMetrics(self.font)
            char1 = metric.elidedText(chars[0] or names[0], Qt.ElideRight, size.width()- hmargin*2)
            char2 = metric.elidedText(chars[1] or names[1], Qt.ElideRight, size.width()- hmargin*2)
            rect1 = metric.tightBoundingRect(char1)
            pos1 = getPos(0, rect1)
            rect2 = metric.tightBoundingRect(char2)
            pos2 = getPos(1, rect2)
            painter.setFont(self.font)
            painter.drawText(pos1, char1)
            painter.drawText(pos2, char2)
        else:
            for i, char in enumerate(chars):
                char = char or names[i]
                fontCoef = 3.5 if len(char) == 1 else 5.5
                self.font.setPixelSize(standartSize / fontCoef)
#                 if len(char) == 1:
#                     self.font.setPixelSize(standartSize / 3.5)
#                 else:
#                     self.font.setPixelSize(standartSize / 5.5)
                
                metric = QFontMetrics(self.font)
#                 if char.startswith('dead_'):
#                     char = 'dead'

                char = metric.elidedText(char, Qt.ElideRight, size.width()/2.0)
                
                
                painter.setFont(self.font)
                painter.drawText(getPos(i, metric.tightBoundingRect(char)), char)
        
        painter.end()
        
        self.content = QGraphicsPixmapItem(pix, self)
        
        tooltip = ""
        for char, name in zip(chars, names):
            tooltip += u"<b>{}</b> {}<br/>".format(char, name)
         
        self.setToolTip(tooltip)
    
    def setShortcutItem(self, item):
        self._remapItem = None
        val = item.displayValue
        if item.displayType == d.GR_TEXT:
            self.setText(val)
        else:
            self.setIcon(val, sizeCoef=0.8, isPath=True)
        self._shortcutItem = item
        self.setColor('content')
        
        self.setMItemTooltip()
        
    def setRemapItem(self, item):
        self._shortcutItem = None
        self._remapItem = item
        self.setColor('content')
        
    def item(self):
        return self._shortcutItem or self._remapItem
        
    def hasItem(self):
        return bool(self._shortcutItem or self._remapItem)
    
    
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.isModifier():
                self.view().modifierPressed.emit(self._modifier)
            else:
                self.view().keyPressed.emit(self)
        else:
            event.ignore()
        
    def mouseDoubleClickEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.view().keyDoubleClicked.emit(self)
        else:
            event.ignore()
  
    def mouseReleaseEvent(self, event):
        self.view().keyReleased.emit(event.scenePos())
        
    def mouseMoveEvent(self, event):
        if self.hasItem():
            self.view().keyMove.emit(event.scenePos())
        else:
            event.ignore()
    
    def hoverEnterEvent(self, event):
        self.updateColor(QColor(self._color.rgb() + 0x0E0E0E), 0x222222)
        
    def hoverLeaveEvent(self, event):
        self.restoreColor()
    
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
        self.setMinimumSize(400, 180)
        self.setScene(QGraphicsScene(self))
        self._display = display.Display()
        self._keys = []
        self._modifierKeys = []
        self._space = 5.0
        self._keySize = 40.0
        self.model = ()
        self._mode = d.SHORTCUT_MODE
        self._currentModifier = self._display.numMask()
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
                    
                if self._display.isModifier(keycode):
                    key.setModifier(self._display.getModMask(keycode))
                    self._modifierKeys.append(key)
                    
                if self._display.isKeypadKey(keycode):
                    key.setIsKeypadKey(True)
                
                if info == km.EMPTY:
                    key.unused()
                self._keys.append(key)
                addY = coef[2]*si+1 if len(coef) == 3 else 0
                key.setPos(x, y+addY)
                x += w + sp
            y += si + sp
            x = 0
    
    def loadLayout(self):
        meth = self.loadShortKey if self._mode == d.SHORTCUT_MODE else self.loadRemapKey
        for key in self._keys:
            if not key.isUsed():
                continue
            meth(key)
            key.setEnabled_(self.isEnabled())
            
       
    def loadRemapKey(self, key):
        key.clear()
        item = self._subMapping[key.keycode()]
        if item:
            chars, names = [], []
            for keysym in item.keysyms:
                chars.append(display.keysym2char(keysym))
                names.append(display.keysym2name(keysym))
                
            while not names[-1]:
                chars.pop(-1)
                names.pop(-1)
            key.setRemapItem(item)
            key.setMapChars(chars, names)
                
                
        else:
            charsNames = self._display.keycode2charsAndNames(key.keycode())
            key.setColor('default')
            key.setMapChars(*charsNames)
            
        if key.isModifier():
            key.setEnabled(False)
            key.setColor('no-char')
       
    def loadShortKey(self, key):
        key.clear()
        char, name = self._display.keycode2char(key.keycode(), self._currentModifier)
        keycode = key.keycode()
        mods = self._display.removeNumLockMask(keycode, self._currentModifier)
        item = self._subMapping[keycode, mods]
        if item:
            key.setShortcutItem(item)
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
                elif name == 'VoidSymbol':
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
                key.noSymbol()
            
    
    def mapping(self):
        return self.mainWindow.mapping()
    
    def slotModifierPressed(self, mod):
        if self._mode == d.SHORTCUT_MODE:
            self.toggleModifier(mod)
            self.loadLayout()
        
    def toggleModifier(self, mod):
        if self._currentModifier & mod:
            self._currentModifier ^= mod
        else:
            self._currentModifier |= mod
            
    def display(self):
        return self._display
    
    def slotEditKey(self, key):
        if key.isModifier():
            return
        if self._mode == d.SHORTCUT_MODE:
            dlg = dialogEditor.ShortcutDialog(self, key.shortcutItem())
            if dlg.exec_():
                item = ShortcutItem(key.keycode(), self._display.removeNumLockMask(key.keycode(), self._currentModifier), *dlg.getData())
                self._subMapping.addItem(item)
                self.loadShortKey(key)
                self._subMapping.save()
                self.keyModified.emit()
        else:
            dlg = dialogEditor.RemappingDialog(self, key.keycode(), key.remapItem())
            if dlg.exec_():
                item = RemapItem(key.keycode(), dlg.keysyms())
                self._subMapping.addItem(item)
                key.setRemapItem(item)
                self.loadRemapKey(key)
                self._subMapping.save()
                self.keyModified.emit()
                
                
    
    def slotKeyReleased(self, pos):
        key = self.keyAt(pos)
        if self.currentPressed and key and key.isEnabled() and \
                    (not key.isModifier() or self._mode == d.REMAPPING_MODE):
                
            sourceMItem = self._subMapping.popItem(self.currentPressed)
            cibleKey = key
            if self._mode == d.SHORTCUT_MODE:
                modMask = self._display.removeNumLockMask(cibleKey.keycode(), self._currentModifier)
                mapKey = (cibleKey.keycode(), modMask)
            else:
                mapKey = cibleKey.keycode()
            cibleMItem = self._subMapping.popItemFromKey(mapKey)
            newCibleMItem = sourceMItem
            newCibleMItem.keycode = cibleKey.keycode()
            if self._mode == d.SHORTCUT_MODE:
                newCibleMItem.modifiers = modMask

            self._subMapping.addItem(newCibleMItem)
            
            if cibleMItem:
                newSourceMItem = cibleMItem
                if self._mode == d.SHORTCUT_MODE:
                    newSourceMItem.keycode = sourceMItem.keycode
                    newSourceMItem.modifiers = sourceMItem.modifiers
                else:
                    newSourceMItem.keysyms = sourceMItem.keysyms
                self._subMapping.addItem(newSourceMItem)
                
            self.loadLayout()
            self._subMapping.save()
            self.keyModified.emit()
            
            
        self.currentPressed = None
        if self.currentHover:
            self.currentHover.restoreColor()
            self.currentHover = None
        self.setCursor(Qt.ArrowCursor)
    
    def slotKeyMove(self, pos):
        key = self.keyAt(pos)
        if not key or not key.isEnabled():
            return
        
        if self.currentPressed:
            if self.currentHover != key:
                if self.currentHover:
                    self.currentHover.restoreColor()
                if key and key.isUsed() and not key.isModifier():
                    key.select()
                    self.currentHover = key
        else:           
            pix = key.pixmap()
            if pix:
                self.setCursor(QCursor(pix))
            self.currentPressed = key.item()
            self.currentHover = key
    
    def slotContext(self, key, pos):
        menu = QMenu()
        editAction = QAction(icons.get('document-edit'), self.tr("Edit..."), self)
        deleteAction = QAction(icons.get('list-remove'), self.tr("Remove"), self)
        menu.addAction(editAction)
        if key.item():
            menu.addAction(deleteAction)

        act = menu.exec_(pos)
        if act == editAction:
            self.keyDoubleClicked.emit(key)
        elif act == deleteAction:
            if key.item():
                self._subMapping.popItem(key.item())
                key.clear()
                self._subMapping.save()
                self.loadLayout()
                self.keyModified.emit()
                
        
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
            
    def setMode(self, mode):
        self._mode = mode
        if mode == d.SHORTCUT_MODE:
            self._subMapping = self.mapping().shortcut
        else:
            self._subMapping = self.mapping().remap
    
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
        if keycode in self._display.modifiersKeycodeList():
            mod = self._display.getModMask(keycode)
            self.modifierPressed.emit(mod)
                
                
    def resizeEvent(self, event):
        self.updateSize()
