import sys
sys.setrecursionlimit(100000)
import random

class seg_tree:
    def __init__(self, n, op, id_ele, left = True):
        self.N = n
        self.n = 1 # pow of 2
        while(self.n < self.N):
            self.n *= 2
        self.op = op
        self.id_ele = id_ele
        self.data = [self.id_ele] * (2 * self.n - 1)

        self.left = left
        self.index = [0] * (2 * self.n - 1)
        for i in range(self.n): self.index[i + self.n - 1] = i
        for i in reversed(range(self.n - 1)):
            self.index[i] = self.index[i * 2 + 1] if left else self.index[i * 2 + 2]
        
    def update(self, idx, v):
        idx += self.n - 1
        self.data[idx] = v
        prefer = 0 if self.left else 1
        while idx > 0:
            idx = (idx - 1) // 2
            self.data[idx] = self.op(self.data[idx * 2 + 1], self.data[idx * 2 + 2])
            self.index[idx] = self.index[idx * 2 + 1 + prefer] if self.data[idx] == self.data[idx * 2 + 1 + prefer] else self.index[idx * 2 + 1 + (1 - prefer)]

    def query(self, a, b):
        # op([a, b))
        return self._query(a, b, 0, 0, self.n)

    def _query(self, a, b, k, l, r):
        prefer = self.N if self.left else -1
        if r <= a or b <= l: return self.id_ele, prefer 
        if a <= l and r <= b: return self.data[k], self.index[k]

        vl, lidx = self._query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr, ridx = self._query(a, b, k * 2 + 2, (l + r) // 2, r)
        ret = self.op(vl, vr)
        if self.left: idx = lidx if vl == ret else ridx
        else: idx = ridx if vr == ret else lidx
        return ret, idx

    def queryAll(self):
        return self.data[0]
    def at(self, idx):
        return self.data[idx + self.n - 1]
    def initialize(self, a):
        for i in range(len(a)): self.data[i + self.n - 1] = a[i]
        prefer = 0 if self.left else 1
        for i in reversed(range(self.n - 1)):
            self.data[i] = self.op(self.data[i * 2 + 1], self.data[i * 2 + 2])
            self.index[i] = self.index[i * 2 + 1 + prefer] if self.data[i] == self.data[i * 2 + 1 + prefer] else self.index[i * 2 + 1 + (1 - prefer)]
        
    def dump(self):
        print()
        h = 0
        cnt = 0
        for i in range(len(self.data)):
            print("{0} ".format(self.data[i]), end="")
            cnt += 1
            if cnt == 2 ** h:
                cnt = 0
                h += 1
                print()
        




def main():
    N = 10
    random.seed(2525)
    a = [random.randrange(0,100) for _ in range(N)]
    print(a)
    #st = seg_tree(N, lambda x,y: x if x >= y else y, int(-1))
    st = seg_tree(N, max, int(-1))
    for i in range(N):
        st.update(i, a[i])
    st.dump()
    a = [random.randrange(0,100) for _ in range(N)]
    print(a)
    st.initialize(a)
    st.dump()

    print(st.query(0,5))
    print(st.query(7,9))
    st.update(3,10000)
    st.dump()
    print(st.query(0,5))
    print(st.query(7,9))
    


if __name__ == "__main__":
    main()
