class Vertex:
    def __init__(self, left = 0, right = 0):
        self.sum = 0
        self.left = left
        self.right = right
        self.left_child = None
        self.right_child = None
    
    def extend(self):
        if (not self.left_child) and self.left < self.right:
            mid = (self.left + self.right) // 2
            self.left_child = Vertex(self.left, mid)
            self.right_child = Vertex(mid + 1, self.right)

    def add(self, k : int, x : int):
        self.extend()
        self.sum += x
        if self.left_child is not None:
            if k <= self.left_child.right:
                self.left_child.add(k, x)
            else:
                self.right_child.add(k, x)
    
    def get_sum(self, u : int, v : int):
        if u <= self.left and v >= self.right:
            return self.sum
        if self.right < v and self.left > u:
            return 0
        self.extend()
        sumLeft = 0
        sumRight = 0
        if self.left_child : sumLeft = self.left_child.get_sum(u, v)
        if self.right_child : sumRight = self.right_child.get_sum(u, v)

        return sumLeft + sumRight

    def printNode(self):
        print("range[", self.left, self.right, ']:',self.sum)
        if self.left_child: 
            self.left_child.printNode()
            self.right_child.printNode()


Ball = Vertex(0, 17)

import random
result = 0
start = tmp = random.randint(0, 17)
end = 0
while(tmp <= 17):
    number = random.randint(0, 100)
    result += number
    Ball.add(tmp, number)
    end = tmp
    tmp = random.randint(tmp, 20)



print(Ball.get_sum(start, end) == result)