import sys
sys.setrecursionlimit(100000)
import random

class fenwick_tree:
    def __init__(self, n):
        self.N = n
        self.n = 1 # pow of 2
        while(self.n < self.N):
            self.n *= 2
        self.data = [0] * (self.n + 1)

    def add(self, idx, x):
        while idx <= self.n:
            self.data[idx] += x
            idx += (idx & -idx)

    def cumulate(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= (idx & -idx)
        return s

class fenwick_tree_abstract:
    def __init__(self, n, op, id_ele):
        self.N = n
        self.n = 1 # pow of 2
        while(self.n < self.N):
            self.n *= 2
        self.op = op
        self.id_ele = id_ele
        self.data = [self.id_ele] * (self.n + 1)

    def add(self, idx, x):
        while idx <= self.n:
            self.data[idx] = self.op(self.data[idx], x)
            idx += (idx & -idx)

    def cumulate(self, idx):
        s = self.id_ele
        while idx > 0:
            s = self.op(s, self.data[idx])
            idx -= (idx & -idx)
        return s


def main():
    N = 10
    random.seed(2525)
    a = [0 for _ in range(N)]
    #a = [random.randrange(0,100) for _ in range(N)]
    print(a)

    #bit = fenwick_tree(N)
    bit = fenwick_tree_abstract(N, lambda a,b: a + b, 0)

    T1 = 100
    T2 = 10
    for t1 in range(T1):
        idx = random.randrange(0,N)
        v = random.randrange(0, 123456)
        a[idx] += v
        bit.add(idx + 1, v)
        for t2 in range(T2):
            rawsum = 0
            r = random.randrange(0, N+1)
            for i in range(r):
                rawsum += a[i]
            bitsum = bit.cumulate(r)
            print("rawsum: {0}, bitsum:{1}".format(rawsum, bitsum))
            if rawsum != bitsum:
                print("rawsum: {0}, bitsum:{1}".format(rawsum, bitsum))
                sys.exit(0)
    
    print(a)
    print("OK")



if __name__ == "__main__":
    main()
