#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
DEPRECATED ::: NOT UP TO DATE :::: NOT WORKING !!!
"""

from pysvg.pysvg import *
from pysvg.objecthelper import *
from pysvg.stylehelper import *

def globaltest():
  oh=ObjectHelper()
  svg=SVG("test")
  
  #testing basic shapes
  svg.addElement(oh.createRect(0,0,400,200,12,12,strokewidth=2, stroke='navy'))
  svg.addElement(oh.createRect(100,50,200,100,strokewidth=2, stroke='navy', fill='yellow'))
  svg.addElement(oh.createCircle(700,500,50,strokewidth=5, stroke='red'))
  svg.addElement(oh.createCircle(810,500,50,strokewidth=5, stroke='yellow', fill='#AAAAAA'))
  svg.addElement(oh.createEllipse(600,50,50,30,strokewidth=5, stroke='red'))
  svg.addElement(oh.createEllipse(700,50,50,30,strokewidth=5, stroke='yellow', fill='#00AABB'))
  style=StyleHelper()
  r=rect(0,0,100,100,12,12,style)
  
  svg.addElement(oh.createLine(0,0,300,300,strokewidth=2,stroke="black"))
  
  #style=StyleHelper()
  #style.setStroke(strokewidth=5, stroke="black")
  #style.fill="blue"
  #style.setGradient(stopcolor='red',stopopacity=1)
  #gradientcircle=circle(700,500,50,style)
  
  #svg.addElement(gradientcircle)
  
  pl=oh.createPolyline(points="50,375 150,375 150,325 250,325 250,375 350,375 350,250 450,250 450,375 \
550,375 550,175 650,175 650,375 750,375 750,100 850,100 850,375 950,375 \
950,25 1050,25 1050,375 1150,375 ",strokewidth=10, stroke='blue')
  svg.addElement(pl)

  pg=oh.createPolygon(points="350,75  379,161 469,161 397,215 \
423,301 350,250 277,301 303,215 231,161 321,161 ",strokewidth=10, stroke='blue', fill='red')
  svg.addElement(pg)
  
   
  style=StyleHelper()
  style.setFontFamily(fontfamily="Verdana", fontsize='5em')
  #style.setFilling(fill="blue")
  style.setFilling(fill='blue')
  t1=text("pySVG with Style",0,650,style_dict=style.getStyleDict())
  t2=text("pySVG simple",0,550)
  svg.addElement(t1)
  svg.addElement(t2)
  #testing container
  style=StyleHelper()
  style.setStroke(strokewidth=2,stroke="green")
  style_dict=style.getStyleDict()
  g=Group(style_dict)
  g.addElement(line(300,300,600,600))
  g.addElement(circle(500,500,50))
  svg.addElement(g)
  
  g=Group(style_dict)
  style_dict = {"stroke":"#000000", "fill":"none" ,"stroke-width":"49" ,"stroke-opacity":"0.027276"}
  p=path(pathData="M 300 100 A 1,1 0 0 1 802,800",style_dict=style_dict)
  #p.appendArcToPath(25,100, 50,-25, -30, 0,1)
  g.addElement(p)
  svg.addElement(g)
  print svg.getXML()
  svg.saveSVG('c:\\test.svg')

def testPath():
  svg=SVG("test")
  style_dict = {"stroke":"#000000", "fill":"none","stroke-width":"49" }
  p=path(pathData="M 300 100 A 1,1 0 0 1 802,800",style_dict=style_dict)
  p.appendArcToPath(25,100, 50,-25, -30, 0,1)
  
  svg.addElement(p)
  print svg.getXML()
  svg.saveSVG('c:\\test.svg')
  
def textText():
  oh=ObjectHelper()
  svg=SVG("test")
  style=StyleHelper()
  style.setFontFamily(fontfamily="Verdana", fontsize='5em')
  style.setFilling(fill="blue")
  t1=text("Verdana, blue, 5em",0,100,style_dict=style.getStyleDict())
  t2=text("pySVG simple",0,200)
  svg.addElement(t1)
  svg.addElement(t2)
  
  rect=oh.createRect(350, 250, 100, 100, fill='green')
  svg.addElement(rect)
  
  style=StyleHelper()
  style.setFontFamily(fontfamily="Times", fontsize='2em', fontstyle='italic', fontweight='bold')
  style.setFilling(fill="red",fillopacity='0.5',fillrule='evenodd')
  #style.fill="blue"
  t3=text("Times, italic, 2em, bold, opacity=0.5, fillrule=evenodd",0,300,style_dict=style.getStyleDict())
  svg.addElement(t3)

  style=StyleHelper()
  style.setFontFamily(fontfamily="Times", fontsize='2em', fontstyle='italic')
  style.setFilling(fill="red",fillopacity='0.5')
  #style.fill="blue"
  t4=text("Times, italic, 2em, non bold, opacity=0.5",0,400,style_dict=style.getStyleDict())
  svg.addElement(t4)

  
  print svg.getXML()
  svg.saveSVG('c:\\test.svg')
  
def textHelloWorld1():
  svg=SVG("Hello World Example") # title is ignored still
  t=text("Hello World",0,200)
  svg.addElement(t)
  print svg.getXML()
  svg.saveSVG('c:\\test.svg')

def textHelloWorld2():
  svg=SVG("Hello World Example") # title is ignored still
  style=StyleHelper()
  style.setFontFamily(fontfamily="Verdana", fontsize='5em')
  style.setFilling(fill="blue")
  t1=text("Hello World",0,100,style_dict=style.getStyleDict())
  svg.addElement(t1)
  print svg.getXML()
  svg.saveSVG('c:\\test.svg')
  
if __name__ == '__main__': testPath()