# -*- coding: utf-8 -*-

from collections import namedtuple
from keysymdef import *

d = namedtuple('d', 'name char info')


keyGroups = {
    'miscellany': {
        #TTY function keys, cleverly chosen to map to ASCII, for convenience of
        #programming, but could have been arbitrary (at the cost of lookup
        #tables in client code).

        XK_BackSpace: d('BackSpace', '', 'back space, back char'),
        XK_Tab: d('Tab', '', ''),
        XK_Linefeed: d('Linefeed', '', 'linefeed, lf'),
        XK_Clear: d('Clear', '', ''),
        XK_Return: d('Return', '', 'return, enter'),
        XK_Pause: d('Pause', '', 'pause, hold'),
        XK_Scroll_Lock: d('Scroll_Lock', '', ''),
        XK_Sys_Req: d('Sys_Req', '', ''),
        XK_Escape: d('Escape', '', ''),
        XK_Delete: d('Delete', '', 'delete, rubout'),



        #International  &  multi-key  character  composition

        XK_Multi_key: d('Multi_key', '', 'multi-key character compose'),
        XK_Codeinput: d('Codeinput', '', ''),
        XK_SingleCandidate: d('SingleCandidate', '', ''),
        XK_MultipleCandidate: d('MultipleCandidate', '', ''),
        XK_PreviousCandidate: d('PreviousCandidate', '', ''),

        #Japanese  keyboard  support

        XK_Kanji: d('Kanji', '', 'kanji, kanji convert'),
        XK_Muhenkan: d('Muhenkan', '', 'cancel conversion'),
        XK_Henkan_Mode: d('Henkan_Mode', '', 'start/stop conversion'),
        XK_Henkan: d('Henkan', '', 'alias for henkan_mode'),
        XK_Romaji: d('Romaji', '', 'to romaji'),
        XK_Hiragana: d('Hiragana', '', 'to hiragana'),
        XK_Katakana: d('Katakana', '', 'to katakana'),
        XK_Hiragana_Katakana: d('Hiragana_Katakana', '', 'hiragana/katakana toggle'),
        XK_Zenkaku: d('Zenkaku', '', 'to zenkaku'),
        XK_Hankaku: d('Hankaku', '', 'to hankaku'),
        XK_Zenkaku_Hankaku: d('Zenkaku_Hankaku', '', 'zenkaku/hankaku toggle'),
        XK_Touroku: d('Touroku', '', 'add to dictionary'),
        XK_Massyo: d('Massyo', '', 'delete from dictionary'),
        XK_Kana_Lock: d('Kana_Lock', '', 'kana lock'),
        XK_Kana_Shift: d('Kana_Shift', '', 'kana shift'),
        XK_Eisu_Shift: d('Eisu_Shift', '', 'alphanumeric shift'),
        XK_Eisu_toggle: d('Eisu_toggle', '', 'alphanumeric toggle'),
        XK_Kanji_Bangou: d('Kanji_Bangou', '', 'codeinput'),
        XK_Zen_Koho: d('Zen_Koho', '', 'multiple/all candidate(s)'),
        XK_Mae_Koho: d('Mae_Koho', '', 'previous candidate'),

        #0xff31  thru  0xff3f  are  under  XK_KOREAN

        #Cursor  control  &  motion

        XK_Home: d('Home', '', ''),
        XK_Left: d('Left', '', 'move left, left arrow'),
        XK_Up: d('Up', '', 'move up, up arrow'),
        XK_Right: d('Right', '', 'move right, right arrow'),
        XK_Down: d('Down', '', 'move down, down arrow'),
        XK_Prior: d('Prior', '', 'prior, previous'),
        XK_Page_Up: d('Page_Up', '', ''),
        XK_Next: d('Next', '', 'next'),
        XK_Page_Down: d('Page_Down', '', ''),
        XK_End: d('End', '', 'eol'),
        XK_Begin: d('Begin', '', 'bol'),


        #Misc  functions

        XK_Select: d('Select', '', 'select, mark'),
        XK_Print: d('Print', '', ''),
        XK_Execute: d('Execute', '', 'execute, run, do'),
        XK_Insert: d('Insert', '', 'insert, insert here'),
        XK_Undo: d('Undo', '', ''),
        XK_Redo: d('Redo', '', 'redo, again'),
        XK_Menu: d('Menu', '', ''),
        XK_Find: d('Find', '', 'find, search'),
        XK_Cancel: d('Cancel', '', 'cancel, stop, abort, exit'),
        XK_Help: d('Help', '', 'help'),
        XK_Break: d('Break', '', ''),
        XK_Mode_switch: d('Mode_switch', '', 'character set switch'),
        XK_script_switch: d('script_switch', '', 'alias for mode_switch'),
        XK_Num_Lock: d('Num_Lock', '', ''),

        #Keypad  functions,  keypad  numbers  cleverly  chosen  to  map  to  ASCII

        XK_KP_Space: d('KP_Space', '', 'space'),
        XK_KP_Tab: d('KP_Tab', '', ''),
        XK_KP_Enter: d('KP_Enter', '', 'enter'),
        XK_KP_F1: d('KP_F1', '', 'pf1, kp_a, ...'),
        XK_KP_F2: d('KP_F2', '', ''),
        XK_KP_F3: d('KP_F3', '', ''),
        XK_KP_F4: d('KP_F4', '', ''),
        XK_KP_Home: d('KP_Home', '', ''),
        XK_KP_Left: d('KP_Left', '', ''),
        XK_KP_Up: d('KP_Up', '', ''),
        XK_KP_Right: d('KP_Right', '', ''),
        XK_KP_Down: d('KP_Down', '', ''),
        XK_KP_Prior: d('KP_Prior', '', ''),
        XK_KP_Page_Up: d('KP_Page_Up', '', ''),
        XK_KP_Next: d('KP_Next', '', ''),
        XK_KP_Page_Down: d('KP_Page_Down', '', ''),
        XK_KP_End: d('KP_End', '', ''),
        XK_KP_Begin: d('KP_Begin', '', ''),
        XK_KP_Insert: d('KP_Insert', '', ''),
        XK_KP_Delete: d('KP_Delete', '', ''),
        XK_KP_Equal: d('KP_Equal', '', 'equals'),
        XK_KP_Multiply: d('KP_Multiply', '', ''),
        XK_KP_Add: d('KP_Add', '', ''),
        XK_KP_Separator: d('KP_Separator', '', 'separator, often comma'),
        XK_KP_Subtract: d('KP_Subtract', '', ''),
        XK_KP_Decimal: d('KP_Decimal', '', ''),
        XK_KP_Divide: d('KP_Divide', '', ''),

        XK_KP_0: d('KP_0', '', ''),
        XK_KP_1: d('KP_1', '', ''),
        XK_KP_2: d('KP_2', '', ''),
        XK_KP_3: d('KP_3', '', ''),
        XK_KP_4: d('KP_4', '', ''),
        XK_KP_5: d('KP_5', '', ''),
        XK_KP_6: d('KP_6', '', ''),
        XK_KP_7: d('KP_7', '', ''),
        XK_KP_8: d('KP_8', '', ''),
        XK_KP_9: d('KP_9', '', ''),



        #Auxiliary functions; note the duplicate definitions for left and right
        #function keys; Sun keyboards and a few other manufacturers have such
        #function key groups on the left and/or right sides of the keyboard.
        #We've not found a keyboard with more than 35 function keys total.

        XK_F1: d('F1', '', ''),
        XK_F2: d('F2', '', ''),
        XK_F3: d('F3', '', ''),
        XK_F4: d('F4', '', ''),
        XK_F5: d('F5', '', ''),
        XK_F6: d('F6', '', ''),
        XK_F7: d('F7', '', ''),
        XK_F8: d('F8', '', ''),
        XK_F9: d('F9', '', ''),
        XK_F10: d('F10', '', ''),
        XK_F11: d('F11', '', ''),
        XK_L1: d('L1', '', ''),
        XK_F12: d('F12', '', ''),
        XK_L2: d('L2', '', ''),
        XK_F13: d('F13', '', ''),
        XK_L3: d('L3', '', ''),
        XK_F14: d('F14', '', ''),
        XK_L4: d('L4', '', ''),
        XK_F15: d('F15', '', ''),
        XK_L5: d('L5', '', ''),
        XK_F16: d('F16', '', ''),
        XK_L6: d('L6', '', ''),
        XK_F17: d('F17', '', ''),
        XK_L7: d('L7', '', ''),
        XK_F18: d('F18', '', ''),
        XK_L8: d('L8', '', ''),
        XK_F19: d('F19', '', ''),
        XK_L9: d('L9', '', ''),
        XK_F20: d('F20', '', ''),
        XK_L10: d('L10', '', ''),
        XK_F21: d('F21', '', ''),
        XK_R1: d('R1', '', ''),
        XK_F22: d('F22', '', ''),
        XK_R2: d('R2', '', ''),
        XK_F23: d('F23', '', ''),
        XK_R3: d('R3', '', ''),
        XK_F24: d('F24', '', ''),
        XK_R4: d('R4', '', ''),
        XK_F25: d('F25', '', ''),
        XK_R5: d('R5', '', ''),
        XK_F26: d('F26', '', ''),
        XK_R6: d('R6', '', ''),
        XK_F27: d('F27', '', ''),
        XK_R7: d('R7', '', ''),
        XK_F28: d('F28', '', ''),
        XK_R8: d('R8', '', ''),
        XK_F29: d('F29', '', ''),
        XK_R9: d('R9', '', ''),
        XK_F30: d('F30', '', ''),
        XK_R10: d('R10', '', ''),
        XK_F31: d('F31', '', ''),
        XK_R11: d('R11', '', ''),
        XK_F32: d('F32', '', ''),
        XK_R12: d('R12', '', ''),
        XK_F33: d('F33', '', ''),
        XK_R13: d('R13', '', ''),
        XK_F34: d('F34', '', ''),
        XK_R14: d('R14', '', ''),
        XK_F35: d('F35', '', ''),
        XK_R15: d('R15', '', ''),

        #Modifiers

        XK_Shift_L: d('Shift_L', '', 'left shift'),
        XK_Shift_R: d('Shift_R', '', 'right shift'),
        XK_Control_L: d('Control_L', '', 'left control'),
        XK_Control_R: d('Control_R', '', 'right control'),
        XK_Caps_Lock: d('Caps_Lock', '', 'caps lock'),
        XK_Shift_Lock: d('Shift_Lock', '', 'shift lock'),

        XK_Meta_L: d('Meta_L', '', 'left meta'),
        XK_Meta_R: d('Meta_R', '', 'right meta'),
        XK_Alt_L: d('Alt_L', '', 'left alt'),
        XK_Alt_R: d('Alt_R', '', 'right alt'),
        XK_Super_L: d('Super_L', '', 'left super'),
        XK_Super_R: d('Super_R', '', 'right super'),
        XK_Hyper_L: d('Hyper_L', '', 'left hyper'),
        XK_Hyper_R: d('Hyper_R', '', 'right hyper'),
    },


    #Keyboard (XKB) Extension function and modifier keys
    #(from Appendix C of "The X Keyboard Extension: Protocol Specification")
    #Byte 3 = 0xfe

    'xkb_keys': {
        XK_ISO_Lock: d('ISO_Lock', '', ''),
        XK_ISO_Level2_Latch: d('ISO_Level2_Latch', '', ''),
        XK_ISO_Level3_Shift: d('ISO_Level3_Shift', '', ''),
        XK_ISO_Level3_Latch: d('ISO_Level3_Latch', '', ''),
        XK_ISO_Level3_Lock: d('ISO_Level3_Lock', '', ''),
        XK_ISO_Level5_Shift: d('ISO_Level5_Shift', '', ''),
        XK_ISO_Level5_Latch: d('ISO_Level5_Latch', '', ''),
        XK_ISO_Level5_Lock: d('ISO_Level5_Lock', '', ''),
        XK_ISO_Group_Shift: d('ISO_Group_Shift', '', 'alias for mode_switch'),
        XK_ISO_Group_Latch: d('ISO_Group_Latch', '', ''),
        XK_ISO_Group_Lock: d('ISO_Group_Lock', '', ''),
        XK_ISO_Next_Group: d('ISO_Next_Group', '', ''),
        XK_ISO_Next_Group_Lock: d('ISO_Next_Group_Lock', '', ''),
        XK_ISO_Prev_Group: d('ISO_Prev_Group', '', ''),
        XK_ISO_Prev_Group_Lock: d('ISO_Prev_Group_Lock', '', ''),
        XK_ISO_First_Group: d('ISO_First_Group', '', ''),
        XK_ISO_First_Group_Lock: d('ISO_First_Group_Lock', '', ''),
        XK_ISO_Last_Group: d('ISO_Last_Group', '', ''),
        XK_ISO_Last_Group_Lock: d('ISO_Last_Group_Lock', '', ''),

        XK_ISO_Left_Tab: d('ISO_Left_Tab', '', ''),
        XK_ISO_Move_Line_Up: d('ISO_Move_Line_Up', '', ''),
        XK_ISO_Move_Line_Down: d('ISO_Move_Line_Down', '', ''),
        XK_ISO_Partial_Line_Up: d('ISO_Partial_Line_Up', '', ''),
        XK_ISO_Partial_Line_Down: d('ISO_Partial_Line_Down', '', ''),
        XK_ISO_Partial_Space_Left: d('ISO_Partial_Space_Left', '', ''),
        XK_ISO_Partial_Space_Right: d('ISO_Partial_Space_Right', '', ''),
        XK_ISO_Set_Margin_Left: d('ISO_Set_Margin_Left', '', ''),
        XK_ISO_Set_Margin_Right: d('ISO_Set_Margin_Right', '', ''),
        XK_ISO_Release_Margin_Left: d('ISO_Release_Margin_Left', '', ''),
        XK_ISO_Release_Margin_Right: d('ISO_Release_Margin_Right', '', ''),
        XK_ISO_Release_Both_Margins: d('ISO_Release_Both_Margins', '', ''),
        XK_ISO_Fast_Cursor_Left: d('ISO_Fast_Cursor_Left', '', ''),
        XK_ISO_Fast_Cursor_Right: d('ISO_Fast_Cursor_Right', '', ''),
        XK_ISO_Fast_Cursor_Up: d('ISO_Fast_Cursor_Up', '', ''),
        XK_ISO_Fast_Cursor_Down: d('ISO_Fast_Cursor_Down', '', ''),
        XK_ISO_Continuous_Underline: d('ISO_Continuous_Underline', '', ''),
        XK_ISO_Discontinuous_Underline: d('ISO_Discontinuous_Underline', '', ''),
        XK_ISO_Emphasize: d('ISO_Emphasize', '', ''),
        XK_ISO_Center_Object: d('ISO_Center_Object', '', ''),
        XK_ISO_Enter: d('ISO_Enter', '', ''),

        XK_dead_grave: d('dead_grave', '', ''),
        XK_dead_acute: d('dead_acute', '', ''),
        XK_dead_circumflex: d('dead_circumflex', '', ''),
        XK_dead_tilde: d('dead_tilde', '', ''),
        XK_dead_perispomeni: d('dead_perispomeni', '', 'alias for dead_tilde'),
        XK_dead_macron: d('dead_macron', '', ''),
        XK_dead_breve: d('dead_breve', '', ''),
        XK_dead_abovedot: d('dead_abovedot', '', ''),
        XK_dead_diaeresis: d('dead_diaeresis', '', ''),
        XK_dead_abovering: d('dead_abovering', '', ''),
        XK_dead_doubleacute: d('dead_doubleacute', '', ''),
        XK_dead_caron: d('dead_caron', '', ''),
        XK_dead_cedilla: d('dead_cedilla', '', ''),
        XK_dead_ogonek: d('dead_ogonek', '', ''),
        XK_dead_iota: d('dead_iota', '', ''),
        XK_dead_voiced_sound: d('dead_voiced_sound', '', ''),
        XK_dead_semivoiced_sound: d('dead_semivoiced_sound', '', ''),
        XK_dead_belowdot: d('dead_belowdot', '', ''),
        XK_dead_hook: d('dead_hook', '', ''),
        XK_dead_horn: d('dead_horn', '', ''),
        XK_dead_stroke: d('dead_stroke', '', ''),
        XK_dead_abovecomma: d('dead_abovecomma', '', ''),
        XK_dead_psili: d('dead_psili', '', 'alias for dead_abovecomma'),
        XK_dead_abovereversedcomma: d('dead_abovereversedcomma', '', ''),
        XK_dead_dasia: d('dead_dasia', '', 'alias for dead_abovereversedcomma'),
        XK_dead_doublegrave: d('dead_doublegrave', '', ''),
        XK_dead_belowring: d('dead_belowring', '', ''),
        XK_dead_belowmacron: d('dead_belowmacron', '', ''),
        XK_dead_belowcircumflex: d('dead_belowcircumflex', '', ''),
        XK_dead_belowtilde: d('dead_belowtilde', '', ''),
        XK_dead_belowbreve: d('dead_belowbreve', '', ''),
        XK_dead_belowdiaeresis: d('dead_belowdiaeresis', '', ''),
        XK_dead_invertedbreve: d('dead_invertedbreve', '', ''),
        XK_dead_belowcomma: d('dead_belowcomma', '', ''),
        XK_dead_currency: d('dead_currency', '', ''),

        #dead  vowels  for  universal  syllable  entry
        XK_dead_a: d('dead_a', '', ''),
        XK_dead_A: d('dead_A', '', ''),
        XK_dead_e: d('dead_e', '', ''),
        XK_dead_E: d('dead_E', '', ''),
        XK_dead_i: d('dead_i', '', ''),
        XK_dead_I: d('dead_I', '', ''),
        XK_dead_o: d('dead_o', '', ''),
        XK_dead_O: d('dead_O', '', ''),
        XK_dead_u: d('dead_u', '', ''),
        XK_dead_U: d('dead_U', '', ''),
        XK_dead_small_schwa: d('dead_small_schwa', '', ''),
        XK_dead_capital_schwa: d('dead_capital_schwa', '', ''),

        XK_First_Virtual_Screen: d('First_Virtual_Screen', '', ''),
        XK_Prev_Virtual_Screen: d('Prev_Virtual_Screen', '', ''),
        XK_Next_Virtual_Screen: d('Next_Virtual_Screen', '', ''),
        XK_Last_Virtual_Screen: d('Last_Virtual_Screen', '', ''),
        XK_Terminate_Server: d('Terminate_Server', '', ''),

        XK_AccessX_Enable: d('AccessX_Enable', '', ''),
        XK_AccessX_Feedback_Enable: d('AccessX_Feedback_Enable', '', ''),
        XK_RepeatKeys_Enable: d('RepeatKeys_Enable', '', ''),
        XK_SlowKeys_Enable: d('SlowKeys_Enable', '', ''),
        XK_BounceKeys_Enable: d('BounceKeys_Enable', '', ''),
        XK_StickyKeys_Enable: d('StickyKeys_Enable', '', ''),
        XK_MouseKeys_Enable: d('MouseKeys_Enable', '', ''),
        XK_MouseKeys_Accel_Enable: d('MouseKeys_Accel_Enable', '', ''),
        XK_Overlay1_Enable: d('Overlay1_Enable', '', ''),
        XK_Overlay2_Enable: d('Overlay2_Enable', '', ''),
        XK_AudibleBell_Enable: d('AudibleBell_Enable', '', ''),

        XK_Pointer_Left: d('Pointer_Left', '', ''),
        XK_Pointer_Right: d('Pointer_Right', '', ''),
        XK_Pointer_Up: d('Pointer_Up', '', ''),
        XK_Pointer_Down: d('Pointer_Down', '', ''),
        XK_Pointer_UpLeft: d('Pointer_UpLeft', '', ''),
        XK_Pointer_UpRight: d('Pointer_UpRight', '', ''),
        XK_Pointer_DownLeft: d('Pointer_DownLeft', '', ''),
        XK_Pointer_DownRight: d('Pointer_DownRight', '', ''),
        XK_Pointer_Button_Dflt: d('Pointer_Button_Dflt', '', ''),
        XK_Pointer_Button1: d('Pointer_Button1', '', ''),
        XK_Pointer_Button2: d('Pointer_Button2', '', ''),
        XK_Pointer_Button3: d('Pointer_Button3', '', ''),
        XK_Pointer_Button4: d('Pointer_Button4', '', ''),
        XK_Pointer_Button5: d('Pointer_Button5', '', ''),
        XK_Pointer_DblClick_Dflt: d('Pointer_DblClick_Dflt', '', ''),
        XK_Pointer_DblClick1: d('Pointer_DblClick1', '', ''),
        XK_Pointer_DblClick2: d('Pointer_DblClick2', '', ''),
        XK_Pointer_DblClick3: d('Pointer_DblClick3', '', ''),
        XK_Pointer_DblClick4: d('Pointer_DblClick4', '', ''),
        XK_Pointer_DblClick5: d('Pointer_DblClick5', '', ''),
        XK_Pointer_Drag_Dflt: d('Pointer_Drag_Dflt', '', ''),
        XK_Pointer_Drag1: d('Pointer_Drag1', '', ''),
        XK_Pointer_Drag2: d('Pointer_Drag2', '', ''),
        XK_Pointer_Drag3: d('Pointer_Drag3', '', ''),
        XK_Pointer_Drag4: d('Pointer_Drag4', '', ''),
        XK_Pointer_Drag5: d('Pointer_Drag5', '', ''),

        XK_Pointer_EnableKeys: d('Pointer_EnableKeys', '', ''),
        XK_Pointer_Accelerate: d('Pointer_Accelerate', '', ''),
        XK_Pointer_DfltBtnNext: d('Pointer_DfltBtnNext', '', ''),
        XK_Pointer_DfltBtnPrev: d('Pointer_DfltBtnPrev', '', ''),

    },


    #3270 Terminal Keys
    #Byte 3 = 0xfd

    '3270': {
        XK_3270_Duplicate: d('3270_Duplicate', '', ''),
        XK_3270_FieldMark: d('3270_FieldMark', '', ''),
        XK_3270_Right2: d('3270_Right2', '', ''),
        XK_3270_Left2: d('3270_Left2', '', ''),
        XK_3270_BackTab: d('3270_BackTab', '', ''),
        XK_3270_EraseEOF: d('3270_EraseEOF', '', ''),
        XK_3270_EraseInput: d('3270_EraseInput', '', ''),
        XK_3270_Reset: d('3270_Reset', '', ''),
        XK_3270_Quit: d('3270_Quit', '', ''),
        XK_3270_PA1: d('3270_PA1', '', ''),
        XK_3270_PA2: d('3270_PA2', '', ''),
        XK_3270_PA3: d('3270_PA3', '', ''),
        XK_3270_Test: d('3270_Test', '', ''),
        XK_3270_Attn: d('3270_Attn', '', ''),
        XK_3270_CursorBlink: d('3270_CursorBlink', '', ''),
        XK_3270_AltCursor: d('3270_AltCursor', '', ''),
        XK_3270_KeyClick: d('3270_KeyClick', '', ''),
        XK_3270_Jump: d('3270_Jump', '', ''),
        XK_3270_Ident: d('3270_Ident', '', ''),
        XK_3270_Rule: d('3270_Rule', '', ''),
        XK_3270_Copy: d('3270_Copy', '', ''),
        XK_3270_Play: d('3270_Play', '', ''),
        XK_3270_Setup: d('3270_Setup', '', ''),
        XK_3270_Record: d('3270_Record', '', ''),
        XK_3270_ChangeScreen: d('3270_ChangeScreen', '', ''),
        XK_3270_DeleteWord: d('3270_DeleteWord', '', ''),
        XK_3270_ExSelect: d('3270_ExSelect', '', ''),
        XK_3270_CursorSelect: d('3270_CursorSelect', '', ''),
        XK_3270_PrintScreen: d('3270_PrintScreen', '', ''),
        XK_3270_Enter: d('3270_Enter', '', ''),
    },


    #Latin 1
    #(ISO/IEC 8859-1 = Unicode U+0020..U+00FF)
    #Byte 3 = 0
    'latin1': {
        XK_space: d('space', u"\u0020", 'space'), #  
        XK_exclam: d('exclam', u"\u0021", 'exclamation mark'), # !
        XK_quotedbl: d('quotedbl', u"\u0022", 'quotation mark'), # "
        XK_numbersign: d('numbersign', u"\u0023", 'number sign'), # #
        XK_dollar: d('dollar', u"\u0024", 'dollar sign'), # $
        XK_percent: d('percent', u"\u0025", 'percent sign'), # %
        XK_ampersand: d('ampersand', u"\u0026", 'ampersand'), # &
        XK_apostrophe: d('apostrophe', u"\u0027", 'apostrophe'), # '
        XK_parenleft: d('parenleft', u"\u0028", 'left parenthesis'), # (
        XK_parenright: d('parenright', u"\u0029", 'right parenthesis'), # )
        XK_asterisk: d('asterisk', u"\u002A", 'asterisk'), # *
        XK_plus: d('plus', u"\u002B", 'plus sign'), # +
        XK_comma: d('comma', u"\u002C", 'comma'), # ,
        XK_minus: d('minus', u"\u002D", 'hyphen-minus'), # -
        XK_period: d('period', u"\u002E", 'full stop'), # .
        XK_slash: d('slash', u"\u002F", 'solidus'), # /
        XK_0: d('0', u"\u0030", 'digit zero'), # 0
        XK_1: d('1', u"\u0031", 'digit one'), # 1
        XK_2: d('2', u"\u0032", 'digit two'), # 2
        XK_3: d('3', u"\u0033", 'digit three'), # 3
        XK_4: d('4', u"\u0034", 'digit four'), # 4
        XK_5: d('5', u"\u0035", 'digit five'), # 5
        XK_6: d('6', u"\u0036", 'digit six'), # 6
        XK_7: d('7', u"\u0037", 'digit seven'), # 7
        XK_8: d('8', u"\u0038", 'digit eight'), # 8
        XK_9: d('9', u"\u0039", 'digit nine'), # 9
        XK_colon: d('colon', u"\u003A", 'colon'), # :
        XK_semicolon: d('semicolon', u"\u003B", 'semicolon'), # ;
        XK_less: d('less', u"\u003C", 'less-than sign'), # <
        XK_equal: d('equal', u"\u003D", 'equals sign'), # =
        XK_greater: d('greater', u"\u003E", 'greater-than sign'), # >
        XK_question: d('question', u"\u003F", 'question mark'), # ?
        XK_at: d('at', u"\u0040", 'commercial at'), # @
        XK_A: d('A', u"\u0041", 'latin capital letter a'), # A
        XK_B: d('B', u"\u0042", 'latin capital letter b'), # B
        XK_C: d('C', u"\u0043", 'latin capital letter c'), # C
        XK_D: d('D', u"\u0044", 'latin capital letter d'), # D
        XK_E: d('E', u"\u0045", 'latin capital letter e'), # E
        XK_F: d('F', u"\u0046", 'latin capital letter f'), # F
        XK_G: d('G', u"\u0047", 'latin capital letter g'), # G
        XK_H: d('H', u"\u0048", 'latin capital letter h'), # H
        XK_I: d('I', u"\u0049", 'latin capital letter i'), # I
        XK_J: d('J', u"\u004A", 'latin capital letter j'), # J
        XK_K: d('K', u"\u004B", 'latin capital letter k'), # K
        XK_L: d('L', u"\u004C", 'latin capital letter l'), # L
        XK_M: d('M', u"\u004D", 'latin capital letter m'), # M
        XK_N: d('N', u"\u004E", 'latin capital letter n'), # N
        XK_O: d('O', u"\u004F", 'latin capital letter o'), # O
        XK_P: d('P', u"\u0050", 'latin capital letter p'), # P
        XK_Q: d('Q', u"\u0051", 'latin capital letter q'), # Q
        XK_R: d('R', u"\u0052", 'latin capital letter r'), # R
        XK_S: d('S', u"\u0053", 'latin capital letter s'), # S
        XK_T: d('T', u"\u0054", 'latin capital letter t'), # T
        XK_U: d('U', u"\u0055", 'latin capital letter u'), # U
        XK_V: d('V', u"\u0056", 'latin capital letter v'), # V
        XK_W: d('W', u"\u0057", 'latin capital letter w'), # W
        XK_X: d('X', u"\u0058", 'latin capital letter x'), # X
        XK_Y: d('Y', u"\u0059", 'latin capital letter y'), # Y
        XK_Z: d('Z', u"\u005A", 'latin capital letter z'), # Z
        XK_bracketleft: d('bracketleft', u"\u005B", 'left square bracket'), # [
        XK_backslash: d('backslash', u"\u005C", 'reverse solidus'), # \
        XK_bracketright: d('bracketright', u"\u005D", 'right square bracket'), # ]
        XK_asciicircum: d('asciicircum', u"\u005E", 'circumflex accent'), # ^
        XK_underscore: d('underscore', u"\u005F", 'low line'), # _
        XK_grave: d('grave', u"\u0060", 'grave accent'), # `
        XK_a: d('a', u"\u0061", 'latin small letter a'), # a
        XK_b: d('b', u"\u0062", 'latin small letter b'), # b
        XK_c: d('c', u"\u0063", 'latin small letter c'), # c
        XK_d: d('d', u"\u0064", 'latin small letter d'), # d
        XK_e: d('e', u"\u0065", 'latin small letter e'), # e
        XK_f: d('f', u"\u0066", 'latin small letter f'), # f
        XK_g: d('g', u"\u0067", 'latin small letter g'), # g
        XK_h: d('h', u"\u0068", 'latin small letter h'), # h
        XK_i: d('i', u"\u0069", 'latin small letter i'), # i
        XK_j: d('j', u"\u006A", 'latin small letter j'), # j
        XK_k: d('k', u"\u006B", 'latin small letter k'), # k
        XK_l: d('l', u"\u006C", 'latin small letter l'), # l
        XK_m: d('m', u"\u006D", 'latin small letter m'), # m
        XK_n: d('n', u"\u006E", 'latin small letter n'), # n
        XK_o: d('o', u"\u006F", 'latin small letter o'), # o
        XK_p: d('p', u"\u0070", 'latin small letter p'), # p
        XK_q: d('q', u"\u0071", 'latin small letter q'), # q
        XK_r: d('r', u"\u0072", 'latin small letter r'), # r
        XK_s: d('s', u"\u0073", 'latin small letter s'), # s
        XK_t: d('t', u"\u0074", 'latin small letter t'), # t
        XK_u: d('u', u"\u0075", 'latin small letter u'), # u
        XK_v: d('v', u"\u0076", 'latin small letter v'), # v
        XK_w: d('w', u"\u0077", 'latin small letter w'), # w
        XK_x: d('x', u"\u0078", 'latin small letter x'), # x
        XK_y: d('y', u"\u0079", 'latin small letter y'), # y
        XK_z: d('z', u"\u007A", 'latin small letter z'), # z
        XK_braceleft: d('braceleft', u"\u007B", 'left curly bracket'), # {
        XK_bar: d('bar', u"\u007C", 'vertical line'), # |
        XK_braceright: d('braceright', u"\u007D", 'right curly bracket'), # }
        XK_asciitilde: d('asciitilde', u"\u007E", 'tilde'), # ~

        XK_nobreakspace: d('nobreakspace', u"\u00A0", 'no-break space'), #  
        XK_exclamdown: d('exclamdown', u"\u00A1", 'inverted exclamation mark'), # ¡
        XK_cent: d('cent', u"\u00A2", 'cent sign'), # ¢
        XK_sterling: d('sterling', u"\u00A3", 'pound sign'), # £
        XK_currency: d('currency', u"\u00A4", 'currency sign'), # ¤
        XK_yen: d('yen', u"\u00A5", 'yen sign'), # ¥
        XK_brokenbar: d('brokenbar', u"\u00A6", 'broken bar'), # ¦
        XK_section: d('section', u"\u00A7", 'section sign'), # §
        XK_diaeresis: d('diaeresis', u"\u00A8", 'diaeresis'), # ¨
        XK_copyright: d('copyright', u"\u00A9", 'copyright sign'), # ©
        XK_ordfeminine: d('ordfeminine', u"\u00AA", 'feminine ordinal indicator'), # ª
        XK_guillemotleft: d('guillemotleft', u"\u00AB", 'left-pointing double angle quotation mark'), # «
        XK_notsign: d('notsign', u"\u00AC", 'not sign'), # ¬
        XK_hyphen: d('hyphen', u"\u00AD", 'soft hyphen'), # ­
        XK_registered: d('registered', u"\u00AE", 'registered sign'), # ®
        XK_macron: d('macron', u"\u00AF", 'macron'), # ¯
        XK_degree: d('degree', u"\u00B0", 'degree sign'), # °
        XK_plusminus: d('plusminus', u"\u00B1", 'plus-minus sign'), # ±
        XK_twosuperior: d('twosuperior', u"\u00B2", 'superscript two'), # ²
        XK_threesuperior: d('threesuperior', u"\u00B3", 'superscript three'), # ³
        XK_acute: d('acute', u"\u00B4", 'acute accent'), # ´
        XK_mu: d('mu', u"\u00B5", 'micro sign'), # µ
        XK_paragraph: d('paragraph', u"\u00B6", 'pilcrow sign'), # ¶
        XK_periodcentered: d('periodcentered', u"\u00B7", 'middle dot'), # ·
        XK_cedilla: d('cedilla', u"\u00B8", 'cedilla'), # ¸
        XK_onesuperior: d('onesuperior', u"\u00B9", 'superscript one'), # ¹
        XK_masculine: d('masculine', u"\u00BA", 'masculine ordinal indicator'), # º
        XK_guillemotright: d('guillemotright', u"\u00BB", 'right-pointing double angle quotation mark'), # »
        XK_onequarter: d('onequarter', u"\u00BC", 'vulgar fraction one quarter'), # ¼
        XK_onehalf: d('onehalf', u"\u00BD", 'vulgar fraction one half'), # ½
        XK_threequarters: d('threequarters', u"\u00BE", 'vulgar fraction three quarters'), # ¾
        XK_questiondown: d('questiondown', u"\u00BF", 'inverted question mark'), # ¿
        XK_Agrave: d('Agrave', u"\u00C0", 'latin capital letter a with grave'), # À
        XK_Aacute: d('Aacute', u"\u00C1", 'latin capital letter a with acute'), # Á
        XK_Acircumflex: d('Acircumflex', u"\u00C2", 'latin capital letter a with circumflex'), # Â
        XK_Atilde: d('Atilde', u"\u00C3", 'latin capital letter a with tilde'), # Ã
        XK_Adiaeresis: d('Adiaeresis', u"\u00C4", 'latin capital letter a with diaeresis'), # Ä
        XK_Aring: d('Aring', u"\u00C5", 'latin capital letter a with ring above'), # Å
        XK_AE: d('AE', u"\u00C6", 'latin capital letter ae'), # Æ
        XK_Ccedilla: d('Ccedilla', u"\u00C7", 'latin capital letter c with cedilla'), # Ç
        XK_Egrave: d('Egrave', u"\u00C8", 'latin capital letter e with grave'), # È
        XK_Eacute: d('Eacute', u"\u00C9", 'latin capital letter e with acute'), # É
        XK_Ecircumflex: d('Ecircumflex', u"\u00CA", 'latin capital letter e with circumflex'), # Ê
        XK_Ediaeresis: d('Ediaeresis', u"\u00CB", 'latin capital letter e with diaeresis'), # Ë
        XK_Igrave: d('Igrave', u"\u00CC", 'latin capital letter i with grave'), # Ì
        XK_Iacute: d('Iacute', u"\u00CD", 'latin capital letter i with acute'), # Í
        XK_Icircumflex: d('Icircumflex', u"\u00CE", 'latin capital letter i with circumflex'), # Î
        XK_Idiaeresis: d('Idiaeresis', u"\u00CF", 'latin capital letter i with diaeresis'), # Ï
        XK_ETH: d('ETH', u"\u00D0", 'latin capital letter eth'), # Ð
        XK_Ntilde: d('Ntilde', u"\u00D1", 'latin capital letter n with tilde'), # Ñ
        XK_Ograve: d('Ograve', u"\u00D2", 'latin capital letter o with grave'), # Ò
        XK_Oacute: d('Oacute', u"\u00D3", 'latin capital letter o with acute'), # Ó
        XK_Ocircumflex: d('Ocircumflex', u"\u00D4", 'latin capital letter o with circumflex'), # Ô
        XK_Otilde: d('Otilde', u"\u00D5", 'latin capital letter o with tilde'), # Õ
        XK_Odiaeresis: d('Odiaeresis', u"\u00D6", 'latin capital letter o with diaeresis'), # Ö
        XK_multiply: d('multiply', u"\u00D7", 'multiplication sign'), # ×
        XK_Oslash: d('Oslash', u"\u00D8", 'latin capital letter o with stroke'), # Ø
        XK_Ooblique: d('Ooblique', u"\u00D8", 'latin capital letter o with stroke'), # Ø
        XK_Ugrave: d('Ugrave', u"\u00D9", 'latin capital letter u with grave'), # Ù
        XK_Uacute: d('Uacute', u"\u00DA", 'latin capital letter u with acute'), # Ú
        XK_Ucircumflex: d('Ucircumflex', u"\u00DB", 'latin capital letter u with circumflex'), # Û
        XK_Udiaeresis: d('Udiaeresis', u"\u00DC", 'latin capital letter u with diaeresis'), # Ü
        XK_Yacute: d('Yacute', u"\u00DD", 'latin capital letter y with acute'), # Ý
        XK_THORN: d('THORN', u"\u00DE", 'latin capital letter thorn'), # Þ
        XK_ssharp: d('ssharp', u"\u00DF", 'latin small letter sharp s'), # ß
        XK_agrave: d('agrave', u"\u00E0", 'latin small letter a with grave'), # à
        XK_aacute: d('aacute', u"\u00E1", 'latin small letter a with acute'), # á
        XK_acircumflex: d('acircumflex', u"\u00E2", 'latin small letter a with circumflex'), # â
        XK_atilde: d('atilde', u"\u00E3", 'latin small letter a with tilde'), # ã
        XK_adiaeresis: d('adiaeresis', u"\u00E4", 'latin small letter a with diaeresis'), # ä
        XK_aring: d('aring', u"\u00E5", 'latin small letter a with ring above'), # å
        XK_ae: d('ae', u"\u00E6", 'latin small letter ae'), # æ
        XK_ccedilla: d('ccedilla', u"\u00E7", 'latin small letter c with cedilla'), # ç
        XK_egrave: d('egrave', u"\u00E8", 'latin small letter e with grave'), # è
        XK_eacute: d('eacute', u"\u00E9", 'latin small letter e with acute'), # é
        XK_ecircumflex: d('ecircumflex', u"\u00EA", 'latin small letter e with circumflex'), # ê
        XK_ediaeresis: d('ediaeresis', u"\u00EB", 'latin small letter e with diaeresis'), # ë
        XK_igrave: d('igrave', u"\u00EC", 'latin small letter i with grave'), # ì
        XK_iacute: d('iacute', u"\u00ED", 'latin small letter i with acute'), # í
        XK_icircumflex: d('icircumflex', u"\u00EE", 'latin small letter i with circumflex'), # î
        XK_idiaeresis: d('idiaeresis', u"\u00EF", 'latin small letter i with diaeresis'), # ï
        XK_eth: d('eth', u"\u00F0", 'latin small letter eth'), # ð
        XK_ntilde: d('ntilde', u"\u00F1", 'latin small letter n with tilde'), # ñ
        XK_ograve: d('ograve', u"\u00F2", 'latin small letter o with grave'), # ò
        XK_oacute: d('oacute', u"\u00F3", 'latin small letter o with acute'), # ó
        XK_ocircumflex: d('ocircumflex', u"\u00F4", 'latin small letter o with circumflex'), # ô
        XK_otilde: d('otilde', u"\u00F5", 'latin small letter o with tilde'), # õ
        XK_odiaeresis: d('odiaeresis', u"\u00F6", 'latin small letter o with diaeresis'), # ö
        XK_division: d('division', u"\u00F7", 'division sign'), # ÷
        XK_oslash: d('oslash', u"\u00F8", 'latin small letter o with stroke'), # ø
        XK_ooblique: d('ooblique', u"\u00F8", 'latin small letter o with stroke'), # ø
        XK_ugrave: d('ugrave', u"\u00F9", 'latin small letter u with grave'), # ù
        XK_uacute: d('uacute', u"\u00FA", 'latin small letter u with acute'), # ú
        XK_ucircumflex: d('ucircumflex', u"\u00FB", 'latin small letter u with circumflex'), # û
        XK_udiaeresis: d('udiaeresis', u"\u00FC", 'latin small letter u with diaeresis'), # ü
        XK_yacute: d('yacute', u"\u00FD", 'latin small letter y with acute'), # ý
        XK_thorn: d('thorn', u"\u00FE", 'latin small letter thorn'), # þ
        XK_ydiaeresis: d('ydiaeresis', u"\u00FF", 'latin small letter y with diaeresis'), # ÿ
    },


    #Latin 2
    #Byte 3 = 1

    'latin2': {
        XK_Aogonek: d('Aogonek', u"\u0104", 'latin capital letter a with ogonek'), # Ą
        XK_breve: d('breve', u"\u02D8", 'breve'), # ˘
        XK_Lstroke: d('Lstroke', u"\u0141", 'latin capital letter l with stroke'), # Ł
        XK_Lcaron: d('Lcaron', u"\u013D", 'latin capital letter l with caron'), # Ľ
        XK_Sacute: d('Sacute', u"\u015A", 'latin capital letter s with acute'), # Ś
        XK_Scaron: d('Scaron', u"\u0160", 'latin capital letter s with caron'), # Š
        XK_Scedilla: d('Scedilla', u"\u015E", 'latin capital letter s with cedilla'), # Ş
        XK_Tcaron: d('Tcaron', u"\u0164", 'latin capital letter t with caron'), # Ť
        XK_Zacute: d('Zacute', u"\u0179", 'latin capital letter z with acute'), # Ź
        XK_Zcaron: d('Zcaron', u"\u017D", 'latin capital letter z with caron'), # Ž
        XK_Zabovedot: d('Zabovedot', u"\u017B", 'latin capital letter z with dot above'), # Ż
        XK_aogonek: d('aogonek', u"\u0105", 'latin small letter a with ogonek'), # ą
        XK_ogonek: d('ogonek', u"\u02DB", 'ogonek'), # ˛
        XK_lstroke: d('lstroke', u"\u0142", 'latin small letter l with stroke'), # ł
        XK_lcaron: d('lcaron', u"\u013E", 'latin small letter l with caron'), # ľ
        XK_sacute: d('sacute', u"\u015B", 'latin small letter s with acute'), # ś
        XK_caron: d('caron', u"\u02C7", 'caron'), # ˇ
        XK_scaron: d('scaron', u"\u0161", 'latin small letter s with caron'), # š
        XK_scedilla: d('scedilla', u"\u015F", 'latin small letter s with cedilla'), # ş
        XK_tcaron: d('tcaron', u"\u0165", 'latin small letter t with caron'), # ť
        XK_zacute: d('zacute', u"\u017A", 'latin small letter z with acute'), # ź
        XK_doubleacute: d('doubleacute', u"\u02DD", 'double acute accent'), # ˝
        XK_zcaron: d('zcaron', u"\u017E", 'latin small letter z with caron'), # ž
        XK_zabovedot: d('zabovedot', u"\u017C", 'latin small letter z with dot above'), # ż
        XK_Racute: d('Racute', u"\u0154", 'latin capital letter r with acute'), # Ŕ
        XK_Abreve: d('Abreve', u"\u0102", 'latin capital letter a with breve'), # Ă
        XK_Lacute: d('Lacute', u"\u0139", 'latin capital letter l with acute'), # Ĺ
        XK_Cacute: d('Cacute', u"\u0106", 'latin capital letter c with acute'), # Ć
        XK_Ccaron: d('Ccaron', u"\u010C", 'latin capital letter c with caron'), # Č
        XK_Eogonek: d('Eogonek', u"\u0118", 'latin capital letter e with ogonek'), # Ę
        XK_Ecaron: d('Ecaron', u"\u011A", 'latin capital letter e with caron'), # Ě
        XK_Dcaron: d('Dcaron', u"\u010E", 'latin capital letter d with caron'), # Ď
        XK_Dstroke: d('Dstroke', u"\u0110", 'latin capital letter d with stroke'), # Đ
        XK_Nacute: d('Nacute', u"\u0143", 'latin capital letter n with acute'), # Ń
        XK_Ncaron: d('Ncaron', u"\u0147", 'latin capital letter n with caron'), # Ň
        XK_Odoubleacute: d('Odoubleacute', u"\u0150", 'latin capital letter o with double acute'), # Ő
        XK_Rcaron: d('Rcaron', u"\u0158", 'latin capital letter r with caron'), # Ř
        XK_Uring: d('Uring', u"\u016E", 'latin capital letter u with ring above'), # Ů
        XK_Udoubleacute: d('Udoubleacute', u"\u0170", 'latin capital letter u with double acute'), # Ű
        XK_Tcedilla: d('Tcedilla', u"\u0162", 'latin capital letter t with cedilla'), # Ţ
        XK_racute: d('racute', u"\u0155", 'latin small letter r with acute'), # ŕ
        XK_abreve: d('abreve', u"\u0103", 'latin small letter a with breve'), # ă
        XK_lacute: d('lacute', u"\u013A", 'latin small letter l with acute'), # ĺ
        XK_cacute: d('cacute', u"\u0107", 'latin small letter c with acute'), # ć
        XK_ccaron: d('ccaron', u"\u010D", 'latin small letter c with caron'), # č
        XK_eogonek: d('eogonek', u"\u0119", 'latin small letter e with ogonek'), # ę
        XK_ecaron: d('ecaron', u"\u011B", 'latin small letter e with caron'), # ě
        XK_dcaron: d('dcaron', u"\u010F", 'latin small letter d with caron'), # ď
        XK_dstroke: d('dstroke', u"\u0111", 'latin small letter d with stroke'), # đ
        XK_nacute: d('nacute', u"\u0144", 'latin small letter n with acute'), # ń
        XK_ncaron: d('ncaron', u"\u0148", 'latin small letter n with caron'), # ň
        XK_odoubleacute: d('odoubleacute', u"\u0151", 'latin small letter o with double acute'), # ő
        XK_rcaron: d('rcaron', u"\u0159", 'latin small letter r with caron'), # ř
        XK_uring: d('uring', u"\u016F", 'latin small letter u with ring above'), # ů
        XK_udoubleacute: d('udoubleacute', u"\u0171", 'latin small letter u with double acute'), # ű
        XK_tcedilla: d('tcedilla', u"\u0163", 'latin small letter t with cedilla'), # ţ
        XK_abovedot: d('abovedot', u"\u02D9", 'dot above'), # ˙
    },


    #Latin 3
    #Byte 3 = 2

    'latin3': {
        XK_Hstroke: d('Hstroke', u"\u0126", 'latin capital letter h with stroke'), # Ħ
        XK_Hcircumflex: d('Hcircumflex', u"\u0124", 'latin capital letter h with circumflex'), # Ĥ
        XK_Iabovedot: d('Iabovedot', u"\u0130", 'latin capital letter i with dot above'), # İ
        XK_Gbreve: d('Gbreve', u"\u011E", 'latin capital letter g with breve'), # Ğ
        XK_Jcircumflex: d('Jcircumflex', u"\u0134", 'latin capital letter j with circumflex'), # Ĵ
        XK_hstroke: d('hstroke', u"\u0127", 'latin small letter h with stroke'), # ħ
        XK_hcircumflex: d('hcircumflex', u"\u0125", 'latin small letter h with circumflex'), # ĥ
        XK_idotless: d('idotless', u"\u0131", 'latin small letter dotless i'), # ı
        XK_gbreve: d('gbreve', u"\u011F", 'latin small letter g with breve'), # ğ
        XK_jcircumflex: d('jcircumflex', u"\u0135", 'latin small letter j with circumflex'), # ĵ
        XK_Cabovedot: d('Cabovedot', u"\u010A", 'latin capital letter c with dot above'), # Ċ
        XK_Ccircumflex: d('Ccircumflex', u"\u0108", 'latin capital letter c with circumflex'), # Ĉ
        XK_Gabovedot: d('Gabovedot', u"\u0120", 'latin capital letter g with dot above'), # Ġ
        XK_Gcircumflex: d('Gcircumflex', u"\u011C", 'latin capital letter g with circumflex'), # Ĝ
        XK_Ubreve: d('Ubreve', u"\u016C", 'latin capital letter u with breve'), # Ŭ
        XK_Scircumflex: d('Scircumflex', u"\u015C", 'latin capital letter s with circumflex'), # Ŝ
        XK_cabovedot: d('cabovedot', u"\u010B", 'latin small letter c with dot above'), # ċ
        XK_ccircumflex: d('ccircumflex', u"\u0109", 'latin small letter c with circumflex'), # ĉ
        XK_gabovedot: d('gabovedot', u"\u0121", 'latin small letter g with dot above'), # ġ
        XK_gcircumflex: d('gcircumflex', u"\u011D", 'latin small letter g with circumflex'), # ĝ
        XK_ubreve: d('ubreve', u"\u016D", 'latin small letter u with breve'), # ŭ
        XK_scircumflex: d('scircumflex', u"\u015D", 'latin small letter s with circumflex'), # ŝ
    },



    #Latin 4
    #Byte 3 = 3

    'latin4': {
        XK_kra: d('kra', u"\u0138", 'latin small letter kra'), # ĸ
        XK_Rcedilla: d('Rcedilla', u"\u0156", 'latin capital letter r with cedilla'), # Ŗ
        XK_Itilde: d('Itilde', u"\u0128", 'latin capital letter i with tilde'), # Ĩ
        XK_Lcedilla: d('Lcedilla', u"\u013B", 'latin capital letter l with cedilla'), # Ļ
        XK_Emacron: d('Emacron', u"\u0112", 'latin capital letter e with macron'), # Ē
        XK_Gcedilla: d('Gcedilla', u"\u0122", 'latin capital letter g with cedilla'), # Ģ
        XK_Tslash: d('Tslash', u"\u0166", 'latin capital letter t with stroke'), # Ŧ
        XK_rcedilla: d('rcedilla', u"\u0157", 'latin small letter r with cedilla'), # ŗ
        XK_itilde: d('itilde', u"\u0129", 'latin small letter i with tilde'), # ĩ
        XK_lcedilla: d('lcedilla', u"\u013C", 'latin small letter l with cedilla'), # ļ
        XK_emacron: d('emacron', u"\u0113", 'latin small letter e with macron'), # ē
        XK_gcedilla: d('gcedilla', u"\u0123", 'latin small letter g with cedilla'), # ģ
        XK_tslash: d('tslash', u"\u0167", 'latin small letter t with stroke'), # ŧ
        XK_ENG: d('ENG', u"\u014A", 'latin capital letter eng'), # Ŋ
        XK_eng: d('eng', u"\u014B", 'latin small letter eng'), # ŋ
        XK_Amacron: d('Amacron', u"\u0100", 'latin capital letter a with macron'), # Ā
        XK_Iogonek: d('Iogonek', u"\u012E", 'latin capital letter i with ogonek'), # Į
        XK_Eabovedot: d('Eabovedot', u"\u0116", 'latin capital letter e with dot above'), # Ė
        XK_Imacron: d('Imacron', u"\u012A", 'latin capital letter i with macron'), # Ī
        XK_Ncedilla: d('Ncedilla', u"\u0145", 'latin capital letter n with cedilla'), # Ņ
        XK_Omacron: d('Omacron', u"\u014C", 'latin capital letter o with macron'), # Ō
        XK_Kcedilla: d('Kcedilla', u"\u0136", 'latin capital letter k with cedilla'), # Ķ
        XK_Uogonek: d('Uogonek', u"\u0172", 'latin capital letter u with ogonek'), # Ų
        XK_Utilde: d('Utilde', u"\u0168", 'latin capital letter u with tilde'), # Ũ
        XK_Umacron: d('Umacron', u"\u016A", 'latin capital letter u with macron'), # Ū
        XK_amacron: d('amacron', u"\u0101", 'latin small letter a with macron'), # ā
        XK_iogonek: d('iogonek', u"\u012F", 'latin small letter i with ogonek'), # į
        XK_eabovedot: d('eabovedot', u"\u0117", 'latin small letter e with dot above'), # ė
        XK_imacron: d('imacron', u"\u012B", 'latin small letter i with macron'), # ī
        XK_ncedilla: d('ncedilla', u"\u0146", 'latin small letter n with cedilla'), # ņ
        XK_omacron: d('omacron', u"\u014D", 'latin small letter o with macron'), # ō
        XK_kcedilla: d('kcedilla', u"\u0137", 'latin small letter k with cedilla'), # ķ
        XK_uogonek: d('uogonek', u"\u0173", 'latin small letter u with ogonek'), # ų
        XK_utilde: d('utilde', u"\u0169", 'latin small letter u with tilde'), # ũ
        XK_umacron: d('umacron', u"\u016B", 'latin small letter u with macron'), # ū
    },


    #Latin 8
    'latin8': {
        XK_Wcircumflex: d('Wcircumflex', u"\u0174", 'latin capital letter w with circumflex'), # Ŵ
        XK_wcircumflex: d('wcircumflex', u"\u0175", 'latin small letter w with circumflex'), # ŵ
        XK_Ycircumflex: d('Ycircumflex', u"\u0176", 'latin capital letter y with circumflex'), # Ŷ
        XK_ycircumflex: d('ycircumflex', u"\u0177", 'latin small letter y with circumflex'), # ŷ
        XK_Babovedot: d('Babovedot', u"\u1E02", 'latin capital letter b with dot above'), # Ḃ
        XK_babovedot: d('babovedot', u"\u1E03", 'latin small letter b with dot above'), # ḃ
        XK_Dabovedot: d('Dabovedot', u"\u1E0A", 'latin capital letter d with dot above'), # Ḋ
        XK_dabovedot: d('dabovedot', u"\u1E0B", 'latin small letter d with dot above'), # ḋ
        XK_Fabovedot: d('Fabovedot', u"\u1E1E", 'latin capital letter f with dot above'), # Ḟ
        XK_fabovedot: d('fabovedot', u"\u1E1F", 'latin small letter f with dot above'), # ḟ
        XK_Mabovedot: d('Mabovedot', u"\u1E40", 'latin capital letter m with dot above'), # Ṁ
        XK_mabovedot: d('mabovedot', u"\u1E41", 'latin small letter m with dot above'), # ṁ
        XK_Pabovedot: d('Pabovedot', u"\u1E56", 'latin capital letter p with dot above'), # Ṗ
        XK_pabovedot: d('pabovedot', u"\u1E57", 'latin small letter p with dot above'), # ṗ
        XK_Sabovedot: d('Sabovedot', u"\u1E60", 'latin capital letter s with dot above'), # Ṡ
        XK_sabovedot: d('sabovedot', u"\u1E61", 'latin small letter s with dot above'), # ṡ
        XK_Tabovedot: d('Tabovedot', u"\u1E6A", 'latin capital letter t with dot above'), # Ṫ
        XK_tabovedot: d('tabovedot', u"\u1E6B", 'latin small letter t with dot above'), # ṫ
        XK_Wgrave: d('Wgrave', u"\u1E80", 'latin capital letter w with grave'), # Ẁ
        XK_wgrave: d('wgrave', u"\u1E81", 'latin small letter w with grave'), # ẁ
        XK_Wacute: d('Wacute', u"\u1E82", 'latin capital letter w with acute'), # Ẃ
        XK_wacute: d('wacute', u"\u1E83", 'latin small letter w with acute'), # ẃ
        XK_Wdiaeresis: d('Wdiaeresis', u"\u1E84", 'latin capital letter w with diaeresis'), # Ẅ
        XK_wdiaeresis: d('wdiaeresis', u"\u1E85", 'latin small letter w with diaeresis'), # ẅ
        XK_Ygrave: d('Ygrave', u"\u1EF2", 'latin capital letter y with grave'), # Ỳ
        XK_ygrave: d('ygrave', u"\u1EF3", 'latin small letter y with grave'), # ỳ
    },


    #Latin 9
    #Byte 3 = 0x13

    'latin9': {
        XK_OE: d('OE', u"\u0152", 'latin capital ligature oe'), # Œ
        XK_oe: d('oe', u"\u0153", 'latin small ligature oe'), # œ
        XK_Ydiaeresis: d('Ydiaeresis', u"\u0178", 'latin capital letter y with diaeresis'), # Ÿ
    },


    #Katakana
    #Byte 3 = 4

    'katakana': {
        XK_overline: d('overline', u"\u203E", 'overline'), # ‾
        XK_kana_fullstop: d('kana_fullstop', u"\u3002", 'ideographic full stop'), # 。
        XK_kana_openingbracket: d('kana_openingbracket', u"\u300C", 'left corner bracket'), # 「
        XK_kana_closingbracket: d('kana_closingbracket', u"\u300D", 'right corner bracket'), # 」
        XK_kana_comma: d('kana_comma', u"\u3001", 'ideographic comma'), # 、
        XK_kana_conjunctive: d('kana_conjunctive', u"\u30FB", 'katakana middle dot'), # ・
        XK_kana_WO: d('kana_WO', u"\u30F2", 'katakana letter wo'), # ヲ
        XK_kana_a: d('kana_a', u"\u30A1", 'katakana letter small a'), # ァ
        XK_kana_i: d('kana_i', u"\u30A3", 'katakana letter small i'), # ィ
        XK_kana_u: d('kana_u', u"\u30A5", 'katakana letter small u'), # ゥ
        XK_kana_e: d('kana_e', u"\u30A7", 'katakana letter small e'), # ェ
        XK_kana_o: d('kana_o', u"\u30A9", 'katakana letter small o'), # ォ
        XK_kana_ya: d('kana_ya', u"\u30E3", 'katakana letter small ya'), # ャ
        XK_kana_yu: d('kana_yu', u"\u30E5", 'katakana letter small yu'), # ュ
        XK_kana_yo: d('kana_yo', u"\u30E7", 'katakana letter small yo'), # ョ
        XK_kana_tsu: d('kana_tsu', u"\u30C3", 'katakana letter small tu'), # ッ
        XK_prolongedsound: d('prolongedsound', u"\u30FC", 'katakana-hiragana prolonged sound mark'), # ー
        XK_kana_A: d('kana_A', u"\u30A2", 'katakana letter a'), # ア
        XK_kana_I: d('kana_I', u"\u30A4", 'katakana letter i'), # イ
        XK_kana_U: d('kana_U', u"\u30A6", 'katakana letter u'), # ウ
        XK_kana_E: d('kana_E', u"\u30A8", 'katakana letter e'), # エ
        XK_kana_O: d('kana_O', u"\u30AA", 'katakana letter o'), # オ
        XK_kana_KA: d('kana_KA', u"\u30AB", 'katakana letter ka'), # カ
        XK_kana_KI: d('kana_KI', u"\u30AD", 'katakana letter ki'), # キ
        XK_kana_KU: d('kana_KU', u"\u30AF", 'katakana letter ku'), # ク
        XK_kana_KE: d('kana_KE', u"\u30B1", 'katakana letter ke'), # ケ
        XK_kana_KO: d('kana_KO', u"\u30B3", 'katakana letter ko'), # コ
        XK_kana_SA: d('kana_SA', u"\u30B5", 'katakana letter sa'), # サ
        XK_kana_SHI: d('kana_SHI', u"\u30B7", 'katakana letter si'), # シ
        XK_kana_SU: d('kana_SU', u"\u30B9", 'katakana letter su'), # ス
        XK_kana_SE: d('kana_SE', u"\u30BB", 'katakana letter se'), # セ
        XK_kana_SO: d('kana_SO', u"\u30BD", 'katakana letter so'), # ソ
        XK_kana_TA: d('kana_TA', u"\u30BF", 'katakana letter ta'), # タ
        XK_kana_CHI: d('kana_CHI', u"\u30C1", 'katakana letter ti'), # チ
        XK_kana_TSU: d('kana_TSU', u"\u30C4", 'katakana letter tu'), # ツ
        XK_kana_TE: d('kana_TE', u"\u30C6", 'katakana letter te'), # テ
        XK_kana_TO: d('kana_TO', u"\u30C8", 'katakana letter to'), # ト
        XK_kana_NA: d('kana_NA', u"\u30CA", 'katakana letter na'), # ナ
        XK_kana_NI: d('kana_NI', u"\u30CB", 'katakana letter ni'), # ニ
        XK_kana_NU: d('kana_NU', u"\u30CC", 'katakana letter nu'), # ヌ
        XK_kana_NE: d('kana_NE', u"\u30CD", 'katakana letter ne'), # ネ
        XK_kana_NO: d('kana_NO', u"\u30CE", 'katakana letter no'), # ノ
        XK_kana_HA: d('kana_HA', u"\u30CF", 'katakana letter ha'), # ハ
        XK_kana_HI: d('kana_HI', u"\u30D2", 'katakana letter hi'), # ヒ
        XK_kana_FU: d('kana_FU', u"\u30D5", 'katakana letter hu'), # フ
        XK_kana_HE: d('kana_HE', u"\u30D8", 'katakana letter he'), # ヘ
        XK_kana_HO: d('kana_HO', u"\u30DB", 'katakana letter ho'), # ホ
        XK_kana_MA: d('kana_MA', u"\u30DE", 'katakana letter ma'), # マ
        XK_kana_MI: d('kana_MI', u"\u30DF", 'katakana letter mi'), # ミ
        XK_kana_MU: d('kana_MU', u"\u30E0", 'katakana letter mu'), # ム
        XK_kana_ME: d('kana_ME', u"\u30E1", 'katakana letter me'), # メ
        XK_kana_MO: d('kana_MO', u"\u30E2", 'katakana letter mo'), # モ
        XK_kana_YA: d('kana_YA', u"\u30E4", 'katakana letter ya'), # ヤ
        XK_kana_YU: d('kana_YU', u"\u30E6", 'katakana letter yu'), # ユ
        XK_kana_YO: d('kana_YO', u"\u30E8", 'katakana letter yo'), # ヨ
        XK_kana_RA: d('kana_RA', u"\u30E9", 'katakana letter ra'), # ラ
        XK_kana_RI: d('kana_RI', u"\u30EA", 'katakana letter ri'), # リ
        XK_kana_RU: d('kana_RU', u"\u30EB", 'katakana letter ru'), # ル
        XK_kana_RE: d('kana_RE', u"\u30EC", 'katakana letter re'), # レ
        XK_kana_RO: d('kana_RO', u"\u30ED", 'katakana letter ro'), # ロ
        XK_kana_WA: d('kana_WA', u"\u30EF", 'katakana letter wa'), # ワ
        XK_kana_N: d('kana_N', u"\u30F3", 'katakana letter n'), # ン
        XK_voicedsound: d('voicedsound', u"\u309B", 'katakana-hiragana voiced sound mark'), # ゛
        XK_semivoicedsound: d('semivoicedsound', u"\u309C", 'katakana-hiragana semi-voiced sound mark'), # ゜
        XK_kana_switch: d('kana_switch', '', 'alias for mode_switch'),
    },


    #Arabic
    #Byte 3 = 5

    'arabic': {
        XK_Farsi_0: d('Farsi_0', u"\u06F0", 'extended arabic-indic digit zero'), # ۰
        XK_Farsi_1: d('Farsi_1', u"\u06F1", 'extended arabic-indic digit one'), # ۱
        XK_Farsi_2: d('Farsi_2', u"\u06F2", 'extended arabic-indic digit two'), # ۲
        XK_Farsi_3: d('Farsi_3', u"\u06F3", 'extended arabic-indic digit three'), # ۳
        XK_Farsi_4: d('Farsi_4', u"\u06F4", 'extended arabic-indic digit four'), # ۴
        XK_Farsi_5: d('Farsi_5', u"\u06F5", 'extended arabic-indic digit five'), # ۵
        XK_Farsi_6: d('Farsi_6', u"\u06F6", 'extended arabic-indic digit six'), # ۶
        XK_Farsi_7: d('Farsi_7', u"\u06F7", 'extended arabic-indic digit seven'), # ۷
        XK_Farsi_8: d('Farsi_8', u"\u06F8", 'extended arabic-indic digit eight'), # ۸
        XK_Farsi_9: d('Farsi_9', u"\u06F9", 'extended arabic-indic digit nine'), # ۹
        XK_Arabic_percent: d('Arabic_percent', u"\u066A", 'arabic percent sign'), # ٪
        XK_Arabic_superscript_alef: d('Arabic_superscript_alef', u"\u0670", 'arabic letter superscript alef'), # ٰ
        XK_Arabic_tteh: d('Arabic_tteh', u"\u0679", 'arabic letter tteh'), # ٹ
        XK_Arabic_peh: d('Arabic_peh', u"\u067E", 'arabic letter peh'), # پ
        XK_Arabic_tcheh: d('Arabic_tcheh', u"\u0686", 'arabic letter tcheh'), # چ
        XK_Arabic_ddal: d('Arabic_ddal', u"\u0688", 'arabic letter ddal'), # ڈ
        XK_Arabic_rreh: d('Arabic_rreh', u"\u0691", 'arabic letter rreh'), # ڑ
        XK_Arabic_comma: d('Arabic_comma', u"\u060C", 'arabic comma'), # ،
        XK_Arabic_fullstop: d('Arabic_fullstop', u"\u06D4", 'arabic full stop'), # ۔
        XK_Arabic_0: d('Arabic_0', u"\u0660", 'arabic-indic digit zero'), # ٠
        XK_Arabic_1: d('Arabic_1', u"\u0661", 'arabic-indic digit one'), # ١
        XK_Arabic_2: d('Arabic_2', u"\u0662", 'arabic-indic digit two'), # ٢
        XK_Arabic_3: d('Arabic_3', u"\u0663", 'arabic-indic digit three'), # ٣
        XK_Arabic_4: d('Arabic_4', u"\u0664", 'arabic-indic digit four'), # ٤
        XK_Arabic_5: d('Arabic_5', u"\u0665", 'arabic-indic digit five'), # ٥
        XK_Arabic_6: d('Arabic_6', u"\u0666", 'arabic-indic digit six'), # ٦
        XK_Arabic_7: d('Arabic_7', u"\u0667", 'arabic-indic digit seven'), # ٧
        XK_Arabic_8: d('Arabic_8', u"\u0668", 'arabic-indic digit eight'), # ٨
        XK_Arabic_9: d('Arabic_9', u"\u0669", 'arabic-indic digit nine'), # ٩
        XK_Arabic_semicolon: d('Arabic_semicolon', u"\u061B", 'arabic semicolon'), # ؛
        XK_Arabic_question_mark: d('Arabic_question_mark', u"\u061F", 'arabic question mark'), # ؟
        XK_Arabic_hamza: d('Arabic_hamza', u"\u0621", 'arabic letter hamza'), # ء
        XK_Arabic_maddaonalef: d('Arabic_maddaonalef', u"\u0622", 'arabic letter alef with madda above'), # آ
        XK_Arabic_hamzaonalef: d('Arabic_hamzaonalef', u"\u0623", 'arabic letter alef with hamza above'), # أ
        XK_Arabic_hamzaonwaw: d('Arabic_hamzaonwaw', u"\u0624", 'arabic letter waw with hamza above'), # ؤ
        XK_Arabic_hamzaunderalef: d('Arabic_hamzaunderalef', u"\u0625", 'arabic letter alef with hamza below'), # إ
        XK_Arabic_hamzaonyeh: d('Arabic_hamzaonyeh', u"\u0626", 'arabic letter yeh with hamza above'), # ئ
        XK_Arabic_alef: d('Arabic_alef', u"\u0627", 'arabic letter alef'), # ا
        XK_Arabic_beh: d('Arabic_beh', u"\u0628", 'arabic letter beh'), # ب
        XK_Arabic_tehmarbuta: d('Arabic_tehmarbuta', u"\u0629", 'arabic letter teh marbuta'), # ة
        XK_Arabic_teh: d('Arabic_teh', u"\u062A", 'arabic letter teh'), # ت
        XK_Arabic_theh: d('Arabic_theh', u"\u062B", 'arabic letter theh'), # ث
        XK_Arabic_jeem: d('Arabic_jeem', u"\u062C", 'arabic letter jeem'), # ج
        XK_Arabic_hah: d('Arabic_hah', u"\u062D", 'arabic letter hah'), # ح
        XK_Arabic_khah: d('Arabic_khah', u"\u062E", 'arabic letter khah'), # خ
        XK_Arabic_dal: d('Arabic_dal', u"\u062F", 'arabic letter dal'), # د
        XK_Arabic_thal: d('Arabic_thal', u"\u0630", 'arabic letter thal'), # ذ
        XK_Arabic_ra: d('Arabic_ra', u"\u0631", 'arabic letter reh'), # ر
        XK_Arabic_zain: d('Arabic_zain', u"\u0632", 'arabic letter zain'), # ز
        XK_Arabic_seen: d('Arabic_seen', u"\u0633", 'arabic letter seen'), # س
        XK_Arabic_sheen: d('Arabic_sheen', u"\u0634", 'arabic letter sheen'), # ش
        XK_Arabic_sad: d('Arabic_sad', u"\u0635", 'arabic letter sad'), # ص
        XK_Arabic_dad: d('Arabic_dad', u"\u0636", 'arabic letter dad'), # ض
        XK_Arabic_tah: d('Arabic_tah', u"\u0637", 'arabic letter tah'), # ط
        XK_Arabic_zah: d('Arabic_zah', u"\u0638", 'arabic letter zah'), # ظ
        XK_Arabic_ain: d('Arabic_ain', u"\u0639", 'arabic letter ain'), # ع
        XK_Arabic_ghain: d('Arabic_ghain', u"\u063A", 'arabic letter ghain'), # غ
        XK_Arabic_tatweel: d('Arabic_tatweel', u"\u0640", 'arabic tatweel'), # ـ
        XK_Arabic_feh: d('Arabic_feh', u"\u0641", 'arabic letter feh'), # ف
        XK_Arabic_qaf: d('Arabic_qaf', u"\u0642", 'arabic letter qaf'), # ق
        XK_Arabic_kaf: d('Arabic_kaf', u"\u0643", 'arabic letter kaf'), # ك
        XK_Arabic_lam: d('Arabic_lam', u"\u0644", 'arabic letter lam'), # ل
        XK_Arabic_meem: d('Arabic_meem', u"\u0645", 'arabic letter meem'), # م
        XK_Arabic_noon: d('Arabic_noon', u"\u0646", 'arabic letter noon'), # ن
        XK_Arabic_ha: d('Arabic_ha', u"\u0647", 'arabic letter heh'), # ه
        XK_Arabic_waw: d('Arabic_waw', u"\u0648", 'arabic letter waw'), # و
        XK_Arabic_alefmaksura: d('Arabic_alefmaksura', u"\u0649", 'arabic letter alef maksura'), # ى
        XK_Arabic_yeh: d('Arabic_yeh', u"\u064A", 'arabic letter yeh'), # ي
        XK_Arabic_fathatan: d('Arabic_fathatan', u"\u064B", 'arabic fathatan'), # ً
        XK_Arabic_dammatan: d('Arabic_dammatan', u"\u064C", 'arabic dammatan'), # ٌ
        XK_Arabic_kasratan: d('Arabic_kasratan', u"\u064D", 'arabic kasratan'), # ٍ
        XK_Arabic_fatha: d('Arabic_fatha', u"\u064E", 'arabic fatha'), # َ
        XK_Arabic_damma: d('Arabic_damma', u"\u064F", 'arabic damma'), # ُ
        XK_Arabic_kasra: d('Arabic_kasra', u"\u0650", 'arabic kasra'), # ِ
        XK_Arabic_shadda: d('Arabic_shadda', u"\u0651", 'arabic shadda'), # ّ
        XK_Arabic_sukun: d('Arabic_sukun', u"\u0652", 'arabic sukun'), # ْ
        XK_Arabic_madda_above: d('Arabic_madda_above', u"\u0653", 'arabic maddah above'), # ٓ
        XK_Arabic_hamza_above: d('Arabic_hamza_above', u"\u0654", 'arabic hamza above'), # ٔ
        XK_Arabic_hamza_below: d('Arabic_hamza_below', u"\u0655", 'arabic hamza below'), # ٕ
        XK_Arabic_jeh: d('Arabic_jeh', u"\u0698", 'arabic letter jeh'), # ژ
        XK_Arabic_veh: d('Arabic_veh', u"\u06A4", 'arabic letter veh'), # ڤ
        XK_Arabic_keheh: d('Arabic_keheh', u"\u06A9", 'arabic letter keheh'), # ک
        XK_Arabic_gaf: d('Arabic_gaf', u"\u06AF", 'arabic letter gaf'), # گ
        XK_Arabic_noon_ghunna: d('Arabic_noon_ghunna', u"\u06BA", 'arabic letter noon ghunna'), # ں
        XK_Arabic_heh_doachashmee: d('Arabic_heh_doachashmee', u"\u06BE", 'arabic letter heh doachashmee'), # ھ
        XK_Farsi_yeh: d('Farsi_yeh', u"\u06CC", 'arabic letter farsi yeh'), # ی
        XK_Arabic_farsi_yeh: d('Arabic_farsi_yeh', u"\u06CC", 'arabic letter farsi yeh'), # ی
        XK_Arabic_yeh_baree: d('Arabic_yeh_baree', u"\u06D2", 'arabic letter yeh barree'), # ے
        XK_Arabic_heh_goal: d('Arabic_heh_goal', u"\u06C1", 'arabic letter heh goal'), # ہ
        XK_Arabic_switch: d('Arabic_switch', '', 'alias for mode_switch'),
    },


    #Cyrillic
    #Byte 3 = 6
    'cyrillic': {
        XK_Cyrillic_GHE_bar: d('Cyrillic_GHE_bar', u"\u0492", 'cyrillic capital letter ghe with stroke'), # Ғ
        XK_Cyrillic_ghe_bar: d('Cyrillic_ghe_bar', u"\u0493", 'cyrillic small letter ghe with stroke'), # ғ
        XK_Cyrillic_ZHE_descender: d('Cyrillic_ZHE_descender', u"\u0496", 'cyrillic capital letter zhe with descender'), # Җ
        XK_Cyrillic_zhe_descender: d('Cyrillic_zhe_descender', u"\u0497", 'cyrillic small letter zhe with descender'), # җ
        XK_Cyrillic_KA_descender: d('Cyrillic_KA_descender', u"\u049A", 'cyrillic capital letter ka with descender'), # Қ
        XK_Cyrillic_ka_descender: d('Cyrillic_ka_descender', u"\u049B", 'cyrillic small letter ka with descender'), # қ
        XK_Cyrillic_KA_vertstroke: d('Cyrillic_KA_vertstroke', u"\u049C", 'cyrillic capital letter ka with vertical stroke'), # Ҝ
        XK_Cyrillic_ka_vertstroke: d('Cyrillic_ka_vertstroke', u"\u049D", 'cyrillic small letter ka with vertical stroke'), # ҝ
        XK_Cyrillic_EN_descender: d('Cyrillic_EN_descender', u"\u04A2", 'cyrillic capital letter en with descender'), # Ң
        XK_Cyrillic_en_descender: d('Cyrillic_en_descender', u"\u04A3", 'cyrillic small letter en with descender'), # ң
        XK_Cyrillic_U_straight: d('Cyrillic_U_straight', u"\u04AE", 'cyrillic capital letter straight u'), # Ү
        XK_Cyrillic_u_straight: d('Cyrillic_u_straight', u"\u04AF", 'cyrillic small letter straight u'), # ү
        XK_Cyrillic_U_straight_bar: d('Cyrillic_U_straight_bar', u"\u04B0", 'cyrillic capital letter straight u with stroke'), # Ұ
        XK_Cyrillic_u_straight_bar: d('Cyrillic_u_straight_bar', u"\u04B1", 'cyrillic small letter straight u with stroke'), # ұ
        XK_Cyrillic_HA_descender: d('Cyrillic_HA_descender', u"\u04B2", 'cyrillic capital letter ha with descender'), # Ҳ
        XK_Cyrillic_ha_descender: d('Cyrillic_ha_descender', u"\u04B3", 'cyrillic small letter ha with descender'), # ҳ
        XK_Cyrillic_CHE_descender: d('Cyrillic_CHE_descender', u"\u04B6", 'cyrillic capital letter che with descender'), # Ҷ
        XK_Cyrillic_che_descender: d('Cyrillic_che_descender', u"\u04B7", 'cyrillic small letter che with descender'), # ҷ
        XK_Cyrillic_CHE_vertstroke: d('Cyrillic_CHE_vertstroke', u"\u04B8", 'cyrillic capital letter che with vertical stroke'), # Ҹ
        XK_Cyrillic_che_vertstroke: d('Cyrillic_che_vertstroke', u"\u04B9", 'cyrillic small letter che with vertical stroke'), # ҹ
        XK_Cyrillic_SHHA: d('Cyrillic_SHHA', u"\u04BA", 'cyrillic capital letter shha'), # Һ
        XK_Cyrillic_shha: d('Cyrillic_shha', u"\u04BB", 'cyrillic small letter shha'), # һ

        XK_Cyrillic_SCHWA: d('Cyrillic_SCHWA', u"\u04D8", 'cyrillic capital letter schwa'), # Ә
        XK_Cyrillic_schwa: d('Cyrillic_schwa', u"\u04D9", 'cyrillic small letter schwa'), # ә
        XK_Cyrillic_I_macron: d('Cyrillic_I_macron', u"\u04E2", 'cyrillic capital letter i with macron'), # Ӣ
        XK_Cyrillic_i_macron: d('Cyrillic_i_macron', u"\u04E3", 'cyrillic small letter i with macron'), # ӣ
        XK_Cyrillic_O_bar: d('Cyrillic_O_bar', u"\u04E8", 'cyrillic capital letter barred o'), # Ө
        XK_Cyrillic_o_bar: d('Cyrillic_o_bar', u"\u04E9", 'cyrillic small letter barred o'), # ө
        XK_Cyrillic_U_macron: d('Cyrillic_U_macron', u"\u04EE", 'cyrillic capital letter u with macron'), # Ӯ
        XK_Cyrillic_u_macron: d('Cyrillic_u_macron', u"\u04EF", 'cyrillic small letter u with macron'), # ӯ

        XK_Serbian_dje: d('Serbian_dje', u"\u0452", 'cyrillic small letter dje'), # ђ
        XK_Macedonia_gje: d('Macedonia_gje', u"\u0453", 'cyrillic small letter gje'), # ѓ
        XK_Cyrillic_io: d('Cyrillic_io', u"\u0451", 'cyrillic small letter io'), # ё
        XK_Ukrainian_ie: d('Ukrainian_ie', u"\u0454", 'cyrillic small letter ukrainian ie'), # є
        XK_Macedonia_dse: d('Macedonia_dse', u"\u0455", 'cyrillic small letter dze'), # ѕ
        XK_Ukrainian_i: d('Ukrainian_i', u"\u0456", 'cyrillic small letter byelorussian-ukrainian i'), # і
        XK_Ukrainian_yi: d('Ukrainian_yi', u"\u0457", 'cyrillic small letter yi'), # ї
        XK_Cyrillic_je: d('Cyrillic_je', u"\u0458", 'cyrillic small letter je'), # ј
        XK_Cyrillic_lje: d('Cyrillic_lje', u"\u0459", 'cyrillic small letter lje'), # љ
        XK_Cyrillic_nje: d('Cyrillic_nje', u"\u045A", 'cyrillic small letter nje'), # њ
        XK_Serbian_tshe: d('Serbian_tshe', u"\u045B", 'cyrillic small letter tshe'), # ћ
        XK_Macedonia_kje: d('Macedonia_kje', u"\u045C", 'cyrillic small letter kje'), # ќ
        XK_Ukrainian_ghe_with_upturn: d('Ukrainian_ghe_with_upturn', u"\u0491", 'cyrillic small letter ghe with upturn'), # ґ
        XK_Byelorussian_shortu: d('Byelorussian_shortu', u"\u045E", 'cyrillic small letter short u'), # ў
        XK_Cyrillic_dzhe: d('Cyrillic_dzhe', u"\u045F", 'cyrillic small letter dzhe'), # џ
        XK_numerosign: d('numerosign', u"\u2116", 'numero sign'), # №
        XK_Serbian_DJE: d('Serbian_DJE', u"\u0402", 'cyrillic capital letter dje'), # Ђ
        XK_Macedonia_GJE: d('Macedonia_GJE', u"\u0403", 'cyrillic capital letter gje'), # Ѓ
        XK_Cyrillic_IO: d('Cyrillic_IO', u"\u0401", 'cyrillic capital letter io'), # Ё
        XK_Ukrainian_IE: d('Ukrainian_IE', u"\u0404", 'cyrillic capital letter ukrainian ie'), # Є
        XK_Macedonia_DSE: d('Macedonia_DSE', u"\u0405", 'cyrillic capital letter dze'), # Ѕ
        XK_Ukrainian_I: d('Ukrainian_I', u"\u0406", 'cyrillic capital letter byelorussian-ukrainian i'), # І
        XK_Ukrainian_YI: d('Ukrainian_YI', u"\u0407", 'cyrillic capital letter yi'), # Ї
        XK_Cyrillic_JE: d('Cyrillic_JE', u"\u0408", 'cyrillic capital letter je'), # Ј
        XK_Cyrillic_LJE: d('Cyrillic_LJE', u"\u0409", 'cyrillic capital letter lje'), # Љ
        XK_Cyrillic_NJE: d('Cyrillic_NJE', u"\u040A", 'cyrillic capital letter nje'), # Њ
        XK_Serbian_TSHE: d('Serbian_TSHE', u"\u040B", 'cyrillic capital letter tshe'), # Ћ
        XK_Macedonia_KJE: d('Macedonia_KJE', u"\u040C", 'cyrillic capital letter kje'), # Ќ
        XK_Ukrainian_GHE_WITH_UPTURN: d('Ukrainian_GHE_WITH_UPTURN', u"\u0490", 'cyrillic capital letter ghe with upturn'), # Ґ
        XK_Byelorussian_SHORTU: d('Byelorussian_SHORTU', u"\u040E", 'cyrillic capital letter short u'), # Ў
        XK_Cyrillic_DZHE: d('Cyrillic_DZHE', u"\u040F", 'cyrillic capital letter dzhe'), # Џ
        XK_Cyrillic_yu: d('Cyrillic_yu', u"\u044E", 'cyrillic small letter yu'), # ю
        XK_Cyrillic_a: d('Cyrillic_a', u"\u0430", 'cyrillic small letter a'), # а
        XK_Cyrillic_be: d('Cyrillic_be', u"\u0431", 'cyrillic small letter be'), # б
        XK_Cyrillic_tse: d('Cyrillic_tse', u"\u0446", 'cyrillic small letter tse'), # ц
        XK_Cyrillic_de: d('Cyrillic_de', u"\u0434", 'cyrillic small letter de'), # д
        XK_Cyrillic_ie: d('Cyrillic_ie', u"\u0435", 'cyrillic small letter ie'), # е
        XK_Cyrillic_ef: d('Cyrillic_ef', u"\u0444", 'cyrillic small letter ef'), # ф
        XK_Cyrillic_ghe: d('Cyrillic_ghe', u"\u0433", 'cyrillic small letter ghe'), # г
        XK_Cyrillic_ha: d('Cyrillic_ha', u"\u0445", 'cyrillic small letter ha'), # х
        XK_Cyrillic_i: d('Cyrillic_i', u"\u0438", 'cyrillic small letter i'), # и
        XK_Cyrillic_shorti: d('Cyrillic_shorti', u"\u0439", 'cyrillic small letter short i'), # й
        XK_Cyrillic_ka: d('Cyrillic_ka', u"\u043A", 'cyrillic small letter ka'), # к
        XK_Cyrillic_el: d('Cyrillic_el', u"\u043B", 'cyrillic small letter el'), # л
        XK_Cyrillic_em: d('Cyrillic_em', u"\u043C", 'cyrillic small letter em'), # м
        XK_Cyrillic_en: d('Cyrillic_en', u"\u043D", 'cyrillic small letter en'), # н
        XK_Cyrillic_o: d('Cyrillic_o', u"\u043E", 'cyrillic small letter o'), # о
        XK_Cyrillic_pe: d('Cyrillic_pe', u"\u043F", 'cyrillic small letter pe'), # п
        XK_Cyrillic_ya: d('Cyrillic_ya', u"\u044F", 'cyrillic small letter ya'), # я
        XK_Cyrillic_er: d('Cyrillic_er', u"\u0440", 'cyrillic small letter er'), # р
        XK_Cyrillic_es: d('Cyrillic_es', u"\u0441", 'cyrillic small letter es'), # с
        XK_Cyrillic_te: d('Cyrillic_te', u"\u0442", 'cyrillic small letter te'), # т
        XK_Cyrillic_u: d('Cyrillic_u', u"\u0443", 'cyrillic small letter u'), # у
        XK_Cyrillic_zhe: d('Cyrillic_zhe', u"\u0436", 'cyrillic small letter zhe'), # ж
        XK_Cyrillic_ve: d('Cyrillic_ve', u"\u0432", 'cyrillic small letter ve'), # в
        XK_Cyrillic_softsign: d('Cyrillic_softsign', u"\u044C", 'cyrillic small letter soft sign'), # ь
        XK_Cyrillic_yeru: d('Cyrillic_yeru', u"\u044B", 'cyrillic small letter yeru'), # ы
        XK_Cyrillic_ze: d('Cyrillic_ze', u"\u0437", 'cyrillic small letter ze'), # з
        XK_Cyrillic_sha: d('Cyrillic_sha', u"\u0448", 'cyrillic small letter sha'), # ш
        XK_Cyrillic_e: d('Cyrillic_e', u"\u044D", 'cyrillic small letter e'), # э
        XK_Cyrillic_shcha: d('Cyrillic_shcha', u"\u0449", 'cyrillic small letter shcha'), # щ
        XK_Cyrillic_che: d('Cyrillic_che', u"\u0447", 'cyrillic small letter che'), # ч
        XK_Cyrillic_hardsign: d('Cyrillic_hardsign', u"\u044A", 'cyrillic small letter hard sign'), # ъ
        XK_Cyrillic_YU: d('Cyrillic_YU', u"\u042E", 'cyrillic capital letter yu'), # Ю
        XK_Cyrillic_A: d('Cyrillic_A', u"\u0410", 'cyrillic capital letter a'), # А
        XK_Cyrillic_BE: d('Cyrillic_BE', u"\u0411", 'cyrillic capital letter be'), # Б
        XK_Cyrillic_TSE: d('Cyrillic_TSE', u"\u0426", 'cyrillic capital letter tse'), # Ц
        XK_Cyrillic_DE: d('Cyrillic_DE', u"\u0414", 'cyrillic capital letter de'), # Д
        XK_Cyrillic_IE: d('Cyrillic_IE', u"\u0415", 'cyrillic capital letter ie'), # Е
        XK_Cyrillic_EF: d('Cyrillic_EF', u"\u0424", 'cyrillic capital letter ef'), # Ф
        XK_Cyrillic_GHE: d('Cyrillic_GHE', u"\u0413", 'cyrillic capital letter ghe'), # Г
        XK_Cyrillic_HA: d('Cyrillic_HA', u"\u0425", 'cyrillic capital letter ha'), # Х
        XK_Cyrillic_I: d('Cyrillic_I', u"\u0418", 'cyrillic capital letter i'), # И
        XK_Cyrillic_SHORTI: d('Cyrillic_SHORTI', u"\u0419", 'cyrillic capital letter short i'), # Й
        XK_Cyrillic_KA: d('Cyrillic_KA', u"\u041A", 'cyrillic capital letter ka'), # К
        XK_Cyrillic_EL: d('Cyrillic_EL', u"\u041B", 'cyrillic capital letter el'), # Л
        XK_Cyrillic_EM: d('Cyrillic_EM', u"\u041C", 'cyrillic capital letter em'), # М
        XK_Cyrillic_EN: d('Cyrillic_EN', u"\u041D", 'cyrillic capital letter en'), # Н
        XK_Cyrillic_O: d('Cyrillic_O', u"\u041E", 'cyrillic capital letter o'), # О
        XK_Cyrillic_PE: d('Cyrillic_PE', u"\u041F", 'cyrillic capital letter pe'), # П
        XK_Cyrillic_YA: d('Cyrillic_YA', u"\u042F", 'cyrillic capital letter ya'), # Я
        XK_Cyrillic_ER: d('Cyrillic_ER', u"\u0420", 'cyrillic capital letter er'), # Р
        XK_Cyrillic_ES: d('Cyrillic_ES', u"\u0421", 'cyrillic capital letter es'), # С
        XK_Cyrillic_TE: d('Cyrillic_TE', u"\u0422", 'cyrillic capital letter te'), # Т
        XK_Cyrillic_U: d('Cyrillic_U', u"\u0423", 'cyrillic capital letter u'), # У
        XK_Cyrillic_ZHE: d('Cyrillic_ZHE', u"\u0416", 'cyrillic capital letter zhe'), # Ж
        XK_Cyrillic_VE: d('Cyrillic_VE', u"\u0412", 'cyrillic capital letter ve'), # В
        XK_Cyrillic_SOFTSIGN: d('Cyrillic_SOFTSIGN', u"\u042C", 'cyrillic capital letter soft sign'), # Ь
        XK_Cyrillic_YERU: d('Cyrillic_YERU', u"\u042B", 'cyrillic capital letter yeru'), # Ы
        XK_Cyrillic_ZE: d('Cyrillic_ZE', u"\u0417", 'cyrillic capital letter ze'), # З
        XK_Cyrillic_SHA: d('Cyrillic_SHA', u"\u0428", 'cyrillic capital letter sha'), # Ш
        XK_Cyrillic_E: d('Cyrillic_E', u"\u042D", 'cyrillic capital letter e'), # Э
        XK_Cyrillic_SHCHA: d('Cyrillic_SHCHA', u"\u0429", 'cyrillic capital letter shcha'), # Щ
        XK_Cyrillic_CHE: d('Cyrillic_CHE', u"\u0427", 'cyrillic capital letter che'), # Ч
        XK_Cyrillic_HARDSIGN: d('Cyrillic_HARDSIGN', u"\u042A", 'cyrillic capital letter hard sign'), # Ъ
    },


    #Greek
    #(based on an early draft of, and not quite identical to, ISO/IEC 8859-7)
    #Byte 3 = 7

    'greek': {
        XK_Greek_ALPHAaccent: d('Greek_ALPHAaccent', u"\u0386", 'greek capital letter alpha with tonos'), # Ά
        XK_Greek_EPSILONaccent: d('Greek_EPSILONaccent', u"\u0388", 'greek capital letter epsilon with tonos'), # Έ
        XK_Greek_ETAaccent: d('Greek_ETAaccent', u"\u0389", 'greek capital letter eta with tonos'), # Ή
        XK_Greek_IOTAaccent: d('Greek_IOTAaccent', u"\u038A", 'greek capital letter iota with tonos'), # Ί
        XK_Greek_IOTAdieresis: d('Greek_IOTAdieresis', u"\u03AA", 'greek capital letter iota with dialytika'), # Ϊ
        XK_Greek_OMICRONaccent: d('Greek_OMICRONaccent', u"\u038C", 'greek capital letter omicron with tonos'), # Ό
        XK_Greek_UPSILONaccent: d('Greek_UPSILONaccent', u"\u038E", 'greek capital letter upsilon with tonos'), # Ύ
        XK_Greek_UPSILONdieresis: d('Greek_UPSILONdieresis', u"\u03AB", 'greek capital letter upsilon with dialytika'), # Ϋ
        XK_Greek_OMEGAaccent: d('Greek_OMEGAaccent', u"\u038F", 'greek capital letter omega with tonos'), # Ώ
        XK_Greek_accentdieresis: d('Greek_accentdieresis', u"\u0385", 'greek dialytika tonos'), # ΅
        XK_Greek_horizbar: d('Greek_horizbar', u"\u2015", 'horizontal bar'), # ―
        XK_Greek_alphaaccent: d('Greek_alphaaccent', u"\u03AC", 'greek small letter alpha with tonos'), # ά
        XK_Greek_epsilonaccent: d('Greek_epsilonaccent', u"\u03AD", 'greek small letter epsilon with tonos'), # έ
        XK_Greek_etaaccent: d('Greek_etaaccent', u"\u03AE", 'greek small letter eta with tonos'), # ή
        XK_Greek_iotaaccent: d('Greek_iotaaccent', u"\u03AF", 'greek small letter iota with tonos'), # ί
        XK_Greek_iotadieresis: d('Greek_iotadieresis', u"\u03CA", 'greek small letter iota with dialytika'), # ϊ
        XK_Greek_iotaaccentdieresis: d('Greek_iotaaccentdieresis', u"\u0390", 'greek small letter iota with dialytika and tonos'), # ΐ
        XK_Greek_omicronaccent: d('Greek_omicronaccent', u"\u03CC", 'greek small letter omicron with tonos'), # ό
        XK_Greek_upsilonaccent: d('Greek_upsilonaccent', u"\u03CD", 'greek small letter upsilon with tonos'), # ύ
        XK_Greek_upsilondieresis: d('Greek_upsilondieresis', u"\u03CB", 'greek small letter upsilon with dialytika'), # ϋ
        XK_Greek_upsilonaccentdieresis: d('Greek_upsilonaccentdieresis', u"\u03B0", 'greek small letter upsilon with dialytika and tonos'), # ΰ
        XK_Greek_omegaaccent: d('Greek_omegaaccent', u"\u03CE", 'greek small letter omega with tonos'), # ώ
        XK_Greek_ALPHA: d('Greek_ALPHA', u"\u0391", 'greek capital letter alpha'), # Α
        XK_Greek_BETA: d('Greek_BETA', u"\u0392", 'greek capital letter beta'), # Β
        XK_Greek_GAMMA: d('Greek_GAMMA', u"\u0393", 'greek capital letter gamma'), # Γ
        XK_Greek_DELTA: d('Greek_DELTA', u"\u0394", 'greek capital letter delta'), # Δ
        XK_Greek_EPSILON: d('Greek_EPSILON', u"\u0395", 'greek capital letter epsilon'), # Ε
        XK_Greek_ZETA: d('Greek_ZETA', u"\u0396", 'greek capital letter zeta'), # Ζ
        XK_Greek_ETA: d('Greek_ETA', u"\u0397", 'greek capital letter eta'), # Η
        XK_Greek_THETA: d('Greek_THETA', u"\u0398", 'greek capital letter theta'), # Θ
        XK_Greek_IOTA: d('Greek_IOTA', u"\u0399", 'greek capital letter iota'), # Ι
        XK_Greek_KAPPA: d('Greek_KAPPA', u"\u039A", 'greek capital letter kappa'), # Κ
        XK_Greek_LAMDA: d('Greek_LAMDA', u"\u039B", 'greek capital letter lamda'), # Λ
        XK_Greek_LAMBDA: d('Greek_LAMBDA', u"\u039B", 'greek capital letter lamda'), # Λ
        XK_Greek_MU: d('Greek_MU', u"\u039C", 'greek capital letter mu'), # Μ
        XK_Greek_NU: d('Greek_NU', u"\u039D", 'greek capital letter nu'), # Ν
        XK_Greek_XI: d('Greek_XI', u"\u039E", 'greek capital letter xi'), # Ξ
        XK_Greek_OMICRON: d('Greek_OMICRON', u"\u039F", 'greek capital letter omicron'), # Ο
        XK_Greek_PI: d('Greek_PI', u"\u03A0", 'greek capital letter pi'), # Π
        XK_Greek_RHO: d('Greek_RHO', u"\u03A1", 'greek capital letter rho'), # Ρ
        XK_Greek_SIGMA: d('Greek_SIGMA', u"\u03A3", 'greek capital letter sigma'), # Σ
        XK_Greek_TAU: d('Greek_TAU', u"\u03A4", 'greek capital letter tau'), # Τ
        XK_Greek_UPSILON: d('Greek_UPSILON', u"\u03A5", 'greek capital letter upsilon'), # Υ
        XK_Greek_PHI: d('Greek_PHI', u"\u03A6", 'greek capital letter phi'), # Φ
        XK_Greek_CHI: d('Greek_CHI', u"\u03A7", 'greek capital letter chi'), # Χ
        XK_Greek_PSI: d('Greek_PSI', u"\u03A8", 'greek capital letter psi'), # Ψ
        XK_Greek_OMEGA: d('Greek_OMEGA', u"\u03A9", 'greek capital letter omega'), # Ω
        XK_Greek_alpha: d('Greek_alpha', u"\u03B1", 'greek small letter alpha'), # α
        XK_Greek_beta: d('Greek_beta', u"\u03B2", 'greek small letter beta'), # β
        XK_Greek_gamma: d('Greek_gamma', u"\u03B3", 'greek small letter gamma'), # γ
        XK_Greek_delta: d('Greek_delta', u"\u03B4", 'greek small letter delta'), # δ
        XK_Greek_epsilon: d('Greek_epsilon', u"\u03B5", 'greek small letter epsilon'), # ε
        XK_Greek_zeta: d('Greek_zeta', u"\u03B6", 'greek small letter zeta'), # ζ
        XK_Greek_eta: d('Greek_eta', u"\u03B7", 'greek small letter eta'), # η
        XK_Greek_theta: d('Greek_theta', u"\u03B8", 'greek small letter theta'), # θ
        XK_Greek_iota: d('Greek_iota', u"\u03B9", 'greek small letter iota'), # ι
        XK_Greek_kappa: d('Greek_kappa', u"\u03BA", 'greek small letter kappa'), # κ
        XK_Greek_lamda: d('Greek_lamda', u"\u03BB", 'greek small letter lamda'), # λ
        XK_Greek_lambda: d('Greek_lambda', u"\u03BB", 'greek small letter lamda'), # λ
        XK_Greek_mu: d('Greek_mu', u"\u03BC", 'greek small letter mu'), # μ
        XK_Greek_nu: d('Greek_nu', u"\u03BD", 'greek small letter nu'), # ν
        XK_Greek_xi: d('Greek_xi', u"\u03BE", 'greek small letter xi'), # ξ
        XK_Greek_omicron: d('Greek_omicron', u"\u03BF", 'greek small letter omicron'), # ο
        XK_Greek_pi: d('Greek_pi', u"\u03C0", 'greek small letter pi'), # π
        XK_Greek_rho: d('Greek_rho', u"\u03C1", 'greek small letter rho'), # ρ
        XK_Greek_sigma: d('Greek_sigma', u"\u03C3", 'greek small letter sigma'), # σ
        XK_Greek_finalsmallsigma: d('Greek_finalsmallsigma', u"\u03C2", 'greek small letter final sigma'), # ς
        XK_Greek_tau: d('Greek_tau', u"\u03C4", 'greek small letter tau'), # τ
        XK_Greek_upsilon: d('Greek_upsilon', u"\u03C5", 'greek small letter upsilon'), # υ
        XK_Greek_phi: d('Greek_phi', u"\u03C6", 'greek small letter phi'), # φ
        XK_Greek_chi: d('Greek_chi', u"\u03C7", 'greek small letter chi'), # χ
        XK_Greek_psi: d('Greek_psi', u"\u03C8", 'greek small letter psi'), # ψ
        XK_Greek_omega: d('Greek_omega', u"\u03C9", 'greek small letter omega'), # ω
        XK_Greek_switch: d('Greek_switch', '', 'alias for mode_switch'),
    },


    #Technical
    #(from the DEC VT330/VT420 Technical Character Set, http://vt100.net/charsets/technical.html)
    #Byte 3 = 8

    'technical': {
        XK_leftradical: d('leftradical', u"\u23B7", 'radical symbol bottom'), # ⎷
        XK_topleftradical: d('topleftradical', u"\u250C", 'box drawings light down and right'), # ┌
        XK_horizconnector: d('horizconnector', u"\u2500", 'box drawings light horizontal'), # ─
        XK_topintegral: d('topintegral', u"\u2320", 'top half integral'), # ⌠
        XK_botintegral: d('botintegral', u"\u2321", 'bottom half integral'), # ⌡
        XK_vertconnector: d('vertconnector', u"\u2502", 'box drawings light vertical'), # │
        XK_topleftsqbracket: d('topleftsqbracket', u"\u23A1", 'left square bracket upper corner'), # ⎡
        XK_botleftsqbracket: d('botleftsqbracket', u"\u23A3", 'left square bracket lower corner'), # ⎣
        XK_toprightsqbracket: d('toprightsqbracket', u"\u23A4", 'right square bracket upper corner'), # ⎤
        XK_botrightsqbracket: d('botrightsqbracket', u"\u23A6", 'right square bracket lower corner'), # ⎦
        XK_topleftparens: d('topleftparens', u"\u239B", 'left parenthesis upper hook'), # ⎛
        XK_botleftparens: d('botleftparens', u"\u239D", 'left parenthesis lower hook'), # ⎝
        XK_toprightparens: d('toprightparens', u"\u239E", 'right parenthesis upper hook'), # ⎞
        XK_botrightparens: d('botrightparens', u"\u23A0", 'right parenthesis lower hook'), # ⎠
        XK_leftmiddlecurlybrace: d('leftmiddlecurlybrace', u"\u23A8", 'left curly bracket middle piece'), # ⎨
        XK_rightmiddlecurlybrace: d('rightmiddlecurlybrace', u"\u23AC", 'right curly bracket middle piece'), # ⎬
        XK_topleftsummation: d('topleftsummation', '', ''),
        XK_botleftsummation: d('botleftsummation', '', ''),
        XK_topvertsummationconnector: d('topvertsummationconnector', '', ''),
        XK_botvertsummationconnector: d('botvertsummationconnector', '', ''),
        XK_toprightsummation: d('toprightsummation', '', ''),
        XK_botrightsummation: d('botrightsummation', '', ''),
        XK_rightmiddlesummation: d('rightmiddlesummation', '', ''),
        XK_lessthanequal: d('lessthanequal', u"\u2264", 'less-than or equal to'), # ≤
        XK_notequal: d('notequal', u"\u2260", 'not equal to'), # ≠
        XK_greaterthanequal: d('greaterthanequal', u"\u2265", 'greater-than or equal to'), # ≥
        XK_integral: d('integral', u"\u222B", 'integral'), # ∫
        XK_therefore: d('therefore', u"\u2234", 'therefore'), # ∴
        XK_variation: d('variation', u"\u221D", 'proportional to'), # ∝
        XK_infinity: d('infinity', u"\u221E", 'infinity'), # ∞
        XK_nabla: d('nabla', u"\u2207", 'nabla'), # ∇
        XK_approximate: d('approximate', u"\u223C", 'tilde operator'), # ∼
        XK_similarequal: d('similarequal', u"\u2243", 'asymptotically equal to'), # ≃
        XK_ifonlyif: d('ifonlyif', u"\u21D4", 'left right double arrow'), # ⇔
        XK_implies: d('implies', u"\u21D2", 'rightwards double arrow'), # ⇒
        XK_identical: d('identical', u"\u2261", 'identical to'), # ≡
        XK_radical: d('radical', u"\u221A", 'square root'), # √
        XK_includedin: d('includedin', u"\u2282", 'subset of'), # ⊂
        XK_includes: d('includes', u"\u2283", 'superset of'), # ⊃
        XK_intersection: d('intersection', u"\u2229", 'intersection'), # ∩
        XK_union: d('union', u"\u222A", 'union'), # ∪
        XK_logicaland: d('logicaland', u"\u2227", 'logical and'), # ∧
        XK_logicalor: d('logicalor', u"\u2228", 'logical or'), # ∨
        XK_partialderivative: d('partialderivative', u"\u2202", 'partial differential'), # ∂
        XK_function: d('function', u"\u0192", 'latin small letter f with hook'), # ƒ
        XK_leftarrow: d('leftarrow', u"\u2190", 'leftwards arrow'), # ←
        XK_uparrow: d('uparrow', u"\u2191", 'upwards arrow'), # ↑
        XK_rightarrow: d('rightarrow', u"\u2192", 'rightwards arrow'), # →
        XK_downarrow: d('downarrow', u"\u2193", 'downwards arrow'), # ↓
    },


    #Special
    #(from the DEC VT100 Special Graphics Character Set)
    #Byte 3 = 9

    'special': {
        XK_blank: d('blank', '', ''),
        XK_soliddiamond: d('soliddiamond', u"\u25C6", 'black diamond'), # ◆
        XK_checkerboard: d('checkerboard', u"\u2592", 'medium shade'), # ▒
        XK_ht: d('ht', u"\u2409", 'symbol for horizontal tabulation'), # ␉
        XK_ff: d('ff', u"\u240C", 'symbol for form feed'), # ␌
        XK_cr: d('cr', u"\u240D", 'symbol for carriage return'), # ␍
        XK_lf: d('lf', u"\u240A", 'symbol for line feed'), # ␊
        XK_nl: d('nl', u"\u2424", 'symbol for newline'), # ␤
        XK_vt: d('vt', u"\u240B", 'symbol for vertical tabulation'), # ␋
        XK_lowrightcorner: d('lowrightcorner', u"\u2518", 'box drawings light up and left'), # ┘
        XK_uprightcorner: d('uprightcorner', u"\u2510", 'box drawings light down and left'), # ┐
        XK_upleftcorner: d('upleftcorner', u"\u250C", 'box drawings light down and right'), # ┌
        XK_lowleftcorner: d('lowleftcorner', u"\u2514", 'box drawings light up and right'), # └
        XK_crossinglines: d('crossinglines', u"\u253C", 'box drawings light vertical and horizontal'), # ┼
        XK_horizlinescan1: d('horizlinescan1', u"\u23BA", 'horizontal scan line-1'), # ⎺
        XK_horizlinescan3: d('horizlinescan3', u"\u23BB", 'horizontal scan line-3'), # ⎻
        XK_horizlinescan5: d('horizlinescan5', u"\u2500", 'box drawings light horizontal'), # ─
        XK_horizlinescan7: d('horizlinescan7', u"\u23BC", 'horizontal scan line-7'), # ⎼
        XK_horizlinescan9: d('horizlinescan9', u"\u23BD", 'horizontal scan line-9'), # ⎽
        XK_leftt: d('leftt', u"\u251C", 'box drawings light vertical and right'), # ├
        XK_rightt: d('rightt', u"\u2524", 'box drawings light vertical and left'), # ┤
        XK_bott: d('bott', u"\u2534", 'box drawings light up and horizontal'), # ┴
        XK_topt: d('topt', u"\u252C", 'box drawings light down and horizontal'), # ┬
        XK_vertbar: d('vertbar', u"\u2502", 'box drawings light vertical'), # │
    },


    #Publishing
    #(these are probably from a long forgotten DEC Publishing
    #font that once shipped with DECwrite)
    #Byte 3 = 0x0a

    'publishing': {
        XK_emspace: d('emspace', u"\u2003", 'em space'), #  
        XK_enspace: d('enspace', u"\u2002", 'en space'), #  
        XK_em3space: d('em3space', u"\u2004", 'three-per-em space'), #  
        XK_em4space: d('em4space', u"\u2005", 'four-per-em space'), #  
        XK_digitspace: d('digitspace', u"\u2007", 'figure space'), #  
        XK_punctspace: d('punctspace', u"\u2008", 'punctuation space'), #  
        XK_thinspace: d('thinspace', u"\u2009", 'thin space'), #  
        XK_hairspace: d('hairspace', u"\u200A", 'hair space'), #  
        XK_emdash: d('emdash', u"\u2014", 'em dash'), # —
        XK_endash: d('endash', u"\u2013", 'en dash'), # –
        XK_signifblank: d('signifblank', u"\u2423", 'open box'), # ␣
        XK_ellipsis: d('ellipsis', u"\u2026", 'horizontal ellipsis'), # …
        XK_doubbaselinedot: d('doubbaselinedot', u"\u2025", 'two dot leader'), # ‥
        XK_onethird: d('onethird', u"\u2153", 'vulgar fraction one third'), # ⅓
        XK_twothirds: d('twothirds', u"\u2154", 'vulgar fraction two thirds'), # ⅔
        XK_onefifth: d('onefifth', u"\u2155", 'vulgar fraction one fifth'), # ⅕
        XK_twofifths: d('twofifths', u"\u2156", 'vulgar fraction two fifths'), # ⅖
        XK_threefifths: d('threefifths', u"\u2157", 'vulgar fraction three fifths'), # ⅗
        XK_fourfifths: d('fourfifths', u"\u2158", 'vulgar fraction four fifths'), # ⅘
        XK_onesixth: d('onesixth', u"\u2159", 'vulgar fraction one sixth'), # ⅙
        XK_fivesixths: d('fivesixths', u"\u215A", 'vulgar fraction five sixths'), # ⅚
        XK_careof: d('careof', u"\u2105", 'care of'), # ℅
        XK_figdash: d('figdash', u"\u2012", 'figure dash'), # ‒
        XK_leftanglebracket: d('leftanglebracket', u"\u27E8", 'mathematical left angle bracket'), # ⟨
        XK_decimalpoint: d('decimalpoint', u"\u002E", 'full stop'), # .
        XK_rightanglebracket: d('rightanglebracket', u"\u27E9", 'mathematical right angle bracket'), # ⟩
        XK_marker: d('marker', '', ''),
        XK_oneeighth: d('oneeighth', u"\u215B", 'vulgar fraction one eighth'), # ⅛
        XK_threeeighths: d('threeeighths', u"\u215C", 'vulgar fraction three eighths'), # ⅜
        XK_fiveeighths: d('fiveeighths', u"\u215D", 'vulgar fraction five eighths'), # ⅝
        XK_seveneighths: d('seveneighths', u"\u215E", 'vulgar fraction seven eighths'), # ⅞
        XK_trademark: d('trademark', u"\u2122", 'trade mark sign'), # ™
        XK_signaturemark: d('signaturemark', u"\u2613", 'saltire'), # ☓
        XK_trademarkincircle: d('trademarkincircle', '', ''),
        XK_leftopentriangle: d('leftopentriangle', u"\u25C1", 'white left-pointing triangle'), # ◁
        XK_rightopentriangle: d('rightopentriangle', u"\u25B7", 'white right-pointing triangle'), # ▷
        XK_emopencircle: d('emopencircle', u"\u25CB", 'white circle'), # ○
        XK_emopenrectangle: d('emopenrectangle', u"\u25AF", 'white vertical rectangle'), # ▯
        XK_leftsinglequotemark: d('leftsinglequotemark', u"\u2018", 'left single quotation mark'), # ‘
        XK_rightsinglequotemark: d('rightsinglequotemark', u"\u2019", 'right single quotation mark'), # ’
        XK_leftdoublequotemark: d('leftdoublequotemark', u"\u201C", 'left double quotation mark'), # “
        XK_rightdoublequotemark: d('rightdoublequotemark', u"\u201D", 'right double quotation mark'), # ”
        XK_prescription: d('prescription', u"\u211E", 'prescription take'), # ℞
        XK_minutes: d('minutes', u"\u2032", 'prime'), # ′
        XK_seconds: d('seconds', u"\u2033", 'double prime'), # ″
        XK_latincross: d('latincross', u"\u271D", 'latin cross'), # ✝
        XK_hexagram: d('hexagram', '', ''),
        XK_filledrectbullet: d('filledrectbullet', u"\u25AC", 'black rectangle'), # ▬
        XK_filledlefttribullet: d('filledlefttribullet', u"\u25C0", 'black left-pointing triangle'), # ◀
        XK_filledrighttribullet: d('filledrighttribullet', u"\u25B6", 'black right-pointing triangle'), # ▶
        XK_emfilledcircle: d('emfilledcircle', u"\u25CF", 'black circle'), # ●
        XK_emfilledrect: d('emfilledrect', u"\u25AE", 'black vertical rectangle'), # ▮
        XK_enopencircbullet: d('enopencircbullet', u"\u25E6", 'white bullet'), # ◦
        XK_enopensquarebullet: d('enopensquarebullet', u"\u25AB", 'white small square'), # ▫
        XK_openrectbullet: d('openrectbullet', u"\u25AD", 'white rectangle'), # ▭
        XK_opentribulletup: d('opentribulletup', u"\u25B3", 'white up-pointing triangle'), # △
        XK_opentribulletdown: d('opentribulletdown', u"\u25BD", 'white down-pointing triangle'), # ▽
        XK_openstar: d('openstar', u"\u2606", 'white star'), # ☆
        XK_enfilledcircbullet: d('enfilledcircbullet', u"\u2022", 'bullet'), # •
        XK_enfilledsqbullet: d('enfilledsqbullet', u"\u25AA", 'black small square'), # ▪
        XK_filledtribulletup: d('filledtribulletup', u"\u25B2", 'black up-pointing triangle'), # ▲
        XK_filledtribulletdown: d('filledtribulletdown', u"\u25BC", 'black down-pointing triangle'), # ▼
        XK_leftpointer: d('leftpointer', u"\u261C", 'white left pointing index'), # ☜
        XK_rightpointer: d('rightpointer', u"\u261E", 'white right pointing index'), # ☞
        XK_club: d('club', u"\u2663", 'black club suit'), # ♣
        XK_diamond: d('diamond', u"\u2666", 'black diamond suit'), # ♦
        XK_heart: d('heart', u"\u2665", 'black heart suit'), # ♥
        XK_maltesecross: d('maltesecross', u"\u2720", 'maltese cross'), # ✠
        XK_dagger: d('dagger', u"\u2020", 'dagger'), # †
        XK_doubledagger: d('doubledagger', u"\u2021", 'double dagger'), # ‡
        XK_checkmark: d('checkmark', u"\u2713", 'check mark'), # ✓
        XK_ballotcross: d('ballotcross', u"\u2717", 'ballot x'), # ✗
        XK_musicalsharp: d('musicalsharp', u"\u266F", 'music sharp sign'), # ♯
        XK_musicalflat: d('musicalflat', u"\u266D", 'music flat sign'), # ♭
        XK_malesymbol: d('malesymbol', u"\u2642", 'male sign'), # ♂
        XK_femalesymbol: d('femalesymbol', u"\u2640", 'female sign'), # ♀
        XK_telephone: d('telephone', u"\u260E", 'black telephone'), # ☎
        XK_telephonerecorder: d('telephonerecorder', u"\u2315", 'telephone recorder'), # ⌕
        XK_phonographcopyright: d('phonographcopyright', u"\u2117", 'sound recording copyright'), # ℗
        XK_caret: d('caret', u"\u2038", 'caret'), # ‸
        XK_singlelowquotemark: d('singlelowquotemark', u"\u201A", 'single low-9 quotation mark'), # ‚
        XK_doublelowquotemark: d('doublelowquotemark', u"\u201E", 'double low-9 quotation mark'), # „
        XK_cursor: d('cursor', '', ''),
    },


    #APL
    #Byte 3 = 0x0b

    'apl': {
        XK_leftcaret: d('leftcaret', u"\u003C", 'less-than sign'), # <
        XK_rightcaret: d('rightcaret', u"\u003E", 'greater-than sign'), # >
        XK_downcaret: d('downcaret', u"\u2228", 'logical or'), # ∨
        XK_upcaret: d('upcaret', u"\u2227", 'logical and'), # ∧
        XK_overbar: d('overbar', u"\u00AF", 'macron'), # ¯
        XK_downtack: d('downtack', u"\u22A4", 'down tack'), # ⊤
        XK_upshoe: d('upshoe', u"\u2229", 'intersection'), # ∩
        XK_downstile: d('downstile', u"\u230A", 'left floor'), # ⌊
        XK_underbar: d('underbar', u"\u005F", 'low line'), # _
        XK_jot: d('jot', u"\u2218", 'ring operator'), # ∘
        XK_quad: d('quad', u"\u2395", 'apl functional symbol quad'), # ⎕
        XK_uptack: d('uptack', u"\u22A5", 'up tack'), # ⊥
        XK_circle: d('circle', u"\u25CB", 'white circle'), # ○
        XK_upstile: d('upstile', u"\u2308", 'left ceiling'), # ⌈
        XK_downshoe: d('downshoe', u"\u222A", 'union'), # ∪
        XK_rightshoe: d('rightshoe', u"\u2283", 'superset of'), # ⊃
        XK_leftshoe: d('leftshoe', u"\u2282", 'subset of'), # ⊂
        XK_lefttack: d('lefttack', u"\u22A3", 'left tack'), # ⊣
        XK_righttack: d('righttack', u"\u22A2", 'right tack'), # ⊢
    },


    #Hebrew
    #Byte 3 = 0x0c

    'hebrew': {
        XK_hebrew_doublelowline: d('hebrew_doublelowline', u"\u2017", 'double low line'), # ‗
        XK_hebrew_aleph: d('hebrew_aleph', u"\u05D0", 'hebrew letter alef'), # א
        XK_hebrew_bet: d('hebrew_bet', u"\u05D1", 'hebrew letter bet'), # ב
        XK_hebrew_gimel: d('hebrew_gimel', u"\u05D2", 'hebrew letter gimel'), # ג
        XK_hebrew_dalet: d('hebrew_dalet', u"\u05D3", 'hebrew letter dalet'), # ד
        XK_hebrew_he: d('hebrew_he', u"\u05D4", 'hebrew letter he'), # ה
        XK_hebrew_waw: d('hebrew_waw', u"\u05D5", 'hebrew letter vav'), # ו
        XK_hebrew_zain: d('hebrew_zain', u"\u05D6", 'hebrew letter zayin'), # ז
        XK_hebrew_chet: d('hebrew_chet', u"\u05D7", 'hebrew letter het'), # ח
        XK_hebrew_tet: d('hebrew_tet', u"\u05D8", 'hebrew letter tet'), # ט
        XK_hebrew_yod: d('hebrew_yod', u"\u05D9", 'hebrew letter yod'), # י
        XK_hebrew_finalkaph: d('hebrew_finalkaph', u"\u05DA", 'hebrew letter final kaf'), # ך
        XK_hebrew_kaph: d('hebrew_kaph', u"\u05DB", 'hebrew letter kaf'), # כ
        XK_hebrew_lamed: d('hebrew_lamed', u"\u05DC", 'hebrew letter lamed'), # ל
        XK_hebrew_finalmem: d('hebrew_finalmem', u"\u05DD", 'hebrew letter final mem'), # ם
        XK_hebrew_mem: d('hebrew_mem', u"\u05DE", 'hebrew letter mem'), # מ
        XK_hebrew_finalnun: d('hebrew_finalnun', u"\u05DF", 'hebrew letter final nun'), # ן
        XK_hebrew_nun: d('hebrew_nun', u"\u05E0", 'hebrew letter nun'), # נ
        XK_hebrew_samech: d('hebrew_samech', u"\u05E1", 'hebrew letter samekh'), # ס
        XK_hebrew_ayin: d('hebrew_ayin', u"\u05E2", 'hebrew letter ayin'), # ע
        XK_hebrew_finalpe: d('hebrew_finalpe', u"\u05E3", 'hebrew letter final pe'), # ף
        XK_hebrew_pe: d('hebrew_pe', u"\u05E4", 'hebrew letter pe'), # פ
        XK_hebrew_finalzade: d('hebrew_finalzade', u"\u05E5", 'hebrew letter final tsadi'), # ץ
        XK_hebrew_zade: d('hebrew_zade', u"\u05E6", 'hebrew letter tsadi'), # צ
        XK_hebrew_qoph: d('hebrew_qoph', u"\u05E7", 'hebrew letter qof'), # ק
        XK_hebrew_resh: d('hebrew_resh', u"\u05E8", 'hebrew letter resh'), # ר
        XK_hebrew_shin: d('hebrew_shin', u"\u05E9", 'hebrew letter shin'), # ש
        XK_hebrew_taw: d('hebrew_taw', u"\u05EA", 'hebrew letter tav'), # ת
        XK_Hebrew_switch: d('Hebrew_switch', '', 'alias for mode_switch'),
    },


    #Thai
    #Byte 3 = 0x0d

    'thai': {
        XK_Thai_kokai: d('Thai_kokai', u"\u0E01", 'thai character ko kai'), # ก
        XK_Thai_khokhai: d('Thai_khokhai', u"\u0E02", 'thai character kho khai'), # ข
        XK_Thai_khokhuat: d('Thai_khokhuat', u"\u0E03", 'thai character kho khuat'), # ฃ
        XK_Thai_khokhwai: d('Thai_khokhwai', u"\u0E04", 'thai character kho khwai'), # ค
        XK_Thai_khokhon: d('Thai_khokhon', u"\u0E05", 'thai character kho khon'), # ฅ
        XK_Thai_khorakhang: d('Thai_khorakhang', u"\u0E06", 'thai character kho rakhang'), # ฆ
        XK_Thai_ngongu: d('Thai_ngongu', u"\u0E07", 'thai character ngo ngu'), # ง
        XK_Thai_chochan: d('Thai_chochan', u"\u0E08", 'thai character cho chan'), # จ
        XK_Thai_choching: d('Thai_choching', u"\u0E09", 'thai character cho ching'), # ฉ
        XK_Thai_chochang: d('Thai_chochang', u"\u0E0A", 'thai character cho chang'), # ช
        XK_Thai_soso: d('Thai_soso', u"\u0E0B", 'thai character so so'), # ซ
        XK_Thai_chochoe: d('Thai_chochoe', u"\u0E0C", 'thai character cho choe'), # ฌ
        XK_Thai_yoying: d('Thai_yoying', u"\u0E0D", 'thai character yo ying'), # ญ
        XK_Thai_dochada: d('Thai_dochada', u"\u0E0E", 'thai character do chada'), # ฎ
        XK_Thai_topatak: d('Thai_topatak', u"\u0E0F", 'thai character to patak'), # ฏ
        XK_Thai_thothan: d('Thai_thothan', u"\u0E10", 'thai character tho than'), # ฐ
        XK_Thai_thonangmontho: d('Thai_thonangmontho', u"\u0E11", 'thai character tho nangmontho'), # ฑ
        XK_Thai_thophuthao: d('Thai_thophuthao', u"\u0E12", 'thai character tho phuthao'), # ฒ
        XK_Thai_nonen: d('Thai_nonen', u"\u0E13", 'thai character no nen'), # ณ
        XK_Thai_dodek: d('Thai_dodek', u"\u0E14", 'thai character do dek'), # ด
        XK_Thai_totao: d('Thai_totao', u"\u0E15", 'thai character to tao'), # ต
        XK_Thai_thothung: d('Thai_thothung', u"\u0E16", 'thai character tho thung'), # ถ
        XK_Thai_thothahan: d('Thai_thothahan', u"\u0E17", 'thai character tho thahan'), # ท
        XK_Thai_thothong: d('Thai_thothong', u"\u0E18", 'thai character tho thong'), # ธ
        XK_Thai_nonu: d('Thai_nonu', u"\u0E19", 'thai character no nu'), # น
        XK_Thai_bobaimai: d('Thai_bobaimai', u"\u0E1A", 'thai character bo baimai'), # บ
        XK_Thai_popla: d('Thai_popla', u"\u0E1B", 'thai character po pla'), # ป
        XK_Thai_phophung: d('Thai_phophung', u"\u0E1C", 'thai character pho phung'), # ผ
        XK_Thai_fofa: d('Thai_fofa', u"\u0E1D", 'thai character fo fa'), # ฝ
        XK_Thai_phophan: d('Thai_phophan', u"\u0E1E", 'thai character pho phan'), # พ
        XK_Thai_fofan: d('Thai_fofan', u"\u0E1F", 'thai character fo fan'), # ฟ
        XK_Thai_phosamphao: d('Thai_phosamphao', u"\u0E20", 'thai character pho samphao'), # ภ
        XK_Thai_moma: d('Thai_moma', u"\u0E21", 'thai character mo ma'), # ม
        XK_Thai_yoyak: d('Thai_yoyak', u"\u0E22", 'thai character yo yak'), # ย
        XK_Thai_rorua: d('Thai_rorua', u"\u0E23", 'thai character ro rua'), # ร
        XK_Thai_ru: d('Thai_ru', u"\u0E24", 'thai character ru'), # ฤ
        XK_Thai_loling: d('Thai_loling', u"\u0E25", 'thai character lo ling'), # ล
        XK_Thai_lu: d('Thai_lu', u"\u0E26", 'thai character lu'), # ฦ
        XK_Thai_wowaen: d('Thai_wowaen', u"\u0E27", 'thai character wo waen'), # ว
        XK_Thai_sosala: d('Thai_sosala', u"\u0E28", 'thai character so sala'), # ศ
        XK_Thai_sorusi: d('Thai_sorusi', u"\u0E29", 'thai character so rusi'), # ษ
        XK_Thai_sosua: d('Thai_sosua', u"\u0E2A", 'thai character so sua'), # ส
        XK_Thai_hohip: d('Thai_hohip', u"\u0E2B", 'thai character ho hip'), # ห
        XK_Thai_lochula: d('Thai_lochula', u"\u0E2C", 'thai character lo chula'), # ฬ
        XK_Thai_oang: d('Thai_oang', u"\u0E2D", 'thai character o ang'), # อ
        XK_Thai_honokhuk: d('Thai_honokhuk', u"\u0E2E", 'thai character ho nokhuk'), # ฮ
        XK_Thai_paiyannoi: d('Thai_paiyannoi', u"\u0E2F", 'thai character paiyannoi'), # ฯ
        XK_Thai_saraa: d('Thai_saraa', u"\u0E30", 'thai character sara a'), # ะ
        XK_Thai_maihanakat: d('Thai_maihanakat', u"\u0E31", 'thai character mai han-akat'), # ั
        XK_Thai_saraaa: d('Thai_saraaa', u"\u0E32", 'thai character sara aa'), # า
        XK_Thai_saraam: d('Thai_saraam', u"\u0E33", 'thai character sara am'), # ำ
        XK_Thai_sarai: d('Thai_sarai', u"\u0E34", 'thai character sara i'), # ิ
        XK_Thai_saraii: d('Thai_saraii', u"\u0E35", 'thai character sara ii'), # ี
        XK_Thai_saraue: d('Thai_saraue', u"\u0E36", 'thai character sara ue'), # ึ
        XK_Thai_sarauee: d('Thai_sarauee', u"\u0E37", 'thai character sara uee'), # ื
        XK_Thai_sarau: d('Thai_sarau', u"\u0E38", 'thai character sara u'), # ุ
        XK_Thai_sarauu: d('Thai_sarauu', u"\u0E39", 'thai character sara uu'), # ู
        XK_Thai_phinthu: d('Thai_phinthu', u"\u0E3A", 'thai character phinthu'), # ฺ
        XK_Thai_maihanakat_maitho: d('Thai_maihanakat_maitho', '', ''),
        XK_Thai_baht: d('Thai_baht', u"\u0E3F", 'thai currency symbol baht'), # ฿
        XK_Thai_sarae: d('Thai_sarae', u"\u0E40", 'thai character sara e'), # เ
        XK_Thai_saraae: d('Thai_saraae', u"\u0E41", 'thai character sara ae'), # แ
        XK_Thai_sarao: d('Thai_sarao', u"\u0E42", 'thai character sara o'), # โ
        XK_Thai_saraaimaimuan: d('Thai_saraaimaimuan', u"\u0E43", 'thai character sara ai maimuan'), # ใ
        XK_Thai_saraaimaimalai: d('Thai_saraaimaimalai', u"\u0E44", 'thai character sara ai maimalai'), # ไ
        XK_Thai_lakkhangyao: d('Thai_lakkhangyao', u"\u0E45", 'thai character lakkhangyao'), # ๅ
        XK_Thai_maiyamok: d('Thai_maiyamok', u"\u0E46", 'thai character maiyamok'), # ๆ
        XK_Thai_maitaikhu: d('Thai_maitaikhu', u"\u0E47", 'thai character maitaikhu'), # ็
        XK_Thai_maiek: d('Thai_maiek', u"\u0E48", 'thai character mai ek'), # ่
        XK_Thai_maitho: d('Thai_maitho', u"\u0E49", 'thai character mai tho'), # ้
        XK_Thai_maitri: d('Thai_maitri', u"\u0E4A", 'thai character mai tri'), # ๊
        XK_Thai_maichattawa: d('Thai_maichattawa', u"\u0E4B", 'thai character mai chattawa'), # ๋
        XK_Thai_thanthakhat: d('Thai_thanthakhat', u"\u0E4C", 'thai character thanthakhat'), # ์
        XK_Thai_nikhahit: d('Thai_nikhahit', u"\u0E4D", 'thai character nikhahit'), # ํ
        XK_Thai_leksun: d('Thai_leksun', u"\u0E50", 'thai digit zero'), # ๐
        XK_Thai_leknung: d('Thai_leknung', u"\u0E51", 'thai digit one'), # ๑
        XK_Thai_leksong: d('Thai_leksong', u"\u0E52", 'thai digit two'), # ๒
        XK_Thai_leksam: d('Thai_leksam', u"\u0E53", 'thai digit three'), # ๓
        XK_Thai_leksi: d('Thai_leksi', u"\u0E54", 'thai digit four'), # ๔
        XK_Thai_lekha: d('Thai_lekha', u"\u0E55", 'thai digit five'), # ๕
        XK_Thai_lekhok: d('Thai_lekhok', u"\u0E56", 'thai digit six'), # ๖
        XK_Thai_lekchet: d('Thai_lekchet', u"\u0E57", 'thai digit seven'), # ๗
        XK_Thai_lekpaet: d('Thai_lekpaet', u"\u0E58", 'thai digit eight'), # ๘
        XK_Thai_lekkao: d('Thai_lekkao', u"\u0E59", 'thai digit nine'), # ๙
    },


    #Korean
    #Byte 3 = 0x0e

    'korean': {

        XK_Hangul: d('Hangul', '', 'hangul start/stop(toggle)'),
        XK_Hangul_Start: d('Hangul_Start', '', 'hangul start'),
        XK_Hangul_End: d('Hangul_End', '', 'hangul end, english start'),
        XK_Hangul_Hanja: d('Hangul_Hanja', '', 'start hangul->hanja conversion'),
        XK_Hangul_Jamo: d('Hangul_Jamo', '', 'hangul jamo mode'),
        XK_Hangul_Romaja: d('Hangul_Romaja', '', 'hangul romaja mode'),
        XK_Hangul_Codeinput: d('Hangul_Codeinput', '', 'hangul code input mode'),
        XK_Hangul_Jeonja: d('Hangul_Jeonja', '', 'jeonja mode'),
        XK_Hangul_Banja: d('Hangul_Banja', '', 'banja mode'),
        XK_Hangul_PreHanja: d('Hangul_PreHanja', '', 'pre hanja conversion'),
        XK_Hangul_PostHanja: d('Hangul_PostHanja', '', 'post hanja conversion'),
        XK_Hangul_SingleCandidate: d('Hangul_SingleCandidate', '', 'single candidate'),
        XK_Hangul_MultipleCandidate: d('Hangul_MultipleCandidate', '', 'multiple candidate'),
        XK_Hangul_PreviousCandidate: d('Hangul_PreviousCandidate', '', 'previous candidate'),
        XK_Hangul_Special: d('Hangul_Special', '', 'special symbols'),
        XK_Hangul_switch: d('Hangul_switch', '', 'alias for mode_switch'),

        #Hangul  Consonant  Characters
        XK_Hangul_Kiyeog: d('Hangul_Kiyeog', '', ''),
        XK_Hangul_SsangKiyeog: d('Hangul_SsangKiyeog', '', ''),
        XK_Hangul_KiyeogSios: d('Hangul_KiyeogSios', '', ''),
        XK_Hangul_Nieun: d('Hangul_Nieun', '', ''),
        XK_Hangul_NieunJieuj: d('Hangul_NieunJieuj', '', ''),
        XK_Hangul_NieunHieuh: d('Hangul_NieunHieuh', '', ''),
        XK_Hangul_Dikeud: d('Hangul_Dikeud', '', ''),
        XK_Hangul_SsangDikeud: d('Hangul_SsangDikeud', '', ''),
        XK_Hangul_Rieul: d('Hangul_Rieul', '', ''),
        XK_Hangul_RieulKiyeog: d('Hangul_RieulKiyeog', '', ''),
        XK_Hangul_RieulMieum: d('Hangul_RieulMieum', '', ''),
        XK_Hangul_RieulPieub: d('Hangul_RieulPieub', '', ''),
        XK_Hangul_RieulSios: d('Hangul_RieulSios', '', ''),
        XK_Hangul_RieulTieut: d('Hangul_RieulTieut', '', ''),
        XK_Hangul_RieulPhieuf: d('Hangul_RieulPhieuf', '', ''),
        XK_Hangul_RieulHieuh: d('Hangul_RieulHieuh', '', ''),
        XK_Hangul_Mieum: d('Hangul_Mieum', '', ''),
        XK_Hangul_Pieub: d('Hangul_Pieub', '', ''),
        XK_Hangul_SsangPieub: d('Hangul_SsangPieub', '', ''),
        XK_Hangul_PieubSios: d('Hangul_PieubSios', '', ''),
        XK_Hangul_Sios: d('Hangul_Sios', '', ''),
        XK_Hangul_SsangSios: d('Hangul_SsangSios', '', ''),
        XK_Hangul_Ieung: d('Hangul_Ieung', '', ''),
        XK_Hangul_Jieuj: d('Hangul_Jieuj', '', ''),
        XK_Hangul_SsangJieuj: d('Hangul_SsangJieuj', '', ''),
        XK_Hangul_Cieuc: d('Hangul_Cieuc', '', ''),
        XK_Hangul_Khieuq: d('Hangul_Khieuq', '', ''),
        XK_Hangul_Tieut: d('Hangul_Tieut', '', ''),
        XK_Hangul_Phieuf: d('Hangul_Phieuf', '', ''),
        XK_Hangul_Hieuh: d('Hangul_Hieuh', '', ''),

        #Hangul  Vowel  Characters
        XK_Hangul_A: d('Hangul_A', '', ''),
        XK_Hangul_AE: d('Hangul_AE', '', ''),
        XK_Hangul_YA: d('Hangul_YA', '', ''),
        XK_Hangul_YAE: d('Hangul_YAE', '', ''),
        XK_Hangul_EO: d('Hangul_EO', '', ''),
        XK_Hangul_E: d('Hangul_E', '', ''),
        XK_Hangul_YEO: d('Hangul_YEO', '', ''),
        XK_Hangul_YE: d('Hangul_YE', '', ''),
        XK_Hangul_O: d('Hangul_O', '', ''),
        XK_Hangul_WA: d('Hangul_WA', '', ''),
        XK_Hangul_WAE: d('Hangul_WAE', '', ''),
        XK_Hangul_OE: d('Hangul_OE', '', ''),
        XK_Hangul_YO: d('Hangul_YO', '', ''),
        XK_Hangul_U: d('Hangul_U', '', ''),
        XK_Hangul_WEO: d('Hangul_WEO', '', ''),
        XK_Hangul_WE: d('Hangul_WE', '', ''),
        XK_Hangul_WI: d('Hangul_WI', '', ''),
        XK_Hangul_YU: d('Hangul_YU', '', ''),
        XK_Hangul_EU: d('Hangul_EU', '', ''),
        XK_Hangul_YI: d('Hangul_YI', '', ''),
        XK_Hangul_I: d('Hangul_I', '', ''),

        #Hangul  syllable-final  (JongSeong)  Characters
        XK_Hangul_J_Kiyeog: d('Hangul_J_Kiyeog', '', ''),
        XK_Hangul_J_SsangKiyeog: d('Hangul_J_SsangKiyeog', '', ''),
        XK_Hangul_J_KiyeogSios: d('Hangul_J_KiyeogSios', '', ''),
        XK_Hangul_J_Nieun: d('Hangul_J_Nieun', '', ''),
        XK_Hangul_J_NieunJieuj: d('Hangul_J_NieunJieuj', '', ''),
        XK_Hangul_J_NieunHieuh: d('Hangul_J_NieunHieuh', '', ''),
        XK_Hangul_J_Dikeud: d('Hangul_J_Dikeud', '', ''),
        XK_Hangul_J_Rieul: d('Hangul_J_Rieul', '', ''),
        XK_Hangul_J_RieulKiyeog: d('Hangul_J_RieulKiyeog', '', ''),
        XK_Hangul_J_RieulMieum: d('Hangul_J_RieulMieum', '', ''),
        XK_Hangul_J_RieulPieub: d('Hangul_J_RieulPieub', '', ''),
        XK_Hangul_J_RieulSios: d('Hangul_J_RieulSios', '', ''),
        XK_Hangul_J_RieulTieut: d('Hangul_J_RieulTieut', '', ''),
        XK_Hangul_J_RieulPhieuf: d('Hangul_J_RieulPhieuf', '', ''),
        XK_Hangul_J_RieulHieuh: d('Hangul_J_RieulHieuh', '', ''),
        XK_Hangul_J_Mieum: d('Hangul_J_Mieum', '', ''),
        XK_Hangul_J_Pieub: d('Hangul_J_Pieub', '', ''),
        XK_Hangul_J_PieubSios: d('Hangul_J_PieubSios', '', ''),
        XK_Hangul_J_Sios: d('Hangul_J_Sios', '', ''),
        XK_Hangul_J_SsangSios: d('Hangul_J_SsangSios', '', ''),
        XK_Hangul_J_Ieung: d('Hangul_J_Ieung', '', ''),
        XK_Hangul_J_Jieuj: d('Hangul_J_Jieuj', '', ''),
        XK_Hangul_J_Cieuc: d('Hangul_J_Cieuc', '', ''),
        XK_Hangul_J_Khieuq: d('Hangul_J_Khieuq', '', ''),
        XK_Hangul_J_Tieut: d('Hangul_J_Tieut', '', ''),
        XK_Hangul_J_Phieuf: d('Hangul_J_Phieuf', '', ''),
        XK_Hangul_J_Hieuh: d('Hangul_J_Hieuh', '', ''),

        #Ancient  Hangul  Consonant  Characters
        XK_Hangul_RieulYeorinHieuh: d('Hangul_RieulYeorinHieuh', '', ''),
        XK_Hangul_SunkyeongeumMieum: d('Hangul_SunkyeongeumMieum', '', ''),
        XK_Hangul_SunkyeongeumPieub: d('Hangul_SunkyeongeumPieub', '', ''),
        XK_Hangul_PanSios: d('Hangul_PanSios', '', ''),
        XK_Hangul_KkogjiDalrinIeung: d('Hangul_KkogjiDalrinIeung', '', ''),
        XK_Hangul_SunkyeongeumPhieuf: d('Hangul_SunkyeongeumPhieuf', '', ''),
        XK_Hangul_YeorinHieuh: d('Hangul_YeorinHieuh', '', ''),

        #Ancient  Hangul  Vowel  Characters
        XK_Hangul_AraeA: d('Hangul_AraeA', '', ''),
        XK_Hangul_AraeAE: d('Hangul_AraeAE', '', ''),

        #Ancient  Hangul  syllable-final  (JongSeong)  Characters
        XK_Hangul_J_PanSios: d('Hangul_J_PanSios', '', ''),
        XK_Hangul_J_KkogjiDalrinIeung: d('Hangul_J_KkogjiDalrinIeung', '', ''),
        XK_Hangul_J_YeorinHieuh: d('Hangul_J_YeorinHieuh', '', ''),

        #Korean  currency  symbol
        XK_Korean_Won: d('Korean_Won', u"\u20A9", 'won sign'), # ₩

    },


    #Armenian

    'armenian': {
        XK_Armenian_ligature_ew: d('Armenian_ligature_ew', u"\u0587", 'armenian small ligature ech yiwn'), # և
        XK_Armenian_full_stop: d('Armenian_full_stop', u"\u0589", 'armenian full stop'), # ։
        XK_Armenian_verjaket: d('Armenian_verjaket', u"\u0589", 'armenian full stop'), # ։
        XK_Armenian_separation_mark: d('Armenian_separation_mark', u"\u055D", 'armenian comma'), # ՝
        XK_Armenian_but: d('Armenian_but', u"\u055D", 'armenian comma'), # ՝
        XK_Armenian_hyphen: d('Armenian_hyphen', u"\u058A", 'armenian hyphen'), # ֊
        XK_Armenian_yentamna: d('Armenian_yentamna', u"\u058A", 'armenian hyphen'), # ֊
        XK_Armenian_exclam: d('Armenian_exclam', u"\u055C", 'armenian exclamation mark'), # ՜
        XK_Armenian_amanak: d('Armenian_amanak', u"\u055C", 'armenian exclamation mark'), # ՜
        XK_Armenian_accent: d('Armenian_accent', u"\u055B", 'armenian emphasis mark'), # ՛
        XK_Armenian_shesht: d('Armenian_shesht', u"\u055B", 'armenian emphasis mark'), # ՛
        XK_Armenian_question: d('Armenian_question', u"\u055E", 'armenian question mark'), # ՞
        XK_Armenian_paruyk: d('Armenian_paruyk', u"\u055E", 'armenian question mark'), # ՞
        XK_Armenian_AYB: d('Armenian_AYB', u"\u0531", 'armenian capital letter ayb'), # Ա
        XK_Armenian_ayb: d('Armenian_ayb', u"\u0561", 'armenian small letter ayb'), # ա
        XK_Armenian_BEN: d('Armenian_BEN', u"\u0532", 'armenian capital letter ben'), # Բ
        XK_Armenian_ben: d('Armenian_ben', u"\u0562", 'armenian small letter ben'), # բ
        XK_Armenian_GIM: d('Armenian_GIM', u"\u0533", 'armenian capital letter gim'), # Գ
        XK_Armenian_gim: d('Armenian_gim', u"\u0563", 'armenian small letter gim'), # գ
        XK_Armenian_DA: d('Armenian_DA', u"\u0534", 'armenian capital letter da'), # Դ
        XK_Armenian_da: d('Armenian_da', u"\u0564", 'armenian small letter da'), # դ
        XK_Armenian_YECH: d('Armenian_YECH', u"\u0535", 'armenian capital letter ech'), # Ե
        XK_Armenian_yech: d('Armenian_yech', u"\u0565", 'armenian small letter ech'), # ե
        XK_Armenian_ZA: d('Armenian_ZA', u"\u0536", 'armenian capital letter za'), # Զ
        XK_Armenian_za: d('Armenian_za', u"\u0566", 'armenian small letter za'), # զ
        XK_Armenian_E: d('Armenian_E', u"\u0537", 'armenian capital letter eh'), # Է
        XK_Armenian_e: d('Armenian_e', u"\u0567", 'armenian small letter eh'), # է
        XK_Armenian_AT: d('Armenian_AT', u"\u0538", 'armenian capital letter et'), # Ը
        XK_Armenian_at: d('Armenian_at', u"\u0568", 'armenian small letter et'), # ը
        XK_Armenian_TO: d('Armenian_TO', u"\u0539", 'armenian capital letter to'), # Թ
        XK_Armenian_to: d('Armenian_to', u"\u0569", 'armenian small letter to'), # թ
        XK_Armenian_ZHE: d('Armenian_ZHE', u"\u053A", 'armenian capital letter zhe'), # Ժ
        XK_Armenian_zhe: d('Armenian_zhe', u"\u056A", 'armenian small letter zhe'), # ժ
        XK_Armenian_INI: d('Armenian_INI', u"\u053B", 'armenian capital letter ini'), # Ի
        XK_Armenian_ini: d('Armenian_ini', u"\u056B", 'armenian small letter ini'), # ի
        XK_Armenian_LYUN: d('Armenian_LYUN', u"\u053C", 'armenian capital letter liwn'), # Լ
        XK_Armenian_lyun: d('Armenian_lyun', u"\u056C", 'armenian small letter liwn'), # լ
        XK_Armenian_KHE: d('Armenian_KHE', u"\u053D", 'armenian capital letter xeh'), # Խ
        XK_Armenian_khe: d('Armenian_khe', u"\u056D", 'armenian small letter xeh'), # խ
        XK_Armenian_TSA: d('Armenian_TSA', u"\u053E", 'armenian capital letter ca'), # Ծ
        XK_Armenian_tsa: d('Armenian_tsa', u"\u056E", 'armenian small letter ca'), # ծ
        XK_Armenian_KEN: d('Armenian_KEN', u"\u053F", 'armenian capital letter ken'), # Կ
        XK_Armenian_ken: d('Armenian_ken', u"\u056F", 'armenian small letter ken'), # կ
        XK_Armenian_HO: d('Armenian_HO', u"\u0540", 'armenian capital letter ho'), # Հ
        XK_Armenian_ho: d('Armenian_ho', u"\u0570", 'armenian small letter ho'), # հ
        XK_Armenian_DZA: d('Armenian_DZA', u"\u0541", 'armenian capital letter ja'), # Ձ
        XK_Armenian_dza: d('Armenian_dza', u"\u0571", 'armenian small letter ja'), # ձ
        XK_Armenian_GHAT: d('Armenian_GHAT', u"\u0542", 'armenian capital letter ghad'), # Ղ
        XK_Armenian_ghat: d('Armenian_ghat', u"\u0572", 'armenian small letter ghad'), # ղ
        XK_Armenian_TCHE: d('Armenian_TCHE', u"\u0543", 'armenian capital letter cheh'), # Ճ
        XK_Armenian_tche: d('Armenian_tche', u"\u0573", 'armenian small letter cheh'), # ճ
        XK_Armenian_MEN: d('Armenian_MEN', u"\u0544", 'armenian capital letter men'), # Մ
        XK_Armenian_men: d('Armenian_men', u"\u0574", 'armenian small letter men'), # մ
        XK_Armenian_HI: d('Armenian_HI', u"\u0545", 'armenian capital letter yi'), # Յ
        XK_Armenian_hi: d('Armenian_hi', u"\u0575", 'armenian small letter yi'), # յ
        XK_Armenian_NU: d('Armenian_NU', u"\u0546", 'armenian capital letter now'), # Ն
        XK_Armenian_nu: d('Armenian_nu', u"\u0576", 'armenian small letter now'), # ն
        XK_Armenian_SHA: d('Armenian_SHA', u"\u0547", 'armenian capital letter sha'), # Շ
        XK_Armenian_sha: d('Armenian_sha', u"\u0577", 'armenian small letter sha'), # շ
        XK_Armenian_VO: d('Armenian_VO', u"\u0548", 'armenian capital letter vo'), # Ո
        XK_Armenian_vo: d('Armenian_vo', u"\u0578", 'armenian small letter vo'), # ո
        XK_Armenian_CHA: d('Armenian_CHA', u"\u0549", 'armenian capital letter cha'), # Չ
        XK_Armenian_cha: d('Armenian_cha', u"\u0579", 'armenian small letter cha'), # չ
        XK_Armenian_PE: d('Armenian_PE', u"\u054A", 'armenian capital letter peh'), # Պ
        XK_Armenian_pe: d('Armenian_pe', u"\u057A", 'armenian small letter peh'), # պ
        XK_Armenian_JE: d('Armenian_JE', u"\u054B", 'armenian capital letter jheh'), # Ջ
        XK_Armenian_je: d('Armenian_je', u"\u057B", 'armenian small letter jheh'), # ջ
        XK_Armenian_RA: d('Armenian_RA', u"\u054C", 'armenian capital letter ra'), # Ռ
        XK_Armenian_ra: d('Armenian_ra', u"\u057C", 'armenian small letter ra'), # ռ
        XK_Armenian_SE: d('Armenian_SE', u"\u054D", 'armenian capital letter seh'), # Ս
        XK_Armenian_se: d('Armenian_se', u"\u057D", 'armenian small letter seh'), # ս
        XK_Armenian_VEV: d('Armenian_VEV', u"\u054E", 'armenian capital letter vew'), # Վ
        XK_Armenian_vev: d('Armenian_vev', u"\u057E", 'armenian small letter vew'), # վ
        XK_Armenian_TYUN: d('Armenian_TYUN', u"\u054F", 'armenian capital letter tiwn'), # Տ
        XK_Armenian_tyun: d('Armenian_tyun', u"\u057F", 'armenian small letter tiwn'), # տ
        XK_Armenian_RE: d('Armenian_RE', u"\u0550", 'armenian capital letter reh'), # Ր
        XK_Armenian_re: d('Armenian_re', u"\u0580", 'armenian small letter reh'), # ր
        XK_Armenian_TSO: d('Armenian_TSO', u"\u0551", 'armenian capital letter co'), # Ց
        XK_Armenian_tso: d('Armenian_tso', u"\u0581", 'armenian small letter co'), # ց
        XK_Armenian_VYUN: d('Armenian_VYUN', u"\u0552", 'armenian capital letter yiwn'), # Ւ
        XK_Armenian_vyun: d('Armenian_vyun', u"\u0582", 'armenian small letter yiwn'), # ւ
        XK_Armenian_PYUR: d('Armenian_PYUR', u"\u0553", 'armenian capital letter piwr'), # Փ
        XK_Armenian_pyur: d('Armenian_pyur', u"\u0583", 'armenian small letter piwr'), # փ
        XK_Armenian_KE: d('Armenian_KE', u"\u0554", 'armenian capital letter keh'), # Ք
        XK_Armenian_ke: d('Armenian_ke', u"\u0584", 'armenian small letter keh'), # ք
        XK_Armenian_O: d('Armenian_O', u"\u0555", 'armenian capital letter oh'), # Օ
        XK_Armenian_o: d('Armenian_o', u"\u0585", 'armenian small letter oh'), # օ
        XK_Armenian_FE: d('Armenian_FE', u"\u0556", 'armenian capital letter feh'), # Ֆ
        XK_Armenian_fe: d('Armenian_fe', u"\u0586", 'armenian small letter feh'), # ֆ
        XK_Armenian_apostrophe: d('Armenian_apostrophe', u"\u055A", 'armenian apostrophe'), # ՚
    },


    #Georgian

    'georgian': {
        XK_Georgian_an: d('Georgian_an', u"\u10D0", 'georgian letter an'), # ა
        XK_Georgian_ban: d('Georgian_ban', u"\u10D1", 'georgian letter ban'), # ბ
        XK_Georgian_gan: d('Georgian_gan', u"\u10D2", 'georgian letter gan'), # გ
        XK_Georgian_don: d('Georgian_don', u"\u10D3", 'georgian letter don'), # დ
        XK_Georgian_en: d('Georgian_en', u"\u10D4", 'georgian letter en'), # ე
        XK_Georgian_vin: d('Georgian_vin', u"\u10D5", 'georgian letter vin'), # ვ
        XK_Georgian_zen: d('Georgian_zen', u"\u10D6", 'georgian letter zen'), # ზ
        XK_Georgian_tan: d('Georgian_tan', u"\u10D7", 'georgian letter tan'), # თ
        XK_Georgian_in: d('Georgian_in', u"\u10D8", 'georgian letter in'), # ი
        XK_Georgian_kan: d('Georgian_kan', u"\u10D9", 'georgian letter kan'), # კ
        XK_Georgian_las: d('Georgian_las', u"\u10DA", 'georgian letter las'), # ლ
        XK_Georgian_man: d('Georgian_man', u"\u10DB", 'georgian letter man'), # მ
        XK_Georgian_nar: d('Georgian_nar', u"\u10DC", 'georgian letter nar'), # ნ
        XK_Georgian_on: d('Georgian_on', u"\u10DD", 'georgian letter on'), # ო
        XK_Georgian_par: d('Georgian_par', u"\u10DE", 'georgian letter par'), # პ
        XK_Georgian_zhar: d('Georgian_zhar', u"\u10DF", 'georgian letter zhar'), # ჟ
        XK_Georgian_rae: d('Georgian_rae', u"\u10E0", 'georgian letter rae'), # რ
        XK_Georgian_san: d('Georgian_san', u"\u10E1", 'georgian letter san'), # ს
        XK_Georgian_tar: d('Georgian_tar', u"\u10E2", 'georgian letter tar'), # ტ
        XK_Georgian_un: d('Georgian_un', u"\u10E3", 'georgian letter un'), # უ
        XK_Georgian_phar: d('Georgian_phar', u"\u10E4", 'georgian letter phar'), # ფ
        XK_Georgian_khar: d('Georgian_khar', u"\u10E5", 'georgian letter khar'), # ქ
        XK_Georgian_ghan: d('Georgian_ghan', u"\u10E6", 'georgian letter ghan'), # ღ
        XK_Georgian_qar: d('Georgian_qar', u"\u10E7", 'georgian letter qar'), # ყ
        XK_Georgian_shin: d('Georgian_shin', u"\u10E8", 'georgian letter shin'), # შ
        XK_Georgian_chin: d('Georgian_chin', u"\u10E9", 'georgian letter chin'), # ჩ
        XK_Georgian_can: d('Georgian_can', u"\u10EA", 'georgian letter can'), # ც
        XK_Georgian_jil: d('Georgian_jil', u"\u10EB", 'georgian letter jil'), # ძ
        XK_Georgian_cil: d('Georgian_cil', u"\u10EC", 'georgian letter cil'), # წ
        XK_Georgian_char: d('Georgian_char', u"\u10ED", 'georgian letter char'), # ჭ
        XK_Georgian_xan: d('Georgian_xan', u"\u10EE", 'georgian letter xan'), # ხ
        XK_Georgian_jhan: d('Georgian_jhan', u"\u10EF", 'georgian letter jhan'), # ჯ
        XK_Georgian_hae: d('Georgian_hae', u"\u10F0", 'georgian letter hae'), # ჰ
        XK_Georgian_he: d('Georgian_he', u"\u10F1", 'georgian letter he'), # ჱ
        XK_Georgian_hie: d('Georgian_hie', u"\u10F2", 'georgian letter hie'), # ჲ
        XK_Georgian_we: d('Georgian_we', u"\u10F3", 'georgian letter we'), # ჳ
        XK_Georgian_har: d('Georgian_har', u"\u10F4", 'georgian letter har'), # ჴ
        XK_Georgian_hoe: d('Georgian_hoe', u"\u10F5", 'georgian letter hoe'), # ჵ
        XK_Georgian_fi: d('Georgian_fi', u"\u10F6", 'georgian letter fi'), # ჶ
    },


    #Azeri (and other Turkic or Caucasian languages)

    'caucasus': {
        #latin
        XK_Xabovedot: d('Xabovedot', u"\u1E8A", 'latin capital letter x with dot above'), # Ẋ
        XK_Ibreve: d('Ibreve', u"\u012C", 'latin capital letter i with breve'), # Ĭ
        XK_Zstroke: d('Zstroke', u"\u01B5", 'latin capital letter z with stroke'), # Ƶ
        XK_Gcaron: d('Gcaron', u"\u01E6", 'latin capital letter g with caron'), # Ǧ
        XK_Ocaron: d('Ocaron', u"\u01D2", 'latin capital letter o with caron'), # ǒ
        XK_Obarred: d('Obarred', u"\u019F", 'latin capital letter o with middle tilde'), # Ɵ
        XK_xabovedot: d('xabovedot', u"\u1E8B", 'latin small letter x with dot above'), # ẋ
        XK_ibreve: d('ibreve', u"\u012D", 'latin small letter i with breve'), # ĭ
        XK_zstroke: d('zstroke', u"\u01B6", 'latin small letter z with stroke'), # ƶ
        XK_gcaron: d('gcaron', u"\u01E7", 'latin small letter g with caron'), # ǧ
        XK_ocaron: d('ocaron', u"\u01D2", 'latin small letter o with caron'), # ǒ
        XK_obarred: d('obarred', u"\u0275", 'latin small letter barred o'), # ɵ
        XK_SCHWA: d('SCHWA', u"\u018F", 'latin capital letter schwa'), # Ə
        XK_schwa: d('schwa', u"\u0259", 'latin small letter schwa'), # ə
        #those  are  not  really  Caucasus
        #For  Inupiak
        XK_Lbelowdot: d('Lbelowdot', u"\u1E36", 'latin capital letter l with dot below'), # Ḷ
        XK_lbelowdot: d('lbelowdot', u"\u1E37", 'latin small letter l with dot below'), # ḷ
    },


    #Vietnamese

    'vietnamese': {
        XK_Abelowdot: d('Abelowdot', u"\u1EA0", 'latin capital letter a with dot below'), # Ạ
        XK_abelowdot: d('abelowdot', u"\u1EA1", 'latin small letter a with dot below'), # ạ
        XK_Ahook: d('Ahook', u"\u1EA2", 'latin capital letter a with hook above'), # Ả
        XK_ahook: d('ahook', u"\u1EA3", 'latin small letter a with hook above'), # ả
        XK_Acircumflexacute: d('Acircumflexacute', u"\u1EA4", 'latin capital letter a with circumflex and acute'), # Ấ
        XK_acircumflexacute: d('acircumflexacute', u"\u1EA5", 'latin small letter a with circumflex and acute'), # ấ
        XK_Acircumflexgrave: d('Acircumflexgrave', u"\u1EA6", 'latin capital letter a with circumflex and grave'), # Ầ
        XK_acircumflexgrave: d('acircumflexgrave', u"\u1EA7", 'latin small letter a with circumflex and grave'), # ầ
        XK_Acircumflexhook: d('Acircumflexhook', u"\u1EA8", 'latin capital letter a with circumflex and hook above'), # Ẩ
        XK_acircumflexhook: d('acircumflexhook', u"\u1EA9", 'latin small letter a with circumflex and hook above'), # ẩ
        XK_Acircumflextilde: d('Acircumflextilde', u"\u1EAA", 'latin capital letter a with circumflex and tilde'), # Ẫ
        XK_acircumflextilde: d('acircumflextilde', u"\u1EAB", 'latin small letter a with circumflex and tilde'), # ẫ
        XK_Acircumflexbelowdot: d('Acircumflexbelowdot', u"\u1EAC", 'latin capital letter a with circumflex and dot below'), # Ậ
        XK_acircumflexbelowdot: d('acircumflexbelowdot', u"\u1EAD", 'latin small letter a with circumflex and dot below'), # ậ
        XK_Abreveacute: d('Abreveacute', u"\u1EAE", 'latin capital letter a with breve and acute'), # Ắ
        XK_abreveacute: d('abreveacute', u"\u1EAF", 'latin small letter a with breve and acute'), # ắ
        XK_Abrevegrave: d('Abrevegrave', u"\u1EB0", 'latin capital letter a with breve and grave'), # Ằ
        XK_abrevegrave: d('abrevegrave', u"\u1EB1", 'latin small letter a with breve and grave'), # ằ
        XK_Abrevehook: d('Abrevehook', u"\u1EB2", 'latin capital letter a with breve and hook above'), # Ẳ
        XK_abrevehook: d('abrevehook', u"\u1EB3", 'latin small letter a with breve and hook above'), # ẳ
        XK_Abrevetilde: d('Abrevetilde', u"\u1EB4", 'latin capital letter a with breve and tilde'), # Ẵ
        XK_abrevetilde: d('abrevetilde', u"\u1EB5", 'latin small letter a with breve and tilde'), # ẵ
        XK_Abrevebelowdot: d('Abrevebelowdot', u"\u1EB6", 'latin capital letter a with breve and dot below'), # Ặ
        XK_abrevebelowdot: d('abrevebelowdot', u"\u1EB7", 'latin small letter a with breve and dot below'), # ặ
        XK_Ebelowdot: d('Ebelowdot', u"\u1EB8", 'latin capital letter e with dot below'), # Ẹ
        XK_ebelowdot: d('ebelowdot', u"\u1EB9", 'latin small letter e with dot below'), # ẹ
        XK_Ehook: d('Ehook', u"\u1EBA", 'latin capital letter e with hook above'), # Ẻ
        XK_ehook: d('ehook', u"\u1EBB", 'latin small letter e with hook above'), # ẻ
        XK_Etilde: d('Etilde', u"\u1EBC", 'latin capital letter e with tilde'), # Ẽ
        XK_etilde: d('etilde', u"\u1EBD", 'latin small letter e with tilde'), # ẽ
        XK_Ecircumflexacute: d('Ecircumflexacute', u"\u1EBE", 'latin capital letter e with circumflex and acute'), # Ế
        XK_ecircumflexacute: d('ecircumflexacute', u"\u1EBF", 'latin small letter e with circumflex and acute'), # ế
        XK_Ecircumflexgrave: d('Ecircumflexgrave', u"\u1EC0", 'latin capital letter e with circumflex and grave'), # Ề
        XK_ecircumflexgrave: d('ecircumflexgrave', u"\u1EC1", 'latin small letter e with circumflex and grave'), # ề
        XK_Ecircumflexhook: d('Ecircumflexhook', u"\u1EC2", 'latin capital letter e with circumflex and hook above'), # Ể
        XK_ecircumflexhook: d('ecircumflexhook', u"\u1EC3", 'latin small letter e with circumflex and hook above'), # ể
        XK_Ecircumflextilde: d('Ecircumflextilde', u"\u1EC4", 'latin capital letter e with circumflex and tilde'), # Ễ
        XK_ecircumflextilde: d('ecircumflextilde', u"\u1EC5", 'latin small letter e with circumflex and tilde'), # ễ
        XK_Ecircumflexbelowdot: d('Ecircumflexbelowdot', u"\u1EC6", 'latin capital letter e with circumflex and dot below'), # Ệ
        XK_ecircumflexbelowdot: d('ecircumflexbelowdot', u"\u1EC7", 'latin small letter e with circumflex and dot below'), # ệ
        XK_Ihook: d('Ihook', u"\u1EC8", 'latin capital letter i with hook above'), # Ỉ
        XK_ihook: d('ihook', u"\u1EC9", 'latin small letter i with hook above'), # ỉ
        XK_Ibelowdot: d('Ibelowdot', u"\u1ECA", 'latin capital letter i with dot below'), # Ị
        XK_ibelowdot: d('ibelowdot', u"\u1ECB", 'latin small letter i with dot below'), # ị
        XK_Obelowdot: d('Obelowdot', u"\u1ECC", 'latin capital letter o with dot below'), # Ọ
        XK_obelowdot: d('obelowdot', u"\u1ECD", 'latin small letter o with dot below'), # ọ
        XK_Ohook: d('Ohook', u"\u1ECE", 'latin capital letter o with hook above'), # Ỏ
        XK_ohook: d('ohook', u"\u1ECF", 'latin small letter o with hook above'), # ỏ
        XK_Ocircumflexacute: d('Ocircumflexacute', u"\u1ED0", 'latin capital letter o with circumflex and acute'), # Ố
        XK_ocircumflexacute: d('ocircumflexacute', u"\u1ED1", 'latin small letter o with circumflex and acute'), # ố
        XK_Ocircumflexgrave: d('Ocircumflexgrave', u"\u1ED2", 'latin capital letter o with circumflex and grave'), # Ồ
        XK_ocircumflexgrave: d('ocircumflexgrave', u"\u1ED3", 'latin small letter o with circumflex and grave'), # ồ
        XK_Ocircumflexhook: d('Ocircumflexhook', u"\u1ED4", 'latin capital letter o with circumflex and hook above'), # Ổ
        XK_ocircumflexhook: d('ocircumflexhook', u"\u1ED5", 'latin small letter o with circumflex and hook above'), # ổ
        XK_Ocircumflextilde: d('Ocircumflextilde', u"\u1ED6", 'latin capital letter o with circumflex and tilde'), # Ỗ
        XK_ocircumflextilde: d('ocircumflextilde', u"\u1ED7", 'latin small letter o with circumflex and tilde'), # ỗ
        XK_Ocircumflexbelowdot: d('Ocircumflexbelowdot', u"\u1ED8", 'latin capital letter o with circumflex and dot below'), # Ộ
        XK_ocircumflexbelowdot: d('ocircumflexbelowdot', u"\u1ED9", 'latin small letter o with circumflex and dot below'), # ộ
        XK_Ohornacute: d('Ohornacute', u"\u1EDA", 'latin capital letter o with horn and acute'), # Ớ
        XK_ohornacute: d('ohornacute', u"\u1EDB", 'latin small letter o with horn and acute'), # ớ
        XK_Ohorngrave: d('Ohorngrave', u"\u1EDC", 'latin capital letter o with horn and grave'), # Ờ
        XK_ohorngrave: d('ohorngrave', u"\u1EDD", 'latin small letter o with horn and grave'), # ờ
        XK_Ohornhook: d('Ohornhook', u"\u1EDE", 'latin capital letter o with horn and hook above'), # Ở
        XK_ohornhook: d('ohornhook', u"\u1EDF", 'latin small letter o with horn and hook above'), # ở
        XK_Ohorntilde: d('Ohorntilde', u"\u1EE0", 'latin capital letter o with horn and tilde'), # Ỡ
        XK_ohorntilde: d('ohorntilde', u"\u1EE1", 'latin small letter o with horn and tilde'), # ỡ
        XK_Ohornbelowdot: d('Ohornbelowdot', u"\u1EE2", 'latin capital letter o with horn and dot below'), # Ợ
        XK_ohornbelowdot: d('ohornbelowdot', u"\u1EE3", 'latin small letter o with horn and dot below'), # ợ
        XK_Ubelowdot: d('Ubelowdot', u"\u1EE4", 'latin capital letter u with dot below'), # Ụ
        XK_ubelowdot: d('ubelowdot', u"\u1EE5", 'latin small letter u with dot below'), # ụ
        XK_Uhook: d('Uhook', u"\u1EE6", 'latin capital letter u with hook above'), # Ủ
        XK_uhook: d('uhook', u"\u1EE7", 'latin small letter u with hook above'), # ủ
        XK_Uhornacute: d('Uhornacute', u"\u1EE8", 'latin capital letter u with horn and acute'), # Ứ
        XK_uhornacute: d('uhornacute', u"\u1EE9", 'latin small letter u with horn and acute'), # ứ
        XK_Uhorngrave: d('Uhorngrave', u"\u1EEA", 'latin capital letter u with horn and grave'), # Ừ
        XK_uhorngrave: d('uhorngrave', u"\u1EEB", 'latin small letter u with horn and grave'), # ừ
        XK_Uhornhook: d('Uhornhook', u"\u1EEC", 'latin capital letter u with horn and hook above'), # Ử
        XK_uhornhook: d('uhornhook', u"\u1EED", 'latin small letter u with horn and hook above'), # ử
        XK_Uhorntilde: d('Uhorntilde', u"\u1EEE", 'latin capital letter u with horn and tilde'), # Ữ
        XK_uhorntilde: d('uhorntilde', u"\u1EEF", 'latin small letter u with horn and tilde'), # ữ
        XK_Uhornbelowdot: d('Uhornbelowdot', u"\u1EF0", 'latin capital letter u with horn and dot below'), # Ự
        XK_uhornbelowdot: d('uhornbelowdot', u"\u1EF1", 'latin small letter u with horn and dot below'), # ự
        XK_Ybelowdot: d('Ybelowdot', u"\u1EF4", 'latin capital letter y with dot below'), # Ỵ
        XK_ybelowdot: d('ybelowdot', u"\u1EF5", 'latin small letter y with dot below'), # ỵ
        XK_Yhook: d('Yhook', u"\u1EF6", 'latin capital letter y with hook above'), # Ỷ
        XK_yhook: d('yhook', u"\u1EF7", 'latin small letter y with hook above'), # ỷ
        XK_Ytilde: d('Ytilde', u"\u1EF8", 'latin capital letter y with tilde'), # Ỹ
        XK_ytilde: d('ytilde', u"\u1EF9", 'latin small letter y with tilde'), # ỹ
        XK_Ohorn: d('Ohorn', u"\u01A0", 'latin capital letter o with horn'), # Ơ
        XK_ohorn: d('ohorn', u"\u01A1", 'latin small letter o with horn'), # ơ
        XK_Uhorn: d('Uhorn', u"\u01AF", 'latin capital letter u with horn'), # Ư
        XK_uhorn: d('uhorn', u"\u01B0", 'latin small letter u with horn'), # ư

    },


    'currency': {
        XK_EcuSign: d('EcuSign', u"\u20A0", 'euro-currency sign'), # ₠
        XK_ColonSign: d('ColonSign', u"\u20A1", 'colon sign'), # ₡
        XK_CruzeiroSign: d('CruzeiroSign', u"\u20A2", 'cruzeiro sign'), # ₢
        XK_FFrancSign: d('FFrancSign', u"\u20A3", 'french franc sign'), # ₣
        XK_LiraSign: d('LiraSign', u"\u20A4", 'lira sign'), # ₤
        XK_MillSign: d('MillSign', u"\u20A5", 'mill sign'), # ₥
        XK_NairaSign: d('NairaSign', u"\u20A6", 'naira sign'), # ₦
        XK_PesetaSign: d('PesetaSign', u"\u20A7", 'peseta sign'), # ₧
        XK_RupeeSign: d('RupeeSign', u"\u20A8", 'rupee sign'), # ₨
        XK_WonSign: d('WonSign', u"\u20A9", 'won sign'), # ₩
        XK_NewSheqelSign: d('NewSheqelSign', u"\u20AA", 'new sheqel sign'), # ₪
        XK_DongSign: d('DongSign', u"\u20AB", 'dong sign'), # ₫
        XK_EuroSign: d('EuroSign', u"\u20AC", 'euro sign'), # €
    },


    'mathematical': {
        #one,  two  and  three  are  defined  above.
        XK_zerosuperior: d('zerosuperior', u"\u2070", 'superscript zero'), # ⁰
        XK_foursuperior: d('foursuperior', u"\u2074", 'superscript four'), # ⁴
        XK_fivesuperior: d('fivesuperior', u"\u2075", 'superscript five'), # ⁵
        XK_sixsuperior: d('sixsuperior', u"\u2076", 'superscript six'), # ⁶
        XK_sevensuperior: d('sevensuperior', u"\u2077", 'superscript seven'), # ⁷
        XK_eightsuperior: d('eightsuperior', u"\u2078", 'superscript eight'), # ⁸
        XK_ninesuperior: d('ninesuperior', u"\u2079", 'superscript nine'), # ⁹
        XK_zerosubscript: d('zerosubscript', u"\u2080", 'subscript zero'), # ₀
        XK_onesubscript: d('onesubscript', u"\u2081", 'subscript one'), # ₁
        XK_twosubscript: d('twosubscript', u"\u2082", 'subscript two'), # ₂
        XK_threesubscript: d('threesubscript', u"\u2083", 'subscript three'), # ₃
        XK_foursubscript: d('foursubscript', u"\u2084", 'subscript four'), # ₄
        XK_fivesubscript: d('fivesubscript', u"\u2085", 'subscript five'), # ₅
        XK_sixsubscript: d('sixsubscript', u"\u2086", 'subscript six'), # ₆
        XK_sevensubscript: d('sevensubscript', u"\u2087", 'subscript seven'), # ₇
        XK_eightsubscript: d('eightsubscript', u"\u2088", 'subscript eight'), # ₈
        XK_ninesubscript: d('ninesubscript', u"\u2089", 'subscript nine'), # ₉
        XK_partdifferential: d('partdifferential', u"\u2202", 'partial differential'), # ∂
        XK_emptyset: d('emptyset', u"\u2205", 'null set'), # ∅
        XK_elementof: d('elementof', u"\u2208", 'element of'), # ∈
        XK_notelementof: d('notelementof', u"\u2209", 'not an element of'), # ∉
        XK_containsas: d('containsas', u"\u220B", 'contains as member'), # ∋
        XK_squareroot: d('squareroot', u"\u221A", 'square root'), # √
        XK_cuberoot: d('cuberoot', u"\u221B", 'cube root'), # ∛
        XK_fourthroot: d('fourthroot', u"\u221C", 'fourth root'), # ∜
        XK_dintegral: d('dintegral', u"\u222C", 'double integral'), # ∬
        XK_tintegral: d('tintegral', u"\u222D", 'triple integral'), # ∭
        XK_because: d('because', u"\u2235", 'because'), # ∵
        XK_approxeq: d('approxeq', u"\u2245", 'almost equal to'), # ≅
        XK_notapproxeq: d('notapproxeq', u"\u2247", 'not almost equal to'), # ≇
        XK_notidentical: d('notidentical', u"\u2262", 'not identical to'), # ≢
        XK_stricteq: d('stricteq', u"\u2263", 'strictly equivalent to'), # ≣
    },


    'braille': {
        XK_braille_dot_1: d('braille_dot_1', '', ''),
        XK_braille_dot_2: d('braille_dot_2', '', ''),
        XK_braille_dot_3: d('braille_dot_3', '', ''),
        XK_braille_dot_4: d('braille_dot_4', '', ''),
        XK_braille_dot_5: d('braille_dot_5', '', ''),
        XK_braille_dot_6: d('braille_dot_6', '', ''),
        XK_braille_dot_7: d('braille_dot_7', '', ''),
        XK_braille_dot_8: d('braille_dot_8', '', ''),
        XK_braille_dot_9: d('braille_dot_9', '', ''),
        XK_braille_dot_10: d('braille_dot_10', '', ''),
        XK_braille_blank: d('braille_blank', u"\u2800", 'braille pattern blank'), # ⠀
        XK_braille_dots_1: d('braille_dots_1', u"\u2801", 'braille pattern dots-1'), # ⠁
        XK_braille_dots_2: d('braille_dots_2', u"\u2802", 'braille pattern dots-2'), # ⠂
        XK_braille_dots_12: d('braille_dots_12', u"\u2803", 'braille pattern dots-12'), # ⠃
        XK_braille_dots_3: d('braille_dots_3', u"\u2804", 'braille pattern dots-3'), # ⠄
        XK_braille_dots_13: d('braille_dots_13', u"\u2805", 'braille pattern dots-13'), # ⠅
        XK_braille_dots_23: d('braille_dots_23', u"\u2806", 'braille pattern dots-23'), # ⠆
        XK_braille_dots_123: d('braille_dots_123', u"\u2807", 'braille pattern dots-123'), # ⠇
        XK_braille_dots_4: d('braille_dots_4', u"\u2808", 'braille pattern dots-4'), # ⠈
        XK_braille_dots_14: d('braille_dots_14', u"\u2809", 'braille pattern dots-14'), # ⠉
        XK_braille_dots_24: d('braille_dots_24', u"\u280a", 'braille pattern dots-24'), # ⠊
        XK_braille_dots_124: d('braille_dots_124', u"\u280b", 'braille pattern dots-124'), # ⠋
        XK_braille_dots_34: d('braille_dots_34', u"\u280c", 'braille pattern dots-34'), # ⠌
        XK_braille_dots_134: d('braille_dots_134', u"\u280d", 'braille pattern dots-134'), # ⠍
        XK_braille_dots_234: d('braille_dots_234', u"\u280e", 'braille pattern dots-234'), # ⠎
        XK_braille_dots_1234: d('braille_dots_1234', u"\u280f", 'braille pattern dots-1234'), # ⠏
        XK_braille_dots_5: d('braille_dots_5', u"\u2810", 'braille pattern dots-5'), # ⠐
        XK_braille_dots_15: d('braille_dots_15', u"\u2811", 'braille pattern dots-15'), # ⠑
        XK_braille_dots_25: d('braille_dots_25', u"\u2812", 'braille pattern dots-25'), # ⠒
        XK_braille_dots_125: d('braille_dots_125', u"\u2813", 'braille pattern dots-125'), # ⠓
        XK_braille_dots_35: d('braille_dots_35', u"\u2814", 'braille pattern dots-35'), # ⠔
        XK_braille_dots_135: d('braille_dots_135', u"\u2815", 'braille pattern dots-135'), # ⠕
        XK_braille_dots_235: d('braille_dots_235', u"\u2816", 'braille pattern dots-235'), # ⠖
        XK_braille_dots_1235: d('braille_dots_1235', u"\u2817", 'braille pattern dots-1235'), # ⠗
        XK_braille_dots_45: d('braille_dots_45', u"\u2818", 'braille pattern dots-45'), # ⠘
        XK_braille_dots_145: d('braille_dots_145', u"\u2819", 'braille pattern dots-145'), # ⠙
        XK_braille_dots_245: d('braille_dots_245', u"\u281a", 'braille pattern dots-245'), # ⠚
        XK_braille_dots_1245: d('braille_dots_1245', u"\u281b", 'braille pattern dots-1245'), # ⠛
        XK_braille_dots_345: d('braille_dots_345', u"\u281c", 'braille pattern dots-345'), # ⠜
        XK_braille_dots_1345: d('braille_dots_1345', u"\u281d", 'braille pattern dots-1345'), # ⠝
        XK_braille_dots_2345: d('braille_dots_2345', u"\u281e", 'braille pattern dots-2345'), # ⠞
        XK_braille_dots_12345: d('braille_dots_12345', u"\u281f", 'braille pattern dots-12345'), # ⠟
        XK_braille_dots_6: d('braille_dots_6', u"\u2820", 'braille pattern dots-6'), # ⠠
        XK_braille_dots_16: d('braille_dots_16', u"\u2821", 'braille pattern dots-16'), # ⠡
        XK_braille_dots_26: d('braille_dots_26', u"\u2822", 'braille pattern dots-26'), # ⠢
        XK_braille_dots_126: d('braille_dots_126', u"\u2823", 'braille pattern dots-126'), # ⠣
        XK_braille_dots_36: d('braille_dots_36', u"\u2824", 'braille pattern dots-36'), # ⠤
        XK_braille_dots_136: d('braille_dots_136', u"\u2825", 'braille pattern dots-136'), # ⠥
        XK_braille_dots_236: d('braille_dots_236', u"\u2826", 'braille pattern dots-236'), # ⠦
        XK_braille_dots_1236: d('braille_dots_1236', u"\u2827", 'braille pattern dots-1236'), # ⠧
        XK_braille_dots_46: d('braille_dots_46', u"\u2828", 'braille pattern dots-46'), # ⠨
        XK_braille_dots_146: d('braille_dots_146', u"\u2829", 'braille pattern dots-146'), # ⠩
        XK_braille_dots_246: d('braille_dots_246', u"\u282a", 'braille pattern dots-246'), # ⠪
        XK_braille_dots_1246: d('braille_dots_1246', u"\u282b", 'braille pattern dots-1246'), # ⠫
        XK_braille_dots_346: d('braille_dots_346', u"\u282c", 'braille pattern dots-346'), # ⠬
        XK_braille_dots_1346: d('braille_dots_1346', u"\u282d", 'braille pattern dots-1346'), # ⠭
        XK_braille_dots_2346: d('braille_dots_2346', u"\u282e", 'braille pattern dots-2346'), # ⠮
        XK_braille_dots_12346: d('braille_dots_12346', u"\u282f", 'braille pattern dots-12346'), # ⠯
        XK_braille_dots_56: d('braille_dots_56', u"\u2830", 'braille pattern dots-56'), # ⠰
        XK_braille_dots_156: d('braille_dots_156', u"\u2831", 'braille pattern dots-156'), # ⠱
        XK_braille_dots_256: d('braille_dots_256', u"\u2832", 'braille pattern dots-256'), # ⠲
        XK_braille_dots_1256: d('braille_dots_1256', u"\u2833", 'braille pattern dots-1256'), # ⠳
        XK_braille_dots_356: d('braille_dots_356', u"\u2834", 'braille pattern dots-356'), # ⠴
        XK_braille_dots_1356: d('braille_dots_1356', u"\u2835", 'braille pattern dots-1356'), # ⠵
        XK_braille_dots_2356: d('braille_dots_2356', u"\u2836", 'braille pattern dots-2356'), # ⠶
        XK_braille_dots_12356: d('braille_dots_12356', u"\u2837", 'braille pattern dots-12356'), # ⠷
        XK_braille_dots_456: d('braille_dots_456', u"\u2838", 'braille pattern dots-456'), # ⠸
        XK_braille_dots_1456: d('braille_dots_1456', u"\u2839", 'braille pattern dots-1456'), # ⠹
        XK_braille_dots_2456: d('braille_dots_2456', u"\u283a", 'braille pattern dots-2456'), # ⠺
        XK_braille_dots_12456: d('braille_dots_12456', u"\u283b", 'braille pattern dots-12456'), # ⠻
        XK_braille_dots_3456: d('braille_dots_3456', u"\u283c", 'braille pattern dots-3456'), # ⠼
        XK_braille_dots_13456: d('braille_dots_13456', u"\u283d", 'braille pattern dots-13456'), # ⠽
        XK_braille_dots_23456: d('braille_dots_23456', u"\u283e", 'braille pattern dots-23456'), # ⠾
        XK_braille_dots_123456: d('braille_dots_123456', u"\u283f", 'braille pattern dots-123456'), # ⠿
        XK_braille_dots_7: d('braille_dots_7', u"\u2840", 'braille pattern dots-7'), # ⡀
        XK_braille_dots_17: d('braille_dots_17', u"\u2841", 'braille pattern dots-17'), # ⡁
        XK_braille_dots_27: d('braille_dots_27', u"\u2842", 'braille pattern dots-27'), # ⡂
        XK_braille_dots_127: d('braille_dots_127', u"\u2843", 'braille pattern dots-127'), # ⡃
        XK_braille_dots_37: d('braille_dots_37', u"\u2844", 'braille pattern dots-37'), # ⡄
        XK_braille_dots_137: d('braille_dots_137', u"\u2845", 'braille pattern dots-137'), # ⡅
        XK_braille_dots_237: d('braille_dots_237', u"\u2846", 'braille pattern dots-237'), # ⡆
        XK_braille_dots_1237: d('braille_dots_1237', u"\u2847", 'braille pattern dots-1237'), # ⡇
        XK_braille_dots_47: d('braille_dots_47', u"\u2848", 'braille pattern dots-47'), # ⡈
        XK_braille_dots_147: d('braille_dots_147', u"\u2849", 'braille pattern dots-147'), # ⡉
        XK_braille_dots_247: d('braille_dots_247', u"\u284a", 'braille pattern dots-247'), # ⡊
        XK_braille_dots_1247: d('braille_dots_1247', u"\u284b", 'braille pattern dots-1247'), # ⡋
        XK_braille_dots_347: d('braille_dots_347', u"\u284c", 'braille pattern dots-347'), # ⡌
        XK_braille_dots_1347: d('braille_dots_1347', u"\u284d", 'braille pattern dots-1347'), # ⡍
        XK_braille_dots_2347: d('braille_dots_2347', u"\u284e", 'braille pattern dots-2347'), # ⡎
        XK_braille_dots_12347: d('braille_dots_12347', u"\u284f", 'braille pattern dots-12347'), # ⡏
        XK_braille_dots_57: d('braille_dots_57', u"\u2850", 'braille pattern dots-57'), # ⡐
        XK_braille_dots_157: d('braille_dots_157', u"\u2851", 'braille pattern dots-157'), # ⡑
        XK_braille_dots_257: d('braille_dots_257', u"\u2852", 'braille pattern dots-257'), # ⡒
        XK_braille_dots_1257: d('braille_dots_1257', u"\u2853", 'braille pattern dots-1257'), # ⡓
        XK_braille_dots_357: d('braille_dots_357', u"\u2854", 'braille pattern dots-357'), # ⡔
        XK_braille_dots_1357: d('braille_dots_1357', u"\u2855", 'braille pattern dots-1357'), # ⡕
        XK_braille_dots_2357: d('braille_dots_2357', u"\u2856", 'braille pattern dots-2357'), # ⡖
        XK_braille_dots_12357: d('braille_dots_12357', u"\u2857", 'braille pattern dots-12357'), # ⡗
        XK_braille_dots_457: d('braille_dots_457', u"\u2858", 'braille pattern dots-457'), # ⡘
        XK_braille_dots_1457: d('braille_dots_1457', u"\u2859", 'braille pattern dots-1457'), # ⡙
        XK_braille_dots_2457: d('braille_dots_2457', u"\u285a", 'braille pattern dots-2457'), # ⡚
        XK_braille_dots_12457: d('braille_dots_12457', u"\u285b", 'braille pattern dots-12457'), # ⡛
        XK_braille_dots_3457: d('braille_dots_3457', u"\u285c", 'braille pattern dots-3457'), # ⡜
        XK_braille_dots_13457: d('braille_dots_13457', u"\u285d", 'braille pattern dots-13457'), # ⡝
        XK_braille_dots_23457: d('braille_dots_23457', u"\u285e", 'braille pattern dots-23457'), # ⡞
        XK_braille_dots_123457: d('braille_dots_123457', u"\u285f", 'braille pattern dots-123457'), # ⡟
        XK_braille_dots_67: d('braille_dots_67', u"\u2860", 'braille pattern dots-67'), # ⡠
        XK_braille_dots_167: d('braille_dots_167', u"\u2861", 'braille pattern dots-167'), # ⡡
        XK_braille_dots_267: d('braille_dots_267', u"\u2862", 'braille pattern dots-267'), # ⡢
        XK_braille_dots_1267: d('braille_dots_1267', u"\u2863", 'braille pattern dots-1267'), # ⡣
        XK_braille_dots_367: d('braille_dots_367', u"\u2864", 'braille pattern dots-367'), # ⡤
        XK_braille_dots_1367: d('braille_dots_1367', u"\u2865", 'braille pattern dots-1367'), # ⡥
        XK_braille_dots_2367: d('braille_dots_2367', u"\u2866", 'braille pattern dots-2367'), # ⡦
        XK_braille_dots_12367: d('braille_dots_12367', u"\u2867", 'braille pattern dots-12367'), # ⡧
        XK_braille_dots_467: d('braille_dots_467', u"\u2868", 'braille pattern dots-467'), # ⡨
        XK_braille_dots_1467: d('braille_dots_1467', u"\u2869", 'braille pattern dots-1467'), # ⡩
        XK_braille_dots_2467: d('braille_dots_2467', u"\u286a", 'braille pattern dots-2467'), # ⡪
        XK_braille_dots_12467: d('braille_dots_12467', u"\u286b", 'braille pattern dots-12467'), # ⡫
        XK_braille_dots_3467: d('braille_dots_3467', u"\u286c", 'braille pattern dots-3467'), # ⡬
        XK_braille_dots_13467: d('braille_dots_13467', u"\u286d", 'braille pattern dots-13467'), # ⡭
        XK_braille_dots_23467: d('braille_dots_23467', u"\u286e", 'braille pattern dots-23467'), # ⡮
        XK_braille_dots_123467: d('braille_dots_123467', u"\u286f", 'braille pattern dots-123467'), # ⡯
        XK_braille_dots_567: d('braille_dots_567', u"\u2870", 'braille pattern dots-567'), # ⡰
        XK_braille_dots_1567: d('braille_dots_1567', u"\u2871", 'braille pattern dots-1567'), # ⡱
        XK_braille_dots_2567: d('braille_dots_2567', u"\u2872", 'braille pattern dots-2567'), # ⡲
        XK_braille_dots_12567: d('braille_dots_12567', u"\u2873", 'braille pattern dots-12567'), # ⡳
        XK_braille_dots_3567: d('braille_dots_3567', u"\u2874", 'braille pattern dots-3567'), # ⡴
        XK_braille_dots_13567: d('braille_dots_13567', u"\u2875", 'braille pattern dots-13567'), # ⡵
        XK_braille_dots_23567: d('braille_dots_23567', u"\u2876", 'braille pattern dots-23567'), # ⡶
        XK_braille_dots_123567: d('braille_dots_123567', u"\u2877", 'braille pattern dots-123567'), # ⡷
        XK_braille_dots_4567: d('braille_dots_4567', u"\u2878", 'braille pattern dots-4567'), # ⡸
        XK_braille_dots_14567: d('braille_dots_14567', u"\u2879", 'braille pattern dots-14567'), # ⡹
        XK_braille_dots_24567: d('braille_dots_24567', u"\u287a", 'braille pattern dots-24567'), # ⡺
        XK_braille_dots_124567: d('braille_dots_124567', u"\u287b", 'braille pattern dots-124567'), # ⡻
        XK_braille_dots_34567: d('braille_dots_34567', u"\u287c", 'braille pattern dots-34567'), # ⡼
        XK_braille_dots_134567: d('braille_dots_134567', u"\u287d", 'braille pattern dots-134567'), # ⡽
        XK_braille_dots_234567: d('braille_dots_234567', u"\u287e", 'braille pattern dots-234567'), # ⡾
        XK_braille_dots_1234567: d('braille_dots_1234567', u"\u287f", 'braille pattern dots-1234567'), # ⡿
        XK_braille_dots_8: d('braille_dots_8', u"\u2880", 'braille pattern dots-8'), # ⢀
        XK_braille_dots_18: d('braille_dots_18', u"\u2881", 'braille pattern dots-18'), # ⢁
        XK_braille_dots_28: d('braille_dots_28', u"\u2882", 'braille pattern dots-28'), # ⢂
        XK_braille_dots_128: d('braille_dots_128', u"\u2883", 'braille pattern dots-128'), # ⢃
        XK_braille_dots_38: d('braille_dots_38', u"\u2884", 'braille pattern dots-38'), # ⢄
        XK_braille_dots_138: d('braille_dots_138', u"\u2885", 'braille pattern dots-138'), # ⢅
        XK_braille_dots_238: d('braille_dots_238', u"\u2886", 'braille pattern dots-238'), # ⢆
        XK_braille_dots_1238: d('braille_dots_1238', u"\u2887", 'braille pattern dots-1238'), # ⢇
        XK_braille_dots_48: d('braille_dots_48', u"\u2888", 'braille pattern dots-48'), # ⢈
        XK_braille_dots_148: d('braille_dots_148', u"\u2889", 'braille pattern dots-148'), # ⢉
        XK_braille_dots_248: d('braille_dots_248', u"\u288a", 'braille pattern dots-248'), # ⢊
        XK_braille_dots_1248: d('braille_dots_1248', u"\u288b", 'braille pattern dots-1248'), # ⢋
        XK_braille_dots_348: d('braille_dots_348', u"\u288c", 'braille pattern dots-348'), # ⢌
        XK_braille_dots_1348: d('braille_dots_1348', u"\u288d", 'braille pattern dots-1348'), # ⢍
        XK_braille_dots_2348: d('braille_dots_2348', u"\u288e", 'braille pattern dots-2348'), # ⢎
        XK_braille_dots_12348: d('braille_dots_12348', u"\u288f", 'braille pattern dots-12348'), # ⢏
        XK_braille_dots_58: d('braille_dots_58', u"\u2890", 'braille pattern dots-58'), # ⢐
        XK_braille_dots_158: d('braille_dots_158', u"\u2891", 'braille pattern dots-158'), # ⢑
        XK_braille_dots_258: d('braille_dots_258', u"\u2892", 'braille pattern dots-258'), # ⢒
        XK_braille_dots_1258: d('braille_dots_1258', u"\u2893", 'braille pattern dots-1258'), # ⢓
        XK_braille_dots_358: d('braille_dots_358', u"\u2894", 'braille pattern dots-358'), # ⢔
        XK_braille_dots_1358: d('braille_dots_1358', u"\u2895", 'braille pattern dots-1358'), # ⢕
        XK_braille_dots_2358: d('braille_dots_2358', u"\u2896", 'braille pattern dots-2358'), # ⢖
        XK_braille_dots_12358: d('braille_dots_12358', u"\u2897", 'braille pattern dots-12358'), # ⢗
        XK_braille_dots_458: d('braille_dots_458', u"\u2898", 'braille pattern dots-458'), # ⢘
        XK_braille_dots_1458: d('braille_dots_1458', u"\u2899", 'braille pattern dots-1458'), # ⢙
        XK_braille_dots_2458: d('braille_dots_2458', u"\u289a", 'braille pattern dots-2458'), # ⢚
        XK_braille_dots_12458: d('braille_dots_12458', u"\u289b", 'braille pattern dots-12458'), # ⢛
        XK_braille_dots_3458: d('braille_dots_3458', u"\u289c", 'braille pattern dots-3458'), # ⢜
        XK_braille_dots_13458: d('braille_dots_13458', u"\u289d", 'braille pattern dots-13458'), # ⢝
        XK_braille_dots_23458: d('braille_dots_23458', u"\u289e", 'braille pattern dots-23458'), # ⢞
        XK_braille_dots_123458: d('braille_dots_123458', u"\u289f", 'braille pattern dots-123458'), # ⢟
        XK_braille_dots_68: d('braille_dots_68', u"\u28a0", 'braille pattern dots-68'), # ⢠
        XK_braille_dots_168: d('braille_dots_168', u"\u28a1", 'braille pattern dots-168'), # ⢡
        XK_braille_dots_268: d('braille_dots_268', u"\u28a2", 'braille pattern dots-268'), # ⢢
        XK_braille_dots_1268: d('braille_dots_1268', u"\u28a3", 'braille pattern dots-1268'), # ⢣
        XK_braille_dots_368: d('braille_dots_368', u"\u28a4", 'braille pattern dots-368'), # ⢤
        XK_braille_dots_1368: d('braille_dots_1368', u"\u28a5", 'braille pattern dots-1368'), # ⢥
        XK_braille_dots_2368: d('braille_dots_2368', u"\u28a6", 'braille pattern dots-2368'), # ⢦
        XK_braille_dots_12368: d('braille_dots_12368', u"\u28a7", 'braille pattern dots-12368'), # ⢧
        XK_braille_dots_468: d('braille_dots_468', u"\u28a8", 'braille pattern dots-468'), # ⢨
        XK_braille_dots_1468: d('braille_dots_1468', u"\u28a9", 'braille pattern dots-1468'), # ⢩
        XK_braille_dots_2468: d('braille_dots_2468', u"\u28aa", 'braille pattern dots-2468'), # ⢪
        XK_braille_dots_12468: d('braille_dots_12468', u"\u28ab", 'braille pattern dots-12468'), # ⢫
        XK_braille_dots_3468: d('braille_dots_3468', u"\u28ac", 'braille pattern dots-3468'), # ⢬
        XK_braille_dots_13468: d('braille_dots_13468', u"\u28ad", 'braille pattern dots-13468'), # ⢭
        XK_braille_dots_23468: d('braille_dots_23468', u"\u28ae", 'braille pattern dots-23468'), # ⢮
        XK_braille_dots_123468: d('braille_dots_123468', u"\u28af", 'braille pattern dots-123468'), # ⢯
        XK_braille_dots_568: d('braille_dots_568', u"\u28b0", 'braille pattern dots-568'), # ⢰
        XK_braille_dots_1568: d('braille_dots_1568', u"\u28b1", 'braille pattern dots-1568'), # ⢱
        XK_braille_dots_2568: d('braille_dots_2568', u"\u28b2", 'braille pattern dots-2568'), # ⢲
        XK_braille_dots_12568: d('braille_dots_12568', u"\u28b3", 'braille pattern dots-12568'), # ⢳
        XK_braille_dots_3568: d('braille_dots_3568', u"\u28b4", 'braille pattern dots-3568'), # ⢴
        XK_braille_dots_13568: d('braille_dots_13568', u"\u28b5", 'braille pattern dots-13568'), # ⢵
        XK_braille_dots_23568: d('braille_dots_23568', u"\u28b6", 'braille pattern dots-23568'), # ⢶
        XK_braille_dots_123568: d('braille_dots_123568', u"\u28b7", 'braille pattern dots-123568'), # ⢷
        XK_braille_dots_4568: d('braille_dots_4568', u"\u28b8", 'braille pattern dots-4568'), # ⢸
        XK_braille_dots_14568: d('braille_dots_14568', u"\u28b9", 'braille pattern dots-14568'), # ⢹
        XK_braille_dots_24568: d('braille_dots_24568', u"\u28ba", 'braille pattern dots-24568'), # ⢺
        XK_braille_dots_124568: d('braille_dots_124568', u"\u28bb", 'braille pattern dots-124568'), # ⢻
        XK_braille_dots_34568: d('braille_dots_34568', u"\u28bc", 'braille pattern dots-34568'), # ⢼
        XK_braille_dots_134568: d('braille_dots_134568', u"\u28bd", 'braille pattern dots-134568'), # ⢽
        XK_braille_dots_234568: d('braille_dots_234568', u"\u28be", 'braille pattern dots-234568'), # ⢾
        XK_braille_dots_1234568: d('braille_dots_1234568', u"\u28bf", 'braille pattern dots-1234568'), # ⢿
        XK_braille_dots_78: d('braille_dots_78', u"\u28c0", 'braille pattern dots-78'), # ⣀
        XK_braille_dots_178: d('braille_dots_178', u"\u28c1", 'braille pattern dots-178'), # ⣁
        XK_braille_dots_278: d('braille_dots_278', u"\u28c2", 'braille pattern dots-278'), # ⣂
        XK_braille_dots_1278: d('braille_dots_1278', u"\u28c3", 'braille pattern dots-1278'), # ⣃
        XK_braille_dots_378: d('braille_dots_378', u"\u28c4", 'braille pattern dots-378'), # ⣄
        XK_braille_dots_1378: d('braille_dots_1378', u"\u28c5", 'braille pattern dots-1378'), # ⣅
        XK_braille_dots_2378: d('braille_dots_2378', u"\u28c6", 'braille pattern dots-2378'), # ⣆
        XK_braille_dots_12378: d('braille_dots_12378', u"\u28c7", 'braille pattern dots-12378'), # ⣇
        XK_braille_dots_478: d('braille_dots_478', u"\u28c8", 'braille pattern dots-478'), # ⣈
        XK_braille_dots_1478: d('braille_dots_1478', u"\u28c9", 'braille pattern dots-1478'), # ⣉
        XK_braille_dots_2478: d('braille_dots_2478', u"\u28ca", 'braille pattern dots-2478'), # ⣊
        XK_braille_dots_12478: d('braille_dots_12478', u"\u28cb", 'braille pattern dots-12478'), # ⣋
        XK_braille_dots_3478: d('braille_dots_3478', u"\u28cc", 'braille pattern dots-3478'), # ⣌
        XK_braille_dots_13478: d('braille_dots_13478', u"\u28cd", 'braille pattern dots-13478'), # ⣍
        XK_braille_dots_23478: d('braille_dots_23478', u"\u28ce", 'braille pattern dots-23478'), # ⣎
        XK_braille_dots_123478: d('braille_dots_123478', u"\u28cf", 'braille pattern dots-123478'), # ⣏
        XK_braille_dots_578: d('braille_dots_578', u"\u28d0", 'braille pattern dots-578'), # ⣐
        XK_braille_dots_1578: d('braille_dots_1578', u"\u28d1", 'braille pattern dots-1578'), # ⣑
        XK_braille_dots_2578: d('braille_dots_2578', u"\u28d2", 'braille pattern dots-2578'), # ⣒
        XK_braille_dots_12578: d('braille_dots_12578', u"\u28d3", 'braille pattern dots-12578'), # ⣓
        XK_braille_dots_3578: d('braille_dots_3578', u"\u28d4", 'braille pattern dots-3578'), # ⣔
        XK_braille_dots_13578: d('braille_dots_13578', u"\u28d5", 'braille pattern dots-13578'), # ⣕
        XK_braille_dots_23578: d('braille_dots_23578', u"\u28d6", 'braille pattern dots-23578'), # ⣖
        XK_braille_dots_123578: d('braille_dots_123578', u"\u28d7", 'braille pattern dots-123578'), # ⣗
        XK_braille_dots_4578: d('braille_dots_4578', u"\u28d8", 'braille pattern dots-4578'), # ⣘
        XK_braille_dots_14578: d('braille_dots_14578', u"\u28d9", 'braille pattern dots-14578'), # ⣙
        XK_braille_dots_24578: d('braille_dots_24578', u"\u28da", 'braille pattern dots-24578'), # ⣚
        XK_braille_dots_124578: d('braille_dots_124578', u"\u28db", 'braille pattern dots-124578'), # ⣛
        XK_braille_dots_34578: d('braille_dots_34578', u"\u28dc", 'braille pattern dots-34578'), # ⣜
        XK_braille_dots_134578: d('braille_dots_134578', u"\u28dd", 'braille pattern dots-134578'), # ⣝
        XK_braille_dots_234578: d('braille_dots_234578', u"\u28de", 'braille pattern dots-234578'), # ⣞
        XK_braille_dots_1234578: d('braille_dots_1234578', u"\u28df", 'braille pattern dots-1234578'), # ⣟
        XK_braille_dots_678: d('braille_dots_678', u"\u28e0", 'braille pattern dots-678'), # ⣠
        XK_braille_dots_1678: d('braille_dots_1678', u"\u28e1", 'braille pattern dots-1678'), # ⣡
        XK_braille_dots_2678: d('braille_dots_2678', u"\u28e2", 'braille pattern dots-2678'), # ⣢
        XK_braille_dots_12678: d('braille_dots_12678', u"\u28e3", 'braille pattern dots-12678'), # ⣣
        XK_braille_dots_3678: d('braille_dots_3678', u"\u28e4", 'braille pattern dots-3678'), # ⣤
        XK_braille_dots_13678: d('braille_dots_13678', u"\u28e5", 'braille pattern dots-13678'), # ⣥
        XK_braille_dots_23678: d('braille_dots_23678', u"\u28e6", 'braille pattern dots-23678'), # ⣦
        XK_braille_dots_123678: d('braille_dots_123678', u"\u28e7", 'braille pattern dots-123678'), # ⣧
        XK_braille_dots_4678: d('braille_dots_4678', u"\u28e8", 'braille pattern dots-4678'), # ⣨
        XK_braille_dots_14678: d('braille_dots_14678', u"\u28e9", 'braille pattern dots-14678'), # ⣩
        XK_braille_dots_24678: d('braille_dots_24678', u"\u28ea", 'braille pattern dots-24678'), # ⣪
        XK_braille_dots_124678: d('braille_dots_124678', u"\u28eb", 'braille pattern dots-124678'), # ⣫
        XK_braille_dots_34678: d('braille_dots_34678', u"\u28ec", 'braille pattern dots-34678'), # ⣬
        XK_braille_dots_134678: d('braille_dots_134678', u"\u28ed", 'braille pattern dots-134678'), # ⣭
        XK_braille_dots_234678: d('braille_dots_234678', u"\u28ee", 'braille pattern dots-234678'), # ⣮
        XK_braille_dots_1234678: d('braille_dots_1234678', u"\u28ef", 'braille pattern dots-1234678'), # ⣯
        XK_braille_dots_5678: d('braille_dots_5678', u"\u28f0", 'braille pattern dots-5678'), # ⣰
        XK_braille_dots_15678: d('braille_dots_15678', u"\u28f1", 'braille pattern dots-15678'), # ⣱
        XK_braille_dots_25678: d('braille_dots_25678', u"\u28f2", 'braille pattern dots-25678'), # ⣲
        XK_braille_dots_125678: d('braille_dots_125678', u"\u28f3", 'braille pattern dots-125678'), # ⣳
        XK_braille_dots_35678: d('braille_dots_35678', u"\u28f4", 'braille pattern dots-35678'), # ⣴
        XK_braille_dots_135678: d('braille_dots_135678', u"\u28f5", 'braille pattern dots-135678'), # ⣵
        XK_braille_dots_235678: d('braille_dots_235678', u"\u28f6", 'braille pattern dots-235678'), # ⣶
        XK_braille_dots_1235678: d('braille_dots_1235678', u"\u28f7", 'braille pattern dots-1235678'), # ⣷
        XK_braille_dots_45678: d('braille_dots_45678', u"\u28f8", 'braille pattern dots-45678'), # ⣸
        XK_braille_dots_145678: d('braille_dots_145678', u"\u28f9", 'braille pattern dots-145678'), # ⣹
        XK_braille_dots_245678: d('braille_dots_245678', u"\u28fa", 'braille pattern dots-245678'), # ⣺
        XK_braille_dots_1245678: d('braille_dots_1245678', u"\u28fb", 'braille pattern dots-1245678'), # ⣻
        XK_braille_dots_345678: d('braille_dots_345678', u"\u28fc", 'braille pattern dots-345678'), # ⣼
        XK_braille_dots_1345678: d('braille_dots_1345678', u"\u28fd", 'braille pattern dots-1345678'), # ⣽
        XK_braille_dots_2345678: d('braille_dots_2345678', u"\u28fe", 'braille pattern dots-2345678'), # ⣾
        XK_braille_dots_12345678: d('braille_dots_12345678', u"\u28ff", 'braille pattern dots-12345678'), # ⣿
    },


    #Sinhala (http://unicode.org/charts/PDF/U0D80.pdf)
    #http://www.nongnu.org/sinhala/doc/transliteration/sinhala-transliteration_6.html

    'sinhala': {
        XK_Sinh_ng: d('Sinh_ng', u"\u0D82", 'sinhala anusvaraya'), # ං
        XK_Sinh_h2: d('Sinh_h2', u"\u0D83", 'sinhala visargaya'), # ඃ
        XK_Sinh_a: d('Sinh_a', u"\u0D85", 'sinhala ayanna'), # අ
        XK_Sinh_aa: d('Sinh_aa', u"\u0D86", 'sinhala aayanna'), # ආ
        XK_Sinh_ae: d('Sinh_ae', u"\u0D87", 'sinhala aeyanna'), # ඇ
        XK_Sinh_aee: d('Sinh_aee', u"\u0D88", 'sinhala aeeyanna'), # ඈ
        XK_Sinh_i: d('Sinh_i', u"\u0D89", 'sinhala iyanna'), # ඉ
        XK_Sinh_ii: d('Sinh_ii', u"\u0D8A", 'sinhala iiyanna'), # ඊ
        XK_Sinh_u: d('Sinh_u', u"\u0D8B", 'sinhala uyanna'), # උ
        XK_Sinh_uu: d('Sinh_uu', u"\u0D8C", 'sinhala uuyanna'), # ඌ
        XK_Sinh_ri: d('Sinh_ri', u"\u0D8D", 'sinhala iruyanna'), # ඍ
        XK_Sinh_rii: d('Sinh_rii', u"\u0D8E", 'sinhala iruuyanna'), # ඎ
        XK_Sinh_lu: d('Sinh_lu', u"\u0D8F", 'sinhala iluyanna'), # ඏ
        XK_Sinh_luu: d('Sinh_luu', u"\u0D90", 'sinhala iluuyanna'), # ඐ
        XK_Sinh_e: d('Sinh_e', u"\u0D91", 'sinhala eyanna'), # එ
        XK_Sinh_ee: d('Sinh_ee', u"\u0D92", 'sinhala eeyanna'), # ඒ
        XK_Sinh_ai: d('Sinh_ai', u"\u0D93", 'sinhala aiyanna'), # ඓ
        XK_Sinh_o: d('Sinh_o', u"\u0D94", 'sinhala oyanna'), # ඔ
        XK_Sinh_oo: d('Sinh_oo', u"\u0D95", 'sinhala ooyanna'), # ඕ
        XK_Sinh_au: d('Sinh_au', u"\u0D96", 'sinhala auyanna'), # ඖ
        XK_Sinh_ka: d('Sinh_ka', u"\u0D9A", 'sinhala kayanna'), # ක
        XK_Sinh_kha: d('Sinh_kha', u"\u0D9B", 'sinhala maha. kayanna'), # ඛ
        XK_Sinh_ga: d('Sinh_ga', u"\u0D9C", 'sinhala gayanna'), # ග
        XK_Sinh_gha: d('Sinh_gha', u"\u0D9D", 'sinhala maha. gayanna'), # ඝ
        XK_Sinh_ng2: d('Sinh_ng2', u"\u0D9E", 'sinhala kantaja naasikyaya'), # ඞ
        XK_Sinh_nga: d('Sinh_nga', u"\u0D9F", 'sinhala sanyaka gayanna'), # ඟ
        XK_Sinh_ca: d('Sinh_ca', u"\u0DA0", 'sinhala cayanna'), # ච
        XK_Sinh_cha: d('Sinh_cha', u"\u0DA1", 'sinhala maha. cayanna'), # ඡ
        XK_Sinh_ja: d('Sinh_ja', u"\u0DA2", 'sinhala jayanna'), # ජ
        XK_Sinh_jha: d('Sinh_jha', u"\u0DA3", 'sinhala maha. jayanna'), # ඣ
        XK_Sinh_nya: d('Sinh_nya', u"\u0DA4", 'sinhala taaluja naasikyaya'), # ඤ
        XK_Sinh_jnya: d('Sinh_jnya', u"\u0DA5", 'sinhala taaluja sanyooga naasikyaya'), # ඥ
        XK_Sinh_nja: d('Sinh_nja', u"\u0DA6", 'sinhala sanyaka jayanna'), # ඦ
        XK_Sinh_tta: d('Sinh_tta', u"\u0DA7", 'sinhala ttayanna'), # ට
        XK_Sinh_ttha: d('Sinh_ttha', u"\u0DA8", 'sinhala maha. ttayanna'), # ඨ
        XK_Sinh_dda: d('Sinh_dda', u"\u0DA9", 'sinhala ddayanna'), # ඩ
        XK_Sinh_ddha: d('Sinh_ddha', u"\u0DAA", 'sinhala maha. ddayanna'), # ඪ
        XK_Sinh_nna: d('Sinh_nna', u"\u0DAB", 'sinhala muurdhaja nayanna'), # ණ
        XK_Sinh_ndda: d('Sinh_ndda', u"\u0DAC", 'sinhala sanyaka ddayanna'), # ඬ
        XK_Sinh_tha: d('Sinh_tha', u"\u0DAD", 'sinhala tayanna'), # ත
        XK_Sinh_thha: d('Sinh_thha', u"\u0DAE", 'sinhala maha. tayanna'), # ථ
        XK_Sinh_dha: d('Sinh_dha', u"\u0DAF", 'sinhala dayanna'), # ද
        XK_Sinh_dhha: d('Sinh_dhha', u"\u0DB0", 'sinhala maha. dayanna'), # ධ
        XK_Sinh_na: d('Sinh_na', u"\u0DB1", 'sinhala dantaja nayanna'), # න
        XK_Sinh_ndha: d('Sinh_ndha', u"\u0DB3", 'sinhala sanyaka dayanna'), # ඳ
        XK_Sinh_pa: d('Sinh_pa', u"\u0DB4", 'sinhala payanna'), # ප
        XK_Sinh_pha: d('Sinh_pha', u"\u0DB5", 'sinhala maha. payanna'), # ඵ
        XK_Sinh_ba: d('Sinh_ba', u"\u0DB6", 'sinhala bayanna'), # බ
        XK_Sinh_bha: d('Sinh_bha', u"\u0DB7", 'sinhala maha. bayanna'), # භ
        XK_Sinh_ma: d('Sinh_ma', u"\u0DB8", 'sinhala mayanna'), # ම
        XK_Sinh_mba: d('Sinh_mba', u"\u0DB9", 'sinhala amba bayanna'), # ඹ
        XK_Sinh_ya: d('Sinh_ya', u"\u0DBA", 'sinhala yayanna'), # ය
        XK_Sinh_ra: d('Sinh_ra', u"\u0DBB", 'sinhala rayanna'), # ර
        XK_Sinh_la: d('Sinh_la', u"\u0DBD", 'sinhala dantaja layanna'), # ල
        XK_Sinh_va: d('Sinh_va', u"\u0DC0", 'sinhala vayanna'), # ව
        XK_Sinh_sha: d('Sinh_sha', u"\u0DC1", 'sinhala taaluja sayanna'), # ශ
        XK_Sinh_ssha: d('Sinh_ssha', u"\u0DC2", 'sinhala muurdhaja sayanna'), # ෂ
        XK_Sinh_sa: d('Sinh_sa', u"\u0DC3", 'sinhala dantaja sayanna'), # ස
        XK_Sinh_ha: d('Sinh_ha', u"\u0DC4", 'sinhala hayanna'), # හ
        XK_Sinh_lla: d('Sinh_lla', u"\u0DC5", 'sinhala muurdhaja layanna'), # ළ
        XK_Sinh_fa: d('Sinh_fa', u"\u0DC6", 'sinhala fayanna'), # ෆ
        XK_Sinh_al: d('Sinh_al', u"\u0DCA", 'sinhala al-lakuna'), # ්
        XK_Sinh_aa2: d('Sinh_aa2', u"\u0DCF", 'sinhala aela-pilla'), # ා
        XK_Sinh_ae2: d('Sinh_ae2', u"\u0DD0", 'sinhala aeda-pilla'), # ැ
        XK_Sinh_aee2: d('Sinh_aee2', u"\u0DD1", 'sinhala diga aeda-pilla'), # ෑ
        XK_Sinh_i2: d('Sinh_i2', u"\u0DD2", 'sinhala is-pilla'), # ි
        XK_Sinh_ii2: d('Sinh_ii2', u"\u0DD3", 'sinhala diga is-pilla'), # ී
        XK_Sinh_u2: d('Sinh_u2', u"\u0DD4", 'sinhala paa-pilla'), # ු
        XK_Sinh_uu2: d('Sinh_uu2', u"\u0DD6", 'sinhala diga paa-pilla'), # ූ
        XK_Sinh_ru2: d('Sinh_ru2', u"\u0DD8", 'sinhala gaetta-pilla'), # ෘ
        XK_Sinh_e2: d('Sinh_e2', u"\u0DD9", 'sinhala kombuva'), # ෙ
        XK_Sinh_ee2: d('Sinh_ee2', u"\u0DDA", 'sinhala diga kombuva'), # ේ
        XK_Sinh_ai2: d('Sinh_ai2', u"\u0DDB", 'sinhala kombu deka'), # ෛ
        XK_Sinh_o2: d('Sinh_o2', u"\u0DDC", 'sinhala kombuva haa'), # ො
        XK_Sinh_oo2: d('Sinh_oo2', u"\u0DDD", 'sinhala kombuva haa diga'), # ෝ
        XK_Sinh_au2: d('Sinh_au2', u"\u0DDE", 'sinhala kombuva haa gayanukitta'), # ෞ
        XK_Sinh_lu2: d('Sinh_lu2', u"\u0DDF", 'sinhala gayanukitta'), # ෟ
        XK_Sinh_ruu2: d('Sinh_ruu2', u"\u0DF2", 'sinhala diga gaetta-pilla'), # ෲ
        XK_Sinh_luu2: d('Sinh_luu2', u"\u0DF3", 'sinhala diga gayanukitta'), # ෳ
        XK_Sinh_kunddaliya: d('Sinh_kunddaliya', u"\u0DF4", 'sinhala kunddaliya'), # ෴
    },

}