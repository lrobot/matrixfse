#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#concentration of thought =   gyounen
#author: Kerim Mansour
#version 0.6 (TK Version 0.3)
#changes from 0.5
#-changed default encoding to utf8 (kanji work now)
#-added a try, except routine to allow users to save the data in case of an error
#changes from 0.4
#-fixed flag for modofication of files (now only true when actually modified)
#-added more commands (see help panel (ctrl-p))
#-fixed some bugs for setting the title of the window
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
"""
License:
Copyright (c) 2006,2007 Kerim Mansour
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
import Tkinter, traceback
import tkFileDialog,tkFont, tkMessageBox, configDialog
from ConfigParser import  *

class Gyounen_App(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.loadConfig()
        self.initializeGUI()
        self.fileName=""
        #self.encoding = "iso-8859-1"
        self.encoding = "utf8"
        self.w,self.h=self.winfo_screenwidth(),self.winfo_screenheight()
        if self.cfg.get('GUI', 'startfullscreen')=="True":
            self.fullscreen=False 
        self.toggleFullScreen(None)
        self.bindEvents()
        self.modified=False
    
    #------------------------  methods without event binding (all with lower first character)------------------------
    def bindEvents(self):
        self.bind("<Control-t>", self.toggleFullScreen)
        self.bind("<Control-p>", self.OnPreferences)
        self.bind("<Control-l>",self.OnLoadFile)
        self.bind("<Control-s>",self.OnSave)
        self.bind("<Control-a>",self.OnSelectAll)
        self.bind("<Control-n>",self.OnNew)
        self.bind("<Control-q>", self.OnQuit)
        self.bind("<Control-v>", self.OnPaste)
        self.bind("<Control-u>", self.OnUndo)
        self.bind("<Control-r>", self.OnRedo)
        self.bind("<Key>", self.OnKey)
    
    def getConfiguredFont(self, confweight):
        return tkFont.Font(family=self.cfg.get('FONT', 'family'), size=int(self.cfg.get('FONT', 'size')), weight=confweight)
        
    def reconfigureLayout(self):
        """ used to set the font in the textfield 
            after changes in the preferences
        """
        confweight=tkFont.NORMAL
        if self.cfg.get('FONT', 'weight')=='bold':
            confweight=tkFont.BOLD
        configuredfont=self.getConfiguredFont(confweight)
        self.text.configure(font=configuredfont)
        bgColour, fgColour=self.getColour()
        self.text.configure(background=bgColour)
        self.text.configure(foreground=fgColour)
        
        if self.leftPane != None:
            self.leftPane.configure(background=bgColour)
        if self.rightPane != None:
            self.rightPane.configure(background=bgColour)
        
    def toggleFullScreen(self, event):
        if self.fullscreen==False:
            self.overrideredirect(1)
            self.geometry("%dx%d+0+0"%(self.w,self.h)) 
            self.fullscreen=True           
        else:
            self.overrideredirect(0)
            self.geometry("%dx%d+0+0"%(800,600))
            self.fullscreen=False
    
    def getText(self):
        """ used to get non-ascii text saved correctly
        """ 
        return self.text.get(1.0,Tkinter.END).encode(self.encoding)
    
    
                
    def setTitle(self):
        if len(self.fileName)>1:
            if self.modified==True:
                self.title(self.fileName+"*")
            else:
                self.title(self.fileName)
        else:
            self.title("Gyounen - Full Screen Editor (TK-Version 0.1)")
    
    def getColour(self):
        r,g,b=self.cfg.get('GUI', 'bgcolor1'), self.cfg.get('GUI', 'bgcolor2'),self.cfg.get('GUI', 'bgcolor3')        
        bgColour = '#%02x%02x%02x' %  (int(r), int(g), int(b))
        r,g,b=self.cfg.get('FONT', 'fgcolor1'),self.cfg.get('FONT', 'fgcolor2'),self.cfg.get('FONT', 'fgcolor3')
        fgColour = '#%02x%02x%02x' %  (int(r), int(g), int(b))
        return (bgColour, fgColour)
    
    def initializeGUI(self):
        self.grid()
        bgColour, fgColour=self.getColour()
        leftPanel=self.cfg.get('GUI','leftPanel')=='True'
        rightPanel=self.cfg.get('GUI','rightPanel')=='True'
        #do only display and configure those panels that are wanted
        if leftPanel:
            self.leftPane = Tkinter.Label(self,anchor="w",fg="white",bg=bgColour)
            self.leftPane.grid(column=0,row=0,sticky='EWNS')
        else:
            self.leftPane=None
        if rightPanel:
            self.rightPane = Tkinter.Label(self,anchor="w",fg="white",bg=bgColour)
            if leftPanel:
                self.rightPane.grid(column=2,row=0,sticky='EWNS')
                self.grid_columnconfigure(2,weight=1)
            else:
                self.rightPane.grid(column=1,row=0,sticky='EWNS')
                self.grid_columnconfigure(1,weight=1)
        else:
            self.rightPane=None
        
        confweight=tkFont.NORMAL
        if self.cfg.get('FONT', 'weight')=='bold':
            confweight=tkFont.BOLD
            
        configuredfont=configuredfont=self.getConfiguredFont(confweight)
        #TODO: check what configuredwidth was for with the panels
        if leftPanel | rightPanel:
            cfgwidth=int(self.cfg.get('GUI','textareawidth'))
            self.text = Tkinter.Text(self, undo=1,font=configuredfont, width=cfgwidth,insertbackground=fgColour,borderwidth=0,background=bgColour, foreground=fgColour,wrap='word')
            self.text.grid(column=1,row=0,sticky='EWNS')
        else:
            self.text = Tkinter.Text(self, font=configuredfont, insertbackground=fgColour,borderwidth=0,background=bgColour, foreground=fgColour,wrap='word')
            self.text.grid(column=0,row=0,sticky='EWNS')
            
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.text.edit_reset()
        self.text.focus_set()
       
    def loadConfig(self):    
        self.cfg = ConfigParser()
        try:
            self.cfg.read('Gyounentk.config')
        except:
            print "No config file found, initializing defaults"
            self.InitConfigDefaults()
            
    #TODO: fill info if something is amiss
    def initConfigDefaults(self):
        self.cfg.set('GUI', 'version','0.1')
        self.cfg.set('GUI', 'startfullscreen','True')
        self.cfg.set('GUI', 'leftPanel','True')
        self.cfg.set('GUI', 'rightPanel','True')
        self.cfg.set('GUI', 'textareawidth','100')
        self.cfg.set('FONT', 'underlined','False')
        self.cfg.set('FONT', 'size','12')
        self.cfg.set('FONT', 'family','courier')
        self.cfg.set('FONT', 'weight','normal')
        self.cfg.set('FONT', 'fgcolor1','0')
        self.cfg.set('FONT', 'fgcolor2','255')
        self.cfg.set('FONT', 'fgcolor3','0')
        self.cfg.set('GUI', 'bgcolor1','0')
        self.cfg.set('GUI', 'bgcolor2','0')
        self.cfg.set('GUI', 'bgcolor3','0')
    #------------------------------ methods for bindings ---------------------------
    def OnKey(self,event):    
        """ used to mark the text as dirty after a key was pressed
        """  
        if event.char != '': 
          self.text.edit_separator()
          self.modified=True
        #self.text.edit_modified(True)
    
    def OnUndo(self,event):
        try:
            self.text.edit_undo()
            self.modified=True
            #self.text.edit_modified(True)
        except:
            pass #undo stack is empty
    
    def OnRedo(self,event):
        try:
            self.text.edit_redo()
            self.modified=True
            #self.text.edit_modified(True)
        except:
            pass #redo stack is empty
        
    def OnPreferences(self,event):
        cd = configDialog.ConfigDialog(self, 'Preferences')
        
    def OnPaste(self,event):
        #apart of the build in paste functionality we set the position 
        self.text.see(Tkinter.INSERT)
        self.modified=True
        #self.text.edit_modified(True)
        self.setTitle()
    
    def OnSelectAll(self, event):
        self.text.tag_add(Tkinter.SEL, "1.0", Tkinter.END)         
        
    def OnQuit(self,event):
          if self.modified==True:
            if tkMessageBox.askyesno("Text was modified", "Do you want to save before quitting ?"):
                if self.OnSave(None):
                  event.widget.quit()
            else:
              event.widget.quit()
          else:
              event.widget.quit()
        
        
    def OnLoadFile(self,event):
        self.fileName = tkFileDialog.askopenfilename()
        if len(self.fileName)>1:
            f=open(self.fileName,'r')
            self.text.delete("1.0", Tkinter.END)
            self.text.insert(Tkinter.INSERT,f.read())
            self.modified=False
            self.setTitle()
            
    def OnSave(self,event):
      try: 
        if self.fileName=="":
            self.OnSaveAs()
            return
        f=open(self.fileName,'w')
        f.write(self.getText())
        f.close()
        self.modified=False
        return True
      except:
        tkMessageBox.showwarning("Could not save", "Could not save, please copy your text and paste it into some other editor. Please send this error (screenshot) to codeboje.de. \nDetails: \n"+traceback.format_exc())
        
        
    def OnSaveAs(self): 
        self.fileName=tkFileDialog.asksaveasfilename()
        if len(self.fileName)>1:
            f=open(self.fileName,'w')
            f.write(self.getText())
            f.close()
            self.modified=False
            self.setTitle()
            
    
    def OnNew(self,event):
        self.fileName=""
        self.setTitle()
        self.text.delete(1.0,Tkinter.END)
        self.modified=False
        self.text.edit_reset()
    #------------------------------ methods for bindings end ---------------------------        

        
if __name__ == "__main__":
    app = Gyounen_App(None)
    app.title('Gyounen - Full Screen Editor 0.5 (TK-Version 0.2)')
    app.mainloop()