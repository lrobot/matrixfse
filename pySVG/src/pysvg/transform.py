#needs verification and better design
class Transform:
  def __init__(self):
    self.matrix=None
    self.translate=None
    self.scale=None  
    self.rotate=None
    self.skewX=None
    self.skewY=None 
    
  def getXML(self):
    xml="transform="
    if self.matrix!=None:
      xml+="\"matrix(%s)\"" % self.matrix
    if self.translate!=None:
      xml+="\"translate(%s)\" " % self.translate
    if self.scale!=None:
      xml+="\"scale(%s)\" " % self.scale
    if self.rotate!=None:
      xml+="\"rotate(%s)\" " % self.rotate
    if self.skewX!=None:
      xml+="\"skewX(%s)\" " % self.skewX
    if self.skewY!=None:
      xml+="\"skewY(%s)\" " % self.skewY
    xml+="\" "
    if len(xml)>13:
      return xml
    else: #empty style
      return ""
    return xml  