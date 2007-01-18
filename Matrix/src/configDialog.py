#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import tkColorChooser, tkFont, webbrowser
from idlelib.tabpage import TabPageSet

##Copyright notice:
# Most of the code here is inspired by the configDialog of idlelib !
# So the python license applies to this module

class ConfigDialog(Toplevel):
    message=["Control-p = Preferences",\
             "Control-t = Toggle Fullscreen",\
             "Control-l = Load new File",\
             "Control-n = New Document",\
             "Control-a = Select All",\
             "Control-c = Copy",\
             "Control-v = Paste",\
             "Control-u = Undo",\
             "Control-r = Redo",\
             "Control-s = Save",\
             "Control-q = Quit"]
    
    def __init__(self,parent,title):
        Toplevel.__init__(self, parent)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+20,parent.winfo_rooty()+30))
        self.parent = parent
        self.LoadColorCfg()
        self.CreateWidgets()
        self.LoadFontCfg()
        self.resizable(height=FALSE,width=FALSE)
        self.transient(parent)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.Cancel)
        
        self.tabPages.focus_set()
        self.wait_window()

    def LoadColorCfg(self):
        r,g,b=self.parent.cfg.get('GUI', 'bgcolor1'), self.parent.cfg.get('GUI', 'bgcolor2'),self.parent.cfg.get('GUI', 'bgcolor3')        
        self.bgTuplet=r,g,b
        r,g,b=self.parent.cfg.get('FONT', 'fgcolor1'),self.parent.cfg.get('FONT', 'fgcolor2'),self.parent.cfg.get('FONT', 'fgcolor3')
        self.fgTuplet=r,g,b
        
    def CreateWidgets(self):
        self.tabPages = TabPageSet(self,pageNames=['General','Font/Color','External Programs'])
        self.tabPages.ChangePage()#activates default (first) page
        buttonsFrame = Frame(self)
        #action buttons
        self.buttonOk = Button(buttonsFrame,text='Ok', command=self.OnOk,takefocus=FALSE)
        self.buttonApply = Button(buttonsFrame,text='Apply', command=self.Apply,takefocus=FALSE)
        self.buttonCancel = Button(buttonsFrame,text='Cancel', command=self.Cancel,takefocus=FALSE)
        self.CreatePageGeneral()
        self.CreatePageFontTab()
        self.CreateExternalPrograms()
        
        self.buttonOk.pack(side=LEFT,padx=5,pady=5)
        self.buttonApply.pack(side=LEFT,padx=5,pady=5)
        self.buttonCancel.pack(side=LEFT,padx=5,pady=5)
        buttonsFrame.pack(side=BOTTOM)
        self.tabPages.pack(side=TOP,expand=TRUE,fill=BOTH)

    def OnOk(self):
        self.Apply()
        self.parent.reconfigureLayout()
        self.destroy()       
        
    def Cancel(self):
        self.destroy()
    
    def Apply(self):
        self.parent.cfg.set('FONT', 'family',self.fontName)
        self.parent.cfg.set('FONT', 'size',str(self.fontSize))
        weight='normal'
        fontWeight=tkFont.NORMAL
        if self.fontBold.get():
            weight='bold'
            fontWeight=tkFont.BOLD
            
        self.parent.cfg.set('FONT', 'weight',weight)
        
        try:
            int(self.entryTextWidth.get())
            textWidth=self.entryTextWidth.get()
            self.parent.cfg.set('GUI','textareawidth',textWidth)
        except:
            print 'Value in Textwidth field no number, will not be stored' 
               
        if self.leftPanelExist.get():
            self.parent.cfg.set('GUI','leftPanel','True')
        else:
            self.parent.cfg.set('GUI','leftPanel','False')
        
        if self.rightPanelExist.get():
            self.parent.cfg.set('GUI','rightPanel','True')
        else:
            self.parent.cfg.set('GUI','rightPanel','False')
        
        r,g,b= self.fgTuplet
        self.parent.cfg.set('FONT', 'fgcolor1',str(r))
        self.parent.cfg.set('FONT', 'fgcolor2',str(g))
        self.parent.cfg.set('FONT', 'fgcolor3',str(b))    
        
        r,g,b=self.bgTuplet
        self.parent.cfg.set('GUI', 'bgcolor1',str(r))
        self.parent.cfg.set('GUI', 'bgcolor2',str(g))
        self.parent.cfg.set('GUI', 'bgcolor3',str(b))
                
        self.SaveConfig()
        
    def SaveConfig(self):
        filename = "Matrixtk.config"
        configFile=open(filename,"w")
        sections= self.parent.cfg.sections()
        for section in sections:
            configFile.write("["+section+"]\n")
            options= self.parent.cfg.options(section)
            for option in options:
                configFile.write(option+":"+self.parent.cfg.get(section, option)+"\n")
        configFile.close()
        
    def CreateExternalPrograms(self):
        frame=self.tabPages.pages['External Programs']['page']
        labelInfo=Label(frame,justify=LEFT,text='I/A-Spell integration and \nstructured text output comes later')
        labelInfo.pack(side=TOP,anchor=W)
        
    def CreatePageGeneral(self):
        self.textWidth=StringVar(self)
        self.leftPanelExist=BooleanVar(self)
        self.rightPanelExist=BooleanVar(self)
        frame=self.tabPages.pages['General']['page']
        orientationFrame=Frame(frame,borderwidth=2,relief=GROOVE)
        textWidthFrame=Frame(orientationFrame)
        labelNewStartInfo=Label(orientationFrame,justify=LEFT,text='Changes here take effect only after restart')
        labelTextWidth=Label(textWidthFrame,justify=LEFT,text='Width of text (relevent only if all panels deactivated):')
        self.entryTextWidth=Entry(textWidthFrame, width='3')
        self.entryTextWidth.insert(INSERT, self.parent.cfg.get('GUI','textareawidth'))
        self.checkLeftPanel=Checkbutton(orientationFrame,variable=self.leftPanelExist,onvalue=1,offvalue=0,text='Left Panel exists')
        if self.parent.cfg.get('GUI','leftPanel')=='True':
            self.checkLeftPanel.select()
        self.checkRightPanel=Checkbutton(orientationFrame,variable=self.rightPanelExist,onvalue=1,offvalue=0,text='Right Panel exists')
        if self.parent.cfg.get('GUI','rightPanel')=='True':
            self.checkRightPanel.select()
        orientationFrame.pack(side=LEFT,padx=5,pady=10,expand=TRUE,fill=BOTH)
        
        helpCommandsFrame=Frame(orientationFrame,borderwidth=2,relief=GROOVE)
        labelHelpText=Label(helpCommandsFrame,justify=LEFT,text='Available Commands :')
        helpText = Text(helpCommandsFrame, width=50)
        for m in self.message:
            helpText.insert(INSERT,m+"\n")
        helpText['state'] = DISABLED
        
        donateFrame=Frame(orientationFrame,borderwidth=2,relief=GROOVE)

        btnImage = PhotoImage(file="donate.gif") 
        donateBtn = Button(donateFrame, compound=TOP, image=btnImage, command=self.Donate)
        donateBtn.image = btnImage
        labelNewStartInfo.pack(side=TOP,anchor=W)
        self.checkLeftPanel.pack(side=TOP,anchor=W)
        self.checkRightPanel.pack(side=TOP,anchor=W)
        textWidthFrame.pack(side=TOP,anchor=W)
        labelTextWidth.pack(side=LEFT,anchor=W)
        self.entryTextWidth.pack(side=RIGHT,anchor=W)
        helpCommandsFrame.pack(side=TOP,anchor=W)
        labelHelpText.pack(side=TOP,anchor=W)
        helpText.pack(side=TOP,anchor=W)
        donateFrame.pack(side=TOP,anchor=W)
        donateBtn.pack(side=TOP,anchor=W)
        
    def Donate(self):
        webbrowser.open('http://codeboje.de/blog/pages/MatrixFSE.html')
        
    def CreatePageFontTab(self):
        self.fontSize=StringVar(self)
        self.fontBold=BooleanVar(self)
        self.fontName=StringVar(self)
        self.editFont=tkFont.Font(self,('courier',10,'normal'))
        frame=self.tabPages.pages['Font/Color']['page']
        fontFrame=Frame(frame,borderwidth=2,relief=GROOVE)
        fontNameFrame=Frame(fontFrame)
        
        labelFontNameTitle=Label(fontNameFrame,justify=LEFT,text='Font :')
        self.listFontName=Listbox(fontNameFrame,height=5,takefocus=FALSE,exportselection=FALSE)
        self.listFontName.bind('<ButtonRelease-1>',self.OnListFontButtonRelease)
        scrollFont=Scrollbar(fontNameFrame)
        scrollFont.config(command=self.listFontName.yview)
        self.listFontName.config(yscrollcommand=scrollFont.set)
        
        fontParamFrame=Frame(fontFrame)
        labelFontSizeTitle=Label(fontParamFrame,justify=LEFT,text='Size :')
        self.listFontSize=Listbox(fontParamFrame,height=3,width=5,takefocus=FALSE,exportselection=FALSE)
        scrollSize=Scrollbar(fontParamFrame)
        scrollSize.config(command=self.listFontSize.yview)
        self.listFontSize.config(yscrollcommand=scrollSize.set)
        self.listFontSize.bind('<ButtonRelease-1>',self.OnListFontSizeButtonRelease)
        
        checkFontBold=Checkbutton(fontParamFrame,onvalue=1,offvalue=0,text='Bold')
        checkFontBold.bind('<ButtonRelease-1>',self.OnCheckFontBoldButtonRelease)
        colorFrame=Frame(fontFrame)
        buttonSetForegroundColour=Button(colorFrame,text='Foregroundcolor...', command=self.GetFgColour,highlightthickness=0)
        buttonSetBackgroundColour=Button(colorFrame,text='Backgroundcolor...',command=self.GetBgColour,highlightthickness=0)
              
        fontSampleFrame=Frame(fontFrame,relief=SOLID,borderwidth=1)
        r,g,b=self.fgTuplet
        fgColour = '#%02x%02x%02x' %  (int(r), int(g), int(b))
        r,g,b=self.bgTuplet
        bgColour = '#%02x%02x%02x' %  (int(r), int(g), int(b))
        
        self.labelFontSample=Label(fontSampleFrame,text='AaBbCcDdEe\nFfGgHhIiJjK\n1234567890\n#:+=(){}[]',justify=LEFT,font=self.editFont, foreground=fgColour, background=bgColour)
        
        #widget packing
        fontFrame.pack(side=LEFT,padx=5,pady=10,expand=TRUE,fill=BOTH)
        fontNameFrame.pack(side=TOP,padx=5,pady=5,fill=X)
        fontParamFrame.pack(side=TOP,padx=5,pady=5,fill=X)
        colorFrame.pack(side=TOP,padx=5,pady=5,fill=X)
        labelFontNameTitle.pack(side=TOP,anchor=W)
        self.listFontName.pack(side=LEFT,expand=TRUE,fill=X)
        scrollFont.pack(side=LEFT,fill=Y)
        labelFontSizeTitle.pack(side=LEFT,anchor=W)
        self.listFontSize.pack(side=LEFT,anchor=W)
        scrollSize.pack(side=LEFT,fill=Y)
        checkFontBold.pack(side=LEFT,anchor=W,padx=20)
        buttonSetForegroundColour.pack(side=TOP,anchor=W,padx=20)
        buttonSetBackgroundColour.pack(side=BOTTOM,anchor=W,padx=20)
        fontSampleFrame.pack(side=TOP,padx=5,pady=5,expand=TRUE,fill=BOTH)
        self.labelFontSample.pack(expand=TRUE,fill=BOTH)
        
        return frame


    def OnCheckFontBoldButtonRelease(self,event):
        self.fontBold.set(not self.fontBold.get())
        self.SetFontSample()
        
    def OnListFontButtonRelease(self,event):
        font = self.listFontName.get(ANCHOR)
        self.fontName=font.lower()#.set(font.lower())
        self.SetFontSample()
    
    def OnListFontSizeButtonRelease(self,event):
        font = self.listFontSize.get(ANCHOR)
        self.fontSize=font#.set(font.lower())
        self.SetFontSample()

    def LoadFontCfg(self):
        ##base editor font selection list
        fonts=list(tkFont.families(self))
        fonts.sort()
        for font in fonts:
            self.listFontName.insert(END,font)
        configuredFont=self.parent.cfg.get('FONT', 'family')
        lc_configuredFont = configuredFont.lower()
        self.fontName=lc_configuredFont#.set(lc_configuredFont)
        lc_fonts = [s.lower() for s in fonts]
        if lc_configuredFont in lc_fonts:
            currentFontIndex = lc_fonts.index(lc_configuredFont)
            self.listFontName.see(currentFontIndex)
            self.listFontName.select_set(currentFontIndex)
            self.listFontName.select_anchor(currentFontIndex)
        ##font size dropdown
        counter=0
        selSize=1
        self.fontSize=self.parent.cfg.get('FONT', 'size') 
        for size in range(7,40):
            self.listFontSize.insert(END,size)
            if size==int(self.fontSize):
                selSize=counter
            counter=counter+1
        
        self.listFontSize.see(selSize)
        self.listFontSize.select_set(selSize)
        self.listFontSize.select_anchor(selSize)
        ##fontWeight
        if self.parent.cfg.get('FONT','weight') == 'normal':
            self.fontBold.set(False)
        else:
            self.fontBold.set(True)
        ##font sample
        self.SetFontSample()
        
    def SetFontSample(self,event=None):
        fontName=self.fontName
        if self.fontBold.get():
            fontWeight=tkFont.BOLD
        else:
            fontWeight=tkFont.NORMAL
        self.editFont.config(size=self.fontSize,
                weight=fontWeight,family=fontName)
    
    def GetBgColour(self):
        layer='background'
        self.GetColour(layer,self.bgTuplet)
        
    def GetFgColour(self):
        layer='foreground'
        self.GetColour(layer,self.fgTuplet)
            
    def GetColour(self, layer,tuplet):   
        r,g,b=tuplet
        prevColour = '#%02x%02x%02x' %  (int(r), int(g), int(b))
        rgbTuplet, colourString = tkColorChooser.askcolor(parent=self, title='Pick new colour for : '+layer,initialcolor=prevColour)
        if layer=='foreground':
            self.fgTuplet=rgbTuplet
            self.labelFontSample.config(foreground=colourString)
        else:
            self.bgTuplet=rgbTuplet
            self.labelFontSample.config(background=colourString)
        
