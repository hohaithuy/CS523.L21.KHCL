class Node:
    def __init__(self, optimal = None, open_bracket = None, close_bracket = None):
        self.optimal = optimal
        self.open_bracket = open_bracket
        self.close_bracket = close_bracket
    def __str__(self): 
        return str(self.optimal)

def add(Left : Node, Right : Node) -> Node:
    res = Node()
    tmp = min(Left.open_bracket, Right.close_bracket)
    res.optimal = Left.optimal + Right.optimal + tmp * 2
    
    res.open_bracket = Left.open_bracket + Right.open_bracket - tmp
    res.close_bracket = Left.close_bracket + Right.close_bracket - tmp
    return res

def build(s, st, id : int, l : int, r : int):
    if l == r:
        if s[l] == '(': st[id] = Node(0, 1, 0)
        else: st[id] = Node(0, 0, 1)
        return
    
    mid = (l + r) // 2
    build(s, st, id * 2, l, mid)
    build(s, st, id * 2 + 1, mid + 1, r)

    st[id] = add(st[id * 2], st[id * 2 + 1]) 

def query(id : int, l : int, r : int, u : int, v : int, st):
    if v < l or r < u:
        return Node(0, 0, 0)
    if u <= l and r <= v:
        return st[id]
    
    mid = (l + r) // 2
    return add(query(id * 2, l, mid, u, v, st), query(id * 2 + 1, mid+1, r, u, v, st))

# Node st[MAXN * 4]
s = input()
st = [Node(0, 0, 0)] * 4 * len(s)
l = 0
r = len(s) - 1
build(s, st, 1, l, r)

n = int(input())
for i in range(n):
    u, v = map(int, input().split())
    print(query(1, l, r, u - 1, v - 1, st))



