'''
Created on 12.04.2009

@author: kerim
'''
import types
#import pysvg.util as util
from attributedelements import *




#TODO: FIX ME
def wrap_xml(xml):
    return '''<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>'''+xml

def save(element,filename):
    f = open(filename, 'w')
    f.write(wrap_xml(element.getXML()))
    f.close()

class style(BaseElement):
    def __init__(self, ):
        BaseElement.__init__(self,'style')
    
    def set_type(self,content_type):
        self._attributes['type']=content_type
    def get_type(self):
        return self.attributes['type']
    
    def set_media(self,media_descriptors):
        self._attributes['media']=media_descriptors
    def get_media(self):
        return self.attributes['media']
    
    def set_title(self,title):
        self._attributes['title']=title
    def get_title(self):
        return self.attributes['title']

class script(BaseElement):
    def __init__(self, ):
        BaseElement.__init__(self,'script')
    
    def set_externalResourcesRequired(self, externalResourcesRequired):
        self._attributes['externalResourcesRequired']=externalResourcesRequired
    def get_externalResourcesRequired(self):
        return self._attributes.get('externalResourcesRequired')
    
    def set_type(self,content_type):
        self._attributes['type']=content_type
    def get_type(self):
        return self.attributes['type']
    #xlink attrib
    #xlink:type, xlink:href, xlink:role, xlink:arcrole, xlink:title, xlink:show, xlink:actuate
    def set_xlink_type(self,xlink_type):
        self._attributes['xlink:type']=xlink_type
    def get_xlink_type(self):
        return self.attributes['xlink:type']
    
    def set_xlink_href(self,xlink_href):
        self._attributes['xlink:href']=xlink_href
    def get_xlink_href(self):
        return self.attributes['xlink:href']
    
    def set_xlink_role(self,xlink_role):
        self._attributes['xlink:role']=xlink_role
    def get_xlink_role(self):
        return self.attributes['xlink:role']
    
    def set_xlink_arcrole(self,xlink_arcrole):
        self._attributes['xlink:arcrole']=xlink_arcrole
    def get_xlink_arcrole(self):
        return self.attributes['xlink:arcrole']
    
    def set_xlink_title(self,xlink_title):
        self._attributes['xlink:title']=xlink_title
    def get_xlink_title(self):
        return self.attributes['xlink:title']
    
    def set_xlink_show(self,xlink_show):
        self._attributes['xlink:show']=xlink_show
    def get_xlink_show(self):
        return self.attributes['xlink:show']
    
    def set_xlink_actuate(self,xlink_actuate):
        self._attributes['xlink:actuate']=xlink_actuate
    def get_xlink_actuate(self):
        return self.attributes['xlink:actuate']


class pattern(StyledElement):
    def __init__(self, x=None, y=None,width=None, height=None, patternUnits=None, patternContentUnits=None, patternTransform=None, viewBox=None, preserveAspectRatio=None):
        StyledElement.__init__(self,'pattern')
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        self.set_patternUnits(patternUnits)
        self.set_patternContentUnits(patternContentUnits)
        self.set_patternTransform(patternTransform)
        self.set_viewBox(viewBox)
        self.set_preserveAspectRatio(preserveAspectRatio)
    
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_height(self, height):
        self._attributes['height']=height
    
    def get_height(self):
        return self._attributes.get('height')
    
    def set_width(self, width):
        self._attributes['width']=width
    
    def get_width(self):
        return self._attributes.get('width')
    
    def set_patternUnits(self, patternUnits):
        self._attributes['patternUnits']=patternUnits
    
    def get_patternUnits(self):
        return self._attributes.get('patternUnits')
    
    def set_patternContentUnits(self, patternContentUnits):
        self._attributes['patternContentUnits']=patternContentUnits
    
    def get_patternContentUnits(self):
        return self._attributes.get('patternContentUnits')
    
    def set_patternTransform(self, patternTransform):
        self._attributes['patternTransform']=patternTransform
    
    def get_patternTransform(self):
        return self._attributes.get('patternTransform')
    
    def set_viewBox(self, viewBox):
        self._attributes['viewBox']=viewBox
    
    def get_viewBox(self):
        return self._attributes.get('viewBox')
    
    def set_preserveAspectRatio(self, preserveAspectRatio):
        self._attributes['preserveAspectRatio']=preserveAspectRatio
    
    def get_preserveAspectRatio(self):
        return self._attributes.get('preserveAspectRatio')
    
class stop(GradientElement):
    def __init__(self, offset=None):
        GradientElement.__init__(self,'stop')
        self.set_offset(offset)
    
    def set_offset(self, offset):
        self._attributes['offset']=offset
    
    def get_offset(self):
        return self._attributes.get('offset')    
        


class linearGradient(CommonGradientElement):
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        CommonGradientElement.__init__(self,'linearGradient')
        self.set_x1(x1)
        self.set_y1(y1)
        self.set_x2(x2)
        self.set_y2(y2)

    def set_x1(self, x1):
        self._attributes['x1']=x1
    
    def get_x1(self):
        return self._attributes.get('x1')
    
    def set_y1(self, y1):
        self._attributes['y1']=y1
    
    def get_y1(self):
        return self._attributes.get('y1')
    
    def set_x2(self, x2):
        self._attributes['x2']=x2
    
    def get_x2(self):
        return self._attributes.get('x2')
    
    def set_y2(self, y2):
        self._attributes['y2']=y2
    
    def get_y2(self):
        return self._attributes.get('y2')

class stop(GradientElement):
    def __init__(self, offset=None):
        GradientElement.__init__(self,'stop')
        self.set_offset(offset)
        
    def set_offset(self, offset):
        self._attributes['offset']=offset
    
    def get_offset(self):
        return self._attributes.get('offset')
    
    
    
class radialGradient(CommonGradientElement):
    def __init__(self, cx='50%',cy='50%',r='50%', fx='50%',fy='50%'):
        CommonGradientElement.__init__(self,'radialGradient')
        self.set_cx(cx)
        self.set_cy(cy)
        self.set_fx(fx)
        self.set_fy(fy)
        self.set_r(r)
        
    def set_cx(self, cx):
        self._attributes['cx']=cx
    
    def get_cx(self):
        return self._attributes.get('cx')
    
    def set_cy(self, cy):
        self._attributes['cy']=cy
    
    def get_cy(self):
        return self._attributes.get('cy')
    
    def set_fx(self, fx):
        self._attributes['fx']=fx
    
    def get_fx(self):
        return self._attributes.get('fx')
    
    def set_fy(self, fy):
        self._attributes['fy']=fy
    
    def get_fy(self):
        return self._attributes.get('fy')  
    
    def set_r(self, r):
        self._attributes['r']=r
    
    def get_r(self):
        return self._attributes.get('r')  

    

    
class circle(ShapeElement):
    """
    Class representing the cirle element of an svg doc.
    """
    def __init__(self,cx=None,cy=None,r=None):
        ShapeElement.__init__(self,'circle')
        self.set_cx(cx)
        self.set_cy(cy)
        self.set_r(r) 

    def set_cx(self, cx):
        self._attributes['cx']=cx
    
    def get_cx(self):
        return self._attributes.get('cx')
    
    def set_cy(self, cy):
        self._attributes['cy']=cy
    
    def get_cy(self):
        return self._attributes.get('cy')
    
    def setRadius(self, r):
        self._attributes['r']=r
    
    def getRadius(self):
        return self._attributes.get('r')
    #TODO: radius twice for xml parsing
    def set_r(self, r):
        self._attributes['r']=r
    
    def get_r(self):
        return self._attributes.get('r')

class ellipse(ShapeElement):
    """
    Class representing the ellipse element of an svg doc.
    """
    def __init__(self,cx=None,cy=None,rx=None,ry=None):
        ShapeElement.__init__(self,'ellipse')
        self.set_cx(cx)
        self.set_cy(cy)
        self.set_rx(rx)
        self.set_ry(ry)
    
    def set_cx(self, cx):
        self._attributes['cx']=cx
    
    def get_cx(self):
        return self._attributes.get('cx')
    
    def set_cy(self, cy):
        self._attributes['cy']=cy
    
    def get_cy(self):
        return self._attributes.get('cy')
    
    def set_rx(self, rx):
        self._attributes['rx']=rx
    
    def get_rx(self):
        return self._attributes.get('rx')
    
    def set_ry(self, ry):
        self._attributes['ry']=ry
    
    def get_ry(self):
        return self._attributes.get('ry')

class line(ShapeElement):
    """
    Class representing the line element of an svg doc.
    Note that this element is NOT painted VISIBLY by default UNLESS you provide
    a style including STROKE and STROKE-WIDTH
    """
    def __init__(self,x1=None,y1=None,x2=None,y2=None):
        """
        Creates a line
        @type  x1: string or int
        @param x1:  starting x-coordinate
        @type  x1: string or int
        @param y1:  starting y-coordinate
        @type  y2: string or int
        @param x2:  ending x-coordinate
        @type  y2: string or int
        @param y2:  ending y-coordinate
        """
        ShapeElement.__init__(self,'line')
        self.set_x1(x1)
        self.set_y1(y1)
        self.set_x2(x2)
        self.set_y2(y2)
        
    def set_x1(self, x1):
        self._attributes['x1']=x1
    
    def get_x1(self):
        return self._attributes.get('x1')
    
    def set_y1(self, y1):
        self._attributes['y1']=y1
    
    def get_y1(self):
        return self._attributes.get('y1')
    
    def set_x2(self, x2):
        self._attributes['x2']=x2
    
    def get_x2(self):
        return self._attributes.get('x2')
    
    def set_y2(self, y2):
        self._attributes['y2']=y2
    
    def get_y2(self):
        return self._attributes.get('y2')
    
class polyline(ShapeElement):
    """
    Class representing the polyline element of an svg doc.
    """
    def __init__(self, points=None):
        ShapeElement.__init__(self,'polyline')
        self.set_points(points)
        
    def set_points(self,points):
        self._attributes['points']=points
    
    def get_points(self):
        return self._attributes['points']

class polygon(polyline):
    """
    Class representing the polygon element of an svg doc.
    """
    def __init__(self,points=None):
        ShapeElement.__init__(self,'polygon')
        self.set_points(points)
        
class path(ShapeElement):
    def __init__(self,pathData="",pathLength=None,style_dict=None, focusable=None):
        ShapeElement.__init__(self,'path')
        if pathData!='' and not pathData.endswith(' '):
            pathData+=' '
        self.set_d(pathData)
    
    def set_d(self,path):
        self._attributes['d']=path
    
    def get_d(self):
        return self._attributes['d']
"""
  def __append__(self,command, params, relative=True):
    if relative==True:
      self.d+=command.lower()
    else:
      self.d+=command.upper()
    for param in params:
      self.d+=' %s ' %(param)
        
  def appendLineToPath(self,endx,endy, relative=True):
    self.__append__('l',[endx,endy], relative)
  
  def appendHorizontalLineToPath(self,endx, relative=True):
    self.__append__('h',[endx], relative)
      
  def appendVerticalLineToPath(self,endy, relative=True):
    self.__append__('v',[endy], relative)
  
  def appendMoveToPath(self,endx,endy, relative=True):
    self.__append__('m',[endx,endy], relative)
    
  def appendCloseCurve(self):
    self.d+="z"
  
  def appendCubicCurveToPath(self, controlstartx, controlstarty, controlendx, controlendy, endx,endy,relative=True):
    self.__append__('c',[controlstartx, controlstarty, controlendx, controlendy, endx,endy], relative)
  
  def appendCubicShorthandCurveToPath(self,  controlendx, controlendy, endx,endy,relative=True):
    self.__append__('s',[controlendx, controlendy, endx,endy], relative)
    
  def appendQuadraticCurveToPath(self, controlx, controly, endx,endy,relative=True):
    self.__append__('q',[controlx, controly, endx,endy], relative)
  
  def appendQuadraticShorthandCurveToPath(self, endx,endy,relative=True):
    self.__append__('t',[endx,endy], relative)
    
  def appendArcToPath(self,rx,ry,x,y,x_axis_rotation=0,large_arc_flag=0,sweep_flag=1 ,relative=True):
    #self.__append__('a',[rx,ry,x,y,x_axis_rotation,large_arc_flag,sweep_flag], relative)
    self.__append__('a',[rx,ry,x_axis_rotation,large_arc_flag,sweep_flag,x,y], relative)
"""           
class rect(ShapeElement):
    """
    Class representing the rect element of an svg doc.
    """
    def __init__(self, x=None, y=None, width=None, height=None, rx=None, ry=None):
        ShapeElement.__init__(self,'rect')
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_rx(rx)
        self.set_ry(ry)
    
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_rx(self, rx):
        self._attributes['rx']=rx
    
    def get_rx(self):
        return self._attributes.get('rx')
    
    def set_ry(self, ry):
        self._attributes['ry']=ry
    
    def get_ry(self):
        return self._attributes.get('ry')
    
    def set_height(self, height):
        self._attributes['height']=height
    
    def get_height(self):
        return self._attributes.get('height')
    
    def set_width(self, width):
        self._attributes['width']=width
    
    def get_width(self):
        return self._attributes.get('width')

        
class text(ShapeElement):
    """
    Class representing the text element of an svg doc.
    """
    def __init__(self, content=None, x=None, y=None, dx=None, dy=None, rotate=None, textLength=None, lengthAdjust=None, elementName='text'):
        ShapeElement.__init__(self,elementName)
        if content <> None:
            self.appendTextContent(content)
        self.set_x(x)
        self.set_y(y)
        self.set_dx(dx)
        self.set_dy(dy)
        self.set_rotate(rotate)
        self.set_textLength(textLength)
        self.set_lengthAdjust(lengthAdjust)
    
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_dx(self, dx):
        self._attributes['dx']=dx
    
    def get_dx(self):
        return self._attributes.get('dx')
    
    def set_dy(self, dy):
        self._attributes['dy']=dy
    
    def get_dy(self):
        return self._attributes.get('dy')
    
    def set_rotate(self, rotate):
        self._attributes['rotate']=rotate
    
    def get_rotate(self):
        return self._attributes.get('rotate')
    
    def set_textLength(self, textLength):
        self._attributes['textLength']=textLength
    
    def get_textLength(self):
        return self._attributes.get('textLength')
    
    def set_lengthAdjust(self, lengthAdjust):
        self._attributes['lengthAdjust']=lengthAdjust
    
    def get_lengthAdjust(self):
        return self._attributes.get('lengthAdjust')
    
    def set_font_size(self, fontSize):
        self._attributes['font-size']=fontSize
    
    def get_font_size(self):
        return self._attributes.get('font-size')

class tspan(text):
    """
    Class representing the tspan element of an svg doc.
    """
    def __init__(self, x=None, y=None, dx=None, dy=None, rotate=None, textLength=None, lengthAdjust=None):
        text.__init__(self,elementName='tspan')

class a(GraphicalEventsElement):
    def __init__(self, target=None):
        GraphicalEventsElement.__init__(self, 'a')
        self.set_target(target)
    
    def set_target(self, target):
        self._attributes['target']=target
    
    def get_target(self):
        return self._attributes.get('target')
    
    #xlink attrib
    #xlink:type, xlink:href, xlink:role, xlink:arcrole, xlink:title, xlink:show, xlink:actuate
    def set_xlink_type(self,xlink_type):
        self._attributes['xlink:type']=xlink_type
    def get_xlink_type(self):
        return self.attributes['xlink:type']
    
    def set_xlink_href(self,xlink_href):
        self._attributes['xlink:href']=xlink_href
    def get_xlink_href(self):
        return self.attributes['xlink:href']
    
    def set_xlink_role(self,xlink_role):
        self._attributes['xlink:role']=xlink_role
    def get_xlink_role(self):
        return self.attributes['xlink:role']
    
    def set_xlink_arcrole(self,xlink_arcrole):
        self._attributes['xlink:arcrole']=xlink_arcrole
    def get_xlink_arcrole(self):
        return self.attributes['xlink:arcrole']
    
    def set_xlink_title(self,xlink_title):
        self._attributes['xlink:title']=xlink_title
    def get_xlink_title(self):
        return self.attributes['xlink:title']
    
    def set_xlink_show(self,xlink_show):
        self._attributes['xlink:show']=xlink_show
    def get_xlink_show(self):
        return self.attributes['xlink:show']
    
    def set_xlink_actuate(self,xlink_actuate):
        self._attributes['xlink:actuate']=xlink_actuate
    def get_xlink_actuate(self):
        return self.attributes['xlink:actuate']
    
class g(GraphicalEventsElement):
     def __init__(self):
        GraphicalEventsElement.__init__(self,'g')
    
class defs(GraphicalEventsElement):
     def __init__(self):
        GraphicalEventsElement.__init__(self,'defs')
                 
class svg(DocumentElement):
    def __init__(self, x=None, y=None, width=None, height=None):
        DocumentElement.__init__(self,'svg')  
        self.set_xmlns('http://www.w3.org/2000/svg')
        self.set_xmlns_xlink('http://www.w3.org/1999/xlink')
        self.setAttribute('version','1.1')
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
    
    def set_xmlns(self, xmlns):
        self._attributes['xmlns']=xmlns
    
    def get_xmlns(self):
        return self._attributes.get('xmlns')
    
    def set_xmlns_xlink(self, xmlns_xlink):
        self._attributes['xmlns:xlink']=xmlns_xlink
    
    def get_xmlns_xlink(self):
        return self._attributes.get('xmlns:xlink')
    
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_height(self, height):
        self._attributes['height']=height
    
    def get_height(self):
        return self._attributes.get('height')
    
    def set_width(self, width):
        self._attributes['width']=width
    
    def get_width(self):
        return self._attributes.get('width')
    
    def set_baseProfile(self,baseProfile):
        self._attributes['baseProfile']=baseProfile
    
    def get_baseProfile(self):
        return self._attributes['baseProfile']
    
    def set_viewBox(self,viewBox):
        self._attributes['viewBox']=viewBox
    
    def get_viewBox(self):
        return self._attributes['viewBox']
    
    def set_preserveAspectRatio(self,preserveAspectRatio):
        self._attributes['preserveAspectRatio']=preserveAspectRatio
    
    def get_preserveAspectRatio(self):
        return self._attributes['preserveAspectRatio']
    
    def set_zoomAndPan(self,zoomAndPan):
        self._attributes['zoomAndPan']=zoomAndPan
    
    def get_zoomAndPan(self):
        return self._attributes['zoomAndPan']
    
    def set_contentScriptType(self,contentScriptType):
        self._attributes['contentScriptType']=contentScriptType
    
    def get_contentScriptType(self):
        return self._attributes['contentScriptType']
    
    def set_contentStyleType(self,contentStyleType):
        self._attributes['contentStyleType']=contentStyleType
    
    def get_contentStyleType(self):
        return self._attributes['contentStyleType']
    
class image(ShapeElement, script):
    def __init__(self, x=None, y=None, width=None, height=None):
        ShapeElement.__init__(self,'image')  
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_preserveAspectRatio

    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')   
    
    def set_height(self, height):
        self._attributes['height']=height
    
    def get_height(self):
        return self._attributes.get('height')
    
    def set_width(self, width):
        self._attributes['width']=width
    
    def get_width(self):
        return self._attributes.get('width')
    
    def set_embedded(self, embedded):
        self._attributes['embedded']=embedded
    
    def get_embedded(self):
        return self._attributes.get('embedded')
    
    def set_preserveAspectRatio(self, preserveAspectRatio):
        self._attributes['preserveAspectRatio']=preserveAspectRatio
    
    def get_preserveAspectRatio(self):
        return self._attributes.get('preserveAspectRatio')
             
class desc(BaseElement):
    def __init__(self):
        BaseElement.__init__(self,'desc')  
    
    def set_class(self, aClass):
        self._attributes['class']=aClass
    
    def get_class(self):
        return self._attributes.get('class')
    
    #style.attrib TODO remove and make superclass
    def set_style(self, style):
        self._attributes['style']=style
    
    def get_style(self):
        return self._attributes.get('style')
    
    def set_content(self, content):
        self._attributes['content']=content
    
    def get_content(self):
        return self._attributes.get('content')

#TODO wrong inheritence
class title(desc):
    def __init__(self):
        desc.__init__(self,'title')  


class filter(StyledElement):
    def __init__(self, x=None, y=None, width=None, height=None,filterRes=None, filterUnits=None, primitiveUnits=None):
        StyledElement.__init__(self,'filter')  
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_filterRes(filterRes)
        self.set_filterUnits(filterUnits)
        self.set_primitiveUnits(primitiveUnits)
        
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_height(self, height):
        self._attributes['height']=height
    
    def get_height(self):
        return self._attributes.get('height')
    
    def set_width(self, width):
        self._attributes['width']=width
    
    def get_width(self):
        return self._attributes.get('width')
    
    def set_filterRes(self, filterRes):
        self._attributes['filterRes']=filterRes
    
    def get_filterRes(self):
        return self._attributes.get('filterRes')
    
    def set_filterUnits(self, filterUnits):
        self._attributes['filterUnits']=filterUnits
    
    def get_filterUnits(self):
        return self._attributes.get('filterUnits')
    
    def set_primitiveUnits(self, primitiveUnits):
        self._attributes['primitiveUnits']=primitiveUnits
    
    def get_primitiveUnits(self):
        return self._attributes.get('primitiveUnits')
    
    #xlink attrib
    #xlink:type, xlink:href, xlink:role, xlink:arcrole, xlink:title, xlink:show, xlink:actuate
    def set_xlink_type(self,xlink_type):
        self._attributes['xlink:type']=xlink_type
    def get_xlink_type(self):
        return self.attributes['xlink:type']
    
    def set_xlink_href(self,xlink_href):
        self._attributes['xlink:href']=xlink_href
    def get_xlink_href(self):
        return self.attributes['xlink:href']
    
    def set_xlink_role(self,xlink_role):
        self._attributes['xlink:role']=xlink_role
    def get_xlink_role(self):
        return self.attributes['xlink:role']
    
    def set_xlink_arcrole(self,xlink_arcrole):
        self._attributes['xlink:arcrole']=xlink_arcrole
    def get_xlink_arcrole(self):
        return self.attributes['xlink:arcrole']
    
    def set_xlink_title(self,xlink_title):
        self._attributes['xlink:title']=xlink_title
    def get_xlink_title(self):
        return self.attributes['xlink:title']
    
    def set_xlink_show(self,xlink_show):
        self._attributes['xlink:show']=xlink_show
    def get_xlink_show(self):
        return self.attributes['xlink:show']
    
    def set_xlink_actuate(self,xlink_actuate):
        self._attributes['xlink:actuate']=xlink_actuate
    def get_xlink_actuate(self):
        return self.attributes['xlink:actuate']
    
    def set_externalResourcesRequired(self, externalResourcesRequired):
        self._attributes['externalResourcesRequired']=externalResourcesRequired
    def get_externalResourcesRequired(self):
        return self._attributes.get('externalResourcesRequired')

class feComponentTransfer(FilterPrimitiveWithInElement):
    def __init__(self):
        FilterPrimitiveWithInElement.__init__(self,'feComponentTransfer')

class feTile(FilterPrimitiveWithInElement):
    def __init__(self):
        FilterPrimitiveWithInElement.__init__(self,'feTile')
        
class feMerge(FilterPrimitiveWithInElement):
    def __init__(self):
        FilterPrimitiveWithInElement.__init__(self,'feMerge')

class feMergeNode(FilterPrimitiveElement):
    def __init__(self):
        FilterPrimitiveWithInElement.__init__(self,'feMergeNode')      
        
class feBlend(FilterPrimitiveWithInElement):
    def __init__(self, in2=None, mode=None):
        FilterPrimitiveWithInElement.__init__(self,'feBlend')  
        self.set_in2(in2)
        self.set_mode(mode)
    
    def set_in2(self, in2):
        self._attributes['in2']=in2
    def get_in2(self):
        return self._attributes.get('in2')
    
    def set_mode(self, mode):
        self._attributes['mode']=mode
    def get_mode(self):
        return self._attributes.get('mode')
    
class feColorMatrix(FilterPrimitiveWithInElement):
    def __init__(self, type=None, values=None):
        FilterPrimitiveWithInElement.__init__(self,'feColorMatrix')  
        self.set_type(type)
        self.set_values(values)
    
    def set_type(self, type):
        self._attributes['type']=type
    def get_type(self):
        return self._attributes.get('type')
    
    def set_values(self, values):
        self._attributes['values']=values
    def get_values(self):
        return self._attributes.get('values')

class feGaussianBlur(FilterPrimitiveWithInElement):
    def __init__(self, stdDeviation=None):
        FilterPrimitiveWithInElement.__init__(self,'feGaussianBlur')  
        self.set_stdDeviation(stdDeviation)
    
    def set_stdDeviation(self, stdDeviation):
        self._attributes['stdDeviation']=stdDeviation
    def get_stdDeviation(self):
        return self._attributes.get('stdDeviation')
    
class feComposite(FilterPrimitiveWithInElement):
    def __init__(self, in2=None, operator=None, k1=None, k2=None, k3=None, k4=None):
        FilterPrimitiveWithInElement.__init__(self,'feComposite')  
        self.set_in2(in2)
        self.set_k1(k1)
        self.set_k2(k2)
        self.set_k3(k3)
        self.set_k4(k4)
        self.set_operator(operator)
    
    def set_in2(self, in2):
        self._attributes['in2']=in2
    def get_in2(self):
        return self._attributes.get('in2')
    
    def set_operator(self, operator):
        self._attributes['operator']=operator
    def get_operator(self):
        return self._attributes.get('operator')
    
    def set_k1(self, k1):
        self._attributes['k1']=k1
    def get_k1(self):
        return self._attributes.get('k1')
    def set_k2(self, k2):
        self._attributes['k2']=k2
    def get_k2(self):
        return self._attributes.get('k2')
    def set_k3(self, k3):
        self._attributes['k3']=k3
    def get_k3(self):
        return self._attributes.get('k3')
    def set_k4(self, k4):
        self._attributes['k4']=k4
    def get_k4(self):
        return self._attributes.get('k4')

class feSpecularLighting(FilterPrimitiveWithInElement):
    def __init__(self, lighting_color=None, surfaceScale=None, specularConstant=None, specularExponent=None, kernelUnitLength=None):
        FilterPrimitiveWithInElement.__init__(self,'feSpecularLighting') 
        self.set_lighting_color(lighting_color)
        self.set_surfaceScale(surfaceScale)
        self.set_specularConstant(specularConstant)
        self.set_specularExponent(specularExponent)
        self.set_kernelUnitLength(kernelUnitLength)
    
    def set_lighting_color(self, lighting_color):
        self._attributes['lighting-color']=lighting_color
    def get_lighting_color(self):
        return self._attributes.get('lighting-color')
    
    def set_surfaceScale(self, surfaceScale):
        self._attributes['surfaceScale']=surfaceScale
    def get_surfaceScale(self):
        return self._attributes.get('surfaceScale')
    
    def set_specularConstant(self, specularConstant):
        self._attributes['specularConstant']=specularConstant
    def get_specularConstant(self):
        return self._attributes.get('specularConstant')
    
    def set_specularExponent(self, specularExponent):
        self._attributes['specularExponent']=specularExponent
    def get_specularExponent(self):
        return self._attributes.get('specularExponent')
    
    def set_kernelUnitLength(self, kernelUnitLength):
        self._attributes['kernelUnitLength']=kernelUnitLength
    def get_kernelUnitLength(self):
        return self._attributes.get('kernelUnitLength')


class feFuncElement(BaseElement):
    def __init__(self, elementName, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        BaseElement.__init__(self,elementName)
        self.set_type(type)
        self.set_tableValues(tableValues)
        self.set_slope(slope)
        self.set_intercept(intercept)
        self.set_amplitude(amplitude)
        self.set_exponent(exponent)
        self.set_offset(offset)
    
    def set_type(self, type):
        self._attributes['type']=type
    def get_type(self):
        return self._attributes.get('type')
    
    def set_tableValues(self, tableValues):
        self._attributes['tableValues']=tableValues
    def get_tableValues(self):
        return self._attributes.get('tableValues')
    
    def set_slope(self, slope):
        self._attributes['slope']=slope
    def get_slope(self):
        return self._attributes.get('slope')
    
    def set_intercept(self, intercept):
        self._attributes['intercept']=intercept
    def get_intercept(self):
        return self._attributes.get('intercept')
    
    def set_amplitude(self,amplitude ):
        self._attributes['amplitude']=amplitude
    def get_amplitude(self):
        return self._attributes.get('amplitude')
    
    def set_exponent(self,exponent ):
        self._attributes['exponent']=exponent
    def get_exponent(self):
        return self._attributes.get('exponent')
    
    def set_offset(self, offset):
        self._attributes['offset']=offset
    def get_offset(self):
        return self._attributes.get('offset')

class feDistantLight(BaseElement):
    def __init__(self, azimuth=None, elevation=None):
        BaseElement.__init__(self,'feDistantLight')
        self.set_azimuth(azimuth)
        self.set_elevation(elevation)
    
    def set_azimuth(self,azimuth):
        self._attributes['azimuth']=azimuth
    def get_azimuth(self):
        return self._attributes.get('azimuth')
    
    def set_elevation(self, elevation):
        self._attributes['elevation']=elevation
    def get_elevation(self):
        return self._attributes.get('elevation')   

class fePointLight(BaseElement):
    def __init__(self, x=None, y=None, z=None):
        BaseElement.__init__(self,'fePointLight')
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
         
    def set_x(self, x):
        self._attributes['x']=x
    
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    
    def get_y(self):
        return self._attributes.get('y')
    
    def set_z(self, z):
        self._attributes['z']=z
    
    def get_z(self):
        return self._attributes.get('z')

class feSpotLight(BaseElement):
    def __init__(self, x=None, y=None, z=None, pointsAtX=None,pointsAtY=None, pointsAtZ=None, specularExponent=None, limitingConeAngle=None):
        BaseElement.__init__(self,'feSpotLight')
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_pointsAtX(pointsAtX)
        self.set_pointsAtY(pointsAtY)
        self.set_pointsAtZ(pointsAtZ)
        self.set_specularExponent(specularExponent)
        self.set_limitingConeAngle(limitingConeAngle)
 
    def set_x(self, x):
        self._attributes['x']=x
    def get_x(self):
        return self._attributes.get('x')
    
    def set_y(self, y):
        self._attributes['y']=y
    def get_y(self):
        return self._attributes.get('y')
    
    def set_z(self, z):
        self._attributes['z']=z
    def get_z(self):
        return self._attributes.get('z')
    
    def set_pointsAtX(self, pointsAtX):
        self._attributes['pointsAtX']=pointsAtX
    def get_pointsAtX(self):
        return self._attributes.get('pointsAtX')
    
    def set_pointsAtY(self, pointsAtY):
        self._attributes['pointsAtY']=pointsAtY
    def get_pointsAtY(self):
        return self._attributes.get('pointsAtY')
    
    def set_pointsAtZ(self, pointsAtZ):
        self._attributes['pointsAtZ']=pointsAtZ
    def get_pointsAtZ(self):
        return self._attributes.get('pointsAtZ')
    
    def set_specularExponent(self, specularExponent):
        self._attributes['specularExponent']=specularExponent
    def get_specularExponent(self):
        return self._attributes.get('specularExponent')
    
    def set_limitingConeAngle(self, limitingConeAngle):
        self._attributes['limitingConeAngle']=limitingConeAngle
    def get_limitingConeAngle(self):
        return self._attributes.get('limitingConeAngle')
    
class feFuncR(feFuncElement):
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        feFuncElement.__init__(self,'feFuncR',type, tableValues, slope, intercept, amplitude, exponent, offset)
             
class feFuncG(feFuncR):
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
         feFuncElement.__init__(self,'feFuncG',type, tableValues, slope, intercept, amplitude, exponent, offset)
        
class feFuncB(feFuncR):
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
         feFuncElement.__init__(self,'feFuncB',type, tableValues, slope, intercept, amplitude, exponent, offset)
        
class feFuncA(feFuncR):
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        feFuncElement.__init__(self,'feFuncA',type, tableValues, slope, intercept, amplitude, exponent, offset)
                                
