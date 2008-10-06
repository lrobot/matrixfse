#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
 
import Tkinter
"""
License:
Copyright (c) 2008 Kerim Mansour
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

states=['black','white','red','blue','green']
introtext="""Hi and welcome to MCTU.
This program will cycle through 5 different colors while in fullscreen so you can check your TFT monitor.
Each pixel is made up of three transistors in your TFT (one for red, one for blue and one for green).
Any color can be represented through the combination of these three colors.
So defects can be determined by going through these three colors plus white and black.

Black means that all transistors should be deactivated. 
If you see something then there is at least one transistor defect and always on. 

White means that all transistors should be activated. 
If you see some pixel in a different color then it means that at least one transistor is defect and always off.

Red means that only those transistors for red should be active. 
If you see a different color then you know that at least one transistor is always on/of and it is NOT the red one.

Blue means that only those transistors for blue should be active. 
If you see a different color then you know that at least one transistor is always on/of and it is NOT the blue one.

Green means that only those transistors for green should be active. 
If you see a different color then you know that at least one transistor is always on/of and it is NOT the green one.

So basically you can determine any defect by combining the results of these 5 tests.

Go through the colors by pressing ANY key.
Exit this program at any time by using either the Escape key or Control-q
"""
class MCTU(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.state=-1
    self.setFullScreen()
    self.grid()
    self.pane = Tkinter.Label(self, text=introtext,font=("Helvetica", 16),background='black', foreground='white')
    self.pane.grid(column=0,row=0,sticky='EWNS')
    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.bind("<Control-q>", self.OnQuit)
    self.bind("<Key-Escape>", self.OnQuit)
    self.bind("<Key>", self.OnKey)
    
  def setFullScreen(self):
    self.w,self.h=self.winfo_screenwidth(),self.winfo_screenheight()
    self.overrideredirect(1)
    self.geometry("%dx%d+0+0"%(self.w,self.h))
  
  def OnQuit(self,event):
    event.widget.quit()
    
  def OnKey(self,event):
    self.state+=1
    if self.state>=len(states):
      self.state=0
    self.switchColorStates()
  
  def switchColorStates(self):
    if self.state<len(states):
      self.pane.configure(text="",background=states[self.state])

if __name__ == "__main__":
    app = MCTU(None)
    app.title('MCTU - Monitor Calibration and Testing Utility')
    app.mainloop()
    