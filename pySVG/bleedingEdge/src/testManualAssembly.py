from pysvg import *
'''
Created on 15.04.2009

@author: kerim
'''
s=svgType()
s.set_height(300)
s.set_width(400)
l=lineType()
l.set_x1(100)
l.set_x2(200)
l.set_y1(100)
l.set_y2(200)
l.set_stroke('#00C')
l.set_stroke_width('2px')
s.addElement(l)

l=lineType()
l.set_x1(210)
l.set_x2(300)
l.set_y1(200)
l.set_y2(300)
l.set_style("stroke:#00C;stroke-width:2px")
s.addElement(l)
t=textType(x="10",y="20")
obj_ = t.mixedclass_(MixedContainer.CategoryText, MixedContainer.TypeNone, '', "huhu")

t.content_.append(obj_)
            
s.addElement(t)
f=open('c:\\test.svg','wb')
s.export(f, level=0, namespace_='',namespacedef_='xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"', name_='')
