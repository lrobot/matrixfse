import sys, wx, webbrowser
import  wx.html as  html
import markdown

"""
License:
Copyright (c) 2007,2008 Kerim Mansour
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

OPEN_BROWSER=wx.NewId()

sampleText="""
Sample Text
=================

This is a sample markdown text. Click  **Refresh** to see the **HTML Output** that corresponds to your markdown.

I picked the original text from the [markdownpage here][orig] 

[orig]: http://daringfireball.net/projects/markdown/
Download
--------

[Markdown 1.0.1][dl] (18 KB) -- 17 Dec 2004

[dl]: http://daringfireball.net/projects/downloads/Markdown_1.0.1.zip


Introduction
------------

Markdown is a text-to-HTML conversion tool for web writers. Markdown
allows you to write using an easy-to-read, easy-to-write plain text
format, then convert it to structurally valid XHTML (or HTML).

Thus, "Markdown" is two things: (1) a plain text formatting syntax;
and (2) a software tool, written in Perl, that converts the plain text
formatting to HTML. See the [Syntax][] page for details pertaining to
Markdown's formatting syntax. You can try it out, right now, using the
online [Dingus][].

  [syntax]: /projects/markdown/syntax
  [dingus]: /projects/markdown/dingus

The overriding design goal for Markdown's formatting syntax is to make
it as readable as possible. The idea is that a Markdown-formatted
document should be publishable as-is, as plain text, without looking
like it's been marked up with tags or formatting instructions. While
Markdown's syntax has been influenced by several existing text-to-HTML
filters, the single biggest source of inspiration for Markdown's
syntax is the format of plain text email.

The best way to get a feel for Markdown's formatting syntax is simply
to look at a Markdown-formatted document. For example, you can view
the Markdown source for the article text on this page here:
<http://daringfireball.net/projects/markdown/index.text>

(You can use this '.text' suffix trick to view the Markdown source for
the content of each of the pages in this section, e.g. the
[Syntax][s_src] and [License][l_src] pages.)

  [s_src]: /projects/markdown/syntax.text
  [l_src]: /projects/markdown/license.text

Markdown is free software, available under a BSD-style open source
license. If you enjoy using Markdown, please considering making a
small donation to support further development. See the [License] [pl]
page for more information.

  [pl]: /projects/markdown/license


Discussion List <a id="discussion-list" />
---------------

I've set up a public [mailing list for discussion about Markdown] [ml].
Any topic related to Markdown -- both its formatting syntax and
its software -- is fair game for discussion. Anyone who is interested
is welcome to join.

It's my hope that the mailing list will lead to good ideas for future
improvements to Markdown.

  [ml]: http://six.pairlist.net/mailman/listinfo/markdown-discuss


Installation and Requirements <a id="install" />
-----------------------------

Markdown requires Perl 5.6.0 or later. Welcome to the 21st Century.
Markdown also requires the standard Perl library module [Digest::MD5]
[md5], which is probably already installed on your server.

  [md5]: http://search.cpan.org/dist/Digest-MD5/MD5.pm


### Movable Type ###

Markdown works with Movable Type version 2.6 or later (including
Movable Type 3.0).

1.  Copy the "Markdown.pl" file into your Movable Type "plugins"
  directory. The "plugins" directory should be in the same directory
  as "mt.cgi"; if the "plugins" directory doesn't already exist, use
  your FTP program to create it. Your installation should look like
  this:

        (mt home)/plugins/Markdown.pl

2.  Once installed, Markdown will appear as an option in Movable Type's
  Text Formatting pop-up menu. This is selectable on a per-post basis:
  
  ![Screenshot of Movable Type 'Text Formatting' Menu][tfmenu]
  
  Markdown translates your posts to HTML when you publish; the posts
  themselves are stored in your MT database in Markdown format.

3.  If you also install SmartyPants 1.5 (or later), Markdown will
  offer a second text formatting option: "Markdown With
  SmartyPants". This option is the same as the regular "Markdown"
  formatter, except that it automatically uses SmartyPants to create
  typographically correct curly quotes, em-dashes, and ellipses. See
  the [SmartyPants web page][sp] for more information.

4.  To make Markdown (or "Markdown With SmartyPants") your default
  text formatting option for new posts, go to Weblog Config:
  Preferences.

Note that by default, Markdown produces XHTML output. To configure
Markdown to produce HTML 4 output, see "Configuration", below.

  [sp]: http://daringfireball.net/projects/smartypants/



### Blosxom ###

Markdown works with Blosxom version 2.0 or later.

1.  Rename the "Markdown.pl" plug-in to "Markdown" (case is
    important). Movable Type requires plug-ins to have a ".pl"
    extension; Blosxom forbids it.

2.  Copy the "Markdown" plug-in file to your Blosxom plug-ins folder.
    If you're not sure where your Blosxom plug-ins folder is, see the
    Blosxom documentation for information.

3.  That's it. The entries in your weblog will now automatically be
  processed by Markdown.

4.  If you'd like to apply Markdown formatting only to certain
  posts, rather than all of them, Markdown can optionally be used in
  conjunction with Blosxom's [Meta][] plug-in. First, install the
  Meta plug-in. Next, open the Markdown plug-in file in a text
  editor, and set the configuration variable `$g_blosxom_use_meta`
  to 1. Then, simply include a "`meta-markup: Markdown`" header line
  at the top of each post you compose using Markdown.

  [meta]: http://www.blosxom.com/plugins/meta/meta.htm


### BBEdit ###

Markdown works with BBEdit 6.1 or later on Mac OS X. It also works
with BBEdit 5.1 or later and MacPerl 5.6.1 on Mac OS 8.6 or later. If
you're running Mac OS X 10.2 (Jaguar), you may need to install the
Perl module [Digest::MD5] [md5] from CPAN; Digest::MD5 comes
pre-installed on Mac OS X 10.3 (Panther).

1.  Copy the "Markdown.pl" file to appropriate filters folder in your
  "BBEdit Support" folder. On Mac OS X, this should be:

        BBEdit Support/Unix Support/Unix Filters/

    See the BBEdit documentation for more details on the location of
    these folders.

    You can rename "Markdown.pl" to whatever you wish.

2.  That's it. To use Markdown, select some text in a BBEdit document,
  then choose Markdown from the Filters sub-menu in the "#!" menu, or
  the Filters floating palette



Configuration  <a id="configuration"></a>
-------------

By default, Markdown produces XHTML output for tags with empty elements.
E.g.:

    <br />

Markdown can be configured to produce HTML-style tags; e.g.:

    <br>


### Movable Type ###

You need to use a special `MTMarkdownOptions` container tag in each
Movable Type template where you want HTML 4-style output:

    <MTMarkdownOptions output='html4'>
        ... put your entry content here ...
    </MTMarkdownOptions>

The easiest way to use MTMarkdownOptions is probably to put the
opening tag right after your `<body>` tag, and the closing tag right
before `</body>`.

To suppress Markdown processing in a particular template, i.e. to
publish the raw Markdown-formatted text without translation into
(X)HTML, set the `output` attribute to 'raw':

    <MTMarkdownOptions output='raw'>
        ... put your entry content here ...
    </MTMarkdownOptions>


### Command-Line ###

Use the `--html4tags` command-line switch to produce HTML output from a
Unix-style command line. E.g.:

    % perl Markdown.pl --html4tags foo.text

Type `perldoc Markdown.pl`, or read the POD documentation within the
Markdown.pl source code for more information.


Acknowledgements <a id="acknowledgements" />
----------------

[Aaron Swartz][] deserves a tremendous amount of credit for helping to
design Markdown's formatting syntax. Markdown is *much* better thanks
to Aaron's ideas, feedback, and testing. Also, Aaron's [html2text][]
is a very handy (and free) utility for turning HTML into
Markdown-formatted plain text.

[Nathaniel Irons][], [Dan Benjamin][], [Daniel Bogan][], and [Jason Perkins][]
also deserve thanks for their feedback.

[Michel Fortin][] has ported Markdown to PHP; it's a splendid port, and highly recommended for anyone looking for a PHP implementation of Markdown.

  [Aaron Swartz]:    http://www.aaronsw.com/
  [Nathaniel Irons]:  http://bumppo.net/
  [Dan Benjamin]:    http://hivelogic.com/
  [Daniel Bogan]:    http://waferbaby.com/
  [Jason Perkins]:    http://pressedpants.com/
  [Michel Fortin]:    http://www.michelf.com/projects/php-markdown/
  [html2text]:          http://www.aaronsw.com/2002/html2text/
 
  [tfmenu]: /graphics/markdown/mt_textformat_menu.png
"""
    
class HtmlPanel(wx.Panel):
    def __init__(self, parent, frame, textWindow):
      wx.Panel.__init__(self, parent, -1, style=wx.NO_FULL_REPAINT_ON_RESIZE)
      self.frame = frame
      self.textWindow=textWindow
      self.html= html.HtmlWindow(parent,  style=wx.NO_FULL_REPAINT_ON_RESIZE)
      
      #self.html.SetRelatedFrame(frame, frame.GetTitle())
      #self.html.SetRelatedStatusBar(0)
        
      self.box = wx.BoxSizer(wx.VERTICAL) #global container
      headbox = wx.BoxSizer(wx.HORIZONTAL) #heading
      subbox = wx.BoxSizer(wx.HORIZONTAL) # buttons
        
        
      previewText = wx.StaticText(self, -1, "HTML-Preview")
      previewText.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Verdana'))
      headbox.Add(previewText, 0, wx.CENTER, 10)
        
      self.refreshbtn = wx.Button(self, -1, "Refresh")
      self.Bind(wx.EVT_BUTTON, self.MarkDownRefresh, self.refreshbtn)
      subbox.Add(self.refreshbtn, 1, wx.GROW | wx.ALL, 2)

      self.autorefreshbtn = wx.CheckBox(self, -1, "AutoRefresh")
      self.Bind(wx.EVT_CHECKBOX, self.OnAutoRefresh, self.autorefreshbtn)
      self.autorefreshbtn.SetValue(False)
      self.autorefreshbtn.Enable(False)
      subbox.Add(self.autorefreshbtn, 1, wx.GROW | wx.ALL, 2)
        
      btn = wx.Button(self, -1, "Open in Browser")
      self.Bind(wx.EVT_BUTTON, self.OpenBrowser, btn)
      subbox.Add(btn, 1, wx.GROW | wx.ALL, 2)
        
      self.box.Add(headbox, 0, wx.GROW)
      self.box.Add(self.html, 1, wx.GROW)
      self.box.Add(subbox, 0, wx.GROW)
      self.SetSizer(self.box)
      self.SetAutoLayout(True)

    def AutoUpdateMarkdown(self,event):
      if self.autorefreshbtn.GetValue()==True:
        self.MarkDownRefresh(None)
   
    def MarkDownRefresh(self,event):
      html = markdown.markdown(self.textWindow.GetValue())
      self.html.SetPage(html)
    
    def OnAutoRefresh(self,event):
      if self.autorefreshbtn.GetValue()==True:
        self.refreshbtn.Enable(False)
      else:
        self.refreshbtn.Enable(True)
    
    def OpenBrowser(self,event):
      html = markdown.markdown(self.textWindow.GetValue())
      file=open("temp.html",'w')
      html = markdown.markdown(self.textWindow.GetValue())
      text=unicode.encode(html,'utf8')
      file.write(text)
      file.close()
      webbrowser.open('temp.html') 

class TextPanel(wx.Panel):
    def __init__(self, parent):
      wx.Panel.__init__(self, parent,-1, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        
      self.box = wx.BoxSizer(wx.VERTICAL) #global container
      headbox = wx.BoxSizer(wx.HORIZONTAL) #controls ?
      
      previewText = wx.StaticText(self, -1, "Controls will come here")
      previewText.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Verdana'))
      headbox.Add(previewText, 0, wx.CENTER, 10)
        
      self.textWindow = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.DefaultSize, 
                        wx.TE_MULTILINE|wx.SUNKEN_BORDER )
      self.textWindow.SetValue(sampleText)
      self.box.Add(headbox, 0, wx.GROW)
      self.box.Add(self.textWindow, 1, wx.GROW)
        
      self.SetSizer(self.box)
      self.SetAutoLayout(True)
      
  
    def GetValue(self):
      return self.textWindow.GetValue()
          
class MarkieFrame(wx.Frame):
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition,
            size=(800,600), style=wx.DEFAULT_FRAME_STYLE ):

      wx.Frame.__init__(self, parent, ID, title, pos, size, style)
      splitter=wx.SplitterWindow(self, ID,style = wx.SP_LIVE_UPDATE)
        
      self.text=TextPanel(splitter)
      self.html = HtmlPanel(splitter,splitter,self.text)
      #splitter.SplitVertically(self.text,self.html)
      splitter.SplitVertically(self.html,self.text)
      
    def exitApp(self,event):
      sys.exit()
        
#---------------- run the program -----------------------
def main(argv=None):
    app = wx.App(False)
    frame = MarkieFrame(None, -1, ' ')
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()