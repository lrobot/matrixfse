RELEASE NOTES


INSTALLATION:
WINDOWS:
1) Use the installer
2) Run Matrix.exe

LINUX/MAC:
1) Extract the zip
2) Run matrix.py


RELEASE NOTES:
Version 0.3b
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


Changelist
#version 0.3b (TK Version 0.1b)
#changes from 0.3
#-added undo (ctrl-u)
#-added redo (ctrl-r)
#-fixed a bug related to setting background in the side panels
#changes from 0.2
#-switched to Tkinter
#-removed Scrollbar
#-added configuration panel (colors, font, textareawidth, left and right panel)
#-configuration is saved completely now
#changes from 0.1
#-included two side panels and put the textcontrol in between them
#-switched to utf-8
#-included configuration mechanism (load cfg ok, save missing !)
#-cleaned up some code (refactoring, extracting methods)


Requirements

 -  Windows / Linux (not tested) / Mac (not tested)
 -  Python (developed  under 2.5 but should work with older versions too)
 

File Features
        o New  Document: Ctrl+N
        o Load Document: Ctrl+L
        o Save Document: Ctrl+S
        o Save As Document: None
        o Quit: Ctrl+Q

  Edit Features
        o Cut: Ctrl+X
        o Copy: Ctrl+C
        o Paste: Ctrl+V
        o Select All: Ctrl+A

  Control Features
        o Toggle Fullscreen: Ctrl+T
		o Preferences: Ctrl+P

Bugs 
 o None that i am aware of


Future releases
        o 0.4
                - configurable documents directory
                - i18n
                - better support for encoding

        o 0.5
                - aspell / ispell integration
                - run any external program with edited text as input

