#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
class DecimalField(wx.TextCtrl):
    def __init__(self, parent, ID, title,
                 position, size):
        wx.TextCtrl.__init__(self, parent, ID, title,
                            position, size)
        wx.EVT_CHAR(self, self.OnChar)
        #wx.EVT_KILL_FOCUS(self, self.Finish)
      
    def OnChar(self, event):
        key = event.GetKeyCode()
        print key
        #print event.GetKey
        if key > 47 and key < 58: #range for numbers
            event.Skip()
        elif key == 46: #we allow only for one decimal point 
            if '.' not in self.GetValue():
                if self.GetInsertionPoint() != 0:
                    event.Skip()
        elif key == 8 or key == 127: #backspace and del
            event.Skip()
        elif key== 314 or key == 316: #cursor left and right
            event.Skip()
            
class ConfDialog(wx.Dialog):
    def __init__(
            self, parent, ID, options, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE         
            ):
        
        wx.Dialog.__init__(self,parent,ID,title,pos,size,style)
        self.options=options

        
        content = wx.BoxSizer(wx.VERTICAL)
        
        dirContent = wx.BoxSizer(wx.HORIZONTAL)
        dirTxt=wx.StaticText(self, -1, "Startdirectory:", (15, 50), (75, -1))
        self.dirChoice = wx.GenericDirCtrl(self, -1,style=wx.DIRCTRL_DIR_ONLY)
            
        dirContent.Add(dirTxt, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        dirContent.Add(self.dirChoice, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        fileTypeContent = wx.BoxSizer(wx.HORIZONTAL)
        self.fileTypeCb = wx.CheckBox(self, -1, "FileTypes")
        self.fileTypeCb.Bind(wx.EVT_CHECKBOX, self.setFTEnabled)
        self.fileType = wx.TextCtrl(self, -1, "")
        self.fileType.SetEditable(False)
        fileTypeContent.Add(self.fileTypeCb, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        fileTypeContent.Add(self.fileType, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        fileSizeContent = wx.BoxSizer(wx.HORIZONTAL)
        self.fileSizeMinCb = wx.CheckBox(self, -1, "Min.  FileSize (MB)")
        self.fileSizeMinCb.Bind(wx.EVT_CHECKBOX, self.setSizeMinEnabled)
        self.fileSizeMaxCb = wx.CheckBox(self, -1, "Max. FileSize (MB)")
        self.fileSizeMaxCb.Bind(wx.EVT_CHECKBOX, self.setSizeMaxEnabled)
        self.fileSizeEntry = DecimalField(self,-1,"",wx.Point(20, 10), wx.Size(50, 20))
        self.fileSizeMaxEntry = DecimalField(self,-1,"",wx.Point(20, 10), wx.Size(50, 20))
        self.fileSizeEntry.SetEditable(False)
        self.fileSizeMaxEntry.SetEditable(False)
        fileSizeContent.Add(self.fileSizeMinCb, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        fileSizeContent.Add(self.fileSizeEntry, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        fileSizeContent.Add(self.fileSizeMaxCb, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        fileSizeContent.Add(self.fileSizeMaxEntry, 3, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        content.Add(dirContent, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        content.Add(fileSizeContent, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        content.Add(fileTypeContent, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        btnsizer = wx.StdDialogButtonSizer()
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        content.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(content)
        content.Fit(self)
    
    def setFTEnabled(self,event):
        self.fileType.SetEditable(self.fileTypeCb.IsChecked())
    
    def setSizeMinEnabled(self,event):
        self.fileSizeEntry.SetEditable(self.fileSizeMinCb.IsChecked())
    
    def setSizeMaxEnabled(self,event):
        self.fileSizeMaxEntry.SetEditable(self.fileSizeMaxCb.IsChecked())
