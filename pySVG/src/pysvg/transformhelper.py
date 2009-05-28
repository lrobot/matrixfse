class TransformHelper:
  def __init__(self):
    self.transform_dict={}
  
  def setMatrix(self,matrix):
    self.transform_dict["matrix"]='matrix(%s)' % matrix
  
  def setMatrix(self, a, b, c, d, e, f):
    self.transform_dict["matrix"]='matrix(%s %s %s %s %s %s)' %(a,b,c,d,e,f)
  
  def setRotation(self,rotate):
    self.transform_dict["rotate"]='rotate(%s)' % rotate
  
  def setRotation(self,rotation, cx=None, cy=None):
    if cx!=None and cy!= None:
      self.transform_dict["rotate"]='rotate(%s %s %s)' % (rotation,cx,cy)
    else:
      self.transform_dict["rotate"]='rotate(%s)' % (rotation)
    
  def setTranslation(self,translate):
    self.transform_dict["translate"]='translate(%s)' % (translate)
  
  def setTranslation(self, x, y=0):
    self.transform_dict["translate"]='translate(%s %s)' % (x,y)
    
  def setScaling(self,scale):
    self.transform_dict["scale"]='scale(%s)' % (scale)
  
  def setScaling(self, x=None, y=None):
    if x==None and y!=None:
      x=y
    elif x!=None and y==None:
      y=x
    self.transform_dict["scale"]='scale(%s %s)' % (x,y)
  
  def setSkewY(self,skewY):
    self.transform_dict["skewY"]='skewY(%s)' % (skewY)
  
  def setSkewX(self,skewX):
    self.transform_dict["skewX"]='skewX(%s)' % (skewX)
 
  def getTransformDict(self):
    return self.transform_dict
    
  def getTransform(self):
      string=''#style="'
      for key, value in self.transform_dict.items():
          if value <> None and value <> '':
              #string+=str(key)+':'+str(value)+'; '
              string+=str(value)+' '
      #str+='"\n'
      return string
  """  
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
  """