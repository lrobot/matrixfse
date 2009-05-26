#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
This module is used to create the pySVG Logo.
"""

from pysvg.core import *

def main():
  mySVG=svg(0,0, width="100%", height="100%")
  
  t=text("pySVG", x=0,y=100)
  group=g()
  group.set_transform("rotate(-30)")
  t.set_stroke_width('1px')
  t.set_stroke('#00C')
  t.set_fill('none')
  t.set_font_size("36")
  group.addElement(t)
  
  mySVG.addElement(group)
  
  print mySVG.getXML()
  f = open('pySVGLogo.svg', 'w')
  f.write(wrap_xml(mySVG.getXML()))
  f.close()
  
if __name__ == '__main__': 
  main()