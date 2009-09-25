#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
'''
(C) 2008, 2009 Kerim Mansour
For licensing information please refer to license.txt
'''
from attributes import *
from core import *

class filter(BaseElement, CoreAttrib, XLinkAttrib, ExternalAttrib, StyleAttrib, PresentationAttrib, PointAttrib, DimensionAttrib):
    """
    Class representing the filter element of an svg doc.
    """
    def __init__(self, x=None, y=None, width=None, height=None,filterRes=None, filterUnits=None, primitiveUnits=None):
        BaseElement.__init__(self,'filter')
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_filterRes(filterRes)
        self.set_filterUnits(filterUnits)
        self.set_primitiveUnits(primitiveUnits)
        
    def set_filterUnits(self, filterUnits):
        self._attributes['filterUnits']=filterUnits
    def get_filterUnits(self):
        return self._attributes.get('filterUnits')

    def set_primitiveUnits(self, primitiveUnits):
        self._attributes['primitiveUnits']=primitiveUnits
    def get_primitiveUnits(self):
        return self._attributes.get('primitiveUnits')

    def set_filterRes(self, filterRes):
        self._attributes['filterRes']=filterRes
    def get_filterRes(self):
        return self._attributes.get('filterRes')
        
class feComponentTransfer(BaseElement, CoreAttrib, FilterColorAttrib, FilterPrimitiveWithInAttrib):
    """
    Class representing the feComponentTransfer element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feComponentTransfer')
        

class feBlend(feComponentTransfer):
    """
    Class representing the feBlend element of an svg doc.
    """
    def __init__(self, in2=None, mode=None):
        BaseElement.__init__(self,'feBlend')
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

class feColorMatrix(feComponentTransfer):
    """
    Class representing the feColorMatrix element of an svg doc.
    """
    def __init__(self, type=None, values=None):
        BaseElement.__init__(self,'feColorMatrix')
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

class feComposite(feComponentTransfer):
    """
    Class representing the feComposite element of an svg doc.
    """
    def __init__(self, in2=None, operator=None, k1=None, k2=None, k3=None, k4=None):
        BaseElement.__init__(self,'feComposite')
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

class feConvolveMatrix(feComponentTransfer):
    """
    Class representing the feConvolveMatrix element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feConvolveMatrix')
    
    def set_order(self, order):
        self._attributes['order']=order
    def get_order(self):
        return self._attributes.get('order')
    
    def set_kernelMatrix(self, kernelMatrix):
        self._attributes['kernelMatrix']=kernelMatrix
    def get_kernelMatrix(self):
        return self._attributes.get('kernelMatrix')

    def set_divisor(self, divisor):
        self._attributes['divisor']=divisor
    def get_divisor(self):
        return self._attributes.get('divisor')

    def set_bias(self, bias):
        self._attributes['bias']=bias
    def get_bias(self):
        return self._attributes.get('bias')

    def set_targetX(self, targetX):
        self._attributes['targetX']=targetX
    def get_targetX(self):
        return self._attributes.get('targetX')
    
    def set_targetY(self, targetY):
        self._attributes['targetY']=targetY
    def get_targetY(self):
        return self._attributes.get('targetY')
    
    def set_edgeMode(self, edgeMode):
        self._attributes['edgeMode']=edgeMode
    def get_edgeMode(self):
        return self._attributes.get('edgeMode')

    def set_kernelUnitLength(self, kernelUnitLength):
        self._attributes['kernelUnitLength']=kernelUnitLength
    def get_kernelUnitLength(self):
        return self._attributes.get('kernelUnitLength')
    
    def set_preserveAlpha(self, preserveAlpha):
        self._attributes['preserveAlpha']=preserveAlpha
    def get_preserveAlpha(self):
        return self._attributes.get('preserveAlpha')

class feDiffuseLighting(feComponentTransfer, StyleAttrib, PaintAttrib):
    """
    Class representing the feDiffuseLighting element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feDiffuseLighting')
    
    def set_lighting_color(self, lighting_color):
        self._attributes['lighting-color']=lighting_color
    def get_lighting_color(self):
        return self._attributes.get('lighting-color')
    
    def set_surfaceScale(self, surfaceScale):
        self._attributes['surfaceScale']=surfaceScale
    def get_surfaceScale(self):
        return self._attributes.get('surfaceScale')

    def set_diffuseConstant(self, diffuseConstant):
        self._attributes['diffuseConstant']=diffuseConstant
    def get_diffuseConstant(self):
        return self._attributes.get('diffuseConstant')

    def set_kernelUnitLength(self, kernelUnitLength):
        self._attributes['kernelUnitLength']=kernelUnitLength
    def get_kernelUnitLength(self):
        return self._attributes.get('kernelUnitLength')

class feDisplacementMap(feComponentTransfer):
    """
    Class representing the feDisplacementMap element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feDisplacementMap')
    
    def set_in2(self, in2):
        self._attributes['in2']=in2
    def get_in2(self):
        return self._attributes.get('in2')
    
    def set_scale(self, scale):
        self._attributes['scale']=scale
    def get_scale(self):
        return self._attributes.get('scale')
    
    def set_xChannelSelector(self, xChannelSelector):
        self._attributes['xChannelSelector']=xChannelSelector
    def get_xChannelSelector(self):
        return self._attributes.get('xChannelSelector')
    
    def set_yChannelSelector(self, yChannelSelector):
        self._attributes['yChannelSelector']=yChannelSelector
    def get_yChannelSelector(self):
        return self._attributes.get('yChannelSelector')

class feFlood(feComponentTransfer, StyleAttrib, PaintAttrib):
    """
    Class representing the feFlood element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feFlood')
    
    def set_flood_color(self, flood_color):
        self._attributes['flood-color']=flood_color
    def get_flood_color(self):
        return self._attributes.get('flood-color')
    
    def set_flood_opacity(self, flood_opacity):
        self._attributes['flood-opacity']=flood_opacity
    def get_flood_opacity(self):
        return self._attributes.get('flood-opacity')
    
class feGaussianBlur(feComponentTransfer):
    """
    Class representing the feGaussianBlur element of an svg doc.
    """
    def __init__(self, stdDeviation=None):
        BaseElement.__init__(self,'feGaussianBlur')
        self.set_stdDeviation(stdDeviation)
        
    def set_stdDeviation(self, stdDeviation):
        self._attributes['stdDeviation']=stdDeviation
    def get_stdDeviation(self):
        return self._attributes.get('stdDeviation')

class feImage(BaseElement, CoreAttrib, XLinkAttrib, FilterColorAttrib, FilterPrimitiveAttrib, ExternalAttrib, StyleAttrib, PresentationAttrib):
    """
    Class representing the feImage element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feImage')

class feMerge(BaseElement, CoreAttrib):
    """
    Class representing the feMerge element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feMerge')
 
    def set_in(self, inValue):
        self._attributes['in']=inValue
    def get_in(self):
        return self._attributes.get('in')

class feMergeNode(BaseElement, CoreAttrib, FilterColorAttrib, FilterPrimitiveAttrib):
    """
    Class representing the feMergeNode element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feMergeNode')

class feMorphology(feComponentTransfer):
    """
    Class representing the feMorphology element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feMorphology')
    
    def set_operator(self, operator):
        self._attributes['operator']=operator
    def get_operator(self):
        return self._attributes.get('operator')
    
    def set_radius(self, radius):
        self._attributes['radius']=radius
    def get_radius(self):
        return self._attributes.get('radius')

class feOffset(feComponentTransfer, DeltaPointAttrib):
    """
    Class representing the feOffset element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feOffset')

class feSpecularLighting(feComponentTransfer, StyleAttrib, PaintAttrib):
    """
    Class representing the feSpecularLighting element of an svg doc.
    """
    def __init__(self, lighting_color=None, surfaceScale=None, specularConstant=None, specularExponent=None, kernelUnitLength=None):
        BaseElement.__init__(self,'feSpecularLighting')
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
    
class feTile(feComponentTransfer):
    """
    Class representing the feTile element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feTile')
        
class feTurbulence(BaseElement, CoreAttrib, FilterColorAttrib, FilterPrimitiveAttrib):
    """
    Class representing the feTurbulence element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'feTurbulence')
        
    def set_baseFrequency(self, baseFrequency):
        self._attributes['baseFrequency']=baseFrequency
    def get_baseFrequency(self):
        return self._attributes.get('baseFrequency')  
    
    def set_numOctaves(self, numOctaves):
        self._attributes['numOctaves']=numOctaves
    def get_numOctaves(self):
        return self._attributes.get('numOctaves')  
    
    def set_seed(self, seed):
        self._attributes['seed']=seed
    def get_seed(self):
        return self._attributes.get('seed')  
    
    def set_stitchTiles(self, stitchTiles):
        self._attributes['stitchTiles']=stitchTiles
    def get_stitchTiles(self):
        return self._attributes.get('stitchTiles')  
    
    def set_type(self, type):
        self._attributes['type']=type
    def get_type(self):
        return self._attributes.get('type')

class feDistantLight(BaseElement, CoreAttrib):
    """
    Class representing the feDistantLight element of an svg doc.
    """
    def __init__(self, azimuth=None, elevation=None):
        BaseElement.__init__(self,'feDistantLight')
        self.set_azimuth(azimuth)
        self.set_elevation(elevation)
        
    def set_azimuth(self, azimuth):
        self._attributes['azimuth']=azimuth
    def get_azimuth(self):
        return self._attributes.get('azimuth')
    
    def set_elevation(self, elevation):
        self._attributes['elevation']=elevation
    def get_elevation(self):
        return self._attributes.get('elevation')

class fePointLight(BaseElement, CoreAttrib, PointAttrib):
    """
    Class representing the fePointLight element of an svg doc.
    """
    def __init__(self, x=None, y=None, z=None):
        BaseElement.__init__(self,'fePointLight')
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        
    def set_z(self, z):
        self._attributes['z']=z
    def get_z(self):
        return self._attributes.get('z')

class feSpotLight(fePointLight):
    """
    Class representing the feSpotLight element of an svg doc.
    """
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
    
class feFuncR(BaseElement, CoreAttrib):
    """
    Class representing the feFuncR element of an svg doc.
    """
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        BaseElement.__init__(self,'feFuncR')
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
    
    def set_amplitude(self, amplitude):
        self._attributes['amplitude']=amplitude
    def get_amplitude(self):
        return self._attributes.get('amplitude')
    
    def set_exponent(self, exponent):
        self._attributes['exponent']=exponent
    def get_exponent(self):
        return self._attributes.get('exponent')
    
    def set_offset(self, offset):
        self._attributes['offset']=offset
    def get_offset(self):
        return self._attributes.get('offset')

class feFuncG(feFuncR):
    """
    Class representing the feFuncG element of an svg doc.
    """
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        BaseElement.__init__(self,'feFuncG')
        self.set_type(type)
        self.set_tableValues(tableValues)
        self.set_slope(slope)
        self.set_intercept(intercept)
        self.set_amplitude(amplitude)
        self.set_exponent(exponent)
        self.set_offset(offset)
        
class feFuncB(feFuncR):
    """
    Class representing the feFuncB element of an svg doc.
    """
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        BaseElement.__init__(self,'feFuncB')
        self.set_type(type)
        self.set_tableValues(tableValues)
        self.set_slope(slope)
        self.set_intercept(intercept)
        self.set_amplitude(amplitude)
        self.set_exponent(exponent)
        self.set_offset(offset)
        
class feFuncA(feFuncR):
    """
    Class representing the feFuncA element of an svg doc.
    """
    def __init__(self, type=None, tableValues=None, slope=None, intercept=None, amplitude=None, exponent=None, offset=None):
        BaseElement.__init__(self,'feFuncA')
        self.set_type(type)
        self.set_tableValues(tableValues)
        self.set_slope(slope)
        self.set_intercept(intercept)
        self.set_amplitude(amplitude)
        self.set_exponent(exponent)
        self.set_offset(offset)