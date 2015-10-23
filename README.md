This is not an official Google product.

# Terminal.app Function Keys
Mac OS X Terminal.app profile which enables functional keys with modifiers.

It's a known problem that a lot of proper keyboard shortcuts, like <kbd>Shift-F2</kbd>
or <kbd>Alt-PgUp</kbd> do not work properly when used from Mac OS X Terminal.app

I created this Terminal.app profile which enables
all the combinations of <kbd>F1</kbd>-<kbd>F12</kbd>, cursor keys, page up/down
with shift, alt and control.

## How to use?
Download `Function Keys.terminal` file and import it into Terminal
(Preferences|Profile| * |Import...).
This may require Mac OS X Yosemite or later to be installed.

In case you're using compact Apple keyboard:

```
PgUp:        Fn-Up
PgDn:        Fn-Down
Home:        Fn-Left
End:         Fn-Right
```

## Other useful shortcuts
For some reason known shortcuts for linux terminals do not work properly. So, shortcuts like
<kbd>Control-W</kbd> could still be useful.

## Is it working at all?
There are some tricks as bare mac os bash abd byobu/tmux implement keyboard handling differently.
For example: `\0331;1P` is recognised as <kbd>F1</kbd> in `byobu/tmux`, but is not a valid
combination in bash itself, as `\033OP` works for both.


# Full list of all bindings

You can do it by hand, if you don't want to use my files:

```
Key     Action
     F1 \033OP
    ⇧F1 \033[1;2P
    ⌥F1 \033[1;3P
    ⌃F1 \033[1;5P
   ⌥⇧F1 \033[1;4P
   ⌃⇧F1 \033[1;6P
   ⌥⌃F1 \033[1;7P
  ⌥⌃⇧F1 \033[1;8P
     F2 \033OQ
    ⇧F2 \033[1;2Q
    ⌥F2 \033[1;3Q
    ⌃F2 \033[1;5Q
   ⌥⇧F2 \033[1;4Q
   ⌃⇧F2 \033[1;6Q
   ⌥⌃F2 \033[1;7Q
  ⌥⌃⇧F2 \033[1;8Q
     F3 \033OR
    ⇧F3 \033[1;2R
    ⌥F3 \033[1;3R
    ⌃F3 \033[1;5R
   ⌥⇧F3 \033[1;4R
   ⌃⇧F3 \033[1;6R
   ⌥⌃F3 \033[1;7R
  ⌥⌃⇧F3 \033[1;8R
     F4 \033OS
    ⇧F4 \033[1;2S
    ⌥F4 \033[1;3S
    ⌃F4 \033[1;5S
   ⌥⇧F4 \033[1;4S
   ⌃⇧F4 \033[1;6S
   ⌥⌃F4 \033[1;7S
  ⌥⌃⇧F4 \033[1;8S
     F5 \033[15~
    ⇧F5 \033[15;2~
    ⌥F5 \033[15;3~
    ⌃F5 \033[15;5~
   ⌥⇧F5 \033[15;4~
   ⌃⇧F5 \033[15;6~
   ⌥⌃F5 \033[15;7~
  ⌥⌃⇧F5 \033[15;8~
     F6 \033[17~
    ⇧F6 \033[17;2~
    ⌥F6 \033[17;3~
    ⌃F6 \033[17;5~
   ⌥⇧F6 \033[17;4~
   ⌃⇧F6 \033[17;6~
   ⌥⌃F6 \033[17;7~
  ⌥⌃⇧F6 \033[17;8~
     F7 \033[18~
    ⇧F7 \033[18;2~
    ⌥F7 \033[18;3~
    ⌃F7 \033[18;5~
   ⌥⇧F7 \033[18;4~
   ⌃⇧F7 \033[18;6~
   ⌥⌃F7 \033[18;7~
  ⌥⌃⇧F7 \033[18;8~
     F8 \033[19~
    ⇧F8 \033[19;2~
    ⌥F8 \033[19;3~
    ⌃F8 \033[19;5~
   ⌥⇧F8 \033[19;4~
   ⌃⇧F8 \033[19;6~
   ⌥⌃F8 \033[19;7~
  ⌥⌃⇧F8 \033[19;8~
     F9 \033[20~
    ⇧F9 \033[20;2~
    ⌥F9 \033[20;3~
    ⌃F9 \033[20;5~
   ⌥⇧F9 \033[20;4~
   ⌃⇧F9 \033[20;6~
   ⌥⌃F9 \033[20;7~
  ⌥⌃⇧F9 \033[20;8~
    F10 \033[21~
   ⇧F10 \033[21;2~
   ⌥F10 \033[21;3~
   ⌃F10 \033[21;5~
  ⌥⇧F10 \033[21;4~
  ⌃⇧F10 \033[21;6~
  ⌥⌃F10 \033[21;7~
 ⌥⌃⇧F10 \033[21;8~
    F11 \033[23~
   ⇧F11 \033[23;2~
   ⌥F11 \033[23;3~
   ⌃F11 \033[23;5~
  ⌥⇧F11 \033[23;4~
  ⌃⇧F11 \033[23;6~
  ⌥⌃F11 \033[23;7~
 ⌥⌃⇧F11 \033[23;8~
    F12 \033[24~
   ⇧F12 \033[24;2~
   ⌥F12 \033[24;3~
   ⌃F12 \033[24;5~
  ⌥⇧F12 \033[24;4~
  ⌃⇧F12 \033[24;6~
  ⌥⌃F12 \033[24;7~
 ⌥⌃⇧F12 \033[24;8~
      ← \033[D
     ⇧← \033[1;2D
     ⌥← \033[1;3D
     ⌃← \033[1;5D
    ⌥⇧← \033[1;4D
    ⌃⇧← \033[1;6D
    ⌥⌃← \033[1;7D
   ⌥⌃⇧← \033[1;8D
      ↑ \033[A
     ⇧↑ \033[1;2A
     ⌥↑ \033[1;3A
     ⌃↑ \033[1;5A
    ⌥⇧↑ \033[1;4A
    ⌃⇧↑ \033[1;6A
    ⌥⌃↑ \033[1;7A
   ⌥⌃⇧↑ \033[1;8A
      → \033[C
     ⇧→ \033[1;2C
     ⌥→ \033[1;3C
     ⌃→ \033[1;5C
    ⌥⇧→ \033[1;4C
    ⌃⇧→ \033[1;6C
    ⌥⌃→ \033[1;7C
   ⌥⌃⇧→ \033[1;8C
      ↓ \033[B
     ⇧↓ \033[1;2B
     ⌥↓ \033[1;3B
     ⌃↓ \033[1;5B
    ⌥⇧↓ \033[1;4B
    ⌃⇧↓ \033[1;6B
    ⌥⌃↓ \033[1;7B
   ⌥⌃⇧↓ \033[1;8B
      ↖ \033[H
     ⇧↖ \033[1;2H
     ⌥↖ \033[1;3H
     ⌃↖ \033[1;5H
    ⌥⇧↖ \033[1;4H
    ⌃⇧↖ \033[1;6H
    ⌥⌃↖ \033[1;7H
   ⌥⌃⇧↖ \033[1;8H
      ↘ \033[F
     ⇧↘ \033[1;2F
     ⌥↘ \033[1;3F
     ⌃↘ \033[1;5F
    ⌥⇧↘ \033[1;4F
    ⌃⇧↘ \033[1;6F
    ⌥⌃↘ \033[1;7F
   ⌥⌃⇧↘ \033[1;8F
      ⇞ \033[5~
     ⇧⇞ \033[5;2~
     ⌥⇞ \033[5;3~
     ⌃⇞ \033[5;5~
    ⌥⇧⇞ \033[5;4~
    ⌃⇧⇞ \033[5;6~
    ⌥⌃⇞ \033[5;7~
   ⌥⌃⇧⇞ \033[5;8~
      ⇟ \033[6~
     ⇧⇟ \033[6;2~
     ⌥⇟ \033[6;3~
     ⌃⇟ \033[6;5~
    ⌥⇧⇟ \033[6;4~
    ⌃⇧⇟ \033[6;6~
    ⌥⌃⇟ \033[6;7~
   ⌥⌃⇧⇟ \033[6;8~
      ⌦ \033[3~
     ⇧⌦ \033[3;2~
     ⌥⌦ \033[3;3~
     ⌃⌦ \033[3;5~
    ⌥⇧⌦ \033[3;4~
    ⌃⇧⌦ \033[3;6~
    ⌥⌃⌦ \033[3;7~
   ⌥⌃⇧⌦ \033[3;8~
```
