#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

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
  sh.setFilling("#000")
  sh.setFontSize("24px")
  t=text("Objects and Effects in ...", 30, 40, style_dict=sh.getStyleDict())
  elements.append(t)
  sh=StyleHelper()
  sh.setFontSize("13px")
  t=text("[The red circle, explanation texts and textlinks WILL (but are not yet) connected to JavaScript.]", 360, 35, style_dict=sh.getStyleDict())
  elements.append(t)
  
  elements.append(createText("Rectangle",230,90))
  elements.append(createText("Circle",230,180))
  elements.append(createText("Ellipse",230,275))
  elements.append(createText("Polygon",100,350))
  elements.append(createText("Polyline",270,350))
  elements.append(createText("Line",270,470))
  elements.append(createText("Path",190,570))
  elements.append(createText("flowing Text",800,550))
  elements.append(createText("linear gradient",600,90))
  elements.append(createText("radial gradient",600,170))
  elements.append(createText("opacity",600,310))
  elements.append(createText("filter",600,440))
  elements.append(createText("animation",800,375))
  
  elements.append(createText("pattern",600,550))
  elements.append(createText("group + transformation",780,190))
  elements.append(createText("external Picture",800,310))
  elements.append(createText("Textlink",800,495))
  
  return elements

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
  #for element in createMainBorderAndTexts():
   # svg.addElement(element)
  for element in createShapes():
    svg.addElement(element)
  print svg.getXML()
  svg.saveSVG('tpySVG.svg')
if __name__ == '__main__': 
  main()