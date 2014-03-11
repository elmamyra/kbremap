import speedy_keyboard_app.keyTools as keyTools

pathDef = "/usr/include/X11/keysymdef.h"




with open(pathDef) as f:
    with open("keyGroups.py", 'w') as out:
        out.write("\ngroups = (\n")
        start = False
        tab = ' '*4
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
                    out.write('{}{},\n'.format(tab, keysymHex))
#                     out.write('{}("{}", {}, {}),\n'.format(tab, name, keysymHex, char))
                    
        out.write(")")
        
