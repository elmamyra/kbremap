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

from PySide.QtGui import *  # @UnusedWildImport
from PySide.QtCore import * # @UnusedWildImport
from widgets import Separator
from kbremap_app import mapping
from kbremap_app import util
import xml.etree.ElementTree as ET
import os

class BaseDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowTitle(self.tr("Export"))
        layout = QVBoxLayout(self)
        self.listWidget = QListWidget()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                     accepted=self.accept, rejected=self.reject)
        
        layout.addWidget(self.listWidget)
        layout.addWidget(Separator())
        layout.addWidget(buttonBox)
            
    def __iter__(self):
        for i in range(self.listWidget.count()):
            witem = self.listWidget.item(i)
            if witem.checkState() == Qt.Checked:
                yield witem.data(Qt.UserRole)

class ExportDialog(BaseDialog):
    def __init__(self, parent):
        BaseDialog.__init__(self, parent)
        
        for name, title in mapping.getAllNamesAndTitles():
            witem = QListWidgetItem(title)
            witem.setData(Qt.UserRole, name)
            witem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            self.listWidget.addItem(witem)
            witem.setCheckState(Qt.Checked)
        
class ImportDialog(BaseDialog):
    def __init__(self, parent, elements):
        BaseDialog.__init__(self, parent)
        
        for i, elt in enumerate(elements):
            title = elt.get('title')
            witem = QListWidgetItem(title)
            witem.setData(Qt.UserRole, i)
            witem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            self.listWidget.addItem(witem)
            witem.setCheckState(Qt.Checked)
            


def export(parent):
    dlg = ExportDialog(parent)
    if dlg.exec_():
        tree = mapping.loadTree()
        root = tree.getroot()
        exportElt = ET.Element('mappingList', attrib={'version': root.get('version')})
        for name in dlg:
            elt = root.find("mapping[@name='{}']".format(name))
            elt.attrib.pop('isCurrent', None)
            exportElt.append(elt)
        
        tr = parent.tr
        filetypes = "{0} (*.xml)".format(tr("XML Files"))
        path = os.path.join(os.environ['HOME'], 'mappings.xml')
        filename = QFileDialog.getSaveFileName(parent, tr("Export"), path, filetypes)[0]
        
        if filename:
            if os.path.splitext(filename)[1] != '.xml':
                filename += '.xml'
            util.indentXML(exportElt)
         
        tree = ET.ElementTree(exportElt)
        try:
            tree.write(filename, encoding="utf-8", xml_declaration=True)
        except (IOError, OSError) as e:
            QMessageBox.critical(parent, tr("Error"), tr(
                "Can't write to destination:\n\n{url}\n\n{error}").format(
                url=filename, error=e.strerror)) 
        
        
def import_(parent):
    tr = parent.tr  
    filetypes = "{0} (*.xml)".format(tr("XML Files"))
    path = os.path.join(os.environ['HOME'], 'mappings.xml')
    filename = QFileDialog.getOpenFileName(parent, tr("import"), path, filetypes)[0]
    if filename:
        try:
            d = ET.parse(filename)
            elements = list(d.findall('mapping'))
            if not elements:
                QMessageBox.information(parent, tr("No mapping"),
                tr("No keyboard mappings found."))
                return
        except Exception as e:
            QMessageBox.critical(parent, tr("Error"),
            tr("Can't read from source:\n\n{url}\n\n{error}").format(
                url=filename, error=e))
            return
        
        dlg = ImportDialog(parent, elements)
        if dlg.exec_():
            tree = mapping.loadTree()
            root = tree.getroot()
            for index in dlg:
                elt = elements[index]
                name = mapping.getUniqueName()
                title = mapping.getUniqueTile(elt.get('title'))
                elt.set('name', name)
                elt.set('title', title)
                root.append(elt)
                
            mapping.writeTree(tree)
                
                
        
    
    