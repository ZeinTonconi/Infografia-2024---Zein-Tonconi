def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    dx = x1 - x0
    dy = y1 - y0
    xk = x0
    yk = y0
    # parametro de decision inicial
    Pk = 2 * dy - dx

    while xk < x1:
        xk += 1
        if Pk < 0:
            Pk = Pk + 2 * dy
        else:
            Pk = Pk + 2 * dy - 2 * dx
            yk += 1
        points.append((xk, yk))

    return points


if __name__ == "__main__":
    x0 = 3
    y0 = 2
    x1 = 15
    y1 = 11
    points = get_line(x0, y0, x1, y1)
    print(points)


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