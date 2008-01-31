#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
License:
Copyright (c) 2008 Kerim Mansour
All rights reserved.

COMMERCIAL USAGE:
Commercial usage is understood as usage in order to make a profit or in a corporate environment.
For commercial usage please contact kmansour ATT web DOT de

NONCOMMERCIAL USAGE:
The following license applies to NONCOMMERCIAL usage of the software. 
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

"""
Not supported as of yet / NOT Working
Viewport, transforms, gradients....
"""

SVG_HEADER='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny" '''
SVG_FOOTER='</svg>'
END_TAG_LINE='>\n'

class SVG:
  """ Base class for a SVG document """
  def __init__(self,title="svg",description="", height=None,width=None):
    self.title = title
    self.descr = description
    self.height = height
    self.width = width
    self.elements = []
    
  def getXML(self):
    """
    Return a XML representation of the current SVG document.
    This function can be used for debugging purposes.

    @return:  the representation of the current SVG as an xml string
    """
    xml=SVG_HEADER
    xml+=END_TAG_LINE
    for element in self.elements:
      xml+=element.getXML()
    xml+=SVG_FOOTER
    return xml
  
  def saveSVG(self, filename):
    """
    Saves the current SVG document into a file.
    @type  filename: string
    @param filename: file to store the svg in (complete path+filename+extension) 
    """
    f=open(filename,'w')
    xml=self.getXML()
    f.write(xml)
    f.close()
    
  def addElement(self,element):
    """
    Generic method to add any element to the document
    @type  element: Object that contains a getXML method (circle, line, text, polyline, etc....)
    @param element:  the element to add to the doc
    """
    self.elements.append(element)
  
class Group():
  """ Base class for a container element. Different shapes, paths and 
  text can be put together inside a container sharing the same style.
  """
  startXML="<g "
  endTag=">\n"
  endXML="</g>\n"

  def __init__(self,style_dict=None):
    """
    Initialization.
    @type  style: Style
    @param style: The style that should be applied to all elements within this container 
    """
    self.style_dict=style_dict
    self.elements=[]
  
  
  def addElement(self,element):
    """
    Generic method to add any element to the container
    @type  element: Object that contains a getXML method (circle, line, text, polyline, etc....)
    @param element:  the element to add to the container
    """
    self.elements.append(element)
  
  def getXMLFromStyle(self):
    count=0;
    xml="style="
    for key in self.style_dict.keys():
      if self.style_dict.get(key)=="":
        continue
      if count>0:
        xml+='; '
      else:
        xml+='"'
      xml+='%s:%s' %(key,self.style_dict.get(key))
      count+=1
    xml+='" '
    if len(xml)>8:
      return xml
    else: #empty style
      return ""
      
  def getXML(self):
    """
    Return a XML representation of the current SVG document.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current SVG as an xml string
    """
    xml=self.startXML
    xml+=self.getXMLFromStyle()
    xml+=self.endTag
    for element in self.elements:
      xml+=element.getXML()
    xml+=self.endXML
    return xml


  
    
class BaseObject:
  def __init__(self, startTag, style_dict=None, focusable=None,endTag="/>\n"):
    self.startXML=startTag
    self.endXML=endTag
    #self.style=style #deprecated
    self.focusable=focusable
    self.style_dict=style_dict
  
  def getXMLFromStyle(self):
    count=0;
    xml="style="
    for key in self.style_dict.keys():
      if self.style_dict.get(key)=="":
        continue
      if count>0:
        xml+='; '
      else:
        xml+='"'
      xml+='%s:%s' %(key,self.style_dict.get(key))
      count+=1
    xml+='" '
    if len(xml)>8:
      return xml
    else: #empty style
      return ""
    
  def getXML(self):
    #print dir(self)
    xml=self.startXML
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML')==-1:# and item.find('getXML')==-1:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
      elif item=='style_dict':
          if getattr(self,item) != None:
            xml+=self.getXMLFromStyle()
    xml+=self.endXML
    return xml

#NOT painted by default. you MUST supply a style including stroke and stroke-width !
class line(BaseObject):
  def __init__(self,x1=None,y1=None,x2=None,y2=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict,focusable)
    self.x1 = x1
    self.y1 = y1
    self.x2=x2
    self.y2=y2


class ellipse(BaseObject):
  def __init__(self,cx=None,cy=None,rx=None,ry=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.cx = cx
    self.cy = cy
    self.rx=rx
    self.ry=ry
 
    
class rect(BaseObject):
  def __init__(self,x=None,y=None,width=None,height=None, rx=None, ry=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.rx=rx
    self.ry=ry

    
class circle(BaseObject):
  def __init__(self,cx=None,cy=None,r=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.cx = cx
    self.cy = cy
    self.r=r

    
class polyline(BaseObject):
  def __init__(self,points=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.points = points

#todo: baseobject wont work here ... make this class seperate of the hirarchie or try
#to make it work ?    
class polygon(BaseObject):
  def __init__(self,points=None,style_dict=None,focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.points = points


class text(BaseObject):
  def __init__(self,content, x ,y, rotate=None,style_dict=None,editable=None, focusable=None):
    BaseObject.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable,endTag="</text>\n")
    self.x=x
    self.y=y
    self.rotate=rotate
    self.editable=editable
    self.content=content

  def getXML(self):
    #print dir(self)
    xml=self.startXML
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML') ==-1 and item.find('content')==-1:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
      elif item=='style_dict':
          if getattr(self,item) != None:
            xml+=self.getXMLFromStyle()
    xml+=">"
    xml+=self.content
    xml+=self.endXML
    return xml
          
#not supported as of yet
"""
class Text:
class Path:
"""
    

