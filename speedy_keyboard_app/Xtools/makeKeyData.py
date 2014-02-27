#from collections import namedtuple
#from keysymdef import *

#d = namedtuple('d', 'name char info')

pathDef = "/usr/include/X11/keysymdef.h"


#def writeKey(keysym, name, char='', info=''):
#    comment = ''
#    if char:
#        comment = ' # {}'.format(eval(char))
#    else:
#        char = "''"
#    if info:
#        info = "'{}'".format(info)
#    else:
#        info = "''"
#    out.write("{}{}: d('{}', {}, {}),{}\n".format(tab, keysym, name, char, info, comment))
#
#def writeKeysym(key, value):
#    out.write("{} = {}\n".format(key, value))

#with open(pathDef) as f:
#    with open("keysymdef.py", 'w') as outsym:
#        for line in f:
#            if line.startswith("#define "):
#                split = line.split()
#                writeKeysym(split[1], split[2])
#        writeKeysym('KP_DOT_OPERATOR', '0x10022c5')


addedChar = {
#    "XK_Tab": "\t",
#    "XK_Return": "\n",
#    "XK_KP_Space": " ",
    
#    "XK_KP_Tab": "\t",
#    "XK_KP_Enter": "\r",
#    "XK_KP_Equal": "=",
#    "XK_KP_Multiply": "*",
#    "XK_KP_Add": "+",
#    "XK_KP_Separator": ",",
#    "XK_KP_Subtract": "-",
#    "XK_KP_Decimal": ".",
#    "XK_KP_Divide": "/",
#    "XK_KP_0": "0",
#    "XK_KP_1": "1",
#    "XK_KP_2": "2",
#    "XK_KP_3": "3",
#    "XK_KP_4": "4",
#    "XK_KP_5": "5",
#    "XK_KP_6": "6",
#    "XK_KP_7": "7",
#    "XK_KP_8": "8",
#    "XK_KP_9": "9",
}

with open(pathDef) as f:
    with open("keysymdef.py", 'w') as out:
        for line in f:
            if line.startswith("#define "):
                split = line.split()
                out.write("{} = {}\n".format(split[1], split[2]))
    f.seek(0)
    with open("keysData.py", 'w') as out:
        out.write("# -*- coding: utf-8 -*-\n\n")
        out.write("from collections import namedtuple\n")
        out.write("from keysymdef import *\n\n")
        out.write("d = namedtuple('d', 'name char info')\n\n")
        out.write("\nkeyGroups = {\n")
        start = False
        tab = ' '*4
        for line in f:
            if line.startswith("#ifdef"):
                group = line.split()[1][3:].lower()
                out.write("{}'{}': {{\n".format(tab, group))
                tab = ' '*8
                start = True
            elif line.startswith("#endif"):
                out.write("    },\n\n")
                tab = ' '*4
            
            if start:
                split = line.split()
                
                if line.startswith("/*") and len(split) > 1:
                    out.write('{}#{}\n'.format(tab, '  '.join(split[1:-1])))
                elif line.startswith(" * "):
                    out.write('{}#{}\n'.format(tab, ' '.join(split[1:])))
                elif not split:
                    out.write("\n")
                elif line.startswith("#define "):
                    
                    comment = split[3:]
                    char = info = ''
                    if comment:
                        if comment[0].startswith("/*(U+"):
                            char = 'u"\\u{}"'.format(comment[0][5:])
                            info = ' '.join(comment[1:])[:-3].lower()
                        elif comment[1].startswith("U+"):
                            char = 'u"\\u{}"'.format(comment[1][2:])
                            info = ' '.join(comment[2:-1]).lower()
                        else:
                            info = ' '.join(comment[1:-1]).lower()
                        
                    if info in ('deprecated', 'old typo'):
                        continue
                    
                    
                    
                    keysym = split[1]
                    name = keysym[3:]
                    comment = ''
                    if not char:
                        if keysym in addedChar:
                            comment = ' # {}'.format(addedChar[keysym])
                            hexa = hex(ord(addedChar[keysym]))[2:].upper()
                            if len(hexa) == 1:
                                hexa = '0' + hexa
                            char = 'u"\\u00{}"'.format(hexa)
                        else:
                            char = "''"
                    else:
                        comment = ' # {}'.format(eval(char))
                    
                        
                        
                    if info:
                        info = "'{}'".format(info)
                    else:
                        info = "''"
                    out.write("{}{}: d('{}', {}, {}),{}\n".format(tab, keysym, name, char, info, comment))
                
                
                    
                        
                    
                    
        out.write("}")
        
