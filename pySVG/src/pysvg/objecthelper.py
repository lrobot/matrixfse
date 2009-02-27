from pysvg import *
class ObjectHelper:
  """
    Helper class that creates commonly used objects and shapes with predefined styles and
    few but often used parameters. Used to avoid more complex coding for common tasks.
    """
  def createCircle(self, cx, cy, r, strokewidth=1, stroke='black', fill='none'):
    """
    Creates a circle
    @type  cx: string or int
    @param cx:  starting x-coordinate  
    @type  cy: string or int
    @param cy:  starting y-coordinate 
    @type  r: string or int
    @param r:  radius 
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @type  fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param fill:  color with which to fill the element (default: no filling)
    @return:  a circle object
    """
    style_dict={'fill':fill,'stroke-width':strokewidth,'stroke':stroke}
    return circle(cx,cy,r,style_dict)
  
  def createEllipse(self, cx, cy, rx, ry, strokewidth=1, stroke='black', fill='none'):
    """
    Creates an ellipse
    @type  cx: string or int
    @param cx:  starting x-coordinate  
    @type  cy: string or int
    @param cy:  starting y-coordinate 
    @type  rx: string or int
    @param rx:  radius in x direction 
    @type  ry: string or int
    @param ry:  radius in y direction
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @type  fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param fill:  color with which to fill the element (default: no filling)
    @return:  an ellipse object
    """
    style_dict={'fill':fill,'stroke-width':strokewidth,'stroke':stroke}
    return ellipse(cx,cy,rx,ry,style_dict)
   
  def createRect(self, x, y, width, height, rx=None, ry=None, strokewidth=1, stroke='black', fill='none'):
    """
    Creates a Rectangle
    @type  x: string or int
    @param x:  starting x-coordinate  
    @type  y: string or int
    @param y:  starting y-coordinate 
    @type  width: string or int
    @param width:  width of the rectangle  
    @type  height: string or int
    @param height:  height of the rectangle 
    @type  rx: string or int
    @param rx:  For rounded rectangles, the x-axis radius of the ellipse used to round off the corners of the rectangle. 
    @type  ry: string or int
    @param ry:  For rounded rectangles, the y-axis radius of the ellipse used to round off the corners of the rectangle.
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @type  fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param fill:  color with which to fill the element (default: no filling)
    @return:  a rect object
    """
    style_dict={'fill':fill,'stroke-width':strokewidth,'stroke':stroke}
    return rect(x,y,width,height,rx,ry,style_dict)
  
  def createPolygon(self, points, strokewidth=1, stroke='black', fill='none'):
    """
    Creates a Polygon
    @type  points: string in the form "x1,y1 x2,y2 x3,y3"
    @param points:  all points relevant to the polygon
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @type  fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param fill:  color with which to fill the element (default: no filling)
    @return:  a polygon object
    """
    style_dict={'fill':fill,'stroke-width':strokewidth,'stroke':stroke}
    return polygon(points=points,style_dict=style_dict)
  
  def createPolyline(self, points,strokewidth=1, stroke='black'):
    """
    Creates a Polyline
    @type  points: string in the form "x1,y1 x2,y2 x3,y3"
    @param points:  all points relevant to the polygon
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @return:  a polyline object
    """
    style_dict={'fill':'none','stroke-width':strokewidth,'stroke':stroke}
    return polyline(points=points,style_dict=style_dict)
    
    
  def createLine(self,x1,y1,x2,y2,strokewidth=1,stroke="black"):
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
    @type  strokewidth: string or int
    @param strokewidth:  width of the pen used to draw
    @type  stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    @param stroke:  color with which to draw the outer limits
    @return:  a line object
    """
    style_dict={'stroke-width':strokewidth,'stroke':stroke}
    return line(x1,y1,x2,y2,style_dict)
  
  def convertTupleArrayToPoints(self,arrayOfPointTuples):
    """Method used to convert an array of tuples (x,y) into a string
    suitable for createPolygon or createPolyline
    @type  arrayOfPointTuples: An array containing tuples eg.[(x1,y1),(x2,y2]
    @param arrayOfPointTuples:  All points needed to create the shape
    @return a string in the form "x1,y1 x2,y2 x3,y3"
    """
    points=""
    for tuple in arrayOfPointTuples:
      points+=str(tuple[0])+","+str(tuple[1])+" "
    return points