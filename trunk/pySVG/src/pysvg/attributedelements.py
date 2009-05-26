'''
Created on 11.05.2009

@author: kerim
'''

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
    #    if "'" in s1:
        s1 = '%s' % s1.replace('"', "&quot;")
    #    else:
    #        s1 = "'%s'" % s1
    #else:
    #    s1 = '"%s"' % s1
    return s1

class TextContent:
    def __init__(self,content):
        self.content=content
    def setContent(self,content):
        self.content=content
    def getXML(self):
        return self.content
        
class BaseElement:
    """
    This is the base class for all noncontainer svg elements like title etc.
    """
    def __init__(self, elementName):
        """
        initializes the object
        @type  startTag: string 
        @param startTag:  the tag for the svg element name (e.g. <text ) 
        """
        self._elementName=elementName
        self._attributes={}  #key value
        self._textContent=""
        self._subElements=[]
        
    def setTextContent(self,text):
        #self._textContent=text
        self.addElement(TextContent(text))
    
    def appendTextContent(self,text):
        #self._textContent+=text
        self.addElement(TextContent(text))
        
    def addElement(self,element):
        self._subElements.append(element)
    
    def getElementAt(self,pos):
        return self._subElements[pos]
    
    def insertElementAt(self, element, pos):
        return self._subElements.insert(pos, element)
        
    def getXML(self):
        """
        Return a XML representation of the current element.
        This function can be used for debugging purposes. It is also used by getXML in SVG
    
        @return:  the representation of the current element as an xml string
        """
        xml='<'+self._elementName+' '
        for key,value in self._attributes.items():
            if value != None:
                xml+=key+'="'+quote_attrib(str(value))+'" '
        if  len(self._subElements)==0: #self._textContent==None and
            xml+=' />\n'
        else:
            xml+=' >\n'
            #if self._textContent==None:
            for subelement in self._subElements:
                xml+=subelement.getXML()
            #else:
            #if self._textContent!=None:
            #    xml+=self._textContent
            xml+='</'+self._elementName+'>\n'
        #print xml
        return xml

    #generic methods to set and get atributes (should only be used if something is not supported yet
    def setAttribute(self, attribute_name, attribute_value):
        self._attributes[attribute_name]=attribute_value
    
    def getAttribute(self, attribute_name):
        return self._attributes.get(attribute_name)
        
    #stdAttributes that all have
    def set_id(self,id):
        self._attributes['id']=id
    
    def get_id(self):
        return self._attributes.get('id')
    
    def set_xml_base(self,xml_base):
        self._attributes['xml:base']=xml_base
    
    def get_xml_base(self):
        return self._attributes.get('xml:base')


    # langSpaceAttrs
    def set_xml_lang(self, language_code):
        self._attributes['xml:lang']=language_code
    
    def get_xml_lang(self):
        return self._attributes.get('xml:lang')
    
    def set_xml_space(self, xml_space):
        self._attributes['xml:space']=xml_space
    
    def get_xml_space(self):
        return self._attributes.get('xml:space')
    # langSpaceAttrs end
   

    #testAttrs
    def set_requiredFeatures(self, requiredFeatures):
        self._attributes['requiredFeatures']=requiredFeatures
    
    def get_requiredFeatures(self):
        return self._attributes.get('requiredFeatures')
    
    def set_requiredExtensions(self, requiredExtensions):
        self._attributes['requiredExtensions']=requiredExtensions
    
    def get_requiredExtensions(self):
        return self._attributes.get('requiredExtensions')
    
    def set_systemLanguage(self, language_code):
        self._attributes['systemLanguage']=language_code
    
    def get_systemLanguage(self):
        return self._attributes.get('systemLanguage')
    #testAttrs end

class FilterPrimitiveElement(BaseElement):
    def __init__(self, elementName):
        BaseElement.__init__(self, elementName)
    
    def set_filter(self, style):
        self._attributes['filter']=filter
    
    def get_filter(self):
        return self._attributes.get('filter')
    
    def set_color_interpolation_filters(self, color_interpolation_filters):
        self._attributes['color-interpolation-filters']=color_interpolation_filters
    
    def get_color_interpolation_filters(self):
        return self._attributes.get('color-interpolation-filters')
    
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
    
    def set_result(self, result):
        self._attributes['result']=result
    
    def get_result(self):
        return self._attributes.get('result')

class FilterPrimitiveWithInElement(FilterPrimitiveElement):
    def __init__(self, elementName):
        FilterPrimitiveElement.__init__(self, elementName)
    
    def set_in(self, inValue):
        self._attributes['in']=inValue
    
    def get_in(self):
        return self._attributes.get('in')
    
class StyledElement(BaseElement):
    def __init__(self, elementName):
        BaseElement.__init__(self, elementName)
    
    #style.attrib
    def set_style(self, style):
        self._attributes['style']=style
    
    def get_style(self):
        return self._attributes.get('style')

           
class PaintAttributedElement(StyledElement):
    def __init__(self, elementName):
        StyledElement.__init__(self, elementName)
    
    #paint attrib
    #color, color-interpolation, color-rendering, 
    #fill, fill-rule, stroke, stroke-dasharray, stroke-dashoffset, stroke-linecap, stroke-linejoin, stroke-miterlimit, stroke-width, 
    def set_color(self, color):
        self._attributes['color']=color
    
    def get_color(self):
        return self._attributes.get('color')
    
    def set_color_interpolation(self, color_interpolation):
        self._attributes['color-interpolation']=color_interpolation
    
    def get_color_interpolation(self):
        return self._attributes.get('color-interpolation')
    
    def set_color_rendering(self, color_rendering):
        self._attributes['color-rendering']=color_rendering
    
    def get_color_rendering(self):
        return self._attributes.get('color-rendering')
    
    def set_fill(self, fill):
        self._attributes['fill']=fill
    
    def get_fill(self):
        return self._attributes.get('fill')
    
    def set_fill_rule(self, fill_rule):
        self._attributes['fill-rule']=fill_rule
    
    def get_fill_rule(self):
        return self._attributes.get('fill-rule')
    
    def set_stroke(self, stroke):
        self._attributes['stroke']=stroke
    
    def get_stroke(self):
        return self._attributes.get('stroke')
    
    def set_stroke_dasharray(self, stroke_dasharray):
        self._attributes['stroke-dasharray']=stroke_dasharray
    
    def get_stroke_dasharray(self):
        return self._attributes.get('stroke-dasharray')
    
    def set_stroke_dashoffset(self, stroke_dashoffset):
        self._attributes['stroke-dashoffset']=stroke_dashoffset
    
    def get_stroke_dashoffset(self):
        return self._attributes.get('stroke-offset')
    
    def set_stroke_linecap(self, stroke_linecap):
        self._attributes['stroke-linecap']=stroke_linecap
    
    def get_stroke_linecap(self):
        return self._attributes.get('stroke-linecap')
    
    def set_stroke_linejoin(self, stroke_linejoin):
        self._attributes['stroke-linejoin']=stroke_linejoin
    
    def get_stroke_linejoin(self):
        return self._attributes.get('stroke-linejoin')
    
    def set_stroke_miterlimit(self, stroke_miterlimit):
        self._attributes['stroke-miterlimit']=stroke_miterlimit
    
    def get_stroke_miterlimit(self):
        return self._attributes.get('stroke-miterlimit')
    
    def set_stroke_width(self, stroke_width):
        self._attributes['stroke-width']=stroke_width
    
    def get_stroke_width(self):
        return self._attributes.get('stroke-width')
       
class GradientElement(PaintAttributedElement):
    def __init__(self, elementName):
        PaintAttributedElement.__init__(self, elementName)
    #Gradient attrib
    #stop-color, stop-opacity
    def set_stop_color(self, stop_color):
        self._attributes['stop-color']=stop_color
    
    def get_stop_color(self):
        return self._attributes.get('stop-color')
    
    def set_stop_opacity(self, stop_opacity):
        self._attributes['stop-opacity']=stop_opacity
    
    def get_stop_opacity(self):
        return self._attributes.get('stop-opacity')
    
class CommonGradientElement(GradientElement):
    def __init__(self, elementName):
        GradientElement.__init__(self, elementName)
        
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
    
    #External.attrib
    #externalResourcesRequired
    def set_externalResourcesRequired(self, externalResourcesRequired):
        self._attributes['externalResourcesRequired']=externalResourcesRequired
    
    def get_externalResourcesRequired(self):
        return self._attributes.get('externalResourcesRequired')
    
    #attributes common to gradients
    def set_gradientUnits(self, gradientUnits):
        self._attributes['gradientUnits']=gradientUnits
    
    def get_gradientUnits(self):
        return self._attributes.get('gradientUnits')
    
    def set_gradientTransform(self, gradientTransform):
        self._attributes['gradientTransform']=gradientTransform
    
    def get_gradientTransform(self):
        return self._attributes.get('gradientTransform')
    
    def set_spreadMethod(self, spreadMethod):
        self._attributes['spreadMethod']=spreadMethod
    
    def get_spreadMethod(self):
        return self._attributes.get('spreadMethod')
    
class TransformableElement(PaintAttributedElement):
    def __init__(self, elementName):
        StyledElement.__init__(self, elementName)
    
    def set_transform(self, transform):
        self._attributes['transform']=transform
    
    def get_transform(self):
        return self._attributes.get('transform')

class ExternalResourcesElement(TransformableElement):
    def __init__(self, elementName):
        TransformableElement.__init__(self, elementName)
    #External.attrib
    #externalResourcesRequired
    def set_externalResourcesRequired(self, externalResourcesRequired):
        self._attributes['externalResourcesRequired']=externalResourcesRequired
    
    def get_externalResourcesRequired(self):
        return self._attributes.get('externalResourcesRequired')

        
class GraphicalEventsElement(ExternalResourcesElement):
    def __init__(self, elementName):
        ExternalResourcesElement.__init__(self, elementName)
    #GraphicsElementEvents
    #onfocusin, onfocusout, onactivate, onclick, onmousedown, onmouseup, onmouseover, onmousemove, onmouseout, onload
    def set_onfocusin(self, onfocusin):
        self._attributes['onfocusin']=onfocusin
    
    def get_onfocusin(self):
        return self._attributes.get('onfocusin')
    
    def set_onfocusout(self, onfocusout):
        self._attributes['onfocusout']=onfocusout
    
    def get_onfocusout(self):
        return self._attributes.get('onfocusout')
    
    def set_onactivate(self, onactivate):
        self._attributes['onactivate']=onactivate
    
    def get_onactivate(self):
        return self._attributes.get('onactivate')
    
    def set_onclick(self, onclick):
        self._attributes['onclick']=onclick
    
    def get_onclick(self):
        return self._attributes.get('onclick')
    
    def set_onmousedown(self, onmousedown):
        self._attributes['onmousedown']=onmousedown
    
    def get_onmousedown(self):
        return self._attributes.get('onmousedown')
    
    def set_onmouseup(self, onmouseup):
        self._attributes['onmouseup']=onmouseup
    
    def get_onmouseup(self):
        return self._attributes.get('onmouseup')
    
    def set_onmouseover(self, onmouseover):
        self._attributes['onmouseover']=onmouseover
    
    def get_onmouseover(self):
        return self._attributes.get('onmouseover')
    
    def set_onmousemove(self, onmousemove):
        self._attributes['onmousemove']=onmousemove
    
    def get_onmousemove(self):
        return self._attributes.get('onmousemove')
    
    def set_onmouseout(self, onmouseout):
        self._attributes['onmouseout']=onmouseout
    
    def get_onmouseout(self):
        return self._attributes.get('onmouseout')
    
    def set_onload(self, onload):
        self._attributes['onload']=onload
    
    def get_onload(self):
        return self._attributes.get('onload')

class ShapeElement(GraphicalEventsElement):
    """
    Subclasses: rect, circle, line, polyline, polygon, ellipse, path.
    """
    def __init__(self, elementName):
        GraphicalEventsElement.__init__(self, elementName)
    
    #class TODO: see if that is good here
    def set_class(self, aClass):
        self._attributes['class']=aClass
    
    def get_class(self):
        return self._attributes.get('class')
    
    
    #opacity
    #     opacity, stroke-opacity, fill-opacity
    def set_opacity(self, opacity):
        self._attributes['opacity']=opacity
    
    def get_opacity(self):
        return self._attributes.get('opacity')
    
    def set_stroke_opacity(self, stroke_opacity):
        self._attributes['stroke-opacity']=stroke_opacity
    
    def get_stroke_opacity(self):
        return self._attributes.get('stroke-opacity')
    
    def set_fill_opacity(self, fill_opacity):
        self._attributes['fill-opacity']=fill_opacity
    
    def get_fill_opacity(self):
        return self._attributes.get('fill-opacity')
    #Graphics attrib
    #display, image-rendering, pointer-events, shape-rendering, text-rendering, visibility
    def set_display(self, display):
        self._attributes['display']=display
    
    def get_display(self):
        return self._attributes.get('display')
    
    def set_image_rendering(self, image_rendering):
        self._attributes['image-rendering']=image_rendering
    
    def get_image_rendering(self):
        return self._attributes.get('image-rendering')
    
    def set_pointer_events(self, pointer_events):
        self._attributes['pointer-events']=pointer_events
    
    def get_pointer_events(self):
        return self._attributes.get('pointer-events')
    
    def set_shape_rendering(self, shape_rendering):
        self._attributes['shape-rendering']=shape_rendering
    
    def get_shape_rendering(self):
        return self._attributes.get('shape-rendering')
    
    def set_text_rendering(self, text_rendering):
        self._attributes['text-rendering']=text_rendering
    
    def get_text_rendering(self):
        return self._attributes.get('text-rendering')
    
    def set_visibility(self, visibility):
        self._attributes['visibility']=visibility
    
    def get_visibility(self):
        return self._attributes.get('visibility')
    
    #Marker.attrib
    #marker-start, marker-mid, marker-end
    def set_marker_start(self, marker_start):
        self._attributes['marker-start']=marker_start
    
    def get_marker_start(self):
        return self._attributes.get('marker-start')
    
    def set_marker_mid(self, marker_mid):
        self._attributes['marker-mid']=marker_mid
    
    def get_marker_mid(self):
        return self._attributes.get('marker-mid')
    
    def set_marker_end(self, marker_end):
        self._attributes['marker-end']=marker_end
    
    def get_marker_end(self):
        return self._attributes.get('marker-end')
    
    #clip
    #clip-path, clip-rule
    def set_clip_path(self, clip_path):
        self._attributes['clip-path']=clip_path
    
    def get_clip_path(self):
        return self._attributes.get('clip-path')
    
    def set_clip_rule(self, clip_rule):
        self._attributes['clip-rule']=clip_rule
    
    def get_clip_rule(self):
        return self._attributes.get('clip-rule')
    
    #mask.attrib
    #mask
    def set_mask(self, mask):
        self._attributes['mask']=mask
    
    def get_mask(self):
        return self._attributes.get('mask')
    
    #filter.attrib
    #filter
    def set_filter(self, filter):
        self._attributes['filter']=filter
    
    def get_filter(self):
        return self._attributes.get('filter')
    
    #cursor.attrib
    #cursor
    def set_cursor(self, cursor):
        self._attributes['cursor']=cursor
    
    def get_cursor(self):
        return self._attributes.get('cursor')
   


class DocumentElement(GraphicalEventsElement):
    def __init__(self, elementName):
        GraphicalEventsElement.__init__(self, elementName)
    #documentEvent.attr
    #onunload, onabort, onerror, onresize, onscroll, onzoom
    def setOnUnload(self, onunload):
        self._attributes['onunload']=onunload
    
    def getOnUnload(self):
        return self._attributes.get('onunload')
    
    def setOnAbort(self, onabort):
        self._attributes['onabort']=onabort
    
    def getOnAbort(self):
        return self._attributes.get('onabort')
    
    def setOnError(self, onerror):
        self._attributes['onerror']=onerror
    
    def getOnError(self):
        return self._attributes.get('onerror')
    
    def setOnResize(self, onresize):
        self._attributes['onresize']=onresize
    
    def getOnResize(self):
        return self._attributes.get('onresize')
    
    def setOnScroll(self, onscroll):
        self._attributes['onscroll']=onscroll
    
    def getOnScroll(self):
        return self._attributes.get('onscroll')
    
    def setOnZoom(self, onzoom):
        self._attributes['onzoom']=onzoom
    
    def getOnZoom(self):
        return self._attributes.get('onzoom')