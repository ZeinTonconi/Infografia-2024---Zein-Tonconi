import numpy as np

def get_points(x0,y0,x1,y1):

    if(y0>y1):
        x0,y0,x1,y1 = x1,y1,x0,y0

    if(x0>x1):
        leftRight=-1
    else:
        leftRight=1
    
    points = [(x0, y0)]
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    xk = x0
    yk = y0
    # parametro de decision inicial
    Pk = 2 * dy - dx

    while xk != x1:
        xk += leftRight
        if Pk < 0:
            Pk = Pk + 2 * dy
        else:
            Pk = Pk + 2 * dy - 2 * dx
            yk += 1
        points.append((xk, yk))

    return points

def get_line(x0, y0, x1, y1):
    if(abs(x0-x1)>abs(y0-y1)):
        return get_points(x0,y0,x1,y1)
    else:
        pointsRotated = get_points(y0,-x0,y1,-x1)
        return [(-y,x) for x,y in pointsRotated]

def get_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    Pk = 3 - 2 * r
    points += get_symetry_points(xc, yc, x, y)
    while x <= y:
        x += 1
        if Pk < 0:
            Pk += (4 * x) + 6
        else:
            Pk += 4 * (x - y) + 10
            y -= 1
        points += get_symetry_points(xc, yc, x, y)
    return points


def get_symetry_points(xc, yc, x, y):
    return [
        (xc+x, yc+y),
        (xc-x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x),
    ]

def getRectangle(x0,y0,width,height):
    return (get_line(x0,y0,x0+width,y0) + get_line(x0+width, y0, x0+width, y0+height) + 
            get_line(x0+width, y0+height, x0,y0+height) + get_line(x0,y0+height,x0,y0))

def getTriangle(x0,y0,widht,height):
    return (get_line(x0,y0,x0+widht,y0) + get_line(x0+widht,y0,x0+widht//2, y0+height) + get_line(x0+widht//2, y0+height, x0,y0))

def rotatePointByAngle(x,y,cx,cy,angle):
    angleRadians = np.radians(angle)
    # Formula of rotation
    cos = np.cos(angleRadians)
    sin = np.sin(angleRadians)
    
    centerX = x-cx
    centerY = y-cy
    rotatedX = centerX*cos - centerY*sin
    rotatedY = centerX*sin + centerY*cos
    return (int(rotatedX+cx), int(rotatedY+cy))


def getPentagon(x0,y0,r):
    x,y=x0,y0+r
    edges = []
    for i in range(5):
        edges.append((x,y))
        x,y=rotatePointByAngle(x,y,x0,y0,72)

    edges.append((x,y))
    points = []

    for i in range(5):
        points += get_line(edges[i][0],edges[i][1], edges[i+1][0],edges[i+1][1])
    

    return points
