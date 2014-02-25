# -*- coding: utf-8 -*-

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

"""



from Xlib.display import Display
from Xlib import XK, X
from Xlib.keysymdef.publishing import *
from Xlib.keysymdef.technical import *
from Xlib.keysymdef.greek import *
from Xlib.keysymdef.latin1 import *
from Xlib.keysymdef.latin2 import *
from Xlib.keysymdef.latin3 import *
from Xlib.keysymdef.latin4 import *
from Xlib.keysymdef.miscellany import *
from Xlib.keysymdef.xkb import *
import time

#char2keysym = {}
#print len(dir(XK))
#for keyName in dir(XK):
#    print keyName

XK.load_keysym_group('publishing')
XK.load_keysym_group('technical')
XK.load_keysym_group('greek')
XK.load_keysym_group('latin2')
XK.load_keysym_group('latin3')
XK.load_keysym_group('latin4')
XK.load_keysym_group('xkb')

display = Display()
#print XK.string_to_keysym(u'numbersign')

special_X_keysyms = {
    #latin1
#    ' ': 'space',
#    '\t': "Tab",
#    '\n': "Return",
#    '\r': "Return",
#    '\e': "Escape",

    
    
}
char = XK_ETH
print 'char:', display.lookup_string(char).decode('cp1252')

t = time.time()

print time.time() - t
print 'code', display.keysym_to_keycodes(char)



print XK_0, display.keycode_to_keysym(77, 1)
#XK.load_keysym_group('miscellany')
#for a in dir(XK):
#    if eval('XK.'+a) == 16786117:
#        print a


print map(hex, display.get_keyboard_mapping(63, 1)[0])
keypadCode = [63, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 108, 112]
def get(keycode, mod, numLock=False):
    mod = 1
#    if numLock and keycode in keypadCode:
#        if mod == 0:
#            mod = 1
#        elif mod == 1:
#            mod = 0
    
    index = {2:4, 3:5}.get(mod, mod)
    
    
    keysym = display.keycode_to_keysym(keycode, index)
    if not keysym:
        char = ''
    else:
        char = display.lookup_string(keysym)
        if char is None:
            char = ''
#        else:
#            print char, len(char)
#            if len(char) == 1:
#                char = unicode(unichr(ord(char)))
            
#        if char is None:
##            print keycode, keysym
#            char = special.get(keysym, '')
#        else:
#            char = unichr(ord(char))
#    print unichr(ord(char))
#    char = char.decode('utf-8')
    return char
    

special = {
    XK_BackSpace: u'BackSpace',
    XK_Tab: u'Tab',
    XK_ISO_Left_Tab: u'Tab',
    #keypad
    XK_KP_0: u'0',
    XK_KP_1: u'1',   
    XK_KP_2: u'2',   
    XK_KP_3: u'3',   
    XK_KP_4: u'4',   
    XK_KP_5: u'5', 
    XK_KP_6: u'6',   
    XK_KP_7: u'7',   
    XK_KP_8: u'8',   
    XK_KP_9: u'9',
    XK_KP_Divide: u'/',
    XK_KP_Multiply: u'*',
    XK_KP_Subtract: u'-',
    XK_KP_Add: u'+',
    XK_KP_Enter: u'Enter',
    XK_Num_Lock: u'Num\nLock',
    XK_KP_Home: u'Home',
    0x10022c5: u'*',
    0x1002215: u'∕',
    0xFEF9: u'Num\nLock',
    
    #publishing
    XK_emspace: u' ',
    XK_enspace: u' ',
    XK_em3space: u' ',
    XK_emdash: u'—',
    XK_endash: u'–',
    XK_ellipsis: u'…',
    XK_trademark: u'™',
    XK_leftsinglequotemark: u'‘',
    XK_rightsinglequotemark: u'’',
    XK_leftdoublequotemark: u'“',
    XK_rightdoublequotemark: u'”',
    XK_singlelowquotemark: u'‚',
    XK_minutes: u'′',
    XK_seconds: u'″',
    XK_doublelowquotemark: u'„',
    XK_dagger: u'†',
    XK_doubledagger: u'‡',
    XK_oneeighth: u'⅛',
    XK_threeeighths: u'⅜',
    XK_fiveeighths: u'⅝',
    XK_seveneighths: u'⅞',
    XK_leftanglebracket: u'〈',
    XK_rightanglebracket: u'〉',
    XK_enfilledcircbullet: u'•',
    XK_checkmark: u'✓',
    XK_onethird: u'⅓',
    XK_twothirds: u'⅔',
    XK_onefifth: u'⅕',
    XK_twofifths: u'⅖',
    XK_threefifths: u'⅗',
    XK_fourfifths: u'⅘',
    XK_onesixth: u'⅙',
    XK_fivesixths: u'⅚',
    XK_careof: u'℅',
    XK_figdash: u'‒',
    
    #technical
    XK_lessthanequal: u'≤',
    XK_notequal: u'≠',
    XK_greaterthanequal: u'≥',
    XK_leftarrow: u'←',
    XK_downarrow: u'↓',
    XK_rightarrow: u'→',
    XK_uparrow: u'↑',
    XK_approximate: u'≅',
    XK_horizconnector: u'─',
    
    #latin2
    XK_Aogonek: u'Ą',
    XK_breve: u'˘',
    XK_Lstroke: u'Ł',
    XK_Lcaron: u'Ľ',
    XK_Sacute: u'Ś',
    XK_Scaron: u'Š',
    XK_Scedilla: u'Ş',
    XK_Tcaron: u'Ť',
    XK_Zacute: u'Ź',
    XK_Zcaron: u'Ž',
    XK_Zabovedot: u'Ż',
    XK_aogonek: u'ą',
    XK_ogonek: u'˛',
    XK_lstroke: u'ł',
    XK_lcaron: u'ľ',
    XK_sacute: u'ś',
    XK_caron: u'ˇ',
    XK_scaron: u'š',
    XK_scedilla: u'ş',
    XK_tcaron: u'ť',
    XK_zacute: u'ź',
    XK_doubleacute: u'˝',
    XK_zcaron: u'ž',
    XK_zabovedot: u'ż',
    XK_Racute: u'Ŕ',
    XK_Abreve: u'Ă',
    XK_Lacute: u'Ĺ',
    XK_Cacute: u'Ć',
    XK_Ccaron: u'Č',
    XK_Eogonek: u'Ę',
    XK_Ecaron: u'Ě',
    XK_Dcaron: u'Ď',
    XK_Dstroke: u'Đ',
    XK_Nacute: u'Ń',
    XK_Ncaron: u'Ň',
    XK_Odoubleacute: u'Ő',
    XK_Rcaron: u'Ř',
    XK_Uring: u'Ů',
    XK_Udoubleacute: u'Ű',
    XK_Tcedilla: u'Ţ',
    XK_racute: u'ŕ',
    XK_abreve: u'ă',
    XK_lacute: u'ĺ',
    XK_cacute: u'ć',
    XK_ccaron: u'č',
    XK_eogonek: u'ę',
    XK_ecaron: u'ě',
    XK_dcaron: u'ď',
    XK_dstroke: u'đ',
    XK_nacute: u'ń',
    XK_ncaron: u'ň',
    XK_odoubleacute: u'ő',
    XK_udoubleacute: u'ű',
    XK_rcaron: u'ř',
    XK_uring: u'ů',
    XK_tcedilla: u'ţ',
    XK_abovedot: u'˙',
    
    #latin3
    XK_Hstroke: u'Ħ',
    XK_Hcircumflex: u'Ĥ',
    XK_Iabovedot: u'İ',
    XK_Gbreve: u'Ğ',
    XK_Jcircumflex: u'Ĵ',
    XK_hstroke: u'ħ',
    XK_hcircumflex: u'ĥ',
    XK_idotless: u'ı',
    XK_gbreve: u'ğ',
    XK_jcircumflex: u'ĵ',
    XK_Cabovedot: u'Ċ',
    XK_Ccircumflex: u'Ĉ',
    XK_Gabovedot: u'Ġ',
    XK_Gcircumflex: u'Ĝ',
    XK_Ubreve: u'Ŭ',
    XK_Scircumflex: u'Ŝ',
    XK_cabovedot: u'ċ',
    XK_ccircumflex: u'ĉ',
    XK_gabovedot: u'ġ',
    XK_gcircumflex: u'ĝ',
    XK_ubreve: u'ŭ',
    XK_scircumflex: u'ŝ',
    
    #latin4
    XK_kra: u'ĸ',
    XK_kappa: u'ĸ',
    XK_Rcedilla: u'Ŗ',
    XK_Itilde: u'Ĩ',
    XK_Lcedilla: u'Ļ',
    XK_Emacron: u'Ē',
    XK_Gcedilla: u'Ģ',
    XK_Tslash: u'Ŧ',
    XK_rcedilla: u'ŗ',
    XK_itilde: u'ĩ',
    XK_lcedilla: u'ļ',
    XK_emacron: u'ē',
    XK_gcedilla: u'ģ',
    XK_tslash: u'ŧ',
    XK_ENG: u'Ŋ',
    XK_eng: u'ŋ',
    XK_Amacron: u'Ā',
    XK_Iogonek: u'Į',
    XK_Eabovedot: u'Ė',
    XK_Imacron: u'Ī',
    XK_Ncedilla: u'Ņ',
    XK_Omacron: u'Ō',
    XK_Kcedilla: u'Ķ',
    XK_Uogonek: u'Ų',
    XK_Utilde: u'Ũ',
    XK_Umacron: u'Ū',
    XK_amacron: u'ā',
    XK_iogonek: u'į',
    XK_eabovedot: u'ė',
    XK_imacron: u'ī',
    XK_ncedilla: u'ņ',
    XK_omacron: u'ō',
    XK_kcedilla: u'ķ',
    XK_uogonek: u'ų',
    XK_utilde: u'ũ',
    XK_umacron: u'ū',
    
  
    #greek
    XK_Greek_OMEGA: u'Ω',
    XK_Greek_pi: u'π',
    XK_Greek_PI: u'Π',
    XK_Greek_mu: u'μ',
    
    
    #other
    0xb7: u'·',
    0x13bd: u'œ',
    0x13bc: u'Œ',
    0x20ac: u'€',
    0x1001E9E: u'ẞ',
    0x1002033: u'″',
    0x1002032: u'′',
    0x1002212: u'−',
    0x1002030: u'‰',
    0x1002039: u'‹',
    0x100203A: u'›',
    0x1000259: u'ə',
    0x100018f: u'Ə',
    0x1000133: u'ĳ',
    0x100017f: u'ſ',
    0x1000132: u'Ĳ',
    0x1001E70: u'Ṱ',
    0x1001E71: u'ṱ',
    0x1001E12: u'Ḓ',
    0x1001E13: u'ḓ',
    0x1001E3C: u'Ḽ',
    0x1001E3D: u'ḽ',
    0x1001E4A: u'Ṋ',
    0x1001E4B: u'ṋ',
    0x1001E44: u'Ṅ',
    0x1001E45: u'ṅ',
    0x1002026: u'…',
    0x1002166: u'Ⅶ',
    0x1000292: u'ʒ',
    0x10001b7: u'Ʒ',
    0x1000192: u'ƒ',
    0x100204a: u'⁊',
    0x10020a6: u'₦',
    0x1000300: u'̀',
    0x1000153: u'œ',
    0x1000152: u'Œ',
    0x100201c: u'“',
    0x100201d: u'”',
    0x100215b: u'⅛',
    0x100215c: u'⅜',
    0x100215d: u'⅝',
    0x100215e: u'⅞',
    0x1002122: u'™',
    0x1000131: u'ı',
    0x10020b1: u'₱',
    0x1000301: u'́',
    0x1000327: u'̧',
    0x1000303: u'̃',
    0x10020ac: u'€',
    0x1000302: u'̂',
    0x1002190: u'←',
    0x1002192: u'→',
    0x1002191: u'↑',
    0x1002193: u'↓',
    0x1000360: u'͠',
    0x1002213: u'∓',
    0x1000130: u'İ',
    0x100030b: u'̋',
    0x1002018: u'‘',
    0x1002019: u'’',
    0x1000328: u'̨',
    0x1000309: u'̉',
    0x1000323: u'̣',
    0x1002423: u'␣',
    0x1000219: u'ș',
    0x1000218: u'Ș',
    0x100021b: u'ț',
    0x100021a: u'Ț',
    0x10020ab: u'₫',
    0x10001b0: u'ư',
    0x10001af: u'Ư',
    0x10001a1: u'ơ',
    0x10001a0: u'Ơ',
}

for keysym, char in special.items():
    display.rebind_string(keysym, char)



#print 'str', unichr(ord(display.lookup_string(0x13bc)))
#print XK.string_to_keysym("odoubleacute"), XK_odoubleacute
#print XK.keysym_to_string(0x10001a0)
#
#print display.lookup_string(0x10001a1).decode('cp1252')
print "_"*30
with open('/usr/share/pyshared/Xlib/keysymdef/publishing.py') as f:
    for a in f:
        name1, sym = a[:-1].split('=')
        XKname = name1[:-1]
        name = XKname[3:]
#        print name
#        print name[3:]
#        if name in ('space',):
#            print 'NONE', XKname
#            continue
        charName = display.lookup_string(int(sym, 16))
        if not charName:
            print "NONE :" + name1
        
        elif len(charName) > 1:
            print "___ " + charName + " ___"
        else:                  
            char = unichr(ord(charName))
            print "u'{}': '{}',".format(char, name)

print 'code', display.keysym_to_keycodes(XK_figdash)
print ord(u' ')
