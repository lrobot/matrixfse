#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
This module is used to create the pySVG Logo.
"""

from pysvg.pysvg import *
from pysvg.objecthelper import *
from pysvg.transformhelper import *
from pysvg.stylehelper import *

def createText(content, x,y, actions=None):
  t=text(content,x,y)
  return t

def createShapes():
  oh=ObjectHelper()
  sh=StyleHelper()
  elements=[]
  
  #group + transform
  th=TransformHelper()
  th.setRotation('-30')
  g=Group(transform_dict=th.getTransformDict())
  
  sh=StyleHelper()
  sh.setFilling('none')
  sh.setFontSize('36px')
  sh.setStrokeWidth('1px')
  sh.setStroke('#00C')
  t=text('pySVG',0, 100,style_dict=sh.getStyleDict())
  g.addElement(t)
  elements.append(g)
  
  
  return elements

def main():
  svg=SVG("pySVG Logo", "", height="100%", width="100%")
  for element in createShapes():
    svg.addElement(element)
  print svg.getXML()
  svg.saveSVG('pySVGLogo.svg')
if __name__ == '__main__': 
  main()