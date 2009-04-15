#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
DEPRECATED ::: NOT UP TO DATE :::: NOT WORKING !!!
"""

from pysvg.pysvg import *
from pysvg.objecthelper import *
from pysvg.stylehelper import *

def Image():
  svg=SVG("test")
  i=image(x=800,y=250,width=88,height=31,xlink_='http://img0.gmodules.com/ig/images/googlemail.gif',embedded_=False)
  svg.addElement(i)
  i=image(x=900,y=250,width=88,height=31,xlink_='../images.jpg',embedded_=True)
  svg.addElement(i)
  print svg.getXML()
  svg.saveSVG('Image.svg')
    
      

def LinearGradient():
  svg=SVG("test")
  d=Definition()
  
  lg=linearGradient("orange_red")
  lg.addStop(offset='0%',color='rgb(255,255,0)', opacity=1)
  lg.addStop(offset='100%',color='rgb(255,0,0)', opacity=1)
  d.addDefinition(lg)
  
  oh=ObjectHelper()
  e=oh.createEllipse(cx="200", cy="190", rx="85", ry="55", fill="url(#orange_red)")
  
  svg.addElement(d)
  svg.addElement(e)
  print svg.getXML()
  svg.saveSVG('LinearGradient.svg')
  
def RadialGradient():
  svg=SVG("test")
  d=Definition()
   
  lg=radialGradient("grey_blue")
  lg.addStop(offset='0%',color='rgb(200,200,200)', opacity=1)
  lg.addStop(offset='100%',color='rgb(0,0,255)', opacity=1)
  d.addDefinition(lg)
  
  oh=ObjectHelper()
  e=oh.createEllipse(cx="230", cy="200", rx="110", ry="100", fill="url(#grey_blue)")
  
  svg.addElement(d)
  svg.addElement(e)
  print svg.getXML()
  svg.saveSVG('RadialGradient.svg')
  
def Grouping():
  oh=ObjectHelper()
  svg=SVG("test")
  
  #testing container
  style=StyleHelper()
  style.setStrokeWidth(2)
  style.setStroke("green")
  style_dict=style.getStyleDict()
  g=Group(style_dict)
  g.addElement(line(300,300,600,600))
  g.addElement(circle(500,500,50))
  svg.addElement(g)
  
  g=Group(style_dict)
  style_dict = {"stroke":"#000000", "fill":"none" ,"stroke-width":"49" ,"stroke-opacity":"0.027276"}
  p=path(pathData="M 300 100 A 1,1 0 0 1 802,800",style_dict=style_dict)
  p2=path(pathData="M 100 300 A 1,1 0 0 1 802,800",style_dict=style_dict)
  g.addElement(p)
  g.addElement(p2)
  svg.addElement(g)
  print svg.getXML()
  svg.saveSVG('Grouping.svg')


def ComplexShapes():
  oh=ObjectHelper()
  svg=SVG("test")
  pl=oh.createPolyline(points="50,375 150,375 150,325 250,325 250,375 350,375 350,250 450,250 450,375 \
550,375 550,175 650,175 650,375 750,375 750,100 850,100 850,375 950,375 \
950,25 1050,25 1050,375 1150,375 ",strokewidth=10, stroke='blue')
  svg.addElement(pl)
  
  pointsAsTuples=[(350,75),(379,161),(469,161),(397,215),(423,301),(350,250),(277,301),(303,215),(231,161),(321,161)]
  pg=oh.createPolygon(points=oh.convertTupleArrayToPoints(pointsAsTuples),strokewidth=10, stroke='blue', fill='red')
  svg.addElement(pg)
 
  sh=StyleHelper()
  sh.setFilling('#EEE')
  sh.setStroke('#00F')
  sh.setStrokeWidth('2px')
  path1=path('M 40,530 L 100,560 L 60,520 Z', style_dict=sh.getStyleDict())
  
  sh2=StyleHelper()
  sh2.setFilling('#FFC')
  sh2.setStroke('#00F')
  sh2.setStrokeWidth('2px')
  path2=path(style_dict=sh2.getStyleDict())
  path2.appendMoveToPath(190, 520, False)
  #as you can see we can mix strings and ints without trouble
  path2.appendCubicCurveToPath('+0', '+0', 30, 30, -60, 30, True)
  path2.appendCloseCurve()
  
  sh3=StyleHelper()
  sh3.setFilling('none')
  sh3.setStroke('#00F')
  sh3.setStrokeWidth('2px')
  path3=path('M 230,530', style_dict=sh3.getStyleDict())
  path3.appendQuadraticCurveToPath(0, 30, 30, 0)
  path3.appendQuadraticCurveToPath(30, -30, 30, 0)
  path3.appendQuadraticCurveToPath(-0, 30, 30, 0)
  path3.appendQuadraticCurveToPath(30, -20, 30, 0)
  
  svg.addElement(path1)
  svg.addElement(path2)
  svg.addElement(path3)
  
  svg.saveSVG('ComplexShapes.svg')

  
def Shapes():
  oh=ObjectHelper()
  svg=SVG("test")
  
  svg.addElement(oh.createRect(0,0,400,200,12,12,strokewidth=2, stroke='navy'))
  svg.addElement(oh.createRect(100,50,200,100,strokewidth=2, stroke='navy', fill='yellow'))
  svg.addElement(oh.createCircle(700,500,50,strokewidth=5, stroke='red'))
  svg.addElement(oh.createCircle(810,500,50,strokewidth=5, stroke='yellow', fill='#AAAAAA'))
  svg.addElement(oh.createEllipse(600,50,50,30,strokewidth=5, stroke='red'))
  svg.addElement(oh.createEllipse(700,50,50,30,strokewidth=5, stroke='yellow', fill='#00AABB'))
  svg.addElement(oh.createLine(0,0,300,300,strokewidth=2,stroke="black"))
  svg.saveSVG('Shapes.svg')
  
def Line():
  svg=SVG("test")
  style=StyleHelper()
  style.setStrokeWidth(2)
  style.setStroke('black')
  l=line(0,0,300,300, style.getStyleDict())
  svg.addElement(l)
  #second method is easier
  oh=ObjectHelper()
  svg.addElement(oh.createLine(10,0,300,300,strokewidth=2,stroke="blue"))
  svg.saveSVG('Line.svg')
  
def TextFeatures():
  oh=ObjectHelper()
  svg=SVG("test")
  style=StyleHelper()
  style.setFontFamily(fontfamily="Verdana")
  style.setFontSize('5em')
  style.setFilling(fill="blue")
  t1=text("Verdana, blue, 5em",0,100,style_dict=style.getStyleDict())
  t2=text("pySVG simple",0,200)
  svg.addElement(t1)
  svg.addElement(t2)
  
  rect=oh.createRect(350, 250, 100, 100, fill='green')
  svg.addElement(rect)
  
  style=StyleHelper()
  style.setFontFamily(fontfamily="Times")
  style.setFontSize('2em')
  style.setFontStyle('italic')
  style.setFontWeight('bold')
  style.setFilling(fill="red")
  style.setFillOpacity('0.5')
  style.setFillRule('evenodd')
  
  t3=text("Times, italic, 2em, bold, opacity=0.5, fillrule=evenodd",0,300,style_dict=style.getStyleDict())
  svg.addElement(t3)

  style=StyleHelper()
  style.setFontFamily(fontfamily="Times")
  style.setFontSize('2em')
  style.setFontStyle('italic')
  style.setFilling(fill="red")
  style.setFillOpacity('0.5')
  #style.fill="blue"
  t4=text("Times, italic, 2em, non bold, opacity=0.5",0,400,style_dict=style.getStyleDict())
  svg.addElement(t4)

  
  print svg.getXML()
  svg.saveSVG('TextFeatures.svg')
  


def HelloWorld2():
  svg=SVG("Hello World Example") # title is ignored still
  style=StyleHelper()
  style.setFontFamily(fontfamily="Verdana")
  style.setFontSize('5em') #no need for the keywords all the time
  style.setFilling("blue")
  t1=text("Hello World",0,100,style_dict=style.getStyleDict())
  svg.addElement(t1)
  print svg.getXML()
  svg.saveSVG('HelloWorld2.svg')

def HelloWorld1():
  svg=SVG("Hello World Example") # title is ignored still
  t=text("Hello World",0,200)
  svg.addElement(t)
  print svg.getXML()
  svg.saveSVG('HelloWorld1.svg')
  
def tutorialChain():
  HelloWorld1()
  HelloWorld2()
  TextFeatures()
  Shapes()
  Line()
  ComplexShapes()
  Grouping()
  LinearGradient()
  RadialGradient()
  Image()
  
if __name__ == '__main__': 
  tutorialChain()