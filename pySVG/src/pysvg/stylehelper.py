"""
module for all attributes related to styling
"""
"""
Not supported as of yet.

    * Interactivity properties:
          o 'pointer-events'
    * Multimedia properties:
          o 'audio-level'
* Other properties for visual media:
          o 'display'
          o 'visibility'
Also testing is needed for all attributes !
working:

#toto gradient stuff must be seperated i think members for stopcolor etc here are idiotic

"""
class StyleHelper:
  """ Base class for all attributes related to styling
  DEPRECATED: Atually replaced by a dictionary inside pysvg.
  This will become a Helperclass like ObjectHelper
  """
  def __init__(self):
    self.style_dict={
      "font-family":"" ,
      "font-size":"" ,
      "font-style":"" ,
      "font-family":"" ,
      "color":"" ,
      "stop-color":"" ,
      "stop-opacity":"" ,
      "stroke-dasharray":"" ,
      "stroke-dashoffset":"" ,
      "stroke-linecap":"" ,
      "stroke-linejoin":"" ,
      "stroke-miterlimit":"" ,
      "stroke-opacity":"" ,
      "stroke-width":"" ,
      "stroke":"" ,
      "color-rendering":"" ,
      "image-rendering":"" ,
      "shape-rendering":"" ,
      "text-rendering":"" ,
      "solid-color":"" ,
      "solid-opacity":"" ,
      "fill":"" ,
      "fill-opacity":"" ,
      "fill-rule:%s":"" ,
      "vector-effect":"" ,
      "viewport-fill":"" ,
      "viewport-fill-opacity":"" ,
      "display-align":"" ,
      "line-increment":"" ,
      "text-anchor":""                 
    }

  #   Font properties:
  # tested
  def setFontFamily(self, fontfamily="", fontsize="",fontstyle="",fontweight=""):
    self.style_dict["font-family"]=fontfamily
    self.style_dict["font-size"]=fontsize
    self.style_dict["font-style"]=fontstyle
    self.style_dict["font-weight"]=fontweight
    
    #tested
  def setFilling(self, fill="",fillopacity="",fillrule=""):
    self.style_dict["fill"]=fill
    self.style_dict["fill-opacity"]=fillopacity
    self.style_dict["fill-rule"]=fillrule
    
  def setStroke(self,strokewidth="",stroke="",strokeopacity="",strokemiterlimit="",strokelinejoin="",strikelinecap="",strokedashoffset="",strokedasharray=""):
    self.style_dict["stroke-dasharray"]=strokedasharray
    self.style_dict["stroke-dashoffset"]=strokedashoffset
    self.style_dict["stroke-linecap"]=strikelinecap
    self.style_dict["stroke-linejoin"]=strokelinejoin
    self.style_dict["stroke-miterlimit"]=strokemiterlimit
    self.style_dict["stroke-opacity"]=strokeopacity
    self.style_dict["stroke-width"]=strokewidth #tested
    self.style_dict["stroke"]=stroke #tested
    

  #is used to provide a potential indirect value (currentColor) for the 'fill', 'stroke', 'stop-color' properties.
  def setCurrentColor(self,color):
    self.style_dict["color"]=color
     
   
  # Gradient properties:
  def setGradient(self,stopcolor="",stopopacity=""):
    self.style_dict["stop-color"]=stopcolor
    self.style_dict["stop-opacity"]=stopopacity
      
  

  def setRendering(colorrendering="",imagerendering="",shaperendering="", textrendering=""):
    self.style_dict["color-rendering"]=colorrendering
    self.style_dict["image-rendering"]=imagerendering
    self.style_dict["shape-rendering"]=shaperendering
    self.style_dict["text-rendering"]=textrendering
    
  def setSolidProperties(self,solidcolor="",solidopacity=""):
    self.style_dict["solid-color"]=solidcolor
    self.style_dict["solid-opacity"]=solidopacity
  
  def setViewPort(self,vectoreffect="",viewportfill="",viewportfillopacity=""):
    self.style_dict["vector-effect"]=vectoreffect
    self.style_dict["viewport-fill"]=viewportfill
    self.style_dict["viewport-fill_opacity"]=viewportfillopacity
          
  # Text properties
  def setTextProperties(self,displayalign="",lineincrement="",textanchor=""):
    self.style_dict["display-align"]=displayalign
    self.style_dict["line-increment"]=lineincrement
    self.style_dict["text-anchor"]=textanchor

  def getStyleDict(self):
    return self.style_dict
  
  def getXML(self):
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
    
    