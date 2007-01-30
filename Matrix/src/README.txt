RELEASE NOTES


INSTALLATION:
WINDOWS:
1) Use the installer
2) Run Matrix.exe

LINUX/MAC:
1) Extract the zip
2) Run matrix.py


RELEASE NOTES:
Version 0.4
"""
License:
Copyright (c) 2006, Kerim Mansour
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation 
      and/or other materials provided with the distribution.
    * Neither the name of the author nor the names of other contributors 
      may be used to endorse or promote products derived from this software without 
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

Press Ctrl+P to get to the preferences showing you also the keybindings.
This software is in development so do not expect it to work perfectly.
IF you find a bug please mail me at kmansourADDwebDOTde

<strong>Requirements</strong>

 -  Windows / Linux (not tested) / Mac (not tested)
 -  Python (developed  under 2.5 but should work with older versions too)

<strong>Keyboard Shortcuts</strong>

  File Features
        o New  Document: Ctrl+N
        o Load Document: Ctrl+L
        o Insert File  : Ctrl+I
        o Save Document: Ctrl+S
        o Save As Document: None
        o Quit: Ctrl+Q
  Edit Features
        o Cut       : Ctrl+X
        o Copy      : Ctrl+C
        o Paste     : Ctrl+V
        o Undo      : Ctrl+U
        o Redo      : Ctrl+R
        o Select All: Ctrl+A
        o Goto Line : Ctrl+G
        o Find      : Alt+F
        o Replace   : Alt+R
        
  Control Features
    o Toggle Fullscreen: Ctrl+T
	o Preferences: Ctrl+P
		
<strong> Bugs </strong>

        o Taskbar doesnt disaapear under Windows2000 no clue why
        

Changelist

0.4 (changes from 0.3b) (30.01.2007)
-added find(ctrl-f)
-added replace(ctrl-r)
-added insert File (ctrl-i)
-added goto Line (ctrl-g)
-switched to utf-8 encoding as default

0.3b (changes from 0.3)  (18.01.2007)
-added undo (ctrl-u)
-added redo (ctrl-r)
-fixed a bug related to setting background in the side panels

0.3 (changes from 0.2) (17.01.2007)
-switched to Tkinter
-removed Scrollbar
-added configuration panel (colors, font, textareawidth, left and right panel)
-configuration is saved completely now

0.2 (changes from 0.1)
--included two side panels and put the textcontrol in between them
-- switched to utf-8
--included configuration mechanism (load cfg ok, save missing !)
--cleaned up some code (refactoring, extracting methods)
--solved Bug: "Fontcolor and style are allways the same at startup (white, monospaced) because (see future plans)"
--changed initial font color to green and size to 12


Future release plans
o 0.5
  - aspell / ispell integration
  - run any external program with edited text as input
  - better support for encoding (detecting encoding of file?)
  - configurable documents directory
  - i18n


