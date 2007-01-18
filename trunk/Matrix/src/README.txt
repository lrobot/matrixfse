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
<p></p>
Alternatives to this program are <a href="http://they.misled.us/dark-room"  title="Darkroom fullscreen editor">darkroom</a> and <a href="http://www.hogbaysoftware.com/product/writeroom"  title="WriteRoom fullscreen editor">WriteRoom</a>.
Both of these applications are fullscreen editors. WriteRoom is for Mac only, Darkroom is for Windows only. 
As for Linux there is an alternative approach <a href="http://wiredearth-en.blogspot.com/2007/01/darkroom-deluxe-for-linux.html">here</a>
You may want to have a look at those three products.
<p></p>
Darkroom requires .NET 2.0 which is where my problems started....<br>
-I don't have .NET at every pc i work with, nor can i or do i want to install it everywhere.<br>
<br>
Writeroom is for Mac only which I don't have<br>
And the linux solution came after i started work on Matrix and frankly i don't like emacs.
<p></p>
Since i am still learning Python and such a thing is allways a good excercise i simply made it with Python.
<p></p>
The outcome i called "Matrix" in analogy to the computer-screens in the film. Matrix is a fullscreen editor, simple, easy, with no extra special features that nobody needs (well at least I don't). It loads and saves, allows to copy, paste,cut and change the font (size, color). I found the ability to go fullscreen very good. No other applications, task bars etc. to distract you.
Spellchecking and a way to call some external programs will be included in the next versions (i hope).
Personally i still need to start some structured text functionality.
<p></p>
Here are the current releases:
-<a href="http://downloads.codeboje.de/Matrix.exe"  title="Matrix Release 0.3b">0.3b (Windows installer) </a>
-<a href="http://downloads.codeboje.de/Matrix.zip"  title="Matrix Release 0.3b">0.3 b(python sources) </a>
<p></p>Best thing to do after starting is pressing "Ctrl-p" to get an overview of shortcuts.
<p></p>
<pre>
<strong>Requirements</strong>

 -  Windows / Linux (not tested) / Mac (not tested)
 -  Python (developed  under 2.5 but should work with older versions too)

<strong>Keyboard Shortcuts</strong>

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
        o Undo: Ctrl+U
        o Redo: Ctrl+R
        o Select All: Ctrl+A
        
  Control Features
        o Toggle Fullscreen: Ctrl+T
	o Preferences: Ctrl+P
		
<strong> Bugs </strong>

        o Taskbar doesnt disaapear under Windows2000 no clue why
        

Changelist

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

