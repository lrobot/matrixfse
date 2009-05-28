'''
Created on 09.05.2009

@author: kerim
'''
from xml.dom import minidom
from xml.dom import Node
import core

def calculateMethodName(attr):
    name=attr
    name=name.replace(':','_')
    name=name.replace('-','_')
    name='set_'+name
    return name
    
def setAttributes(attrs,obj):
    for attr in attrs.keys():
        if hasattr(obj, calculateMethodName(attr)):
            eval ('obj.'+calculateMethodName(attr))(attrs[attr].value)
        else:
            print calculateMethodName(attr)+' not found in:'+obj._elementName
        
def build(node_, object, packageprefix='core.'):
    attrs = node_.attributes
    if attrs != None:
        setAttributes(attrs, object)
    for child_ in node_.childNodes:
        nodeName_ = child_.nodeName.split(':')[-1]
        if child_.nodeType == Node.ELEMENT_NODE:
            try:
                objectinstance=eval(packageprefix+nodeName_) ()                
            except:
                print 'no class for: '+nodeName_
                continue
            object.addElement(build(child_,objectinstance))
        elif child_.nodeType == Node.TEXT_NODE:
            #print "TextNode:"+child_.nodeValue
            #if child_.nodeValue.startswith('\n'):
            #    print "TextNode starts with return:"+child_.nodeValue
            #else:
            print "TextNode is:"+child_.nodeValue
            #object.setTextContent(child_.nodeValue)
            if child_.nodeValue <> None:
                object.appendTextContent(child_.nodeValue)
        elif child_.nodeType == Node.CDATA_SECTION_NODE:  
            object.setTextContent('<![CDATA['+child_.nodeValue+']]>')          
        else:
            print "Some node:"+nodeName_
    return object

#TODO: packageprefix ?
def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = core.svg()
    build(rootNode,rootObj)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #print rootObj.getXML()
    return rootObj


