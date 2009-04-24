#!/usr/bin/env python

#
# Generated Fri Apr 17 17:38:32 2009 by generateDS.py.
#

import sys
from string import lower as str_lower
from xml.dom import minidom
from xml.sax import handler, make_parser

import core as supermod

class svgTypeSub(supermod.svgType):
    def __init__(self, color_rendering=None, baseline_shift=None, stroke_width=None, flood_opacity=None, lighting_color=None, onload=None, onmousemove=None, alignment_baseline=None, onclick=None, glyph_orientation_vertical=None, onmouseover=None, shape_rendering=None, marker_end=None, flood_color=None, text_anchor=None, onfocusin=None, x=None, cursor_attr=None, stroke_linejoin=None, font_size=None, onfocusout=None, word_spacing=None, viewBox=None, space=None, onresize=None, marker_mid=None, color_interpolation=None, unicode_bidi=None, base=None, clip_rule=None, image_rendering=None, font_family=None, pointer_events=None, requiredFeatures=None, preserveAspectRatio=None, filter_attr=None, contentScriptType=None, text_rendering=None, fill_opacity=None, color=None, marker_start=None, height=None, onscroll=None, contentStyleType=None, color_profile=None, color_interpolation_filters=None, onabort=None, fill_rule=None, width=None, stroke_miterlimit=None, onmouseup=None, font_variant=None, stop_opacity=None, direction=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, dominant_baseline=None, overflow=None, zoomAndPan='magnify', onunload=None, font_size_adjust=None, display=None, mask_attr=None, letter_spacing=None, clip=None, requiredExtensions=None, onerror=None, onmousedown=None, stroke=None, stroke_linecap=None, id=None, fill=None, onzoom=None, font_style=None, font_stretch=None, glyph_orientation_horizontal=None, onactivate=None, font_weight=None, opacity=None, externalResourcesRequired=None, classxx=None, lang=None, writing_mode=None, stroke_opacity=None, stroke_dashoffset=None, text_decoration=None, stop_color=None, stroke_dasharray=None, y=None, enable_background=None, style_attr=None):
        supermod.svgType.__init__(self, color_rendering, baseline_shift, stroke_width, flood_opacity, lighting_color, onload, onmousemove, alignment_baseline, onclick, glyph_orientation_vertical, onmouseover, shape_rendering, marker_end, flood_color, text_anchor, onfocusin, x, cursor_attr, stroke_linejoin, font_size, onfocusout, word_spacing, viewBox, space, onresize, marker_mid, color_interpolation, unicode_bidi, base, clip_rule, image_rendering, font_family, pointer_events, requiredFeatures, preserveAspectRatio, filter_attr, contentScriptType, text_rendering, fill_opacity, color, marker_start, height, onscroll, contentStyleType, color_profile, color_interpolation_filters, onabort, fill_rule, width, stroke_miterlimit, onmouseup, font_variant, stop_opacity, direction, onmouseout, clip_path, visibility, systemLanguage, dominant_baseline, overflow, zoomAndPan, onunload, font_size_adjust, display, mask_attr, letter_spacing, clip, requiredExtensions, onerror, onmousedown, stroke, stroke_linecap, id, fill, onzoom, font_style, font_stretch, glyph_orientation_horizontal, onactivate, font_weight, opacity, externalResourcesRequired, classxx, lang, writing_mode, stroke_opacity, stroke_dashoffset, text_decoration, stop_color, stroke_dasharray, y, enable_background, style_attr)
supermod.svgType.subclass = svgTypeSub
# end class svgTypeSub


class gTypeSub(supermod.gType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, requiredExtensions=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, onload=None, style_attr=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, mask_attr=None, space=None, fill_opacity=None, transform=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, filter_attr=None, onfocusout=None, enable_background=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.gType.__init__(self, stroke_linejoin, font_size, text_rendering, color_rendering, clip, requiredExtensions, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, onload, style_attr, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, mask_attr, space, fill_opacity, transform, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, onactivate, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, onmousemove, onclick, onmouseout, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, systemLanguage, clip_rule, dominant_baseline, onmouseover, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, onfocusin, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, flood_color, text_anchor, text_decoration, stop_color, pointer_events, requiredFeatures, base, stroke_dasharray, onmouseup, filter_attr, onfocusout, enable_background, display, onmousedown, color_interpolation)
supermod.gType.subclass = gTypeSub
# end class gTypeSub


class defsTypeSub(supermod.defsType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, requiredExtensions=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, onload=None, style_attr=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, mask_attr=None, space=None, fill_opacity=None, transform=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, filter_attr=None, onfocusout=None, enable_background=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.defsType.__init__(self, stroke_linejoin, font_size, text_rendering, color_rendering, clip, requiredExtensions, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, onload, style_attr, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, mask_attr, space, fill_opacity, transform, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, onactivate, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, onmousemove, onclick, onmouseout, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, systemLanguage, clip_rule, dominant_baseline, onmouseover, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, onfocusin, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, flood_color, text_anchor, text_decoration, stop_color, pointer_events, requiredFeatures, base, stroke_dasharray, onmouseup, filter_attr, onfocusout, enable_background, display, onmousedown, color_interpolation)
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
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, fill_opacity=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, onload=None, style_attr=None, baseline_shift=None, stroke_width=None, color_profile=None, viewBox=None, flood_opacity=None, lighting_color=None, mask_attr=None, space=None, color_interpolation_filters=None, id=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, base=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, stroke_dasharray=None, onmouseup=None, filter_attr=None, onfocusout=None, preserveAspectRatio=None, enable_background=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.symbolType.__init__(self, stroke_linejoin, font_size, text_rendering, color_rendering, clip, fill_opacity, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, onload, style_attr, baseline_shift, stroke_width, color_profile, viewBox, flood_opacity, lighting_color, mask_attr, space, color_interpolation_filters, id, shape_rendering, font_stretch, stroke_miterlimit, onactivate, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, onmousemove, onclick, onmouseout, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, base, clip_rule, dominant_baseline, onmouseover, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, onfocusin, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, flood_color, text_anchor, text_decoration, stop_color, pointer_events, stroke_dasharray, onmouseup, filter_attr, onfocusout, preserveAspectRatio, enable_background, display, onmousedown, color_interpolation)
supermod.symbolType.subclass = symbolTypeSub
# end class symbolTypeSub


class useTypeSub(supermod.useType):
    def __init__(self, color_rendering=None, show=None, baseline_shift=None, stroke_width=None, flood_opacity=None, lighting_color=None, onload=None, style=None, title=None, onmousemove=None, alignment_baseline=None, role=None, onclick=None, glyph_orientation_vertical=None, onmouseover=None, shape_rendering=None, marker_end=None, flood_color=None, text_anchor=None, onfocusin=None, x=None, stroke_linejoin=None, font_size=None, onfocusout=None, word_spacing=None, space=None, marker_mid=None, unicode_bidi=None, base=None, clip_rule=None, image_rendering=None, font_family=None, filter=None, pointer_events=None, requiredFeatures=None, color_interpolation=None, text_rendering=None, fill_opacity=None, color=None, marker_start=None, actuate=None, height=None, href=None, color_profile=None, color_interpolation_filters=None, fill_rule=None, transform=None, width=None, stroke_miterlimit=None, onmouseup=None, font_variant=None, stop_opacity=None, type_=None, direction=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, dominant_baseline=None, overflow=None, font_size_adjust=None, cursor=None, display=None, letter_spacing=None, clip=None, requiredExtensions=None, onmousedown=None, stroke=None, stroke_linecap=None, id=None, fill=None, arcrole=None, font_style=None, font_stretch=None, glyph_orientation_horizontal=None, onactivate=None, font_weight=None, opacity=None, externalResourcesRequired=None, classxx=None, lang=None, writing_mode=None, stroke_opacity=None, mask=None, stroke_dashoffset=None, text_decoration=None, stop_color=None, stroke_dasharray=None, y=None, enable_background=None):
        supermod.useType.__init__(self, color_rendering, show, baseline_shift, stroke_width, flood_opacity, lighting_color, onload, style, title, onmousemove, alignment_baseline, role, onclick, glyph_orientation_vertical, onmouseover, shape_rendering, marker_end, flood_color, text_anchor, onfocusin, x, stroke_linejoin, font_size, onfocusout, word_spacing, space, marker_mid, unicode_bidi, base, clip_rule, image_rendering, font_family, filter, pointer_events, requiredFeatures, color_interpolation, text_rendering, fill_opacity, color, marker_start, actuate, height, href, color_profile, color_interpolation_filters, fill_rule, transform, width, stroke_miterlimit, onmouseup, font_variant, stop_opacity, type_, direction, onmouseout, clip_path, visibility, systemLanguage, dominant_baseline, overflow, font_size_adjust, cursor, display, letter_spacing, clip, requiredExtensions, onmousedown, stroke, stroke_linecap, id, fill, arcrole, font_style, font_stretch, glyph_orientation_horizontal, onactivate, font_weight, opacity, externalResourcesRequired, classxx, lang, writing_mode, stroke_opacity, mask, stroke_dashoffset, text_decoration, stop_color, stroke_dasharray, y, enable_background)
supermod.useType.subclass = useTypeSub
# end class useTypeSub


class imageTypeSub(supermod.imageType):
    def __init__(self, text_rendering=None, color_rendering=None, clip=None, show='other', color=None, onfocusout=None, actuate=None, height=None, href=None, onload=None, id=None, cursor=None, style=None, title=None, requiredExtensions=None, transform=None, width=None, onmouseup=None, role=None, onactivate=None, onmousemove=None, type_=None, onfocusin=None, opacity=None, onclick=None, onmouseout=None, clip_path=None, overflow=None, visibility=None, base=None, clip_rule=None, onmouseover=None, image_rendering=None, externalResourcesRequired=None, shape_rendering=None, classxx=None, lang=None, arcrole=None, mask=None, space=None, filter=None, pointer_events=None, requiredFeatures=None, systemLanguage=None, y=None, x=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.imageType.__init__(self, text_rendering, color_rendering, clip, show, color, onfocusout, actuate, height, href, onload, id, cursor, style, title, requiredExtensions, transform, width, onmouseup, role, onactivate, onmousemove, type_, onfocusin, opacity, onclick, onmouseout, clip_path, overflow, visibility, base, clip_rule, onmouseover, image_rendering, externalResourcesRequired, shape_rendering, classxx, lang, arcrole, mask, space, filter, pointer_events, requiredFeatures, systemLanguage, y, x, display, onmousedown, color_interpolation)
supermod.imageType.subclass = imageTypeSub
# end class imageTypeSub


class switchTypeSub(supermod.switchType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, requiredExtensions=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, cursor=None, stroke=None, stroke_linecap=None, onload=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, filter=None, style=None, space=None, fill_opacity=None, transform=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, mask=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, onfocusout=None, enable_background=None, display=None, onmousedown=None, color_interpolation=None):
        supermod.switchType.__init__(self, stroke_linejoin, font_size, text_rendering, color_rendering, clip, requiredExtensions, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, cursor, stroke, stroke_linecap, onload, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, filter, style, space, fill_opacity, transform, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, onactivate, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, onmousemove, onclick, onmouseout, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, systemLanguage, clip_rule, dominant_baseline, onmouseover, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, onfocusin, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, mask, flood_color, text_anchor, text_decoration, stop_color, pointer_events, requiredFeatures, base, stroke_dasharray, onmouseup, onfocusout, enable_background, display, onmousedown, color_interpolation)
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
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, flood_opacity=None, text_decoration=None, fill_opacity=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, style_attr=None, markerHeight=None, id=None, baseline_shift=None, stroke_width=None, color_profile=None, viewBox=None, color_rendering=None, refY=None, refX=None, mask_attr=None, clip=None, space=None, color_interpolation_filters=None, glyph_orientation_horizontal=None, orient=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, font_style=None, markerWidth=None, fill=None, opacity=None, lighting_color=None, direction=None, markerUnits=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, flood_color=None, text_anchor=None, marker_mid=None, stop_color=None, pointer_events=None, stroke_dasharray=None, filter_attr=None, preserveAspectRatio=None, enable_background=None, display=None, color_interpolation=None):
        supermod.markerType.__init__(self, stroke_linejoin, font_size, text_rendering, flood_opacity, text_decoration, fill_opacity, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, style_attr, markerHeight, id, baseline_shift, stroke_width, color_profile, viewBox, color_rendering, refY, refX, mask_attr, clip, space, color_interpolation_filters, glyph_orientation_horizontal, orient, shape_rendering, font_stretch, stroke_miterlimit, font_variant, font_style, markerWidth, fill, opacity, lighting_color, direction, markerUnits, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, base, clip_rule, dominant_baseline, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, flood_color, text_anchor, marker_mid, stop_color, pointer_events, stroke_dasharray, filter_attr, preserveAspectRatio, enable_background, display, color_interpolation)
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
    def __init__(self, color_rendering=None, show='other', baseline_shift=None, stroke_width=None, flood_opacity=None, lighting_color=None, title_attr=None, alignment_baseline=None, role=None, glyph_orientation_vertical=None, shape_rendering=None, marker_end=None, flood_color=None, text_anchor=None, patternTransform=None, x=None, cursor_attr=None, stroke_linejoin=None, font_size=None, word_spacing=None, viewBox=None, space=None, marker_mid=None, unicode_bidi=None, base=None, clip_rule=None, image_rendering=None, font_family=None, pointer_events=None, requiredFeatures=None, preserveAspectRatio=None, filter_attr=None, color_interpolation=None, text_rendering=None, fill_opacity=None, color=None, marker_start=None, actuate=None, height=None, href=None, color_profile=None, color_interpolation_filters=None, fill_rule=None, width=None, stroke_miterlimit=None, font_variant=None, stop_opacity=None, type_=None, direction=None, clip_path=None, visibility=None, systemLanguage=None, style_attr=None, overflow=None, font_size_adjust=None, display=None, mask_attr=None, letter_spacing=None, clip=None, requiredExtensions=None, stroke=None, stroke_linecap=None, id=None, fill=None, arcrole=None, font_style=None, font_stretch=None, glyph_orientation_horizontal=None, font_weight=None, opacity=None, patternUnits=None, externalResourcesRequired=None, classxx=None, lang=None, writing_mode=None, stroke_opacity=None, stroke_dashoffset=None, text_decoration=None, stop_color=None, stroke_dasharray=None, y=None, enable_background=None, dominant_baseline=None):
        supermod.patternType.__init__(self, color_rendering, show, baseline_shift, stroke_width, flood_opacity, lighting_color, title_attr, alignment_baseline, role, glyph_orientation_vertical, shape_rendering, marker_end, flood_color, text_anchor, patternTransform, x, cursor_attr, stroke_linejoin, font_size, word_spacing, viewBox, space, marker_mid, unicode_bidi, base, clip_rule, image_rendering, font_family, pointer_events, requiredFeatures, preserveAspectRatio, filter_attr, color_interpolation, text_rendering, fill_opacity, color, marker_start, actuate, height, href, color_profile, color_interpolation_filters, fill_rule, width, stroke_miterlimit, font_variant, stop_opacity, type_, direction, clip_path, visibility, systemLanguage, style_attr, overflow, font_size_adjust, display, mask_attr, letter_spacing, clip, requiredExtensions, stroke, stroke_linecap, id, fill, arcrole, font_style, font_stretch, glyph_orientation_horizontal, font_weight, opacity, patternUnits, externalResourcesRequired, classxx, lang, writing_mode, stroke_opacity, stroke_dashoffset, text_decoration, stop_color, stroke_dasharray, y, enable_background, dominant_baseline)
supermod.patternType.subclass = patternTypeSub
# end class patternTypeSub


class clipPathTypeSub(supermod.clipPathType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, requiredExtensions=None, letter_spacing=None, shape_rendering=None, word_spacing=None, stroke=None, stroke_linecap=None, baseline_shift=None, stroke_width=None, id=None, fill=None, cursor=None, style=None, space=None, fill_opacity=None, transform=None, font_style=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, glyph_orientation_horizontal=None, font_weight=None, opacity=None, direction=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, image_rendering=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, clipPathUnits=None, writing_mode=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, mask=None, stroke_dashoffset=None, text_anchor=None, text_decoration=None, filter=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, display=None):
        supermod.clipPathType.__init__(self, stroke_linejoin, font_size, text_rendering, requiredExtensions, letter_spacing, shape_rendering, word_spacing, stroke, stroke_linecap, baseline_shift, stroke_width, id, fill, cursor, style, space, fill_opacity, transform, font_style, font_stretch, stroke_miterlimit, font_variant, glyph_orientation_horizontal, font_weight, opacity, direction, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, systemLanguage, clip_rule, dominant_baseline, image_rendering, externalResourcesRequired, font_family, classxx, lang, clipPathUnits, writing_mode, stroke_opacity, font_size_adjust, fill_rule, mask, stroke_dashoffset, text_anchor, text_decoration, filter, pointer_events, requiredFeatures, base, stroke_dasharray, display)
supermod.clipPathType.subclass = clipPathTypeSub
# end class clipPathTypeSub


class maskTypeSub(supermod.maskType):
    def __init__(self, stroke_linejoin=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, requiredExtensions=None, color=None, marker_start=None, stroke_dashoffset=None, overflow=None, letter_spacing=None, height=None, word_spacing=None, stroke=None, stroke_linecap=None, style_attr=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, mask_attr=None, space=None, fill_opacity=None, transform=None, color_interpolation_filters=None, shape_rendering=None, width=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, maskUnits=None, marker_mid=None, opacity=None, direction=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, filter_attr=None, y=None, x=None, enable_background=None, display=None, color_interpolation=None):
        supermod.maskType.__init__(self, stroke_linejoin, font_size, text_rendering, color_rendering, clip, requiredExtensions, color, marker_start, stroke_dashoffset, overflow, letter_spacing, height, word_spacing, stroke, stroke_linecap, style_attr, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, mask_attr, space, fill_opacity, transform, color_interpolation_filters, shape_rendering, width, font_stretch, stroke_miterlimit, font_variant, font_style, glyph_orientation_horizontal, fill, maskUnits, marker_mid, opacity, direction, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, systemLanguage, clip_rule, dominant_baseline, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, font_weight, marker_end, stroke_opacity, font_size_adjust, fill_rule, flood_color, text_anchor, text_decoration, stop_color, pointer_events, requiredFeatures, base, stroke_dasharray, filter_attr, y, x, enable_background, display, color_interpolation)
supermod.maskType.subclass = maskTypeSub
# end class maskTypeSub


class filterTypeSub(supermod.filterType):
    def __init__(self, stroke_linejoin=None, fill_rule=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, show='other', color=None, marker_start=None, stroke_dashoffset=None, actuate=None, letter_spacing=None, height=None, word_spacing=None, cursor=None, stroke=None, href=None, arcrole=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, filter=None, style=None, primitiveUnits=None, title=None, fill_opacity=None, glyph_orientation_horizontal=None, color_interpolation_filters=None, shape_rendering=None, width=None, font_stretch=None, role=None, font_variant=None, font_style=None, stroke_miterlimit=None, fill=None, type_=None, marker_mid=None, opacity=None, direction=None, clip_path=None, overflow=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, font_weight=None, marker_end=None, filterRes=None, stroke_opacity=None, filterUnits=None, space=None, mask=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, stroke_linecap=None, stroke_dasharray=None, font_size_adjust=None, y=None, x=None, enable_background=None, display=None, color_interpolation=None):
        supermod.filterType.__init__(self, stroke_linejoin, fill_rule, font_size, text_rendering, color_rendering, clip, show, color, marker_start, stroke_dashoffset, actuate, letter_spacing, height, word_spacing, cursor, stroke, href, arcrole, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, filter, style, primitiveUnits, title, fill_opacity, glyph_orientation_horizontal, color_interpolation_filters, shape_rendering, width, font_stretch, role, font_variant, font_style, stroke_miterlimit, fill, type_, marker_mid, opacity, direction, clip_path, overflow, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, base, clip_rule, dominant_baseline, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, font_weight, marker_end, filterRes, stroke_opacity, filterUnits, space, mask, flood_color, text_anchor, text_decoration, stop_color, pointer_events, stroke_linecap, stroke_dasharray, font_size_adjust, y, x, enable_background, display, color_interpolation)
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
    def __init__(self, in2=None, height=None, width=None, base=None, mode='normal', inxx=None, y=None, x=None, id=None, result=None):
        supermod.feBlendType.__init__(self, in2, height, width, base, mode, inxx, y, x, id, result)
supermod.feBlendType.subclass = feBlendTypeSub
# end class feBlendTypeSub


class feColorMatrixTypeSub(supermod.feColorMatrixType):
    def __init__(self, height=None, width=None, base=None, values=None, result=None, inxx=None, y=None, x=None, type_='matrix', id=None):
        supermod.feColorMatrixType.__init__(self, height, width, base, values, result, inxx, y, x, type_, id)
supermod.feColorMatrixType.subclass = feColorMatrixTypeSub
# end class feColorMatrixTypeSub


class feComponentTransferTypeSub(supermod.feComponentTransferType):
    def __init__(self, height=None, width=None, base=None, result=None, inxx=None, y=None, x=None, id=None, feFuncR=None, feFuncG=None, feFuncB=None, feFuncA=None):
        supermod.feComponentTransferType.__init__(self, height, width, base, result, inxx, y, x, id, feFuncR, feFuncG, feFuncB, feFuncA)
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
    def __init__(self, y=None, width=None, k4=None, in2=None, height=None, k3=None, k2=None, k1=None, base=None, result=None, inxx=None, operator='over', x=None, id=None):
        supermod.feCompositeType.__init__(self, y, width, k4, in2, height, k3, k2, k1, base, result, inxx, operator, x, id)
supermod.feCompositeType.subclass = feCompositeTypeSub
# end class feCompositeTypeSub


class feConvolveMatrixTypeSub(supermod.feConvolveMatrixType):
    def __init__(self, x=None, divisor=None, kernelMatrix=None, targetY=None, kernelUnitLength=None, edgeMode='duplicate', height=None, width=None, bias=None, result=None, targetX=None, inxx=None, y=None, preserveAlpha=None, order=None):
        supermod.feConvolveMatrixType.__init__(self, x, divisor, kernelMatrix, targetY, kernelUnitLength, edgeMode, height, width, bias, result, targetX, inxx, y, preserveAlpha, order)
supermod.feConvolveMatrixType.subclass = feConvolveMatrixTypeSub
# end class feConvolveMatrixTypeSub


class feDiffuseLightingTypeSub(supermod.feDiffuseLightingType):
    def __init__(self, lighting_color=None, style=None, width=None, diffuseConstant=None, classxx=None, y=None, base=None, result=None, inxx=None, id=None, x=None, height=None, surfaceScale=None):
        supermod.feDiffuseLightingType.__init__(self, lighting_color, style, width, diffuseConstant, classxx, y, base, result, inxx, id, x, height, surfaceScale)
supermod.feDiffuseLightingType.subclass = feDiffuseLightingTypeSub
# end class feDiffuseLightingTypeSub


class feDisplacementMapTypeSub(supermod.feDisplacementMapType):
    def __init__(self, scale=None, yChannelSelector='A', in2=None, height=None, width=None, base=None, result=None, xChannelSelector='A', inxx=None, y=None, x=None, id=None):
        supermod.feDisplacementMapType.__init__(self, scale, yChannelSelector, in2, height, width, base, result, xChannelSelector, inxx, y, x, id)
supermod.feDisplacementMapType.subclass = feDisplacementMapTypeSub
# end class feDisplacementMapTypeSub


class feFloodTypeSub(supermod.feFloodType):
    def __init__(self, style=None, flood_opacity=None, flood_color=None, classxx=None, width=None, base=None, result=None, inxx=None, y=None, x=None, height=None, id=None):
        supermod.feFloodType.__init__(self, style, flood_opacity, flood_color, classxx, width, base, result, inxx, y, x, height, id)
supermod.feFloodType.subclass = feFloodTypeSub
# end class feFloodTypeSub


class feGaussianBlurTypeSub(supermod.feGaussianBlurType):
    def __init__(self, height=None, width=None, base=None, result=None, inxx=None, y=None, x=None, stdDeviation=None, id=None):
        supermod.feGaussianBlurType.__init__(self, height, width, base, result, inxx, y, x, stdDeviation, id)
supermod.feGaussianBlurType.subclass = feGaussianBlurTypeSub
# end class feGaussianBlurTypeSub


class feImageTypeSub(supermod.feImageType):
    def __init__(self, stroke_linejoin=None, fill_rule=None, font_size=None, text_rendering=None, color_rendering=None, clip=None, show='other', color=None, marker_start=None, actuate=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, cursor=None, stroke=None, href=None, arcrole=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, filter=None, style=None, space=None, height=None, fill_opacity=None, glyph_orientation_horizontal=None, transform=None, color_interpolation_filters=None, shape_rendering=None, width=None, font_stretch=None, role=None, font_variant=None, font_style=None, stroke_miterlimit=None, fill=None, type_=None, marker_mid=None, opacity=None, direction=None, clip_path=None, result=None, overflow=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, title=None, mask=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, stroke_linecap=None, stroke_dasharray=None, y=None, x=None, enable_background=None, display=None, color_interpolation=None):
        supermod.feImageType.__init__(self, stroke_linejoin, fill_rule, font_size, text_rendering, color_rendering, clip, show, color, marker_start, actuate, letter_spacing, stroke_dashoffset, word_spacing, cursor, stroke, href, arcrole, baseline_shift, stroke_width, color_profile, id, flood_opacity, lighting_color, filter, style, space, height, fill_opacity, glyph_orientation_horizontal, transform, color_interpolation_filters, shape_rendering, width, font_stretch, role, font_variant, font_style, stroke_miterlimit, fill, type_, marker_mid, opacity, direction, clip_path, result, overflow, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, base, clip_rule, dominant_baseline, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, lang, font_weight, marker_end, stroke_opacity, font_size_adjust, title, mask, flood_color, text_anchor, text_decoration, stop_color, pointer_events, stroke_linecap, stroke_dasharray, y, x, enable_background, display, color_interpolation)
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
    def __init__(self, width=None, height=None, y=None, base=None, radius=None, result=None, inxx=None, operator='erode', x=None, id=None):
        supermod.feMorphologyType.__init__(self, width, height, y, base, radius, result, inxx, operator, x, id)
supermod.feMorphologyType.subclass = feMorphologyTypeSub
# end class feMorphologyTypeSub


class feOffsetTypeSub(supermod.feOffsetType):
    def __init__(self, inxx=None, height=None, width=None, base=None, result=None, dx=None, dy=None, y=None, x=None, id=None):
        supermod.feOffsetType.__init__(self, inxx, height, width, base, result, dx, dy, y, x, id)
supermod.feOffsetType.subclass = feOffsetTypeSub
# end class feOffsetTypeSub


class feSpecularLightingTypeSub(supermod.feSpecularLightingType):
    def __init__(self, lighting_color=None, style=None, specularConstant=None, width=None, classxx=None, y=None, base=None, result=None, specularExponent=None, inxx=None, id=None, x=None, height=None, surfaceScale=None):
        supermod.feSpecularLightingType.__init__(self, lighting_color, style, specularConstant, width, classxx, y, base, result, specularExponent, inxx, id, x, height, surfaceScale)
supermod.feSpecularLightingType.subclass = feSpecularLightingTypeSub
# end class feSpecularLightingTypeSub


class feTileTypeSub(supermod.feTileType):
    def __init__(self, height=None, width=None, base=None, result=None, inxx=None, y=None, x=None, id=None):
        supermod.feTileType.__init__(self, height, width, base, result, inxx, y, x, id)
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
    def __init__(self, color_rendering=None, show=None, baseline_shift=None, stroke_width=None, flood_opacity=None, lighting_color=None, onload=None, title_attr=None, onmousemove=None, alignment_baseline=None, role=None, onclick=None, glyph_orientation_vertical=None, onmouseover=None, marker_end=None, flood_color=None, text_anchor=None, onfocusin=None, cursor_attr=None, stroke_linejoin=None, font_size=None, onfocusout=None, word_spacing=None, space=None, marker_mid=None, unicode_bidi=None, base=None, clip_rule=None, image_rendering=None, font_family=None, pointer_events=None, requiredFeatures=None, filter_attr=None, color_interpolation=None, text_rendering=None, fill_opacity=None, color=None, marker_start=None, actuate=None, shape_rendering=None, href=None, color_profile=None, color_interpolation_filters=None, fill_rule=None, transform=None, stroke_miterlimit=None, onmouseup=None, font_variant=None, stop_opacity=None, type_=None, direction=None, onmouseout=None, clip_path=None, visibility=None, systemLanguage=None, dominant_baseline=None, overflow=None, target=None, font_size_adjust=None, display=None, mask_attr=None, letter_spacing=None, clip=None, requiredExtensions=None, onmousedown=None, stroke=None, stroke_linecap=None, id=None, fill=None, arcrole=None, font_style=None, font_stretch=None, glyph_orientation_horizontal=None, onactivate=None, font_weight=None, opacity=None, externalResourcesRequired=None, classxx=None, lang=None, writing_mode=None, stroke_opacity=None, stroke_dashoffset=None, text_decoration=None, stop_color=None, stroke_dasharray=None, enable_background=None, style_attr=None, mixedclass_=None, content_=None):
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
    def __init__(self, requiredExtensions=None, keySplines=None, repeatCount=None, actuate=None, href=None, attributeType=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, show='other', to=None, role=None, dur=None, type_=None, onend=None, begin=None, max=None, attributeName=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', arcrole=None, requiredFeatures=None, base=None, values=None, keyTimes=None, title=None, onrepeat=None, valueOf_=''):
        supermod.animateType.__init__(self, requiredExtensions, keySplines, repeatCount, actuate, href, attributeType, additive, repeatDur, id, fill, end, calcMode, min, show, to, role, dur, type_, onend, begin, max, attributeName, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, arcrole, requiredFeatures, base, values, keyTimes, title, onrepeat)
supermod.animateType.subclass = animateTypeSub
# end class animateTypeSub


class setTypeSub(supermod.setType):
    def __init__(self, requiredExtensions=None, repeatCount=None, actuate=None, href=None, attributeType=None, repeatDur=None, id=None, fill='remove', end=None, min=None, show='other', to=None, role=None, dur=None, type_=None, onend=None, begin=None, max=None, attributeName=None, onbegin=None, systemLanguage=None, externalResourcesRequired=None, restart='always', arcrole=None, requiredFeatures=None, base=None, title=None, onrepeat=None, valueOf_=''):
        supermod.setType.__init__(self, requiredExtensions, repeatCount, actuate, href, attributeType, repeatDur, id, fill, end, min, show, to, role, dur, type_, onend, begin, max, attributeName, onbegin, systemLanguage, externalResourcesRequired, restart, arcrole, requiredFeatures, base, title, onrepeat)
supermod.setType.subclass = setTypeSub
# end class setTypeSub


class animateMotionTypeSub(supermod.animateMotionType):
    def __init__(self, origin=None, keySplines=None, requiredExtensions=None, fromxx=None, repeatCount=None, actuate=None, href=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', title=None, show='other', to=None, role=None, dur=None, type_=None, onend=None, begin=None, max=None, keyPoints=None, keyTimes=None, onbegin=None, systemLanguage=None, accumulate='none', path=None, externalResourcesRequired=None, by=None, restart='always', rotate=None, arcrole=None, requiredFeatures=None, base=None, values=None, min=None, onrepeat=None, mpath=None):
        supermod.animateMotionType.__init__(self, origin, keySplines, requiredExtensions, fromxx, repeatCount, actuate, href, additive, repeatDur, id, fill, end, calcMode, title, show, to, role, dur, type_, onend, begin, max, keyPoints, keyTimes, onbegin, systemLanguage, accumulate, path, externalResourcesRequired, by, restart, rotate, arcrole, requiredFeatures, base, values, min, onrepeat, mpath)
supermod.animateMotionType.subclass = animateMotionTypeSub
# end class animateMotionTypeSub


class mpathTypeSub(supermod.mpathType):
    def __init__(self, title=None, show='other', actuate=None, href=None, role=None, arcrole=None, base=None, externalResourcesRequired=None, type_=None, id=None, valueOf_=''):
        supermod.mpathType.__init__(self, title, show, actuate, href, role, arcrole, base, externalResourcesRequired, type_, id)
supermod.mpathType.subclass = mpathTypeSub
# end class mpathTypeSub


class animateColorTypeSub(supermod.animateColorType):
    def __init__(self, requiredExtensions=None, keySplines=None, repeatCount=None, actuate=None, href=None, attributeType=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, show='other', to=None, role=None, dur=None, type_=None, onend=None, begin=None, max=None, attributeName=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', arcrole=None, requiredFeatures=None, base=None, values=None, keyTimes=None, title=None, onrepeat=None, valueOf_=''):
        supermod.animateColorType.__init__(self, requiredExtensions, keySplines, repeatCount, actuate, href, attributeType, additive, repeatDur, id, fill, end, calcMode, min, show, to, role, dur, type_, onend, begin, max, attributeName, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, arcrole, requiredFeatures, base, values, keyTimes, title, onrepeat)
supermod.animateColorType.subclass = animateColorTypeSub
# end class animateColorTypeSub


class animateTransformTypeSub(supermod.animateTransformType):
    def __init__(self, requiredExtensions=None, keySplines=None, repeatCount=None, actuate=None, href=None, attributeType=None, additive='replace', repeatDur=None, id=None, fill='remove', end=None, calcMode='linear', min=None, show='other', to=None, role=None, dur=None, type_=None, onend=None, begin=None, max=None, attributeName=None, onbegin=None, systemLanguage=None, accumulate='none', fromxx=None, externalResourcesRequired=None, by=None, restart='always', arcrole=None, requiredFeatures=None, base=None, values=None, keyTimes=None, title=None, onrepeat=None, valueOf_=''):
        supermod.animateTransformType.__init__(self, requiredExtensions, keySplines, repeatCount, actuate, href, attributeType, additive, repeatDur, id, fill, end, calcMode, min, show, to, role, dur, type_, onend, begin, max, attributeName, onbegin, systemLanguage, accumulate, fromxx, externalResourcesRequired, by, restart, arcrole, requiredFeatures, base, values, keyTimes, title, onrepeat)
supermod.animateTransformType.subclass = animateTransformTypeSub
# end class animateTransformTypeSub


class fontTypeSub(supermod.fontType):
    def __init__(self, stroke_linejoin=None, vert_adv_y=None, font_size=None, text_rendering=None, flood_opacity=None, vert_origin_x=None, vert_origin_y=None, color=None, marker_start=None, overflow=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, cursor=None, stroke=None, stroke_linecap=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, color_rendering=None, horiz_origin_x=None, horiz_origin_y=None, style=None, clip=None, fill_rule=None, fill_opacity=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, filter=None, opacity=None, lighting_color=None, direction=None, clip_path=None, text_decoration=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, font_weight=None, marker_end=None, stroke_opacity=None, horiz_adv_x=None, font_size_adjust=None, mask=None, flood_color=None, text_anchor=None, marker_mid=None, stop_color=None, pointer_events=None, stroke_dasharray=None, alignment_baseline=None, enable_background=None, display=None, color_interpolation=None, font_face=None, missing_glyph=None):
        supermod.fontType.__init__(self, stroke_linejoin, vert_adv_y, font_size, text_rendering, flood_opacity, vert_origin_x, vert_origin_y, color, marker_start, overflow, letter_spacing, stroke_dashoffset, word_spacing, cursor, stroke, stroke_linecap, baseline_shift, stroke_width, color_profile, id, color_rendering, horiz_origin_x, horiz_origin_y, style, clip, fill_rule, fill_opacity, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, font_variant, font_style, glyph_orientation_horizontal, fill, filter, opacity, lighting_color, direction, clip_path, text_decoration, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, base, clip_rule, dominant_baseline, image_rendering, writing_mode, externalResourcesRequired, font_family, classxx, font_weight, marker_end, stroke_opacity, horiz_adv_x, font_size_adjust, mask, flood_color, text_anchor, marker_mid, stop_color, pointer_events, stroke_dasharray, alignment_baseline, enable_background, display, color_interpolation, font_face, missing_glyph)
supermod.fontType.subclass = fontTypeSub
# end class fontTypeSub


class glyphTypeSub(supermod.glyphType):
    def __init__(self, stroke_linejoin=None, vert_adv_y=None, font_size=None, text_rendering=None, flood_opacity=None, clip=None, fill_opacity=None, color=None, marker_start=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, unicode=None, baseline_shift=None, arabic=None, stroke_width=None, color_profile=None, id=None, color_rendering=None, lighting_color=None, mask_attr=None, han=None, fill_rule=None, stroke_opacity=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, overflow=None, font_family=None, classxx=None, font_weight=None, marker_end=None, d=None, horiz_adv_x=None, vert_text_orient=None, font_size_adjust=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, style_attr=None, stroke_dasharray=None, filter_attr=None, enable_background=None, glyph_name=None, display=None, color_interpolation=None):
        supermod.glyphType.__init__(self, stroke_linejoin, vert_adv_y, font_size, text_rendering, flood_opacity, clip, fill_opacity, color, marker_start, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, unicode, baseline_shift, arabic, stroke_width, color_profile, id, color_rendering, lighting_color, mask_attr, han, fill_rule, stroke_opacity, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, base, clip_rule, dominant_baseline, image_rendering, writing_mode, overflow, font_family, classxx, font_weight, marker_end, d, horiz_adv_x, vert_text_orient, font_size_adjust, flood_color, text_anchor, text_decoration, stop_color, pointer_events, style_attr, stroke_dasharray, filter_attr, enable_background, glyph_name, display, color_interpolation)
supermod.glyphType.subclass = glyphTypeSub
# end class glyphTypeSub


class missing_glyphTypeSub(supermod.missing_glyphType):
    def __init__(self, stroke_linejoin=None, vert_adv_y=None, font_size=None, text_rendering=None, flood_opacity=None, clip=None, fill_opacity=None, color=None, marker_start=None, letter_spacing=None, stroke_dashoffset=None, word_spacing=None, stroke=None, stroke_linecap=None, style_attr=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, color_rendering=None, lighting_color=None, mask_attr=None, fill_rule=None, stroke_opacity=None, color_interpolation_filters=None, shape_rendering=None, font_stretch=None, stroke_miterlimit=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, cursor_attr=None, base=None, clip_rule=None, dominant_baseline=None, image_rendering=None, writing_mode=None, overflow=None, font_family=None, classxx=None, font_weight=None, marker_end=None, d=None, horiz_adv_x=None, font_size_adjust=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, stroke_dasharray=None, filter_attr=None, enable_background=None, display=None, color_interpolation=None):
        supermod.missing_glyphType.__init__(self, stroke_linejoin, vert_adv_y, font_size, text_rendering, flood_opacity, clip, fill_opacity, color, marker_start, letter_spacing, stroke_dashoffset, word_spacing, stroke, stroke_linecap, style_attr, baseline_shift, stroke_width, color_profile, id, color_rendering, lighting_color, mask_attr, fill_rule, stroke_opacity, color_interpolation_filters, shape_rendering, font_stretch, stroke_miterlimit, font_variant, font_style, glyph_orientation_horizontal, fill, marker_mid, opacity, direction, clip_path, alignment_baseline, glyph_orientation_vertical, visibility, unicode_bidi, stop_opacity, cursor_attr, base, clip_rule, dominant_baseline, image_rendering, writing_mode, overflow, font_family, classxx, font_weight, marker_end, d, horiz_adv_x, font_size_adjust, flood_color, text_anchor, text_decoration, stop_color, pointer_events, stroke_dasharray, filter_attr, enable_background, display, color_interpolation)
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
    def __init__(self, stroke_linejoin=None, font_size=None, shape_rendering=None, text_rendering=None, color_rendering=None, clip=None, requiredExtensions=None, color=None, marker_start=None, stroke_dashoffset=None, overflow=None, letter_spacing=None, height=None, word_spacing=None, cursor=None, stroke=None, stroke_linecap=None, onload=None, baseline_shift=None, stroke_width=None, color_profile=None, id=None, flood_opacity=None, lighting_color=None, filter=None, style=None, space=None, fill_opacity=None, transform=None, color_interpolation_filters=None, content=None, width=None, font_stretch=None, stroke_miterlimit=None, onactivate=None, font_variant=None, font_style=None, glyph_orientation_horizontal=None, fill=None, marker_mid=None, opacity=None, direction=None, onmousemove=None, onclick=None, onmouseout=None, clip_path=None, alignment_baseline=None, glyph_orientation_vertical=None, visibility=None, unicode_bidi=None, stop_opacity=None, systemLanguage=None, clip_rule=None, dominant_baseline=None, onmouseover=None, image_rendering=None, writing_mode=None, externalResourcesRequired=None, font_family=None, classxx=None, lang=None, onfocusin=None, font_weight=None, marker_end=None, stroke_opacity=None, font_size_adjust=None, fill_rule=None, mask=None, flood_color=None, text_anchor=None, text_decoration=None, stop_color=None, pointer_events=None, requiredFeatures=None, base=None, stroke_dasharray=None, onmouseup=None, y=None, x=None, enable_background=None, onfocusout=None, display=None, onmousedown=None, color_interpolation=None, valueOf_='', mixedclass_=None, content_=None):
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


