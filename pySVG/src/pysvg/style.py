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
class Style:
  """ Base class for all attributes related to styling
  """
  def __init__(self):
    self.font_family=None
    self.font_size=None
    self.font_style=None
    self.font_weight=None
    self.color=None
    self.stop_color=None
    self.stop_opacity=None
    self.stroke_dasharray=None
    self.stroke_dashoffset=None
    self.stroke_linecap=None
    self.stroke_linejoin=None
    self.stroke_miterlimit=None
    self.stroke_opacity=None
    self.stroke_width=None
    self.stroke=None
    self.color_rendering=None
    self.image_rendering=None
    self.shape_rendering=None
    self.text_rendering=None
    self.solid_color=None
    self.solid_opacity=None
    self.fill=None
    self.fill_opacity=None
    self.fill_rule=None
    self.vector_effect=None
    self.viewport_fill=None
    self.viewport_fill_opacity=None
    self.display_align=None
    self.line_increment=None
    self.text_anchor=None

  #   Font properties:
  # tested
  def setFontFamily(self, fontfamily=None, fontsize=None,fontstyle=None,fontweight=None):
    self.font_family=fontfamily
    self.font_size=fontsize
    self.font_style=fontstyle
    self.font_weight=fontweight

  #is used to provide a potential indirect value (currentColor) for the 'fill', 'stroke', 'stop-color' properties.
  def setCurrentColor(self,color):
    self.color=color
     
   
  # Gradient properties:
  def setGradient(self,stopcolor=None,stopopacity=None):
    self.stop_color=stopcolor
    self.stop_opacity=stopopacity
      
  def setStroke(self,strokewidth=None,stroke=None,strokeopacity=None,strokemiterlimit=None,strokelinejoin=None,strikelinecap=None,strokedashoffset=None,strokedasharray=None):
    self.stroke_dasharray=strokedasharray
    self.stroke_dashoffset=strokedashoffset
    self.stroke_linecap=strikelinecap
    self.stroke_linejoin=strokelinejoin
    self.stroke_miterlimit=strokemiterlimit
    self.stroke_opacity=strokeopacity
    self.stroke_width=strokewidth #tested
    self.stroke=stroke #tested

  def setRendering(colorrendering=None,imagerendering=None,shaperendering=None, textrendering=None):
    self.color_rendering=colorrendering
    self.image_rendering=imagerendering
    self.shape_rendering=shaperendering
    self.text_rendering=textrendering
    
  def setSolidProperties(self,solidcolor=None,solidopacity=None):
    self.solid_color=solidcolor
    self.solid_opacity=solidopacity
    
  #tested
  def setFilling(self, fill=None,fillopacity=None,fillrule=None):
    self.fill=fill
    self.fill_opacity=fillopacity
    self.fill_rule=fillrule
    
  def setViewPort(self,vectoreffect=None,viewportfill=None,viewportfillopacity=None):
    self.vector_effect=vectoreffect
    self.viewport_fill=viewportfill
    self.viewport_fill_opacity=viewportfillopacity
          
  # Text properties
  def setTextProperties(self,displayalign=None,lineincrement=None,textanchor=None):
    self.display_align=displayalign
    self.line_increment=lineincrement
    self.text_anchor=textanchor

  def getXML(self):
    xml="style=\""
    if self.font_family!=None:
      xml+="font-family:%s; " % self.font_family
      
    if self.font_size!=None:
      xml+="font-size:%s; " % self.font_size
    
    if self.font_style!=None:
      xml+="font-style:%s; " % self.font_style
    
    if self.font_family!=None:
      xml+="font-family:%s; " % self.font_family
    
    if self.color!=None:
      xml+="color:%s; " % self.color
    
    if self.stop_color!=None:
      xml+="stop-color:%s; " % self.stop_color
    
    if self.stop_opacity!=None:
      xml+="stop-opacity:%s; " % self.stop_opacity
    
    if self.stroke_dasharray!=None:
      xml+="stroke-dasharray:%s; " % self.stroke_dasharray
    
    if self.stroke_dashoffset!=None:
      xml+="stroke-dashoffset:%s; " % self.stroke_dashoffset
    
    if self.stroke_linecap!=None:
      xml+="stroke-linecap:%s; " % self.stroke_linecap
    
    if self.stroke_linejoin!=None:
      xml+="stroke-linejoin:%s; " % self.stroke_linejoin
    
    if self.stroke_miterlimit!=None:
      xml+="stroke-miterlimit:%s; " % self.stroke_miterlimit
    
    if self.stroke_opacity!=None:
      xml+="stroke-opacity:%s; " % self.stroke_opacity
    
    if self.stroke_width!=None:
      xml+="stroke-width:%s; " % self.stroke_width
   
    if self.stroke!=None:
      xml+="stroke:%s; " % self.stroke
    
    if self.color_rendering!=None:
      xml+="color-rendering:%s; " % self.color_rendering
    
    if self.image_rendering!=None:
      xml+="image-rendering:%s; " % self.image_rendering
    
    if self.shape_rendering!=None:
      xml+="shape-rendering:%s; " % self.shape_rendering
    
    if self.text_rendering!=None:
      xml+="text-rendering:%s; " % self.text_rendering
    
    if self.solid_color!=None:
      xml+="solid-color:%s; " % self.solid_color
    
    if self.solid_opacity!=None:
      xml+="solid-opacity:%s; " % self.solid_opacity
    
    if self.fill!=None:
      xml+="fill:%s; " % self.fill
    
    if self.fill_opacity!=None:
      xml+="fill-opacity:%s; " % self.fill_opacity
    
    if self.fill_rule!=None:
      xml+="fill-rule:%s; " % self.fill_rule
    
    if self.vector_effect!=None:
      xml+="vector-effect:%s; " % self.vector_effect
   
    if self.viewport_fill!=None:
      xml+="viewport-fill:%s; " % self.viewport_fill
    
    if self.viewport_fill_opacity!=None:
      xml+="viewport-fill-opacity:%s; " % self.viewport_fill_opacity
    
    if self.display_align!=None:
      xml+="display-align:%s; " % self.display_align
    
    if self.line_increment!=None:
      xml+="line-increment:%s; " % self.line_increment
    
    if self.text_anchor!=None:
      xml+="text-anchor:%s; " % self.text_anchor
    xml+="\" "
    if len(xml)>9:
      return xml
    else: #empty style
      return ""
