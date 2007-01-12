#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.stc as stc
from ConfigParser import  *
#from wx.lib.expando import ExpandoTextCtrl, EVT_ETC_LAYOUT_NEEDED
#author: Kerim Mansour
#version 0.2
#changes from 0.1
#-included two side panels and put the textcontrol in between them
#- switched to utf-8
#-included configuration mechanism (load cfg ok, save missing !)
#-cleaned up some code (refactoring, extracting methods)
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

#constants for events
NEW=100
LOAD=101
SAVE=102
SAVE_AS=103
EXIT=104
UNDO=110
REDO=111
CUT=112
COPY=113
PASTE=114
SELECT_ALL=115
GOTO=120
FIND=121
REPLACE=122
CHANGE_FONT=150
FULLSCREEN=200
STATISTICS=201
#----------------------------------------------------------------------
class Matrix(wx.Frame):
    def __init__(self):
        
        wx.Frame.__init__(self, None, title="Matrix")
        self.LoadConfig()
        
        gbs = self.gbs = wx.GridBagSizer(1, 3)
        self.p = wx.Panel(self, -1, style = wx.TAB_TRAVERSAL
                     | wx.CLIP_CHILDREN
                     | wx.FULL_REPAINT_ON_RESIZE
                     )
        gbs = self.gbs = wx.GridBagSizer(1, 3)
        self.text = stc.StyledTextCtrl(self.p, -1, size=(int(self.cfg.get('GUI', 'textareawidth')),0),style=wx.TE_MULTILINE|wx.NO_BORDER|wx.TE_NO_VSCROLL)
        self.text.StyleSetBackground(0,wx.Colour(0,0,0))
        self.text.StyleSetForeground(0,wx.Colour(255,255,255))
        #self.text.SetCaretLineBackground(wx.Colour(0,0,0))
        #self.text.SetLeftMarginWidth(0)
        self.text.SetMarginType(0, stc.STC_MARGIN_NUMBER)
        self.text.SetMarginLeft(0)
        self.text.SetMarginRight(20)
        self.text.SetMarginWidth(0,0)
        self.text.SetBackgroundStyle()
        #self.text.SetMarginLeft(-1,0)
        #print self.text.SetBackgroundColour(wx.Colour(0,0,0))
        self.rightPanel = wx.Panel(self.p,-1,style=wx.NO_BORDER)
        self.leftPanel = wx.Panel(self.p,-1,style=wx.NO_BORDER)
        
        gbs.Add(self.rightPanel,(0,0), flag=wx.EXPAND)
        gbs.Add(self.leftPanel,(0,2), flag=wx.EXPAND)
        gbs.Add(self.text,(0,1), flag=wx.EXPAND)
        gbs.AddGrowableRow(0)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(2)
        self.p.SetSizerAndFit(gbs)
        
        #self.text.Bind(wx.EVT_KEY_DOWN, self.handleKey, source=self.text, id=2000)
        
       
        self.SetFont()
        self.SetColors()
        self.Centre()
        self.CreateMenu()

        self.fileName=""
        
    """       
    def handleKey(self, event):
        #print self.text.GetLastPosition()
        insertion= self.text.GetInsertionPoint()
        #x,y =self.text.PositionToXY(insertion)
        #position=wx.Point(x,y)
        #self.text.ShowPosition(position)
        #self.text.ShowPosition(insertion)
        self.text.ShowPosition(self.text.GetLastPosition ())
        if event.GetKeyCode()!=wx.WXK_DOWN and event.GetKeyCode()!=wx.WXK_UP:
            event.Skip()
            return
        if event.GetKeyCode()==wx.WXK_DOWN:
            scroll=+1
        else: 
            scroll=-1
        print scroll
        self.text.ScrollLines(scroll)
        event.Skip()
  """      
    def SetColors(self):
        bgcol1=int(self.cfg.get('GUI', 'bgcolor1'))
        bgcol2=int(self.cfg.get('GUI', 'bgcolor2'))
        bgcol3=int(self.cfg.get('GUI', 'bgcolor3'))

        fgcol1=int(self.cfg.get('FONT', 'fgcolor1'))
        fgcol2=int(self.cfg.get('FONT', 'fgcolor2'))
        fgcol3=int(self.cfg.get('FONT', 'fgcolor3'))
        
        self.text.SetForegroundColour(wx.Colour(fgcol1,fgcol2,fgcol3))
        self.text.SetBackgroundColour(wx.Colour(bgcol1,bgcol2,bgcol3))
        self.leftPanel.SetBackgroundColour(wx.Colour(bgcol1,bgcol2,bgcol3))
        self.rightPanel.SetBackgroundColour(wx.Colour(bgcol1,bgcol2,bgcol3))
        self.p.SetBackgroundColour(wx.Colour(bgcol1,bgcol2,bgcol3))
        
    def CreateMenu(self):
        self.menu = wx.MenuBar()

        # File Menu
        fileMenu = wx.Menu()
        fileMenu.Append( NEW , "&New\tCtrl+N" )
        fileMenu.Append( LOAD , "&Load\tCtrl+L" )
        fileMenu.Append( SAVE , "&Save\tCtrl+S" )
        fileMenu.Append( SAVE_AS , "Save &as" )
        fileMenu.Append( EXIT , "E&xit\tCtrl+Q" )
        # Edit Menu
        editMenu = wx.Menu()
        editMenu.Append( UNDO , "&Undo\tCtrl+Z" )
        editMenu.Append( REDO , "&Redo\tCtrl+Y" )
        editMenu.AppendSeparator()
        editMenu.Append( CUT , "Cu&t\tCtrl+X" )
        editMenu.Append( COPY , "&Copy\tCtrl+C" )
        editMenu.Append( PASTE , "&Paste\tCtrl+V" )
        editMenu.AppendSeparator()
        editMenu.Append( SELECT_ALL , "Select All\tCtrl+A" )
        editMenu.Append( CHANGE_FONT , "Change F&ont\tCtrl+O" )
        # Search Menu
        searchMenu = wx.Menu()
        searchMenu.Append( GOTO , "&Go to...\tCtrl+G" )
        searchMenu.Append( FIND , "&Find...\tCtrl+F" )
        searchMenu.Append( REPLACE , "&Replace...\tCtrl+R" )
        # Extras Menu
        extrasMenu = wx.Menu()
        extrasMenu.Append( FULLSCREEN , "&FullScreen\tCtrl+T" )
        #extrasMenu.Append( STATISTICS , "&Statistics\tCtrl+T" )
        # Add menus to menubar
        self.menu.Append( fileMenu , "&File" )
        self.menu.Append( editMenu , "&Edit" )
        self.menu.Append( searchMenu , "&Search" )
        self.menu.Append( extrasMenu , "&Control" )
        # Set Menu Events
        self.Bind( wx.EVT_MENU , self.OnNew , id = NEW )
        self.Bind( wx.EVT_MENU , self.OnSave , id = SAVE )
        self.Bind( wx.EVT_MENU , self.OnSaveAs , id = SAVE_AS )
        self.Bind( wx.EVT_MENU , self.OnLoad , id = LOAD )
        self.Bind( wx.EVT_MENU , self.OnClose , id = EXIT )
#        self.Bind( wx.EVT_MENU , self.Refresh , id = 104 )
        self.Bind( wx.EVT_MENU , self.OnUndo , id = UNDO )
        self.Bind( wx.EVT_MENU , self.OnRedo , id = REDO )
        self.Bind( wx.EVT_MENU , self.OnCut , id = CUT )
        self.Bind( wx.EVT_MENU , self.OnCopy , id = COPY )
        self.Bind( wx.EVT_MENU , self.OnPaste , id = PASTE )
        self.Bind( wx.EVT_MENU , self.OnSelectAll , id = SELECT_ALL )
        self.Bind( wx.EVT_MENU , self.OnSelectFont , id = CHANGE_FONT )
        #self.Bind( wx.EVT_MENU , self.OnGoTo , id = GOTO )
        self.Bind( wx.EVT_MENU , self.OnShowFind , id = FIND )
        self.Bind( wx.EVT_MENU , self.OnShowFindReplace , id = REPLACE )
        self.Bind(wx.EVT_FIND, self.OnFind)
        self.Bind(wx.EVT_FIND_NEXT, self.OnFind)
        self.Bind(wx.EVT_FIND_REPLACE, self.OnFind)
        self.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnFind)
        self.Bind(wx.EVT_FIND_CLOSE, self.OnFindClose)
        #self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown, id=200)
        self.Bind(wx.EVT_MENU, self.OnFullScreen, id=FULLSCREEN)
        #self.Bind(wx.EVT_MENU, self.handleHotKey, id=200)
        # Set the menu bar
        self.SetMenuBar( self.menu )

    def LoadConfig(self):    
        self.cfg = ConfigParser()
        try:
            self.cfg.read('Matrix.config')
        except:
            print "No config file found, initializing defaults"
            self.InitConfigDefaults()

    #TODO: fill info 
    def InitConfigDefaults(self):
        self.cfg.set('GUI', 'version','0.1')
        self.cfg.set('GUI', 'startfullscreen','True')
        self.cfg.set('GUI', 'textareawidth','800')
        self.cfg.set('FONT', 'underlined','False')
        self.cfg.set('FONT', 'pointsize','12')
        self.cfg.set('FONT', 'type','76')
        self.cfg.set('FONT', 'style','90')
        self.cfg.set('FONT', 'weight','90')
        self.cfg.set('FONT', 'fgcolor1','0')
        self.cfg.set('FONT', 'fgcolor2','255')
        self.cfg.set('FONT', 'fgcolor3','0')
        self.cfg.set('GUI', 'bgcolor1','0')
        self.cfg.set('GUI', 'bgcolor2','0')
        self.cfg.set('GUI', 'bgcolor3','0')
        
    def SetFont(self):
        font = self.text.GetFont()
        if self.cfg.get('FONT', 'underlined')=="False":
            underlined=False
        else:
            underlined=True
        size=int(self.cfg.get('FONT', 'pointsize'))
        type=int(self.cfg.get('FONT', 'type'))
        style=int(self.cfg.get('FONT', 'style'))
        weight=int(self.cfg.get('FONT', 'weight'))
        font =wx.Font(size,type, style,weight,underlined)
        self.text.SetFont(font)

    def OnSelectFont(self, event):
        fontData=wx.FontData()
        fd=wx.FontDialog(self,wx.FontData())
        fd.GetFontData().SetInitialFont(self.text.GetFont())
        fd.GetFontData().SetColour(self.text.GetForegroundColour()) 
        id = fd.ShowModal()
        if id==wx.ID_OK:
            self.text.SetFont(fd.GetFontData().GetChosenFont())
            self.text.SetForegroundColour(fd.GetFontData().GetColour())
        
        r,g,b =fd.GetFontData().GetColour().Get()
        self.cfg.set('FONT', 'fgcolor1',str(r))
        self.cfg.set('FONT', 'fgcolor2',str(g))
        self.cfg.set('FONT', 'fgcolor3',str(b))
        font = fd.GetFontData().GetChosenFont()
        underlined="False"
        if font.GetUnderlined()==True:
            underlined="True"
        self.cfg.set('FONT', 'underlined',underlined)
        self.cfg.set('FONT', 'pointsize',str(font.GetPointSize()))
        self.cfg.set('FONT', 'type', str(font.GetFamily()))
        self.cfg.set('FONT', 'style',str(font.GetStyle()))
        self.cfg.set('FONT', 'weight',str(font.GetWeight()))
        self.SaveConfig()
        fd.Destroy()
        
    def SetTitle(self, title=None):
        if title==None:
            super(Matrix,self).SetTitle(self.fileName)
        else:
            super(Matrix,self).SetTitle(title)
            self.fileName=title
            
    def OnLoad(self, event): 
        loadDialog=wx.FileDialog(self, style=wx.FD_OPEN)
        if loadDialog.ShowModal()==wx.ID_OK:
            self.fileName=loadDialog.GetPath()
            f=open(self.fileName,'r')
            self.text.SetValue(f.read())
            f.close()
            self.SetTitle()
        loadDialog.Destroy()     
    
    def OnNew(self, event): 
        self.text.Clear()
        self.SetTitle(title="")
        
    def OnSave(self, event): 
        if self.fileName=="":
            self.OnSaveAs(event)
            return
        f=open(self.fileName,'w')
        f.write(self.text.GetValue())
        f.close()
        
    def OnSaveAs(self, event): 
        saveDialog=wx.FileDialog(self, style=wx.FD_SAVE)
        if saveDialog.ShowModal()==wx.ID_OK:
            f=open(saveDialog.GetPath(),'w')
            f.write(self.text.GetValue())
            f.close()
        saveDialog.Destroy()
        
    def OnPaste( self , event = None ):
        self.text.Paste()
        
    def OnRedo( self , event = None ):
        self.text.Redo()

    def OnSelectAll( self , event = None ):
        self.text.SelectAll()
    
    def OnUndo( self , event = None ):
        self.text.Undo()

    def OnCopy( self , event = None ):
        self.text.Copy()

    def OnCut( self , event = None ):
        self.text.Cut()
  
    def OnClose( self , event = None ):
        self.Close()
    
    def OnFullScreen(self, event):
        if self.IsFullScreen():
            self.ShowFullScreen(False)
        else:
            self.ShowFullScreen(True)  
    
    def OnShowFind(self, evt):
        #self.DisableButtons()
        data = wx.FindReplaceData()
        dlg = wx.FindReplaceDialog(self, data, "Find")
        dlg.data = data  # save a reference to it...
        dlg.Show(True)
        


    def OnShowFindReplace(self, evt):
        #self.DisableButtons()
        data = wx.FindReplaceData()
        dlg = wx.FindReplaceDialog(self, data, "Find & Replace", wx.FR_REPLACEDIALOG)
        dlg.data = data  # save a reference to it...
        dlg.Show(True)
        
    def OnFindClose(self, evt):
        evt.GetDialog().Destroy()

    def OnFind( self , event):
        findText = event.GetFindString()
        if findText:
            doc=self.text.GetValue()
            findRes = doc.find(findText, self.text.GetInsertionPoint() ,  self.text.GetLastPosition())
            print findRes
            if findRes != -1:
                end = findRes + len( findText )
                #Problem with the textctrl. text might not be in visible scope and
                #2) selection only after find dialog is closed
                #self.text.EnsureVisible( end )
                self.text.SetInsertionPoint(findRes)
                self.text.SetSelection(findRes,end)
                event.GetDialog().Destroy()
                return True
            else:
                self.MessageDialog("Text not found", "Reached the end of the document").show()
                return False
       

    def OnReplace( self , event):
        if self.text.GetSelection() != "":
            self.text.ReplaceSelection( event.GetReplaceString() )
            return self.OnFind( event )
        else:
            print( "Error" , "Nothing is selected." )
            return False

    def OnReplaceAll( self , event):
        while self.OnReplace( event ):
            pass

        
    """    def OnFind(self, evt):
        map = {
            wx.wxEVT_COMMAND_FIND : "FIND",
            wx.wxEVT_COMMAND_FIND_NEXT : "FIND_NEXT",
            wx.wxEVT_COMMAND_FIND_REPLACE : "REPLACE",
            wx.wxEVT_COMMAND_FIND_REPLACE_ALL : "REPLACE_ALL",
            }

        et = evt.GetEventType()
        
        if et in map:
            evtType = map[et]
        else:
            evtType = "**Unknown Event Type**"

        if et in [wx.wxEVT_COMMAND_FIND_REPLACE, wx.wxEVT_COMMAND_FIND_REPLACE_ALL]:
            replaceTxt = "Replace text: %s" % evt.GetReplaceString()
        else:
            replaceTxt = ""
        completeText= self.text.GetValue()
        print("%s -- Find text: %s   Replace text: %s  Flags: %d  \n" %
                       (evtType, evt.GetFindString(), replaceTxt, evt.GetFlags()))
   """     
    def SaveConfig(self):
        filename = "Matrix.config"
        configFile=open(filename,"w")
        sections= self.cfg.sections()
        for section in sections:
            configFile.write("["+section+"]\n")
            options= self.cfg.options(section)
            for option in options:
                configFile.write(option+":"+self.cfg.get(section, option)+"\n")
        configFile.close()

    # Used to display info, warnings, errors (not in use yet)
    def MessageDialog( self , title , text ):
        dialog = wx.MessageDialog( self , text , title , wx.OK | wx.ICON_INFORMATION )
        dialog.ShowModal()
        dialog.Destroy()

#----------------------------------------------------------------------
app = wx.App(False)
frm = Matrix()
frm.Show()
if frm.cfg.get('GUI', 'startfullscreen')=="True":
    frm.ShowFullScreen(True)
    frm.SaveConfig()
app.MainLoop()

