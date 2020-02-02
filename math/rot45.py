# [0,x) x [0,y) @ manhattan -> [0,xx) x [0, yy) chevichef
def m2c (_x,_y,L=1000):
    return (_x + _y), (-_x + _y + L)
def c2m (_xx, _yy,L=1000):
    assert (_xx - _yy + L) % 2 == 0, "cannot invert into integer"
    return (_xx - _yy + L) // 2, (_xx + _yy - L) // 2
def inRange(_t, _l, _r):
    return _l <= _t and _t < _r


def check():
    a = [[i * 5 + j for j in range(5)] for i in range(5)]
    for i in range(5):
        print(a[i])
    b = [[-1] * 10 for i in range(10)]
    for i in range(5):
        for j in range(5):
            nx, ny = m2c(j, i, 5)
            b[ny][nx] = a[i][j]
    
    for i in range(10):
        print(b[i])
    
    c = [[-1] * 5 for i in range(5)]
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] != -1:
                x, y = c2m(j, i, 5)
                c[y][x] = b[i][j]
    
    for i in range(5):
        print(c[i])


if __name__ == "__main__":
    check()