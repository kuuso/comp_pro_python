import sys
sys.setrecursionlimit(100000)
import random

class Acc2:
    def __init__(self):
        self.h = 0
        self.w = 0
        self.acc = None
    def initialize(self, a):
        self.h = len(a)
        self.w = len(a[0])
        self.acc = [[0] * (self.w + 1) for i in range(self.h + 1)]
        for i in range(1, self.h + 1):
            for j in range(1,self.w + 1):
                self.acc[i][j] = a[i-1][j-1]
        for i in range(1,self.h+1):
            for j in range(1, self.w+1):
                self.acc[i][j] += self.acc[i][j-1]
        for j in range(1,self.w + 1):
            for i in range(1, self.h + 1):
                self.acc[i][j] += self.acc[i-1][j]
    def sum(self, x1, y1, x2, y2):
        if x2 < x1 or y2 < y1: return 0
        return (self.acc[y2][x2] - self.acc[y2][x1] - self.acc[y1][x2] + self.acc[y1][x1])

def naive(a, x1, y1, x2, y2):
    tot = 0
    for i in range(y1,y2):
        for j in range(x1,x2):
            tot += a[i][j]
    return tot

def check():
    N = 10
    a = [[i * N + j for j in range(N)] for i in range(N)]
    acc = Acc2()
    acc.initialize(a)

    random.seed(2525)
    for _ in range(4):
        x1 = random.randint(0,N-1)
        y1 = random.randint(0,N-1)
        x2 = random.randint(x1,N)
        y2 = random.randint(y1,N)
        res = acc.sum(x1,y1,x2,y2)
        gt = naive(a, x1,y1,x2,y2)
        print("[{0},{1}) * [{2}, {3}): res:{4} gt:{5}, assert:{6}".format(x1,x2,y1,y2,res,gt,res==gt))


if __name__ == "__main__":
    check()
