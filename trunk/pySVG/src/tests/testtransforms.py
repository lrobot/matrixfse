#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
This module was provided by joel duet to demonstrate Python 3.0 compatibility.
It plays around with transformations: skew, scaling and matrix
"""

from pysvg.pysvg import *
from pysvg.objecthelper import *
from pysvg.transformhelper import *
from pysvg.stylehelper import *
#actions not working
def createText(content, x,y, actions=None):
  t=text(content,x,y)
  return t

def createMainBorderAndTexts():
  oh=ObjectHelper()
  sh=StyleHelper()
  elements=[]
 
  r=oh.createRect("0", "0", "946", "626", strokewidth="2px", stroke="#00C", fill="#FFF")
  elements.append(r)
  
  elements.append(createText("skewX(-40)",320,380))
  elements.append(createText("scaling(1.0 0.5)",600,210))
  elements.append(createText("matrix (0.866,0.5,-0.5,0.866,-300,-200)",50,480))
  
  return elements
 
def createShapes():
  oh=ObjectHelper()
  sh=StyleHelper()
  elements=[]
  
  #skewX
  th=TransformHelper()
  th.setSkewX('-40.0')
  g=Group(transform_dict=th.getTransformDict())
  r=oh.createRect(620, 300, width='100', height='50', rx=10, ry=10, stroke='#F00',strokewidth='2px',fill='none')
  g.addElement(r)
  
  sh=StyleHelper()
  sh.setFilling('none')
  sh.setFontSize('36px')
  sh.setStrokeWidth('1px')
  sh.setStroke('#00C')
  t=text('Text',635, 337,style_dict=sh.getStyleDict())
  g.addElement(t)
  elements.append(g)
  
  #scaling
  th=TransformHelper()
  th.setScaling('1.0','0.5')
  g=Group(transform_dict=th.getTransformDict())
  r=oh.createRect(620, 300, width='100', height='50', rx=10, ry=10, stroke='#F00',strokewidth='2px',fill='none')
  g.addElement(r)
  
  sh=StyleHelper()
  sh.setFilling('none')
  sh.setFontSize('36px')
  sh.setStrokeWidth('1px')
  sh.setStroke('#00C')
  t=text('Text',635, 337,style_dict=sh.getStyleDict())
  g.addElement(t)
  elements.append(g)
  
  #matrix
  th=TransformHelper()
  th.setMatrix('0.866','0.5','-0.5','0.866','-300.0','-200.0')
  g=Group(transform_dict=th.getTransformDict())
  r=oh.createRect(620, 300, width='100', height='50', rx=10, ry=10, stroke='#F00',strokewidth='2px',fill='none')
  g.addElement(r)
  
  sh=StyleHelper()
  sh.setFilling('none')
  sh.setFontSize('36px')
  sh.setStrokeWidth('1px')
  sh.setStroke('#00C')
  t=text('Text',635, 337,style_dict=sh.getStyleDict())
  g.addElement(t)
  elements.append(g)
  
  
  return elements
 
def main():
  svg=SVG("Main Test Screen", "Showing some transforms as example", height="100%", width="100%", viewBox="0 0 950 630")
  for element in createMainBorderAndTexts():
    svg.addElement(element)
  for element in createShapes():
    svg.addElement(element)
  print(svg.getXML())
  svg.saveSVG('testtransforms.svg')
if __name__ == '__main__': 
  main()
