n = int(input())

#Construct a segment tree
ST = [0] * n * 4 

def build(arr, st, id : int, l : int, r : int):
    if l == r:
        st[id] = arr[l]
        return
    else:
        mid = (l + r) // 2
        build(arr, st, id * 2, l, mid)
        build(arr, st, id * 2 + 1, mid + 1, r)
        st[id] = st[id * 2] + st[id * 2 + 1]

def get(st, id : int, l : int, r : int, u : int, v : int):
    if v < l or r < u:
        return 0
    if u <= l and r <= v:
        return st[id]
    mid = (l + r) // 2
    return get(st, id * 2, l, mid, u, v) + get(st, id * 2 + 1, mid + 1, r, u, v)

def update(st, id: int, l : int, r : int, pos : int, val : int):
    if l == r:
        st[id] = val
        return
    mid = (l + r) // 2
    if pos <= mid: update(st, id * 2, l, mid, pos, val)
    else: update(st, id * 2 + 1, mid + 1, r, pos, val)

    st[id] = st[id * 2] + st[id * 2 + 1]
    