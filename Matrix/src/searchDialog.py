from Tkinter import *
import tkSimpleDialog, string

class SearchDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        '''create dialog body.

        return widget that should have initial focus.
        This method should be overridden, and is called
        by the __init__ method.
        '''
        Label(master, text="Find:").grid(row=0, sticky=W)
    
        self.findText = Entry(master)
        self.editorText=self.parent.text
        self.findText.grid(row=0, column=1)
        
        self.wholeWord=BooleanVar()
        self.wholeWord.set(False)
        self.caseSensitive=BooleanVar()
        self.caseSensitive.set(False)
        
        caseCb = Checkbutton(master, text="Match Case",variable=self.caseSensitive)
        caseCb.grid(row=1, columnspan=2, sticky=W)
        #wholeWCb = Checkbutton(master, text="Whole word",variable=self.wholeWord)
        #wholeWCb.grid(row=1, columnspan=2, sticky=E)
        
        self.searchDirection = BooleanVar() #True -> Down, False->Up
        self.searchDirection.set(True)
        rb1=Radiobutton(master, text="Up", variable=self.searchDirection, value=False)
        rb1.pack(anchor=W)
        rb2=Radiobutton(master, text="Down", variable=self.searchDirection, value=True)
        rb2.pack(anchor=W)
        
        rb1.grid(row=2, columnspan=2, sticky=W)
        rb2.grid(row=3, columnspan=2, sticky=W)
        
        return self.findText
    
    def buttonbox(self):
        '''add standard button box.
        override if you do not want the standard buttons
        '''

        box = Frame(self)

        w = Button(box, text="Find", width=10, command=self.find, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.find)
        self.bind("<Escape>", self.cancel)

        box.pack()
    
    def cancel(self, event=None):
        if self.editorText is not None:
            self.editorText.focus_set()
        self.destroy()
        
        
    def find(self,event=None):
        """
        def search(self, pattern, index, stopindex=None,
           forwards=None, backwards=None, exact=None,
           regexp=None, nocase=None, count=None):
        """
        findText=self.findText.get()
        if len(findText)==0:
            return None
        first=self.editorText.index("insert")
        last=None
        
        fw=None
        bw=None
        nc=None
        ex=None
        if self.searchDirection.get():
            fw=True
            if last==None:
                last=self.editorText.index("end")
        else:
            bw=True
            if last==None:
                last=0.0
        if self.caseSensitive.get()==False:
            nc=True
        pos=self.editorText.search(findText,index=first,stopindex=last, forwards=fw, backwards=bw,exact=ex,nocase=nc)
        if pos!='':
            self.show_hit(pos,len(findText),bw)
            return True
        return False
        
    def show_hit(self, position, lengthOfWord,backwards):
        first=position
        last="%s+%sc"% (position, lengthOfWord)    
        
        text = self.editorText
        text.tag_config("hit", foreground="blue", underline=1)
        
        text.tag_remove("sel", "1.0", "end")
        text.tag_add("sel", first, last)
        text.tag_remove("hit", "1.0", "end")
        if first == last:
            text.tag_add("hit", first)
        if backwards:
            text.mark_set("insert", first) 
            if last!=first:
                text.tag_add("hit", first, "%s+%sc"% (position, lengthOfWord))
        else:
            text.mark_set("insert", last)
            if last!=first:
                text.tag_add("hit", first, last)
        text.see("insert")
        text.update_idletasks()
       
        
class ReplaceDialog(SearchDialog):
    def body(self, master):
        '''create dialog body.

        return widget that should have initial focus.
        This method should be overridden, and is called
        by the __init__ method.
        '''
        Label(master, text="Find:").grid(row=0, sticky=W)
        Label(master, text="Replace:").grid(row=1, sticky=W)
    
        self.findText = Entry(master)
        self.replaceText = Entry(master)
        self.editorText=self.parent.text
    
        self.findText.grid(row=0, column=1)
        self.replaceText.grid(row=1, column=1)
    
        self.wholeWord=BooleanVar()
        self.wholeWord.set(False)
        self.caseSensitive=BooleanVar()
        self.caseSensitive.set(False)
        
        caseCb = Checkbutton(master, text="Match Case",variable=self.caseSensitive)
        caseCb.grid(row=2, columnspan=2, sticky=W)
        #wholeWCb = Checkbutton(master, text="Whole word",variable=self.wholeWord)
        #wholeWCb.grid(row=2, columnspan=2, sticky=E)
        
        self.searchDirection = BooleanVar() #True -> Down, False->Up
        self.searchDirection.set(True)
        rb1=Radiobutton(master, text="Up", variable=self.searchDirection, value=False)
        rb1.pack(anchor=W)
        rb2=Radiobutton(master, text="Down", variable=self.searchDirection, value=True)
        rb2.pack(anchor=W)
        
        rb1.grid(row=3, columnspan=2, sticky=W)
        rb2.grid(row=4, columnspan=2, sticky=W)
        
        return self.findText
    
    def buttonbox(self):
        '''add standard button box.
           override if you do not want the standard buttons
        '''

        box = Frame(self)

        w = Button(box, text="Find", width=10, command=self.find, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Replace/Find next", width=20, command=self.replace, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Replace all", width=10, command=self.replaceAll, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.find)
        self.bind("<Escape>", self.cancel)

        box.pack()
        
    def replace(self):
        self.doReplace()
        #find next
        self.find()
    
    def doReplace(self):
        replaceText=self.replaceText.get()
        if len(replaceText)==0:
            return None
        findText=self.findText.get()
        if len(findText)==0:
            return None
        text=self.editorText
        hitlist=text.tag_ranges("hit")
        print hitlist
        firstIndex=hitlist[0]
        lastIndex=None
        if len(hitlist)==2:
            lastIndex=hitlist[1]
        text.edit_separator()
        text.delete(firstIndex,lastIndex)
        text.insert(firstIndex,replaceText)
        text.edit_separator()
        self.editorText.modified=True
        
    def replaceAll(self):
        text=self.editorText
        text.tag_remove("sel", "1.0", "end")
        text.tag_remove("hit", "1.0", "end")
        text.mark_set(INSERT, "1.0")
        while(self.find()==True):
            self.doReplace()
        

