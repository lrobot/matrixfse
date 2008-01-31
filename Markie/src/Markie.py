#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
License:
Copyright (c) 2008, Kerim Mansour
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
import wx
import wx.html as html
import wx.aui
import markdown
import os.path
import os
import shutil

if wx.Platform == '__WXMSW__':
    import  wx.lib.iewin    as  iewin

ID_NewFile = wx.NewId()
ID_LoadFile = wx.NewId()
ID_SaveFile = wx.NewId()
ID_SaveFileAs = wx.NewId()
ID_Quit = wx.NewId()

ID_DirTreePane = wx.NewId()
ID_HTMLPrevPane = wx.NewId()
ID_SavePage = wx.NewId()
ID_SaveHTML = wx.NewId()
ID_SelectTheme = wx.NewId()

ID_CreateMarkdown = wx.NewId()

wildcard = "Markie source (*.markie)|*.markie|"     \
           "Text file (*.txt)|*.txt|" \
           "All files (*.*)|*.*"
           

sampleText="""
Title : Sample Text
=================

This is a sample markdown text. Click  **Refresh** to see the **HTML Output** that corresponds to your markdown.

Here is a [link][nt].
[nt]: http://codeboje.de/

I just made a small release (0.1.0) for the public. Feel free to test and give me feedback.

Here an image:

<p>
<img width="600" style="float:none" src="http://www.codeboje.de/media/articles/completeshapes.PNG" />
</p>


Another Title
------------

1.  list entry 1

     a.  list entry 1a

     b.  entry 1b

     
2. entry 2 

"""


class PyAUIFrame(wx.Frame):
    
    def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.currentFile=None
        self._perspectives = []
        
        # tell FrameManager to manage this frame        
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        
        #self.SetIcon(GetMondrianIcon())

        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(ID_LoadFile, "Load")
        file_menu.Append(ID_SaveFile, "Save")
        file_menu.Append(ID_SaveFileAs, "Save as")
        file_menu.Append(wx.ID_EXIT, "Exit")
        wx.EVT_MENU(self, ID_LoadFile, self.OnLoad)
        wx.EVT_MENU(self, ID_SaveFile, self.OnSave)
        wx.EVT_MENU(self, ID_SaveFileAs, self.OnSaveAs)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)

        view_menu = wx.Menu()
        #view_menu.Append(ID_DirTreePane, "View DirectoryTree Pane")
        #view_menu.Append(ID_HTMLPrevPane, "Recreate Perspective")
        #wx.EVT_MENU(self, ID_HTMLPrevPane, self.OnHTMLPreviewPane)
        
          
        markdown_menu = wx.Menu()
        markdown_menu.Append(ID_CreateMarkdown, "Create Preview")
        markdown_menu.Append(ID_SaveHTML, "Save HTML only")
        markdown_menu.Append(ID_SavePage, "Save complete page")
        markdown_menu.Append(ID_SelectTheme, "Select Page Theme")
        wx.EVT_MENU(self, ID_SaveHTML, self.OnSaveHTML)
        wx.EVT_MENU(self, ID_SavePage, self.OnSaveCreatedPage)
        wx.EVT_MENU(self, ID_SelectTheme, self.OnSelectTheme)
        wx.EVT_MENU(self, ID_CreateMarkdown, self.OnMarkdown)
        #options_menu = wx.Menu()
        #options_menu.AppendRadioItem(ID_SaveFile, "Select Page Theme")
        
        help_menu = wx.Menu()
        
        mb.Append(file_menu, "File")
        #mb.Append(view_menu, "View")
        mb.Append(markdown_menu, "Creation and Options")
        #mb.Append(options_menu, "Options")
        #mb.Append(help_menu, "Help")
        
        self.SetMenuBar(mb)

        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-2, -3])
        self.statusbar.SetStatusText("Ready", 0)
        self.statusbar.SetStatusText("Welcome To Markie!", 1)

        self.SetSize(wx.Size(600, 480))

        # create some toolbars
        tb=self.MakeToolBar()
        
        self.nb = wx.aui.AuiNotebook(self)  #SWITCH WITH SHIFT+TAB ?
        self.textpage = wx.TextCtrl(self.nb, -1, sampleText, style=wx.TE_MULTILINE)
        self.nb.AddPage(self.textpage, "Source Text")
        #self.nb.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE,self.DestroySourceTab)
        
        self.htmlpage = html.HtmlWindow(self.nb,  style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.nb.AddPage(self.htmlpage, "RAW HTML Preview")
        if wx.Platform == '__WXMSW__':
          self.iehtmlpage = iewin.IEHtmlWindow(self, -1, style = wx.NO_FULL_REPAINT_ON_RESIZE)
          self.nb.AddPage(self.iehtmlpage, "IE Preview")
        
        self._mgr.AddPane(tb, wx.aui.AuiPaneInfo().
                          Name("tb").Caption("Toolbar").
                          ToolbarPane().Top().Row(1).
                          LeftDockable(False).RightDockable(False))
        self._mgr.AddPane(self.nb, wx.aui.AuiPaneInfo().Name("text_content").Caption("Source Text").
                          Center().CloseButton(False).MaximizeButton(True))
        # "commit" all changes made to FrameManager   
        self._mgr.Update()
        self.searchThemes()
        self.loadTheme()
    """
    def DestroySourceTab(self,event):
      dlg = wx.MessageDialog(self, 'Any changes will be lost',
                               'Attention',
                               wx.OK | wx.ICON_INFORMATION |
                               wx.CANCEL 
                               )
      if dlg.ShowModal()==wx.ID_CANCEL:           
        dlg.Destroy()
        return
      else:
        event.Skip()
    """   
    def OnExit(self,event):
      if len(self.textpage.GetValue())>0:
         dlg = wx.MessageDialog(self, 'Any changes will be lost',
                               'Attention',
                               wx.OK | wx.ICON_INFORMATION |
                               wx.CANCEL 
                               )
         if dlg.ShowModal()==wx.ID_CANCEL:           
           dlg.Destroy()
           return
         dlg.Destroy()
         self.Close(True)
    """
    def OnHTMLPreviewPane(self,event):
      htmlpagefound=False
      iepagefound=False
      sourcepagefound=False
      for page in range(0,self.nb.GetPageCount()):
        if self.nb.GetPageText(page)=="RAW HTML Preview":
          htmlpagefound=True
        elif self.nb.GetPageText(page)=="IE Preview":
          iepagefound=True
        elif self.nb.GetPageText(page)=="Source Text":
          sourcepagefound=True
      if sourcepagefound==False:
        self.textpage = wx.TextCtrl(self.nb, -1, "", style=wx.TE_MULTILINE)
        self.nb.InsertPage(0,self.iehtmlpage, "Source Text")
          
      if htmlpagefound==False:
        self.htmlpage = html.HtmlWindow(self.nb,  style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.nb.InsertPage(1,self.htmlpage, "RAW HTML Preview")
      
      if iepagefound==False:
        if wx.Platform == '__WXMSW__':
          self.iehtmlpage = iewin.IEHtmlWindow(self, -1, style = wx.NO_FULL_REPAINT_ON_RESIZE)
          self.nb.InsertPage(2,self.iehtmlpage, "IE Preview")
    """ 
      
      
    def searchThemes(self):
      path='themes/'
      self.themes=[]
      for theme in os.listdir(path):
        if theme.find('.svn')==-1 and os.path.isdir(os.path.join(path,theme)):
          self.themes.append(theme)
      print self.themes
      
    def loadTheme(self,template=None, lang='en_US'):
      path='themes/'
      if template!=None:
        path=os.path.join(path,template)
      else:
        path=os.path.join(path,'default')
      self.currentTheme=path
      self.currentTheme=self.currentTheme.decode("latin-1")
      if not os.path.exists(os.path.join(path,'page.template')):
        dlg = wx.MessageDialog(self, path+'page.template'+ 'not found !',
                               'Could not load template', wx.OK | wx.ICON_INFORMATION )
        dlg.ShowModal()           
        dlg.Destroy()
        return
      f=open(os.path.join(path,'page.template'),'rb')
      self.page=f.read()
      self.page = self.page.replace('INCLUDE_LANG', lang)
      
      if os.path.exists(os.path.join(path,'metainf.template')):
        self.replaceTokens(os.path.join(path,'metainf.template'),'INCLUDE_METAINF')
      
      if os.path.exists(os.path.join(path,'header.template')):
        self.replaceTokens(os.path.join(path,'header.template'),'INCLUDE_HEADER')
        
      if os.path.exists(os.path.join(path,'footer.template')):
        self.replaceTokens(os.path.join(path,'footer.template'),'INCLUDE_FOOTER')
    
      
    def replaceTokens(self,filename,token):
       f=open(filename,'rb')
       text=f.read()
       self.page = self.page.replace(token, text)
       f.close()
        
    def OnToolBar(self,event):
      print "huhu"
    
    def OnSelectTheme(self,event):
      dlg = wx.SingleChoiceDialog(
                self, 'Available Themes', 'Select a Theme',
                self.themes, 
                wx.CHOICEDLG_STYLE
                )
      if dlg.ShowModal() == wx.ID_OK:
        #print dlg.GetStringSelection()
        self.loadTheme(dlg.GetStringSelection())
        self.OnMarkdown(event=None,refresh=False)
      
    def OnSaveHTML(self,event):
      dlg = wx.FileDialog(
            self, message="Save created HTMLFile as ...", defaultDir=os.getcwd(), 
            defaultFile="index.html", wildcard="Html (*.html)|*.html", style=wx.SAVE)#| wx.CHANGE_DIR)
      if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        self.currentFile=path
        html=self.OnMarkdown(None,path, False)
        f=open(path,'wb')
        f.write(html)
        f.close()
        
    def OnNew(self,event):
      if len(self.textpage.GetValue())>0:
         dlg = wx.MessageDialog(self, 'Any changes will be lost',
                               'Attention',
                               wx.OK | wx.ICON_INFORMATION |
                               wx.CANCEL 
                               )
         if dlg.ShowModal()==wx.ID_CANCEL:           
           dlg.Destroy()
           return
         dlg.Destroy()
      self.textpage.SetValue("")
      self.htmlpage.SetPage("")
      self.currentFile=None
    
    def OnLoad(self,event):
      dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN)# | wx.CHANGE_DIR)

      if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        f=open(path,'rb')
        self.textpage.SetValue(f.read())
        self.currentFile=path
        f.close()
       
    def OnSave(self,event):
      if self.currentFile==None:
        self.OnSaveAs(None)
      else:
        f=open(self.currentFile,'wb')
        f.write(self.textpage.GetValue())
        f.close()
    
    def OnSaveAs(self,event):
      dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=wildcard, style=wx.SAVE)# | wx.CHANGE_DIR )
      if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        self.currentFile=path
        f=open(path,'wb')
        f.write(self.textpage.GetValue())
        f.close()
    
    def OnSaveCreatedPage(self,event):
      dlg = wx.FileDialog(
            self, message="Save created HTMLFile as ...", defaultDir=os.getcwd(), 
            defaultFile="index.html", wildcard="Html (*.html)|*.html", style=wx.SAVE)# | wx.CHANGE_DIR )
      if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        self.currentFile=path
        html=self.OnMarkdown(None,path, False)
        self.exportPage(html,path)
        
        
        
    def OnMarkdown(self,event, fileName=None, refresh=True):
      html = markdown.markdown(self.textpage.GetValue())
      html=self.page.replace('INCLUDE_CONTENT', html)
      
      if self.htmlpage:
        self.htmlpage.SetPage(html)
        
      self.exportPage(html, fileName)
      if refresh==True:
        self.refreshInternalView()
      return html
      
    def refreshInternalView(self):
      if self.htmlpage:
        self.nb.SetSelection(1)
      
      
    """
    stores the files in a directory
    """
    def exportPage(self, html, fileName=None):
      
      if fileName==None:
        dstpath=os.path.join(os.getcwd(),'previewOutput')
        path= os.path.join(dstpath,'temp.html')
      else:
        dstpath=os.path.dirname(fileName)
        path=fileName
      
      #delete old output
      if os.path.exists(dstpath):
        #try:
        shutil.rmtree(dstpath,ignore_errors=True)
        #except:
        #  print "unale to delete the tree will just copy files"
      
      #copy complete template 
#      shutil.copytree(self.currentTheme, dstpath)
      self.copytree(self.currentTheme, dstpath)
      
      #del .template files
      for file in os.listdir(dstpath):
        if file.endswith('.template'):
          os.remove(os.path.join(dstpath,file))
      
      #save created html
      f=open(path,'wb')
      f.write(html)
      f.close()
        
      if self.iehtmlpage:
        self.iehtmlpage.LoadUrl('file://'+path)
      
    def OnExportPage(self,event):
      pass
         
    def MakeToolBar(self):
        def doBind(item, handler, updateUI=None):
            self.Bind(wx.EVT_TOOL, handler, item)
            if updateUI is not None:
                self.Bind(wx.EVT_UPDATE_UI, updateUI, item)
        # create some toolbars
        tb = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        tb.SetToolBitmapSize(wx.Size(16,16))
        
        doBind(tb.AddTool(ID_NewFile, wx.ArtProvider_GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="New"),self.OnNew)
        doBind(tb.AddTool(ID_LoadFile, wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Load"),self.OnLoad)
        doBind(tb.AddTool(ID_SaveFile, wx.ArtProvider_GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Save"),self.OnSave)
        doBind(tb.AddTool(ID_SaveFileAs, wx.ArtProvider_GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Save As"),self.OnSaveAs)
        tb.AddSeparator()
        doBind(tb.AddTool(ID_CreateMarkdown, wx.ArtProvider_GetBitmap(wx.ART_HELP_SIDE_PANEL, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Create Markdown"),self.OnMarkdown)
        tb.AddSeparator()
        doBind(tb.AddTool(ID_SavePage, wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Store Webpage"),self.OnSaveCreatedPage)
        #doBind(tb.AddTool(ID_SaveHTML, wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Store HTML only"),self.OnSaveHTML)
        #doBind(tb.AddTool(ID_SelectTheme, wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_TOOLBAR, wx.Size(16, 16)),shortHelpString="Select Theme"),self.OnSelectTheme)
        tb.Realize()
        return tb
                       
        
    def copytree(self,src, dst):
      """Ported from shutils to deal with .svn directories
      """
      names = os.listdir(src)
      os.makedirs(dst)
      errors = []
      for name in names:
          srcname = os.path.join(src, name)
          dstname = os.path.join(dst, name)
          try:
            if srcname.find('.svn')>-1:
                continue
            if os.path.isdir(srcname):
                shutil.copytree(srcname, dstname, symlinks)
            else:
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
          except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
          # catch the Error from the recursive copytree so that we can
          # continue with other files
          except Error, err:
            errors.extend(err.args[0])
      try:
        shutil.copystat(src, dst)
      except WindowsError:
        # can't copy file access times on Windows
        pass
      except OSError, why:
        errors.extend((src, dst, str(why)))
      if errors:
        raise Error, errors
      
#---------------- run the program -----------------------
def main(argv=None):
    app = wx.App(False)
    frame = PyAUIFrame(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()