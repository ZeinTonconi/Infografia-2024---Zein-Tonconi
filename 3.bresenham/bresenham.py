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
        print((xk,yk))
        points.append((xk, yk))

    return points

def get_line(x0, y0, x1, y1):
    if(abs(x0-x1)>abs(y0-y1)):
        return get_points(x0,y0,x1,y1)
    else:
        pointsRotated = get_points(y0,-x0,y1,-x1)
        return [(-y,x) for x,y in pointsRotated]
