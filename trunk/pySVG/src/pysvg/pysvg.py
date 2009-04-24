#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
License:
Copyright (c) 2008,2009 Kerim Mansour
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
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '''
SVG_FOOTER='</svg>'
END_TAG_LINE='>\n'

class SVG:
  """ Base class for a SVG document """
  def __init__(self,title="svg",description="", height=None,width=None, viewBox=None):
    self.title = title
    self.descr = description
    self.height = height
    self.width = width
    self.viewBox=viewBox
    self.elements = []
    
  def getXML(self):
    """
    Return a XML representation of the current SVG document.
    This function can be used for debugging purposes.

    @return:  the representation of the current SVG as an xml string
    """
    xml=SVG_HEADER
    #print height, width etc on demand better that this
    if self.height!= None:
      xml+='height="%s" ' % (self.height)
    
    if self.width!= None:
      xml+='width="%s" ' % (self.width)
    
    if self.viewBox!= None:
      xml+='viewBox="%s" ' % (self.viewBox)
      
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

class BaseElement:
  """
  This is the base class for all svg elements like elipses, texts, lines etc.
  """
  def __init__(self, startTag, style_dict=None, focusable=None,endTag="/>\n"):
    """
    initializes the object
    @type  startTag: string 
    @param startTag:  the tag for the svg element name (e.g. <text ) 
    @type  style_dict: dictionary
    @param style_dict:  the style to use for this element 
    @type  focusable: ??
    @param focusable:  ?? 
    """
    self.startXML=startTag
    self.endXML=endTag
    #self.style=style #deprecated
    self.focusable=focusable
    self.style_dict=style_dict
  
  def getXMLFromStyle(self):
    """
    This method converts the information in the style 
    dictionary into svg syntax for the style attribute
    
    @return:  the representation of the current style as an xml string
    """
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
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
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

 
class Group():
  """ Base class for a container element. Different shapes, paths and 
  text can be put together inside a container sharing the same style.
  """
  startXML="<g "
  endTag=">\n"
  endXML="</g>\n"

  def __init__(self,style_dict=None, transform_dict=None):
    """
    Initialization.
    @type  style_dict: dict
    @param style_dict: The style that should be applied to all elements within this container 
    """
    self.style_dict=style_dict
    self.transform_dict=transform_dict
    self.elements=[]
  
  
  def addElement(self,element):
    """
    Generic method to add any element to the container
    @type  element: Object that contains a getXML method (circle, line, text, polyline, etc....)
    @param element:  the element to add to the container
    """
    self.elements.append(element)
  
  def getXMLFromStyle(self):
    """
    This method converts the information in the style 
    dictionary into svg syntax for the style attribute
    
    @return:  the representation of the current style as an xml string
    """
    if self.style_dict==None:
      return""
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
  
  #todo: format is not nice
  def getXMLFromTransform(self):
    """
    This method converts the information in the transform 
    dictionary into svg syntax for the transform attribute
    
    @return:  the representation of the current transformations as an xml string
    """
    if self.transform_dict==None or self.transform_dict.keys()==None:
      return""
    count=0;
    xml="transform="
    for key in self.transform_dict.keys():
      if self.transform_dict.get(key)=="":
        continue
      if count>0:
        xml+='; '
      else:
        xml+='"'
      xml+='%s' %(self.transform_dict.get(key))
      count+=1
    xml+='" '
    if len(xml)>8:
      return xml
    else: #empty style
      return ""
  
  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    xml+=self.getXMLFromStyle()
    xml+=self.getXMLFromTransform()
    xml+=self.endTag
    for element in self.elements:
      xml+=element.getXML()
    xml+=self.endXML
    return xml
#------------new
class Definition():
  """ 
  This class packs all definitions
  """
  startXML="<defs>\n"
  endXML="</defs>\n"

  def __init__(self):
    self.elements=[]
    
  def addDefinition(self,definition):
    self.elements.append(definition)
    
  def removeDefinition(self,id):
    for defintion in self.elements:
      if definition.find('id="'+id+'"')>-1:
        self.elements.remove(definition)
    
  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    #xml+=self.getXMLFromStyle()
    #xml+=self.getXMLFromTransform()
    
    for element in self.elements:
      xml+=element.getXML()
    xml+=self.endXML
    return xml

class radialGradient:
  startXML="<radialGradient "
  endTag=">\n"
  endXML="</radialGradient>\n"
  
  def __init__(self, id,cx='50%',cy='50%',r='50%', fx='50%',fy='50%'):
    self.id=id
    self._stop=[]
    self.cx=cx
    self.cy=cy
    self.r=r
    self.fx=fx
    self.fy=fy
    
  
  def addStop(self,offset,color, opacity):
    s=stop(offset,color, opacity)
    self._stop.append(s)
  
  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML')==-1 and item.find('addStop')==-1 and item.find('end')==-1:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
    xml+=self.endTag
    for element in self._stop:
      xml+=element.getXML()
    xml+=self.endXML
    return xml
  
class linearGradient:
  startXML="<linearGradient "
  endTag=">\n"
  endXML="</linearGradient>\n"
  
  def __init__(self, id,x1='0',y1='0',x2='100%',y2='0'):
    self.id=id
    self._stop=[]
    self.x1=x1
    self.y1=y1
    self.x2=x2
    self.y2=y2
    
  
  def addStop(self,offset,color, opacity):
    s=stop(offset,color, opacity)
    self._stop.append(s)
  
  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML')==-1 and item.find('addStop')==-1 and item.find('end')==-1:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
    xml+=self.endTag
    for element in self._stop:
      xml+=element.getXML()
    xml+=self.endXML
    return xml

class stop(BaseElement):
  def __init__(self,offset,stopcolor, opacity):
    """
    Creates a line
    @type  offset: string
    @param offset:  offset as either percentage or decimal between 0 and 1
    @type  stopcolor: string or int
    @param stopcolor:  starting y-coordinate
    @type  opacity: string or int
    @param opacity:  ending x-coordinate
    """
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", None,None)
    if offset.find('%')==-1 and offset.find('.')==-1:
      offset=offset+'%'
    self.offset = offset
    self.stopcolor = stopcolor
    self.stopopacity=opacity

  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    if self.offset!= None:
      xml+="offset=\"%s\" " %(self.offset)
    if self.stopcolor!= None:
      xml+="stop-color=\"%s\" " %(self.stopcolor)
    if self.stopopacity!= None:
      xml+="stop-opacity=\"%s\" " %(self.stopopacity)
    
    """
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML')==-1:# and item.find('getXML')==-1:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
    """
    xml+=self.endXML
    return xml 


class line(BaseElement):
  """
  Class representing the line element of an svg doc.
  Note that this element is NOT painted VISIBLY by default UNLESS you provide
  a style including STROKE and STROKE-WIDTH
  """
  def __init__(self,x1=None,y1=None,x2=None,y2=None,style_dict=None,focusable=None):
    """
    Creates a line
    @type  x1: string or int
    @param x1:  starting x-coordinate
    @type  x1: string or int
    @param y1:  starting y-coordinate
    @type  y2: string or int
    @param x2:  ending x-coordinate
    @type  y2: string or int
    @param y2:  ending y-coordinate
    @type  style_dict: dictionary
    @param style_dict:  style(s) to use for this element
    @type  focusable: ???
    @param focusable:  ??
    """
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict,focusable)
    self.x1 = x1
    self.y1 = y1
    self.x2=x2
    self.y2=y2


class ellipse(BaseElement):
  """
  Class representing the ellipse element of an svg doc.
  """
  def __init__(self,cx=None,cy=None,rx=None,ry=None,style_dict=None,focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.cx = cx
    self.cy = cy
    self.rx=rx
    self.ry=ry
 
    
class rect(BaseElement):
  """
  Class representing the rect element of an svg doc.
  """
  def __init__(self,x=None,y=None,width=None,height=None, rx=None, ry=None,style_dict=None,focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.rx=rx
    self.ry=ry

    
class circle(BaseElement):
  """
  Class representing the cirle element of an svg doc.
  """
  def __init__(self,cx=None,cy=None,r=None,style_dict=None,focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.cx = cx
    self.cy = cy
    self.r=r

    
class polyline(BaseElement):
  """
  Class representing the polyline element of an svg doc.
  """
  def __init__(self,points=None,style_dict=None,focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.points = points

#todo: BaseElement wont work here ... make this class seperate of the hirarchie or try
#to make it work ?    
class polygon(BaseElement):
  def __init__(self,points=None,style_dict=None,focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    self.points = points


class text(BaseElement):
  """
  Class representing the text element of an svg doc.
  @type  content: string
  @param content:  the text to display
  @type  x: int 
  @param x:  x-coordinate for the text
  @type  y: int 
  @param y:  y-coordinate for the text 
  @type  rotate: int
  @param rotate:  rotation in degrees (negative means counterclockwise) 
  """
  def __init__(self,content, x ,y, rotate=None,style_dict=None,editable=None, focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable,endTag="</text>\n")
    self.x=x
    self.y=y
    self.rotate=rotate
    self.editable=editable
    self.content=content

  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
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

class path(BaseElement):
  def __init__(self,pathData="",pathLength=None,style_dict=None, focusable=None):
    BaseElement.__init__(self,"<"+self.__class__.__name__+" ", style_dict, focusable)
    if pathData!='' and not pathData.endswith(' '):
      pathData+=' '
    self.d=pathData
    #self.pathLength=pathLength

  def __append__(self,command, params, relative=True):
    if relative==True:
      self.d+=command.lower()
    else:
      self.d+=command.upper()
    for param in params:
      self.d+=' %s ' %(param)
        
  def appendLineToPath(self,endx,endy, relative=True):
    self.__append__('l',[endx,endy], relative)
  
  def appendHorizontalLineToPath(self,endx, relative=True):
    self.__append__('h',[endx], relative)
      
  def appendVerticalLineToPath(self,endy, relative=True):
    self.__append__('v',[endy], relative)
  
  def appendMoveToPath(self,endx,endy, relative=True):
    self.__append__('m',[endx,endy], relative)
    
  def appendCloseCurve(self):
    self.d+="z"
  
  def appendCubicCurveToPath(self, controlstartx, controlstarty, controlendx, controlendy, endx,endy,relative=True):
    self.__append__('c',[controlstartx, controlstarty, controlendx, controlendy, endx,endy], relative)
  
  def appendCubicShorthandCurveToPath(self,  controlendx, controlendy, endx,endy,relative=True):
    self.__append__('s',[controlendx, controlendy, endx,endy], relative)
    
  def appendQuadraticCurveToPath(self, controlx, controly, endx,endy,relative=True):
    self.__append__('q',[controlx, controly, endx,endy], relative)
  
  def appendQuadraticShorthandCurveToPath(self, endx,endy,relative=True):
    self.__append__('t',[endx,endy], relative)
    
  def appendArcToPath(self,rx,ry,x,y,x_axis_rotation=0,large_arc_flag=0,sweep_flag=1 ,relative=True):
    #self.__append__('a',[rx,ry,x,y,x_axis_rotation,large_arc_flag,sweep_flag], relative)
    self.__append__('a',[rx,ry,x_axis_rotation,large_arc_flag,sweep_flag,x,y], relative)
        
  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG

    @return:  the representation of the current element as an xml string
    """
    xml=self.startXML
    xml+='d=\"'+self.d+'" '
    for item in dir(self):
      if item.find('_')==-1 and item.find('XML') ==-1 and item.find('append')==-1 and item.find('d')!=0:
        if getattr(self,item) != None:
          xml+=item+"=\"%s\" " %(getattr(self,item))
      elif item=='style_dict':
          if getattr(self,item) != None:
            xml+=self.getXMLFromStyle()
    
    #xml+='d=\"'+self.d+'"'
    xml+=self.endXML
    return xml

class image(BaseElement):
  """ contributed by Kevin, April 2009
  """
  def __init__(self,x=None,y=None,width=None,height=None,xlink_=None,embedded_=False):
      BaseElement.__init__(self,"<"+self.__class__.__name__+" ")
      self.x = x
      self.y = y
      self.height = height
      self.width = width
      self.xlink_ = xlink_
      self.embedded_ = embedded_

  def getXML(self):
    """
    Return a XML representation of the current element.
    This function can be used for debugging purposes. It is also used by getXML in SVG
    
    @return: the representation of the current element as an xml string
    """
    xml=self.startXML
    for item in dir(self):
        if item.find('_')==-1 and item.find('XML')==-1:
            if getattr(self,item) != None:
                xml+=item+"=\"%s\" " %(getattr(self,item))
        elif item=='xlink_':
            if (getattr(self,item) != None) and self.embedded_:
                import base64
                try:
                    infile = open(getattr(self,item),'rb')
                    imdata = base64.b64encode(infile.read())
                    infile.close()
                    fext = getattr(self,item)[-3:]
                    if fext == 'jpg':
                        fext = 'jpeg'
                    imdata = ('data:image/%s;base64,' % fext) + imdata
                    xml+="xlink:href=\"%s\" " %imdata
                except IOError:
                    self.embedded_ = False
            if (getattr(self,item) != None) and not self.embedded_:
                xml+="xlink:href=\"%s\" " %(getattr(self,item))
    xml+=self.endXML
    return xml
    

