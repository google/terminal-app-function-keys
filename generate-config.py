#!env python
# -*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Regenerate "Function Keys.terminal" config file.
# Creates correct xterm mappings for Fn and cursor keys with modificators.
# This config may be created by hand trough Terminal.app itself.

TERMINAL_APP_KEYS = [
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
    "Left", "Up", "Right", "Down", "Home", "End", "PgUp", "PgDown",
    "ForwardDelete",
    # TODO: "Delete", is special it uses different escape codes
]
TERMINAL_APP_MODIFIER_COMBINATIONS = [
    None, "Shift", "Option", "Control",
    "Option-Shift", "Control-Shift", "Option-Control",
    "Option-Control-Shift",
]

# Thanks: http://invisible-island.net/xterm/ctlseqs/ctlseqs.html
#         https://github.com/tmux/tmux/blob/master/xterm-keys.c
XTERM_KEY_ESCAPE_CODES = {
    "F1": "SS3 P",
    "F2": "SS3 Q",
    "F3": "SS3 R",
    "F4": "SS3 S",
    "F5": "CSI 15~",
    "F6": "CSI 17~",
    "F7": "CSI 18~",
    "F8": "CSI 19~",
    "F9": "CSI 20~",
    "F10": "CSI 21~",
    "F11": "CSI 23~",
    "F12": "CSI 24~",
    "Up": "CSI A",
    "Down": "CSI B",
    "Left": "CSI D",
    "Right": "CSI C",
    "Home": "CSI H",
    "End": "CSI F",
    "PgUp": "CSI 5~",
    "PgDown": "CSI 6~",
    "ForwardDelete": "CSI 3~",
    # TODO: "Delete": "CSI 3~", should we try Ctrl-H or \008 or ^??
}
XTERM_KEY_MODIFIER_COMBINATION_CODES = {
    None: "1",
    "Shift": "2",
    "Option": "3",
    "Option-Shift": "4",
    "Control": "5",
    "Control-Shift": "6",
    "Option-Control": "7",
    "Option-Control-Shift": "8",
}
XTERM_ESCAPE_ESCAPES = {
    "SS3": u"\033O",
    "CSI": u"\033[",
}
# Only for "one symbol" key escapes like "SS3 P" when any modifier is on
XTERM_SHORT_MODIFIED_ESCAPE_ESCAPES = {
    "SS3": u"\033[1",
    "CSI": u"\033[1",
}
# Special case for Up/Down and other short sequences

# Thanks: http://heisencoder.net/2008/04/fixing-up-mac-key-bindings-for-windows.html
MAC_KEY_CODES = {
    "F1": "F704",
    "F2": "F705",
    "F3": "F706",
    "F4": "F707",
    "F5": "F708",
    "F6": "F709",
    "F7": "F70A",
    "F8": "F70B",
    "F9": "F70C",
    "F10": "F70D",
    "F11": "F70E",
    "F12": "F70F",
    "Up": "F700",
    "Down": "F701",
    "Left": "F702",
    "Right": "F703",
    "Insert": "F727",
    "Delete": "007F",
    "ForwardDelete": "F728",
    "Home": "F729",
    "End": "F72B",
    "Break": "F732",
    "Tab": "0009",
    "Escape": "001B",
    "Enter": "000A",
    "PgUp": "F72C",
    "PgDown": "F72D",
}
MAC_KEY_MODIFIER_CODES = {
    "Control": "^",
    "Shift": "$",
    "Option": "~",
    "Command": "@",
}

# Thanks: http://apple.stackexchange.com/questions/55727
MAC_GLYPHS = {
    "Apple": u"",
    "Command": u"⌘",
    "Control": u"⌃",
    "Option": u"⌥",
    "Shift": u"⇧",
    "Caps": u"⇪",
    "Delete": u"⌫",
    "ForwardDelete": u"⌦",
    "Tab": u"⇥",
    "Esc": u"⎋",
    "Right": u"→",
    "Left": u"←",
    "Up": u"↑",
    "Down": u"↓",
    "PgUp": u"⇞",
    "PgDown": u"⇟",
    "Home": u"↖",
    "End": u"↘",
    "Space": u"␣",
    "Return": u"↩",
    "Enter": u"⌤",
}

FILE_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ProfileCurrentVersion</key>
	<real>2.04</real>
	<key>keyMapBoundKeys</key>
	<dict>
"""

FILE_KEY_ACTION_ENTRY = """		<key>{}</key>
		<string>{}</string>
"""

FILE_FOOTER = """	</dict>
	<key>name</key>
	<string>Function Keys</string>
	<key>type</key>
	<string>Window Settings</string>
</dict>
</plist>
"""


def main():
    print "Key".ljust(7), "Action"
    f = open("Function Keys.terminal", "w")
    f.write(FILE_HEADER)
    for key in TERMINAL_APP_KEYS:
        assert key
        print_key_code = MAC_GLYPHS[key] if key in MAC_GLYPHS else key
        assert print_key_code   # "F1"
        file_key_code = MAC_KEY_CODES[key]
        assert file_key_code    # "F704"
        escape, code = XTERM_KEY_ESCAPE_CODES[key].split(" ")
        assert escape, code     # "SS3", "P"
        for modifiers_combination in TERMINAL_APP_MODIFIER_COMBINATIONS:
            if len(code) == 1 and modifiers_combination:
                xterm_escape = XTERM_SHORT_MODIFIED_ESCAPE_ESCAPES[escape]
            else:
                xterm_escape = XTERM_ESCAPE_ESCAPES[escape]
            assert xterm_escape     # "\033[1"
            print_key_modifier = "" if not modifiers_combination else "".join(
                [MAC_GLYPHS[x] for x in modifiers_combination.split("-")])
            assert print_key_modifier is not None  # "^"
            file_key_modifier = "" if not modifiers_combination else "".join(
                [MAC_KEY_MODIFIER_CODES[x] for x in modifiers_combination.split("-")])
            assert file_key_modifier is not None   # "^"
            xterm_mod_escape = XTERM_KEY_MODIFIER_COMBINATION_CODES[modifiers_combination]
            assert xterm_mod_escape     # "5"
            if modifiers_combination:
                xterm_key_code = xterm_escape + code[:-1] + ";" + xterm_mod_escape + code[-1]
            else:
                xterm_key_code = xterm_escape + code
            assert xterm_key_code       # "\033O;5P"
            print_action = xterm_key_code.replace(u"\033", "\\033")
            assert print_action         # "\\033O;5P"
            print (print_key_modifier + print_key_code).rjust(7), print_action
            entry_format = FILE_KEY_ACTION_ENTRY.format(
                file_key_modifier + file_key_code, xterm_key_code)
            assert entry_format
            f.write(entry_format)
    f.write(FILE_FOOTER)
    f.close()


if __name__ == '__main__':
    main()
