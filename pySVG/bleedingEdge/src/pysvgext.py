#!/usr/bin/env python

#
# Generated Wed Apr 15 20:04:11 2009 by generateDS.py.
#

import sys
from string import lower as str_lower
from xml.dom import minidom
from xml.sax import handler, make_parser

import pysvg as supermod

class svgTypeSub(supermod.svgType):
    def __init__(self, onmousedown=None, requiredExtensions=None, onerror=None, onfocusout=None, height=None, onscroll=None, contentStyleType=None, style_attr=None, onresize=None, id=None, onabort=None, onload=None, space=None, onzoom=None, viewBox=None, width=None, onmouseup=None, onmousemove=None, onactivate=None, onfocusin=None, onclick=None, onmouseout=None, systemLanguage=None, onmouseover=None, externalResourcesRequired=None, zoomAndPan='magnify', classxx=None, lang=None, onunload=None, requiredFeatures=None, base=None, y=None, x=None, preserveAspectRatio=None, contentScriptType=None):
        supermod.svgType.__init__(self, onmousedown, requiredExtensions, onerror, onfocusout, height, onscroll, contentStyleType, style_attr, onresize, id, onabort, onload, space, onzoom, viewBox, width, onmouseup, onmousemove, onactivate, onfocusin, onclick, onmouseout, systemLanguage, onmouseover, externalResourcesRequired, zoomAndPan, classxx, lang, onunload, requiredFeatures, base, y, x, preserveAspectRatio, contentScriptType)
supermod.svgType.subclass = svgTypeSub
# end class svgTypeSub


class gTypeSub(supermod.gType):
    def __init__(self, requiredExtensions=None, onfocusout=None, onmousedown=None, id=None, onload=None, space=None, transform=None, onmousemove=None, onclick=None, onfocusin=None, onmouseup=None, onmouseout=None, systemLanguage=None, onmouseover=None, externalResourcesRequired=None, classxx=None, lang=None, onactivate=None, requiredFeatures=None, base=None, style_attr=None):
        supermod.gType.__init__(self, requiredExtensions, onfocusout, onmousedown, id, onload, space, transform, onmousemove, onclick, onfocusin, onmouseup, onmouseout, systemLanguage, onmouseover, externalResourcesRequired, classxx, lang, onactivate, requiredFeatures, base, style_attr)
supermod.gType.subclass = gTypeSub
# end class gTypeSub


class defsTypeSub(supermod.defsType):
    def __init__(self, requiredExtensions=None, onfocusout=None, onmousedown=None, id=None, onload=None, space=None, transform=None, onmousemove=None, onclick=None, onfocusin=None, onmouseup=None, onmouseout=None, systemLanguage=None, onmouseover=None, externalResourcesRequired=None, classxx=None, lang=None, onactivate=None, requiredFeatures=None, base=None, style_attr=None):
        supermod.defsType.__init__(self, requiredExtensions, onfocusout, onmousedown, id, onload, space, transform, onmousemove, onclick, onfocusin, onmouseup, onmouseout, systemLanguage, onmouseover, externalResourcesRequired, classxx, lang, onactivate, requiredFeatures, base, style_attr)
supermod.defsType.subclass = defsTypeSub
# end class defsTypeSub


class descTypeSub(supermod.descType):
    def __init__(self, lang=None, style=None, space=None, id=None, content=None, base=None, classxx=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.descType.__init__(self, mixedclass_, content_)
supermod.descType.subclass = descTypeSub
# end class descTypeSub


class titleTypeSub(supermod.titleType):
    def __init__(self, lang=None, style=None, space=None, id=None, content=None, base=None, classxx=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.titleType.__init__(self, mixedclass_, content_)
supermod.titleType.subclass = titleTypeSub
# end class titleTypeSub


class symbolTypeSub(supermod.symbolType):
    def __init__(self, lang=None, onload=None, onclick=None, onmouseout=None, space=None, onfocusout=None, onmouseup=None, classxx=None, viewBox=None, base=None, onmousemove=None, onmouseover=None, onactivate=None, onfocusin=None, id=None, preserveAspectRatio=None, onmousedown=None, externalResourcesRequired=None, style_attr=None):
        supermod.symbolType.__init__(self, lang, onload, onclick, onmouseout, space, onfocusout, onmouseup, classxx, viewBox, base, onmousemove, onmouseover, onactivate, onfocusin, id, preserveAspectRatio, onmousedown, externalResourcesRequired, style_attr)
supermod.symbolType.subclass = symbolTypeSub
# end class symbolTypeSub


class useTypeSub(supermod.useType):
    def __init__(self, show=None, onfocusout=None, actuate=None, height=None, href=None, arcrole=None, id=None, onload=None, style=None, space=None, requiredExtensions=None, transform=None, width=None, onmouseup=None, role=None, onactivate=None, onmousemove=None, type_=None, onfocusin=None, onclick=None, onmouseout=None, base=None, onmouseover=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, title=None, requiredFeatures=None, systemLanguage=None, y=None, x=None):
        supermod.useType.__init__(self, show, onfocusout, actuate, height, href, arcrole, id, onload, style, space, requiredExtensions, transform, width, onmouseup, role, onactivate, onmousemove, type_, onfocusin, onclick, onmouseout, base, onmouseover, externalResourcesRequired, onmousedown, classxx, lang, title, requiredFeatures, systemLanguage, y, x)
supermod.useType.subclass = useTypeSub
# end class useTypeSub


class imageTypeSub(supermod.imageType):
    def __init__(self, text_rendering=None, color_rendering=None, clip=None, show='other', color=None, onfocusout=None, actuate=None, height=None, href=None, onload=None, id=None, cursor=None, style=None, title=None, requiredExtensions=None, transform=None, width=None, onmouseup=None, role=None, onactivate=None, onmousemove=None, type_=None, onfocusin=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, overflow=None, visibility=None, base=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, shape_rendering=None, classxx=None, lang=None, arcrole=None, mask=None, space=None, filter=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.imageType.__init__(self, text_rendering, color_rendering, clip, show, color, onfocusout, actuate, height, href, onload, id, cursor, style, title, requiredExtensions, transform, width, onmouseup, role, onactivate, onmousemove, type_, onfocusin, opacity, onclick, onmouseout, clip_path, overflow, visibility, base, clip_rule, onmouseover, image_rendering, externalResourcesRequired, shape_rendering, classxx, lang, arcrole, mask, space, filter, pointer_events, requiredFeatures, systemLanguage, y, x, display, onmousedown, color_interpolation)
supermod.imageType.subclass = imageTypeSub
# end class imageTypeSub


class switchTypeSub(supermod.switchType):
    def __init__(self, lang=None, onload=None, style=None, onclick=None, onmouseout=None, requiredExtensions=None, onfocusout=None, systemLanguage=None, space=None, onmouseup=None, transform=None, classxx=None, requiredFeatures=None, base=None, onmousemove=None, onmouseover=None, onactivate=None, onfocusin=None, externalResourcesRequired=None, onmousedown=None, id=None):
        supermod.switchType.__init__(self, lang, onload, style, onclick, onmouseout, requiredExtensions, onfocusout, systemLanguage, space, onmouseup, transform, classxx, requiredFeatures, base, onmousemove, onmouseover, onactivate, onfocusin, externalResourcesRequired, onmousedown, id)
supermod.switchType.subclass = switchTypeSub
# end class switchTypeSub


class styleTypeSub(supermod.styleType):
    def __init__(self, title=None, media=None, space=None, base=None, type_=None, id=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.styleType.__init__(self, mixedclass_, content_)
supermod.styleType.subclass = styleTypeSub
# end class styleTypeSub


class pathTypeSub(supermod.pathType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, marker_start=None, shape_rendering=None, stroke=None, stroke_linecap=None, onload=None, pathLength=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onfocusout=None, onmousemove=None, marker_mid=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, marker_end=None, d=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, onfocusin=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, display=None, color_interpolation=None):
        supermod.pathType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, marker_start, shape_rendering, stroke, stroke_linecap, onload, pathLength, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, onmouseup, stroke_miterlimit, onactivate, onfocusout, onmousemove, marker_mid, opacity, onclick, onmouseout, clip_path, visibility, systemLanguage, clip_rule, onmouseover, image_rendering, externalResourcesRequired, onmousedown, classxx, lang, marker_end, d, stroke_opacity, fill_rule, mask, stroke_dashoffset, onfocusin, filter, pointer_events, requiredFeatures, base, stroke_dasharray, display, color_interpolation)
supermod.pathType.subclass = pathTypeSub
# end class pathTypeSub


class rectTypeSub(supermod.rectType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, transform=None, stroke=None, stroke_linecap=None, onload=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, rx=None, ry=None, shape_rendering=None, width=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onmousemove=None, onfocusin=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, height=None, classxx=None, lang=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.rectType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, onfocusout, transform, stroke, stroke_linecap, onload, stroke_width, id, fill, cursor, style, space, fill_opacity, rx, ry, shape_rendering, width, onmouseup, stroke_miterlimit, onactivate, onmousemove, onfocusin, opacity, onclick, onmouseout, clip_path, visibility, systemLanguage, clip_rule, onmouseover, image_rendering, externalResourcesRequired, height, classxx, lang, stroke_opacity, fill_rule, mask, stroke_dashoffset, filter, pointer_events, requiredFeatures, base, stroke_dasharray, y, x, display, onmousedown, color_interpolation)
supermod.rectType.subclass = rectTypeSub
# end class rectTypeSub


class circleTypeSub(supermod.circleType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, shape_rendering=None, cy=None, cx=None, onload=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, r=None, stroke_miterlimit=None, onactivate=None, onmousemove=None, onfocusin=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, stroke_linecap=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, stroke=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, display=None, color_interpolation=None):
        supermod.circleType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, onfocusout, shape_rendering, cy, cx, onload, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, r, stroke_miterlimit, onactivate, onmousemove, onfocusin, opacity, onclick, onmouseout, clip_path, stroke_linecap, visibility, systemLanguage, clip_rule, onmouseover, image_rendering, externalResourcesRequired, onmousedown, classxx, lang, stroke_opacity, fill_rule, mask, stroke_dashoffset, stroke, filter, pointer_events, requiredFeatures, base, stroke_dasharray, onmouseup, display, color_interpolation)
supermod.circleType.subclass = circleTypeSub
# end class circleTypeSub


class ellipseTypeSub(supermod.ellipseType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, ry=None, cy=None, cx=None, onload=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, rx=None, transform=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onmousemove=None, onfocusin=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, stroke_linecap=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, shape_rendering=None, classxx=None, lang=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, stroke=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.ellipseType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, onfocusout, ry, cy, cx, onload, stroke_width, id, fill, cursor, style, space, fill_opacity, rx, transform, onmouseup, stroke_miterlimit, onactivate, onmousemove, onfocusin, opacity, onclick, onmouseout, clip_path, stroke_linecap, visibility, systemLanguage, clip_rule, onmouseover, image_rendering, externalResourcesRequired, shape_rendering, classxx, lang, stroke_opacity, fill_rule, mask, stroke_dashoffset, stroke, filter, pointer_events, requiredFeatures, base, stroke_dasharray, display, onmousedown, color_interpolation)
supermod.ellipseType.subclass = ellipseTypeSub
# end class ellipseTypeSub


class lineTypeSub(supermod.lineType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, marker_start=None, shape_rendering=None, stroke=None, stroke_linecap=None, onload=None, y1=None, y2=None, id=None, fill=None, cursor=None, style=None, stroke_width=None, space=None, fill_opacity=None, transform=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onfocusout=None, onmousemove=None, marker_mid=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, image_rendering=None, x2=None, externalResourcesRequired=None, x1=None, classxx=None, lang=None, marker_end=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, onfocusin=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.lineType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, marker_start, shape_rendering, stroke, stroke_linecap, onload, y1, y2, id, fill, cursor, style, stroke_width, space, fill_opacity, transform, onmouseup, stroke_miterlimit, onactivate, onfocusout, onmousemove, marker_mid, opacity, onclick, onmouseout, clip_path, visibility, systemLanguage, clip_rule, onmouseover, image_rendering, x2, externalResourcesRequired, x1, classxx, lang, marker_end, stroke_opacity, fill_rule, mask, stroke_dashoffset, onfocusin, filter, pointer_events, requiredFeatures, base, stroke_dasharray, display, onmousedown, color_interpolation)
supermod.lineType.subclass = lineTypeSub
# end class lineTypeSub


class polylineTypeSub(supermod.polylineType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, marker_start=None, shape_rendering=None, stroke=None, stroke_linecap=None, onload=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onfocusout=None, onmousemove=None, marker_mid=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, base=None, image_rendering=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, marker_end=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, onfocusin=None, filter=None, pointer_events=None, requiredFeatures=None, points=None, stroke_dasharray=None, display=None, color_interpolation=None):
        supermod.polylineType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, marker_start, shape_rendering, stroke, stroke_linecap, onload, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, onmouseup, stroke_miterlimit, onactivate, onfocusout, onmousemove, marker_mid, opacity, onclick, onmouseout, clip_path, visibility, systemLanguage, clip_rule, onmouseover, base, image_rendering, externalResourcesRequired, onmousedown, classxx, lang, marker_end, stroke_opacity, fill_rule, mask, stroke_dashoffset, onfocusin, filter, pointer_events, requiredFeatures, points, stroke_dasharray, display, color_interpolation)
supermod.polylineType.subclass = polylineTypeSub
# end class polylineTypeSub


class polygonTypeSub(supermod.polygonType):
    def __init__(self, stroke_linejoin=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, marker_start=None, shape_rendering=None, stroke=None, stroke_linecap=None, onload=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, onmouseup=None, stroke_miterlimit=None, onactivate=None, onfocusout=None, onmousemove=None, marker_mid=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, clip_rule=None, onmouseover=None, base=None, image_rendering=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, marker_end=None, stroke_opacity=None, fill_rule=None, mask=None, stroke_dashoffset=None, onfocusin=None, filter=None, pointer_events=None, requiredFeatures=None, points=None, stroke_dasharray=None, display=None, color_interpolation=None):
        supermod.polygonType.__init__(self, stroke_linejoin, text_rendering, color_rendering, requiredExtensions, color, marker_start, shape_rendering, stroke, stroke_linecap, onload, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, onmouseup, stroke_miterlimit, onactivate, onfocusout, onmousemove, marker_mid, opacity, onclick, onmouseout, clip_path, visibility, systemLanguage, clip_rule, onmouseover, base, image_rendering, externalResourcesRequired, onmousedown, classxx, lang, marker_end, stroke_opacity, fill_rule, mask, stroke_dashoffset, onfocusin, filter, pointer_events, requiredFeatures, points, stroke_dasharray, display, color_interpolation)
supermod.polygonType.subclass = polygonTypeSub
# end class polygonTypeSub


class textTypeSub(supermod.textType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, letter_spacing=None, shape_rendering=None, word_spacing=None, stroke=None, stroke_linecap=None, onload=None, baseline_shift=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, lengthAdjust=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, font_weight=None, onfocusin=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, base=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, writing_mode=None, stroke_opacity=None, textLength=None, font_size_adjust=None, fill_rule=None, mask=None, stroke_dashoffset=None, text_anchor=None, text_decoration=None, filter=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, stroke_dasharray=None, onmouseup=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None, mixedclass_=None, content_=None):
        supermod.textType.__init__(self, mixedclass_, content_)
supermod.textType.subclass = textTypeSub
# end class textTypeSub


class tspanTypeSub(supermod.tspanType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, image_rendering=None, letter_spacing=None, shape_rendering=None, word_spacing=None, stroke=None, stroke_linecap=None, onload=None, baseline_shift=None, stroke_width=None, id=None, fill=None, onmouseover=None, cursor=None, style=None, space=None, fill_opacity=None, lengthAdjust=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, font_weight=None, onfocusin=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, base=None, clip_rule=None, dominant_baseline=None, dx=None, dy=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, rotate=None, stroke_opacity=None, textLength=None, font_size_adjust=None, fill_rule=None, mask=None, stroke_dashoffset=None, text_anchor=None, text_decoration=None, filter=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, stroke_dasharray=None, onmouseup=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None, mixedclass_=None, content_=None):
        supermod.tspanType.__init__(self, mixedclass_, content_)
supermod.tspanType.subclass = tspanTypeSub
# end class tspanTypeSub


class trefTypeSub(supermod.trefType):
    def __init__(self, stroke_linejoin=None, fill_rule=None, font_size=None, text_rendering=None, color_rendering=None, requiredExtensions=None, color=None, onfocusout=None, image_rendering=None, actuate=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, cursor=None, stroke=None, href=None, onload=None, baseline_shift=None, stroke_width=None, id=None, fill=None, onmouseover=None, filter=None, style=None, title_attr=None, show='other', glyph_orientation_horizontal=None, lengthAdjust=None, shape_rendering=None, font_stretch=None, role=None, onactivate=None, font_variant=None, font_style=None, stroke_miterlimit=None, font_weight=None, type_=None, onfocusin=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, glyph_orientation_vertical=None, alignment_baseline=None, stroke_linecap=None, visibility=None, unicode_bidi=None, base=None, clip_rule=None, dominant_baseline=None, dx=None, dy=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, rotate=None, stroke_opacity=None, textLength=None, font_size_adjust=None, arcrole=None, mask=None, space=None, text_anchor=None, text_decoration=None, fill_opacity=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, stroke_dasharray=None, onmouseup=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.trefType.__init__(self, stroke_linejoin, fill_rule, font_size, text_rendering, color_rendering, requiredExtensions, color, onfocusout, image_rendering, actuate, letter_spacing, stroke_dashoffset, word_spacing, cursor, stroke, href, onload, baseline_shift, stroke_width, id, fill, onmouseover, filter, style, title_attr, show, glyph_orientation_horizontal, lengthAdjust, shape_rendering, font_stretch, role, onactivate, font_variant, font_style, stroke_miterlimit, font_weight, type_, onfocusin, opacity, direction, onmousemove, onclick, onmouseout, clip_path, glyph_orientation_vertical, alignment_baseline, stroke_linecap, visibility, unicode_bidi, base, clip_rule, dominant_baseline, dx, dy, externalResourcesRequired, font_family, classxx, lang, rotate, stroke_opacity, textLength, font_size_adjust, arcrole, mask, space, text_anchor, text_decoration, fill_opacity, pointer_events, requiredFeatures, systemLanguage, stroke_dasharray, onmouseup, y, x, display, onmousedown, color_interpolation)
supermod.trefType.subclass = trefTypeSub
# end class trefTypeSub


class textPathTypeSub(supermod.textPathType):
    def __init__(self, stroke_linejoin=None, fill_rule=None, font_size=None, text_rendering=None, requiredExtensions=None, onfocusout=None, actuate=None, letter_spacing=None, shape_rendering=None, word_spacing=None, cursor=None, stroke=None, href=None, onload=None, startOffset=None, baseline_shift=None, stroke_width=None, lengthAdjust=None, fill=None, filter=None, style=None, stroke_linecap=None, title_attr=None, space=None, show='other', glyph_orientation_horizontal=None, id=None, font_stretch=None, role=None, onactivate=None, font_variant=None, font_style=None, stroke_miterlimit=None, font_weight=None, type_=None, method=None, opacity=None, direction=None, onclick=None, onmouseout=None, clip_path=None, glyph_orientation_vertical=None, alignment_baseline=None, spacing=None, visibility=None, unicode_bidi=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, image_rendering=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, stroke_opacity=None, textLength=None, font_size_adjust=None, arcrole=None, mask=None, stroke_dashoffset=None, text_anchor=None, text_decoration=None, fill_opacity=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, onmousemove=None, display=None, onmousedown=None, onmouseover=None, mixedclass_=None, content_=None):
        supermod.textPathType.__init__(self, mixedclass_, content_)
supermod.textPathType.subclass = textPathTypeSub
# end class textPathTypeSub


class altGlyphTypeSub(supermod.altGlyphType):
    def __init__(self, stroke_linejoin=None, fill_rule=None, font_size=None, text_rendering=None, color_rendering=None, clip_path=None, requiredExtensions=None, color=None, onfocusout=None, image_rendering=None, actuate=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, cursor=None, stroke=None, href=None, onload=None, baseline_shift=None, stroke_width=None, id=None, fill=None, onmouseover=None, filter=None, style=None, title=None, show='other', glyph_orientation_horizontal=None, font_style=None, shape_rendering=None, font_stretch=None, role=None, onactivate=None, font_variant=None, stroke_miterlimit=None, font_weight=None, type_=None, glyphRef=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, format=None, glyph_orientation_vertical=None, alignment_baseline=None, stroke_linecap=None, visibility=None, unicode_bidi=None, base=None, clip_rule=None, dominant_baseline=None, dx=None, dy=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, rotate=None, stroke_opacity=None, font_size_adjust=None, arcrole=None, mask=None, space=None, text_anchor=None, text_decoration=None, fill_opacity=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, stroke_dasharray=None, onmouseup=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.altGlyphType.__init__(self, mixedclass_, content_)
supermod.altGlyphType.subclass = altGlyphTypeSub
# end class altGlyphTypeSub


class altGlyphDefTypeSub(supermod.altGlyphDefType):
    def __init__(self, base=None, id=None):
        supermod.altGlyphDefType.__init__(self, base, id)
supermod.altGlyphDefType.subclass = altGlyphDefTypeSub
# end class altGlyphDefTypeSub


class altGlyphItemTypeSub(supermod.altGlyphItemType):
    def __init__(self, base=None, id=None, glyphRef=None):
        supermod.altGlyphItemType.__init__(self, base, id, glyphRef)
supermod.altGlyphItemType.subclass = altGlyphItemTypeSub
# end class altGlyphItemTypeSub


class glyphRefTypeSub(supermod.glyphRefType):
    def __init__(self, font_size=None, show='other', actuate=None, href=None, id=None, style=None, title=None, font_style=None, font_stretch=None, role=None, font_variant=None, font_weight=None, type_=None, glyphRef=None, format=None, base=None, dx=None, dy=None, font_family=None, classxx=None, font_size_adjust=None, arcrole=None, y=None, x=None, valueOf_=''):
        supermod.glyphRefType.__init__(self, font_size, show, actuate, href, id, style, title, font_style, font_stretch, role, font_variant, font_weight, type_, glyphRef, format, base, dx, dy, font_family, classxx, font_size_adjust, arcrole, y, x)
supermod.glyphRefType.subclass = glyphRefTypeSub
# end class glyphRefTypeSub


class markerTypeSub(supermod.markerType):
    def __init__(self, refY=None, refX=None, markerUnits=None, lang=None, space=None, classxx=None, viewBox=None, base=None, orient=None, style_attr=None, id=None, markerWidth=None, preserveAspectRatio=None, externalResourcesRequired=None, markerHeight=None):
        supermod.markerType.__init__(self, refY, refX, markerUnits, lang, space, classxx, viewBox, base, orient, style_attr, id, markerWidth, preserveAspectRatio, externalResourcesRequired, markerHeight)
supermod.markerType.subclass = markerTypeSub
# end class markerTypeSub


class color_profileTypeSub(supermod.color_profileType):
    def __init__(self, name=None, rendering_intent='auto', type_=None, show='other', actuate=None, href=None, role=None, arcrole=None, base=None, title=None, local=None, id=None, valueOf_=''):
        supermod.color_profileType.__init__(self, name, rendering_intent, type_, show, actuate, href, role, arcrole, base, title, local, id)
supermod.color_profileType.subclass = color_profileTypeSub
# end class color_profileTypeSub


class linearGradientTypeSub(supermod.linearGradientType):
    def __init__(self, arcrole=None, style=None, y2=None, show='other', title=None, actuate=None, spreadMethod='pad', id=None, gradientUnits=None, x2=None, href=None, role=None, gradientTransform=None, base=None, y1=None, externalResourcesRequired=None, x1=None, type_=None, classxx=None):
        supermod.linearGradientType.__init__(self, arcrole, style, y2, show, title, actuate, spreadMethod, id, gradientUnits, x2, href, role, gradientTransform, base, y1, externalResourcesRequired, x1, type_, classxx)
supermod.linearGradientType.subclass = linearGradientTypeSub
# end class linearGradientTypeSub


class radialGradientTypeSub(supermod.radialGradientType):
    def __init__(self, arcrole=None, show='other', href=None, fy=None, title=None, actuate=None, spreadMethod='pad', gradientUnits=None, fx=None, cy=None, cx=None, role=None, gradientTransform=None, base=None, externalResourcesRequired=None, r=None, type_=None, id=None):
        supermod.radialGradientType.__init__(self, arcrole, show, href, fy, title, actuate, spreadMethod, gradientUnits, fx, cy, cx, role, gradientTransform, base, externalResourcesRequired, r, type_, id)
supermod.radialGradientType.subclass = radialGradientTypeSub
# end class radialGradientTypeSub


class stopTypeSub(supermod.stopType):
    def __init__(self, style=None, classxx=None, stop_color=None, base=None, offset=None, stop_opacity=None, id=None):
        supermod.stopType.__init__(self, style, classxx, stop_color, base, offset, stop_opacity, id)
supermod.stopType.subclass = stopTypeSub
# end class stopTypeSub


class patternTypeSub(supermod.patternType):
    def __init__(self, show='other', actuate=None, height=None, href=None, viewBox=None, title_attr=None, requiredExtensions=None, id=None, width=None, role=None, type_=None, systemLanguage=None, style_attr=None, externalResourcesRequired=None, classxx=None, lang=None, arcrole=None, space=None, requiredFeatures=None, base=None, patternTransform=None, y=None, x=None, preserveAspectRatio=None, patternUnits=None):
        supermod.patternType.__init__(self, show, actuate, height, href, viewBox, title_attr, requiredExtensions, id, width, role, type_, systemLanguage, style_attr, externalResourcesRequired, classxx, lang, arcrole, space, requiredFeatures, base, patternTransform, y, x, preserveAspectRatio, patternUnits)
supermod.patternType.subclass = patternTypeSub
# end class patternTypeSub


class clipPathTypeSub(supermod.clipPathType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, requiredExtensions=None, letter_spacing=None, shape_rendering=None, word_spacing=None, stroke=None, stroke_linecap=None, baseline_shift=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, font_style=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, glyph_orientation_horizontal=None, font_weight=None, opacity=None, direction=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, image_rendering=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, clipPathUnits=None, writing_mode=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, mask=None, stroke_dashoffset=None, text_anchor=None, text_decoration=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, display=None):
        supermod.clipPathType.__init__(self, stroke_linejoin, font_size, text_rendering, requiredExtensions, letter_spacing, shape_rendering, word_spacing, stroke, stroke_linecap, baseline_shift, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, font_style, font_stretch, stroke_miterlimit, font_variant, glyph_orientation_horizontal, font_weight, opacity, direction, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, systemLanguage, clip_rule, dominant_baseline, image_rendering, externalResourcesRequired, font_family, classxx, lang, clipPathUnits, writing_mode, stroke_opacity, font_size_adjust, fill_rule, mask, stroke_dashoffset, text_anchor, text_decoration, filter, pointer_events, requiredFeatures, base, stroke_dasharray, display)
supermod.clipPathType.subclass = clipPathTypeSub
# end class clipPathTypeSub


class maskTypeSub(supermod.maskType):
    def __init__(self, lang=None, systemLanguage=None, id=None, requiredExtensions=None, space=None, transform=None, height=None, width=None, requiredFeatures=None, base=None, style_attr=None, y=None, x=None, externalResourcesRequired=None, maskUnits=None, classxx=None):
        supermod.maskType.__init__(self, lang, systemLanguage, id, requiredExtensions, space, transform, height, width, requiredFeatures, base, style_attr, y, x, externalResourcesRequired, maskUnits, classxx)
supermod.maskType.subclass = maskTypeSub
# end class maskTypeSub


class filterTypeSub(supermod.filterType):
    def __init__(self, lang=None, style=None, filterRes=None, primitiveUnits=None, show='other', type_=None, id=None, title=None, actuate=None, space=None, height=None, width=None, href=None, role=None, arcrole=None, base=None, y=None, x=None, externalResourcesRequired=None, filterUnits=None, classxx=None):
        supermod.filterType.__init__(self, lang, style, filterRes, primitiveUnits, show, type_, id, title, actuate, space, height, width, href, role, arcrole, base, y, x, externalResourcesRequired, filterUnits, classxx)
supermod.filterType.subclass = filterTypeSub
# end class filterTypeSub


class feDistantLightTypeSub(supermod.feDistantLightType):
    def __init__(self, base=None, elevation=None, id=None, azimuth=None):
        supermod.feDistantLightType.__init__(self, base, elevation, id, azimuth)
supermod.feDistantLightType.subclass = feDistantLightTypeSub
# end class feDistantLightTypeSub


class fePointLightTypeSub(supermod.fePointLightType):
    def __init__(self, y=None, x=None, z=None, id=None, base=None):
        supermod.fePointLightType.__init__(self, y, x, z, id, base)
supermod.fePointLightType.subclass = fePointLightTypeSub
# end class fePointLightTypeSub


class feSpotLightTypeSub(supermod.feSpotLightType):
    def __init__(self, pointsAtX=None, limitingConeAngle=None, base=None, specularExponent=None, pointsAtZ=None, y=None, x=None, pointsAtY=None, z=None, id=None):
        supermod.feSpotLightType.__init__(self, pointsAtX, limitingConeAngle, base, specularExponent, pointsAtZ, y, x, pointsAtY, z, id)
supermod.feSpotLightType.subclass = feSpotLightTypeSub
# end class feSpotLightTypeSub


class feBlendTypeSub(supermod.feBlendType):
    def __init__(self, base=None, mode='normal', in2=None, id=None):
        supermod.feBlendType.__init__(self, base, mode, in2, id)
supermod.feBlendType.subclass = feBlendTypeSub
# end class feBlendTypeSub


class feColorMatrixTypeSub(supermod.feColorMatrixType):
    def __init__(self, values=None, base=None, type_='matrix', id=None):
        supermod.feColorMatrixType.__init__(self, values, base, type_, id)
supermod.feColorMatrixType.subclass = feColorMatrixTypeSub
# end class feColorMatrixTypeSub


class feComponentTransferTypeSub(supermod.feComponentTransferType):
    def __init__(self, base=None, id=None, feFuncR=None, feFuncG=None, feFuncB=None, feFuncA=None):
        supermod.feComponentTransferType.__init__(self, base, id, feFuncR, feFuncG, feFuncB, feFuncA)
supermod.feComponentTransferType.subclass = feComponentTransferTypeSub
# end class feComponentTransferTypeSub


class feFuncRTypeSub(supermod.feFuncRType):
    def __init__(self, slope=None, tableValues=None, intercept=None, base=None, amplitude=None, offset=None, type_=None, id=None, exponent=None):
        supermod.feFuncRType.__init__(self, slope, tableValues, intercept, base, amplitude, offset, type_, id, exponent)
supermod.feFuncRType.subclass = feFuncRTypeSub
# end class feFuncRTypeSub


class feFuncGTypeSub(supermod.feFuncGType):
    def __init__(self, slope=None, tableValues=None, intercept=None, base=None, amplitude=None, offset=None, type_=None, id=None, exponent=None):
        supermod.feFuncGType.__init__(self, slope, tableValues, intercept, base, amplitude, offset, type_, id, exponent)
supermod.feFuncGType.subclass = feFuncGTypeSub
# end class feFuncGTypeSub


class feFuncBTypeSub(supermod.feFuncBType):
    def __init__(self, slope=None, tableValues=None, intercept=None, base=None, amplitude=None, offset=None, type_=None, id=None, exponent=None):
        supermod.feFuncBType.__init__(self, slope, tableValues, intercept, base, amplitude, offset, type_, id, exponent)
supermod.feFuncBType.subclass = feFuncBTypeSub
# end class feFuncBTypeSub


class feFuncATypeSub(supermod.feFuncAType):
    def __init__(self, slope=None, tableValues=None, intercept=None, base=None, amplitude=None, offset=None, type_=None, id=None, exponent=None):
        supermod.feFuncAType.__init__(self, slope, tableValues, intercept, base, amplitude, offset, type_, id, exponent)
supermod.feFuncAType.subclass = feFuncATypeSub
# end class feFuncATypeSub


class feCompositeTypeSub(supermod.feCompositeType):
    def __init__(self, in2=None, k3=None, k2=None, k1=None, base=None, k4=None, operator='over', id=None):
        supermod.feCompositeType.__init__(self, in2, k3, k2, k1, base, k4, operator, id)
supermod.feCompositeType.subclass = feCompositeTypeSub
# end class feCompositeTypeSub


class feConvolveMatrixTypeSub(supermod.feConvolveMatrixType):
    def __init__(self, divisor=None, kernelMatrix=None, kernelUnitLength=None, edgeMode='duplicate', bias=None, targetX=None, targetY=None, preserveAlpha=None, order=None):
        supermod.feConvolveMatrixType.__init__(self, divisor, kernelMatrix, kernelUnitLength, edgeMode, bias, targetX, targetY, preserveAlpha, order)
supermod.feConvolveMatrixType.subclass = feConvolveMatrixTypeSub
# end class feConvolveMatrixTypeSub


class feDiffuseLightingTypeSub(supermod.feDiffuseLightingType):
    def __init__(self, lighting_color=None, style=None, diffuseConstant=None, classxx=None, base=None, surfaceScale=None, id=None):
        supermod.feDiffuseLightingType.__init__(self, lighting_color, style, diffuseConstant, classxx, base, surfaceScale, id)
supermod.feDiffuseLightingType.subclass = feDiffuseLightingTypeSub
# end class feDiffuseLightingTypeSub


class feDisplacementMapTypeSub(supermod.feDisplacementMapType):
    def __init__(self, scale=None, yChannelSelector='A', in2=None, base=None, xChannelSelector='A', id=None):
        supermod.feDisplacementMapType.__init__(self, scale, yChannelSelector, in2, base, xChannelSelector, id)
supermod.feDisplacementMapType.subclass = feDisplacementMapTypeSub
# end class feDisplacementMapTypeSub


class feFloodTypeSub(supermod.feFloodType):
    def __init__(self, style=None, flood_opacity=None, flood_color=None, id=None, base=None, classxx=None):
        supermod.feFloodType.__init__(self, style, flood_opacity, flood_color, id, base, classxx)
supermod.feFloodType.subclass = feFloodTypeSub
# end class feFloodTypeSub


class feGaussianBlurTypeSub(supermod.feGaussianBlurType):
    def __init__(self, base=None, stdDeviation=None, id=None):
        supermod.feGaussianBlurType.__init__(self, base, stdDeviation, id)
supermod.feGaussianBlurType.subclass = feGaussianBlurTypeSub
# end class feGaussianBlurTypeSub


class feImageTypeSub(supermod.feImageType):
    def __init__(self, lang=None, style=None, space=None, show='other', title=None, actuate=None, transform=None, id=None, width=None, href=None, role=None, arcrole=None, base=None, y=None, x=None, externalResourcesRequired=None, height=None, type_=None, classxx=None, result=None):
        supermod.feImageType.__init__(self, lang, style, space, show, title, actuate, transform, id, width, href, role, arcrole, base, y, x, externalResourcesRequired, height, type_, classxx, result)
supermod.feImageType.subclass = feImageTypeSub
# end class feImageTypeSub


class feMergeTypeSub(supermod.feMergeType):
    def __init__(self, height=None, width=None, base=None, result=None, y=None, x=None, id=None, feMergeNode=None):
        supermod.feMergeType.__init__(self, height, width, base, result, y, x, id, feMergeNode)
supermod.feMergeType.subclass = feMergeTypeSub
# end class feMergeTypeSub


class feMergeNodeTypeSub(supermod.feMergeNodeType):
    def __init__(self, base=None, id=None, inxx=None):
        supermod.feMergeNodeType.__init__(self, base, id, inxx)
supermod.feMergeNodeType.subclass = feMergeNodeTypeSub
# end class feMergeNodeTypeSub


class feMorphologyTypeSub(supermod.feMorphologyType):
    def __init__(self, operator='erode', base=None, radius=None, id=None):
        supermod.feMorphologyType.__init__(self, operator, base, radius, id)
supermod.feMorphologyType.subclass = feMorphologyTypeSub
# end class feMorphologyTypeSub


class feOffsetTypeSub(supermod.feOffsetType):
    def __init__(self, base=None, id=None, dx=None, dy=None):
        supermod.feOffsetType.__init__(self, base, id, dx, dy)
supermod.feOffsetType.subclass = feOffsetTypeSub
# end class feOffsetTypeSub


class feSpecularLightingTypeSub(supermod.feSpecularLightingType):
    def __init__(self, lighting_color=None, style=None, specularConstant=None, surfaceScale=None, base=None, specularExponent=None, id=None, classxx=None):
        supermod.feSpecularLightingType.__init__(self, lighting_color, style, specularConstant, surfaceScale, base, specularExponent, id, classxx)
supermod.feSpecularLightingType.subclass = feSpecularLightingTypeSub
# end class feSpecularLightingTypeSub


class feTileTypeSub(supermod.feTileType):
    def __init__(self, base=None, id=None):
        supermod.feTileType.__init__(self, base, id)
supermod.feTileType.subclass = feTileTypeSub
# end class feTileTypeSub


class feTurbulenceTypeSub(supermod.feTurbulenceType):
    def __init__(self, baseFrequency=None, type_='turbulence', stitchTiles='noStitch', height=None, width=None, base=None, result=None, x=None, y=None, numOctaves=None, seed=None, id=None):
        supermod.feTurbulenceType.__init__(self, baseFrequency, type_, stitchTiles, height, width, base, result, x, y, numOctaves, seed, id)
supermod.feTurbulenceType.subclass = feTurbulenceTypeSub
# end class feTurbulenceTypeSub


class cursorTypeSub(supermod.cursorType):
    def __init__(self, show='other', requiredExtensions=None, systemLanguage=None, title=None, actuate=None, requiredFeatures=None, href=None, role=None, arcrole=None, base=None, y=None, x=None, externalResourcesRequired=None, type_=None, id=None, valueOf_=''):
        supermod.cursorType.__init__(self, show, requiredExtensions, systemLanguage, title, actuate, requiredFeatures, href, role, arcrole, base, y, x, externalResourcesRequired, type_, id)
supermod.cursorType.subclass = cursorTypeSub
# end class cursorTypeSub


class aTypeSub(supermod.aType):
    def __init__(self, show=None, onfocusout=None, actuate=None, onmousedown=None, href=None, arcrole=None, id=None, onload=None, title_attr=None, space=None, requiredExtensions=None, transform=None, onmouseup=None, role=None, onactivate=None, onmousemove=None, type_=None, onfocusin=None, onclick=None, onmouseout=None, systemLanguage=None, onmouseover=None, externalResourcesRequired=None, classxx=None, lang=None, target=None, requiredFeatures=None, base=None, style_attr=None, mixedclass_=None, content_=None):
        supermod.aType.__init__(self, mixedclass_, content_)
supermod.aType.subclass = aTypeSub
# end class aTypeSub


class viewTypeSub(supermod.viewType):
    def __init__(self, viewTarget=None, viewBox=None, base=None, id=None, preserveAspectRatio=None, zoomAndPan='magnify', externalResourcesRequired=None, valueOf_=''):
        supermod.viewType.__init__(self, viewTarget, viewBox, base, id, preserveAspectRatio, zoomAndPan, externalResourcesRequired)
supermod.viewType.subclass = viewTypeSub
# end class viewTypeSub


class scriptTypeSub(supermod.scriptType):
    def __init__(self, show='other', title=None, actuate=None, href=None, role=None, arcrole=None, base=None, externalResourcesRequired=None, type_=None, id=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.scriptType.__init__(self, mixedclass_, content_)
supermod.scriptType.subclass = scriptTypeSub
# end class scriptTypeSub


class animateTypeSub(supermod.animateType):
    def __init__(self, keySplines=None, repeatCount=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, requiredExtensions=None, to=None, dur=None, onend=None, begin=None, max=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', requiredFeatures=None, base=None, values=None, keyTimes=None, onrepeat=None, valueOf_=''):
        supermod.animateType.__init__(self, keySplines, repeatCount, additive, repeatDur, id, fill, end, calcMode, min, requiredExtensions, to, dur, onend, begin, max, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, requiredFeatures, base, values, keyTimes, onrepeat)
supermod.animateType.subclass = animateTypeSub
# end class animateTypeSub


class setTypeSub(supermod.setType):
    def __init__(self, begin=None, onbegin=None, end=None, dur=None, requiredExtensions=None, fill='remove', max=None, systemLanguage=None, min=None, to=None, requiredFeatures=None, base=None, repeatCount=None, externalResourcesRequired=None, onend=None, repeatDur=None, id=None, restart='always', onrepeat=None, valueOf_=''):
        supermod.setType.__init__(self, begin, onbegin, end, dur, requiredExtensions, fill, max, systemLanguage, min, to, requiredFeatures, base, repeatCount, externalResourcesRequired, onend, repeatDur, id, restart, onrepeat)
supermod.setType.subclass = setTypeSub
# end class setTypeSub


class animateMotionTypeSub(supermod.animateMotionType):
    def __init__(self, origin=None, keySplines=None, requiredExtensions=None, fromxx=None, repeatCount=None, additive='replace', id=None, fill='remove', end=None, calcMode='linear', min=None, repeatDur=None, to=None, dur=None, onend=None, begin=None, max=None, keyPoints=None, onbegin=None, systemLanguage=None, accumulate='none', path=None, externalResourcesRequired=None, by=None, restart='always', rotate=None, requiredFeatures=None, base=None, values=None, keyTimes=None, onrepeat=None, mpath=None):
        supermod.animateMotionType.__init__(self, origin, keySplines, requiredExtensions, fromxx, repeatCount, additive, id, fill, end, calcMode, min, repeatDur, to, dur, onend, begin, max, keyPoints, onbegin, systemLanguage, accumulate, path, externalResourcesRequired, by, restart, rotate, requiredFeatures, base, values, keyTimes, onrepeat, mpath)
supermod.animateMotionType.subclass = animateMotionTypeSub
# end class animateMotionTypeSub


class mpathTypeSub(supermod.mpathType):
    def __init__(self, title=None, show='other', actuate=None, href=None, role=None, arcrole=None, base=None, externalResourcesRequired=None, type_=None, id=None, valueOf_=''):
        supermod.mpathType.__init__(self, title, show, actuate, href, role, arcrole, base, externalResourcesRequired, type_, id)
supermod.mpathType.subclass = mpathTypeSub
# end class mpathTypeSub


class animateColorTypeSub(supermod.animateColorType):
    def __init__(self, keySplines=None, repeatCount=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, requiredExtensions=None, to=None, dur=None, onend=None, begin=None, max=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', requiredFeatures=None, base=None, values=None, keyTimes=None, onrepeat=None, valueOf_=''):
        supermod.animateColorType.__init__(self, keySplines, repeatCount, additive, repeatDur, id, fill, end, calcMode, min, requiredExtensions, to, dur, onend, begin, max, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, requiredFeatures, base, values, keyTimes, onrepeat)
supermod.animateColorType.subclass = animateColorTypeSub
# end class animateColorTypeSub


class animateTransformTypeSub(supermod.animateTransformType):
    def __init__(self, keySplines=None, repeatCount=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, requiredExtensions=None, to=None, dur=None, type_='translate', onend=None, begin=None, max=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', requiredFeatures=None, base=None, values=None, keyTimes=None, onrepeat=None, valueOf_=''):
        supermod.animateTransformType.__init__(self, keySplines, repeatCount, additive, repeatDur, id, fill, end, calcMode, min, requiredExtensions, to, dur, type_, onend, begin, max, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, requiredFeatures, base, values, keyTimes, onrepeat)
supermod.animateTransformType.subclass = animateTransformTypeSub
# end class animateTransformTypeSub


class fontTypeSub(supermod.fontType):
    def __init__(self, horiz_origin_x=None, horiz_origin_y=None, style=None, vert_origin_x=None, horiz_adv_x=None, vert_origin_y=None, id=None, base=None, vert_adv_y=None, externalResourcesRequired=None, classxx=None, font_face=None, missing_glyph=None):
        supermod.fontType.__init__(self, horiz_origin_x, horiz_origin_y, style, vert_origin_x, horiz_adv_x, vert_origin_y, id, base, vert_adv_y, externalResourcesRequired, classxx, font_face, missing_glyph)
supermod.fontType.subclass = fontTypeSub
# end class fontTypeSub


class glyphTypeSub(supermod.glyphType):
    def __init__(self, horiz_adv_x=None, d=None, han=None, vert_text_orient=None, id=None, base=None, vert_adv_y=None, style_attr=None, unicode=None, arabic=None, glyph_name=None, classxx=None):
        supermod.glyphType.__init__(self, horiz_adv_x, d, han, vert_text_orient, id, base, vert_adv_y, style_attr, unicode, arabic, glyph_name, classxx)
supermod.glyphType.subclass = glyphTypeSub
# end class glyphTypeSub


class missing_glyphTypeSub(supermod.missing_glyphType):
    def __init__(self, vert_adv_y=None, d=None, horiz_adv_x=None, id=None, base=None, style_attr=None, classxx=None):
        supermod.missing_glyphType.__init__(self, vert_adv_y, d, horiz_adv_x, id, base, style_attr, classxx)
supermod.missing_glyphType.subclass = missing_glyphTypeSub
# end class missing_glyphTypeSub


class hkernTypeSub(supermod.hkernType):
    def __init__(self, g2=None, g1=None, k=None, u1=None, u2=None, base=None, id=None, valueOf_=''):
        supermod.hkernType.__init__(self, g2, g1, k, u1, u2, base, id)
supermod.hkernType.subclass = hkernTypeSub
# end class hkernTypeSub


class vkernTypeSub(supermod.vkernType):
    def __init__(self, g2=None, g1=None, k=None, u1=None, u2=None, base=None, id=None, valueOf_=''):
        supermod.vkernType.__init__(self, g2, g1, k, u1, u2, base, id)
supermod.vkernType.subclass = vkernTypeSub
# end class vkernTypeSub


class font_faceTypeSub(supermod.font_faceType):
    def __init__(self, slope=None, font_size=None, hanging=None, id=None, ascent=None, font_style=None, strikethrough_position=None, underline_position=None, descent=None, cap_height=None, units_per_em=None, overline_thickness=None, unicode_range=None, font_stretch=None, font_variant=None, x_height=None, centerline=None, mathline=None, panose_1=None, strikethrough_thickness=None, stemh=None, stemv=None, base=None, bbox=None, underline_thickness=None, font_family=None, topline=None, baseline=None, ideographic=None, font_weight=None, overline_position=None, widths=None, accent_height=None, font_face_src=None, definition_src=None):
        supermod.font_faceType.__init__(self, slope, font_size, hanging, id, ascent, font_style, strikethrough_position, underline_position, descent, cap_height, units_per_em, overline_thickness, unicode_range, font_stretch, font_variant, x_height, centerline, mathline, panose_1, strikethrough_thickness, stemh, stemv, base, bbox, underline_thickness, font_family, topline, baseline, ideographic, font_weight, overline_position, widths, accent_height, font_face_src, definition_src)
supermod.font_faceType.subclass = font_faceTypeSub
# end class font_faceTypeSub


class font_face_srcTypeSub(supermod.font_face_srcType):
    def __init__(self, base=None, id=None):
        supermod.font_face_srcType.__init__(self, base, id)
supermod.font_face_srcType.subclass = font_face_srcTypeSub
# end class font_face_srcTypeSub


class font_face_uriTypeSub(supermod.font_face_uriType):
    def __init__(self, title=None, show='other', actuate=None, href=None, role=None, arcrole=None, base=None, type_=None, id=None, font_face_format=None):
        supermod.font_face_uriType.__init__(self, title, show, actuate, href, role, arcrole, base, type_, id, font_face_format)
supermod.font_face_uriType.subclass = font_face_uriTypeSub
# end class font_face_uriTypeSub


class font_face_formatTypeSub(supermod.font_face_formatType):
    def __init__(self, base=None, string=None, id=None, valueOf_=''):
        supermod.font_face_formatType.__init__(self, base, string, id)
supermod.font_face_formatType.subclass = font_face_formatTypeSub
# end class font_face_formatTypeSub


class font_face_nameTypeSub(supermod.font_face_nameType):
    def __init__(self, base=None, name=None, id=None, valueOf_=''):
        supermod.font_face_nameType.__init__(self, base, name, id)
supermod.font_face_nameType.subclass = font_face_nameTypeSub
# end class font_face_nameTypeSub


class definition_srcTypeSub(supermod.definition_srcType):
    def __init__(self, title=None, show='other', actuate=None, href=None, role=None, arcrole=None, base=None, type_=None, id=None, valueOf_=''):
        supermod.definition_srcType.__init__(self, title, show, actuate, href, role, arcrole, base, type_, id)
supermod.definition_srcType.subclass = definition_srcTypeSub
# end class definition_srcTypeSub


class metadataTypeSub(supermod.metadataType):
    def __init__(self, base=None, id=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.metadataType.__init__(self, mixedclass_, content_)
supermod.metadataType.subclass = metadataTypeSub
# end class metadataTypeSub


class foreignObjectTypeSub(supermod.foreignObjectType):
    def __init__(self, requiredExtensions=None, onfocusout=None, height=None, id=None, onload=None, style=None, space=None, transform=None, content=None, width=None, onmouseup=None, onmousemove=None, onclick=None, onfocusin=None, onactivate=None, onmouseout=None, systemLanguage=None, onmouseover=None, externalResourcesRequired=None, onmousedown=None, classxx=None, lang=None, requiredFeatures=None, base=None, y=None, x=None, valueOf_='', mixedclass_=None, content_=None):
        supermod.foreignObjectType.__init__(self, mixedclass_, content_)
supermod.foreignObjectType.subclass = foreignObjectTypeSub
# end class foreignObjectTypeSub



#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in supermod.__dict__:
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = supermod.__dict__[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = supermod.Sax_svgHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def saxParseString(inString):
    parser = make_parser()
    documentHandler = supermod.SaxContentHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.svgType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="svg",
        namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = supermod.svgType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="svg",
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.svgType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from Ext import *\n\n')
    sys.stdout.write('rootObj = svg(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="svg")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')


