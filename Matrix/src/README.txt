RELEASE NOTES


INSTALLATION:
1) Exract the zip into any folder of your choice
2) Run Matrix.exe



RELEASE NOTES:
Version 0.2
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

changes from 0.1
--included two side panels and put the textcontrol in between them
-- switched to utf-8
--included configuration mechanism (load cfg ok, save missing !)
--cleaned up some code (refactoring, extracting methods)


Requirements

 -  Windows / Linux (not tested) / Mac (not tested)
 -  Python (developed  under 2.5 but should work with older versions too)
 -  wxPython (used 0.8.1 but should work with others too)

Keyboard Shortcuts

  File Menu
        o New  Document: Ctrl+N
        o Load Document: Ctrl+L
        o Save Document: Ctrl+S
        o Save Document: None
        o Quit: Ctrl+Q
  Edit Menu
        o Undo: Ctrl+Z
        o Redo: Ctrl+Y
        o Cut: Ctrl+X
        o Copy: Ctrl+C
        o Paste: Ctrl+V
        o Select All: Ctrl+A
        o Change Font: Ctrl+O
  Control Menu
        o Toggle Fullscreen: Ctrl+T

Bugs 

        o Scrollbar should either be disabled or changed in color to match the color of the font selected
        o Using Windows XP the task bar occationally is NOT covered by the app. 
           Seems there is a problem with the property to display the task bar allways as top most component. 
           Sometimes it works despite that property, sometimes it doesn't

Future release plan
               
        o 0.3
                - i18n support
 		- solve scrollbar problem
                - load and save configuration file
        o 0.4
                - statistics functionality (word count, line count)
                - add spell checker functionality


This release is for windows and was generated with p2exe. Since i am not sure what dlls are present on your system i added those that where not part of my windows\system directory. The size increased to around 5 MB that way, but i wanted to make sure it works.
See if you can drop some files and tell me which one. I will try to make a "base package" with those files the majority needed and an "additional dll" package for the rest.
Apart of those files in the release you might need the following which SHOULD BE already present:
 OLEAUT32.dll 
 USER32.dll 
 COMCTL32.dll
 SHELL32.dll 
 ole32.dll 
 WINMM.dll
 WSOCK32.dll 
 comdlg32.dll
 ADVAPI32.dll
 GDI32.dll
 KERNEL32.dll 
 RPCRT4.dll 

If you have python and wxPython installed or simply run linux or max you can drop me a line for the sources. I do not want to publish them at the moment for fairness reasons (WriteRoom makes some money with its product and darkroom respects that as well so far).

License issues
The program is as of 0.1 (and most probably for all versions to come) free to use. Sourcecode WILL be generally available at some future time, i am not yet sure however under what licence that exactly will be. So the program IS free but does NOT come without "cost".
The price is at least one comment in this post about the program. I want to know who uses it, why and what he likes, dislikes, misses etc. So if you use it please do drop me a line.
And if you are so overwhelmed with this programs features that you really dont know how to say thanks (ok ... i am joking) then you can of course allways drop 5 bucks and make me happy the materialistic way as well. 
Just go to http://codeboje.de/blog/archives/Matrix-Fullscreen-Editor.html and click on the donate button.
