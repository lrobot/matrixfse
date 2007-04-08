import sys, wx, webbrowser
import mem
from ctypes import *
"""
License:
Copyright (c) 2007, Kerim Mansour
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

ID_ICON_TIMER = wx.NewId()
OPEN_BROWSER=wx.NewId()

class StatusMeterTaskBarIcon(wx.TaskBarIcon):

    def __init__(self, parent):
        wx.TaskBarIcon.__init__(self)
        self.parentApp = parent
        self.CreateMenu()

    # Create the menu
    def CreateMenu(self):
        self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.ShowMenu)
        self.Bind(wx.EVT_MENU, self.parentApp.OpenBrowser, id=OPEN_BROWSER)
        self.menu=wx.Menu()
        self.menu.Append(OPEN_BROWSER, "Visit codeboje","This will open a new Browser tab")
        self.menu.AppendSeparator()
        self.menu.Append(wx.ID_EXIT, "Close App")
          
    def ShowMenu(self,event):
        self.PopupMenu(self.menu)
     
    #This will create and set the icon that is displayed in the taskbar   
    def SetIconImage(self,text,font=None,fgColor=wx.WHITE,bgColor=wx.BLACK_BRUSH):
        #create a new empty icon and an empty bitmap for the text
        self.noIcon = wx.EmptyIcon()
        self.bitmap=wx.EmptyBitmap(48,48)
        #create a MemoryDC for the pain operations
        memory = wx.MemoryDC()
        
        #Set the font depending on the length of the text (TODO: not yet looking good for
        # sizes > 1 GB)
        if len(text)>3:
            if not font:
                font=self.createDefaultFont()
            size = font.GetPointSize()-1
            size=size-2
            font.SetPointSize(size)
            memory.SetFont(font)
        else:
            if not font:
                font=self.createDefaultFont()
            size = font.GetPointSize()-1
            font.SetPointSize(size)
            memory.SetFont(font)        
        
        #set the foreground color
        if fgColor:
                memory.SetTextForeground( fgColor )
        
        #write free mem size into the bitmap
        self.write(text,self.bitmap,memory,(0,0),fgColor,bgColor)
        #copy bitmap data into the icon
        self.noIcon.CopyFromBitmap(self.bitmap)
        #set the icon
        self.SetIcon(self.noIcon, "Free mem:"+text+ "megabytes")
        
    #if no font is given this font will be used
    def createDefaultFont(self):
        font=wx.FFont(21,wx.FONTFAMILY_DEFAULT)
        return font

    #writes the size of free memory onto the bitmap after drawing the background
    def write(self,  text, bitmap, memory,pos=(0,0), fgColor=wx.WHITE, bgColor=wx.GREEN_BRUSH):
        memory.SelectObject( bitmap )
        memory.SetBrush(bgColor)
        try:
            memory.DrawRectangle(pos[0],pos[1],48,48)
            memory.DrawText(text, pos[0],pos[1])
        finally:
            memory.SelectObject( wx.NullBitmap)
        return bitmap
    

        
class StatusMeterFrame(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, -1, title, size = (1, 1),
            style=wx.FRAME_NO_TASKBAR|wx.NO_FULL_REPAINT_ON_RESIZE)
       
        self.tbicon = StatusMeterTaskBarIcon(self)
        self.tbicon.Bind(wx.EVT_MENU, self.exitApp, id=wx.ID_EXIT) 
        self.timer=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.CheckMemory)
        self.timer.Start(300) # 300 milliseconds
        self.Show(True)
        
    def exitApp(self,event):
        self.timer.Stop()
        self.tbicon.RemoveIcon()
        self.tbicon.Destroy()
        sys.exit()
        
    def OpenBrowser(self,event):
        webbrowser.open('http://codeboje.de/blog/pages/donate.html')
    
    def OpenPrefs(self,event):
        pass
    
    def CheckMemory(self,event):
        memstatus = mem._MEMORYSTATUS()
        windll.kernel32.GlobalMemoryStatus(byref(memstatus ))
        total,free= memstatus.show()
        ffree=int(float(free)/1048576) #in megabytes
        self.tbicon.SetIconImage(str(ffree))
        
#---------------- run the program -----------------------
def main(argv=None):
    app = wx.App(False)
    frame = StatusMeterFrame(None, -1, ' ')
    frame.Show(False)
    app.MainLoop()

if __name__ == '__main__':
    main()