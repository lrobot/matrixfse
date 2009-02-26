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
  """ Helper Class to create a style_dict for those not familiar with svg attribute names.
  """
  def __init__(self):
    self.style_dict={}

  
  # tested below
  def setFontFamily(self, fontfamily):
    self.style_dict["font-family"]=fontfamily
  
  def setFontSize(self, fontsize):
    self.style_dict["font-size"]=fontsize
  
  def setFontStyle(self,fontstyle):
    self.style_dict["font-style"]=fontstyle
  
  def setFontWeight(self,fontweight):
    self.style_dict["font-weight"]=fontweight
    
    #tested
  def setFilling(self, fill):
    self.style_dict["fill"]=fill
  
  def setFillOpacity(self,fillopacity):
    self.style_dict["fill-opacity"]=fillopacity
  
  def setFillRule(self,fillrule):
    self.style_dict["fill-rule"]=fillrule
  
  def setStrokeWidth(self,strokewidth):
    self.style_dict["stroke-width"]=strokewidth
  def setStroke(self,stroke):
    self.style_dict["stroke"]=stroke
  
  #untested below  
  def setStrokeDashArray(self,strokedasharray):
    self.style_dict["stroke-dasharray"]=strokedasharray
  def setStrokeDashOffset(self,strokedashoffset):
    self.style_dict["stroke-dashoffset"]=strokedashoffset
  def setStrokeLineCap(self,strikelinecap):
    self.style_dict["stroke-linecap"]=strikelinecap
  def setStrokeLineJoin(self,strokelinejoin):
    self.style_dict["stroke-linejoin"]=strokelinejoin
  def setStrokeMiterLimit(self,strokemiterlimit):
    self.style_dict["stroke-miterlimit"]=strokemiterlimit
  def setStrokeOpacity(self,strokeopacity):
    self.style_dict["stroke-opacity"]=strokeopacity
    

  #is used to provide a potential indirect value (currentColor) for the 'fill', 'stroke', 'stop-color' properties.
  def setCurrentColor(self, color):
    self.style_dict["color"]=color
     
   
  # Gradient properties:
  def setStopColor(self, stopcolor):
    self.style_dict["stop-color"]=stopcolor
  
  def setStopOpacity(self, stopopacity):
    self.style_dict["stop-opacity"]=stopopacity

  #rendering properties
  def setColorRendering(self, colorrendering):
    self.style_dict["color-rendering"]=colorrendering
   
  def setImageRendering(self, imagerendering):
    self.style_dict["image-rendering"]=imagerendering
    
  def setShapeRendering(self, shaperendering):
    self.style_dict["shape-rendering"]=shaperendering
    
  def setTextRendering(self, textrendering):
    self.style_dict["text-rendering"]=textrendering
    
  def setSolidColor(self,solidcolor):
    self.style_dict["solid-color"]=solidcolor
  
  def setSolidOpacity(self, solidopacity):
    self.style_dict["solid-opacity"]=solidopacity
  
  #Viewport properties  
  def setVectorEffect(self, vectoreffect):
    self.style_dict["vector-effect"]=vectoreffect
    
  def setViewPortFill(self, viewportfill):
    self.style_dict["viewport-fill"]=viewportfill
    
  
  def setViewPortOpacity(self, viewportfillopacity):
    self.style_dict["viewport-fill_opacity"]=viewportfillopacity
          
  # Text properties
  def setDisplayAlign(self,displayalign):
    self.style_dict["display-align"]=displayalign
    
  def setLineIncrement(self, lineincrement):
    self.style_dict["line-increment"]=lineincrement
    
  def setTextAnchor(self, textanchor):
    self.style_dict["text-anchor"]=textanchor

  def getStyleDict(self):
    return self.style_dict
  
    