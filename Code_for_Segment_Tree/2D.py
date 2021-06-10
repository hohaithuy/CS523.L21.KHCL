

def build_y(arr, st, vx: int, lx: int, rx : int, vy : int, ly : int, ry : int):
    if (ly == ry):
        if (lx == rx):
            st[vx][vy] = a[lx][ly]
        else:
            st[vx][vy] = st[vx * 2][vy] + st[vx * 2 + 1][vy]
     else:
        mid = (ly + ry) // 2
        build_y(arr, st, vx, lx, rx, vy * 2, ly, mid)
        build_y(arr, st, vx, lx, rx, vy * 2 + 1, mid + 1, ry)
        st[vx][vy] = st[vx][vy * 2] + st[vx][vy * 2 + 1]
    


def build_x(arr, st, int vx, int lx, int rx):
    if (lx != rx):
        mx = (lx + rx) // 2
        build_x(arr, st, vx * 2, lx, mx)
        build_x(arr, st, vx * 2 + 1, mx + 1, rx)
    
    build_y(arr, st, vx, lx, rx, 1, 0, m - 1)



def sum_y(st, vx : int, vy : int, tly : int, try_ : int, ly : int, ry : int) :
    if (ly > ry):
        return 0
    if (ly == tly and try_ == ry):
        return st[vx][vy]
    tmy = (tly + try_) // 2
    return sum_y(st, vx, vy*2, tly, tmy, ly, min(ry, tmy))
         + sum_y(st, vx, vy*2+1, tmy+1, try_, max(ly, tmy+1), ry)


def sum_x(st, vx: int, tlx : int, trx : int, lx : int, rx : int, ly : int, ry : int) :
    if (lx > rx):
        return 0
    if (lx == tlx && trx == rx):
        return sum_y(st, vx, 1, 0, m-1, ly, ry)
    tmx = (tlx + trx) // 2
    return sum_x(st, vx*2, tlx, tmx, lx, min(rx, tmx), ly, ry)
         + sum_x(st, vx*2+1, tmx+1, trx, max(lx, tmx+1), rx, ly, ry)

