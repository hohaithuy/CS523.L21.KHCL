class Query:
    def __init__(self, l = None, r = None, k = None):
        self.k = k
        self.l = l
        self.r = r
    
    def __str__(self):
        return str(self.k)

def isLessThan(a, b):
    return a.k < b.k

def build(st, id : int, l : int, r : int):
    if l == r:
        st[id] = 1
        return
    mid = (l + r) // 2
    build(st, id * 2, l, mid)
    build(st, id * 2 + 1, mid + 1, r)

    st[id] = st[id * 2] + st[id * 2 + 1]

def update(st, id : int, l : int, r : int, u : int):
    if u < l or r < u:
        return
    
    if l == r:
        st[id] = 0
        return

    mid = (l + r) // 2
    update(st, id * 2, l, mid, u)
    update(st, id * 2 + 1, mid + 1, r, u)
    
    st[id] = st[id * 2] + st[id * 2 + 1]

def get(st, id : int, l : int, r : int, u : int, v : int):
    if v < l or r < u:
        return 0
    if u <= l and r <= v:
        return st[id]

    mid = (l + r) // 2

    return get(st, id * 2, l, mid, u, v) + get(st, id * 2 + 1, mid + 1, r, u, v)







n = int(input())
lst = [int(j) for j in input().split()]
iteration = int(input())
queryArray = []


for times in range(iteration):
    tmp = [int(j) for j in input().split()]
    queryArray.append(Query(tmp[0] - 1, tmp[1] - 1, tmp[2]))

for i in range(iteration):
    for j in range(i + 1, iteration):
        if isLessThan(queryArray[j], queryArray[i]): queryArray[j], queryArray[i] = queryArray[i], queryArray[j]

#khoi tao mang id
id_array = sorted(range(len(lst)), key=lambda k: lst[k])
b = [1] * n * 4

#khoi tao st
st = [Query(0, 0, 0)] * n * 4
build(st, 1, 0, n - 1)



index = 0
for i in queryArray:
    while lst[id_array[index]] <=  i.k:
        b[id_array[index]] = 0
        update(st, 1, 0, n - 1, id_array[index])
        index = index + 1
    print(get(st, 1, 0, n - 1, i.l, i.r))