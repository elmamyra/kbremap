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

from kbremap_app import keyTools
pathDef = "/usr/include/X11/keysymdef.h"

with open(pathDef) as f:
    with open("keyGroups.py", 'w') as out:
        out.write("\ngroups = (\n")
        start = False
        tab = ' '*4
        li = []
        for line in f:
            if line.startswith("#ifdef"):
                group = line.split()[1][3:].lower()
                out.write("{}('{}' ,(\n".format(tab, group))
                tab = ' '*8
                start = True
            elif line.startswith("#endif"):
                tab = ' '*4
                out.write(tab + ")),\n\n")
            
            if start:
                split = line.split()
                if line.startswith("#define "):
                    
                    comment = split[3:]
                    char = ''
                    keysym = split[1]
                    keysymHex = split[2]
                    name = keysym[3:]
                    uni = keyTools.name2unicode(name)
                    if uni:
                        char = 'u"\\u{0:04x}"'.format(uni)
                    else:
                        char = '""'
                    
                    if not keysymHex in li:
                        out.write('{}{},\n'.format(tab, keysymHex))
                        li.append(keysymHex)
#                     out.write('{}("{}", {}, {}),\n'.format(tab, name, keysymHex, char))
                    
        out.write(")")
        
