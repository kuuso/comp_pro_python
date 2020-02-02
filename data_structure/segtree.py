import sys
sys.setrecursionlimit(100000)
import random

class seg_tree:
    def __init__(self, n, op, id_ele):
        self.N = n
        self.n = 1 # pow of 2
        while(self.n < self.N):
            self.n *= 2
        self.op = op
        self.id_ele = id_ele
        self.data = [self.id_ele] * (2 * self.n - 1)

    def update(self, idx, v):
        idx += self.n - 1
        self.data[idx] = v
        while idx > 0:
            idx = (idx - 1) // 2
            self.data[idx] = self.op(self.data[idx * 2 + 1], self.data[idx * 2 + 2])

    def query(self, a, b):
        # op([a, b))
        return self._query(a, b, 0, 0, self.n)

    def _query(self, a, b, k, l, r):
        if r <= a or b <= l: return self.id_ele
        if a <= l and r <= b: return self.data[k]

        vl = self._query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = self._query(a, b, k * 2 + 2, (l + r) // 2, r)
        return self.op(vl, vr)

    def queryAll(self):
        return self.data[0]

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
    st = seg_tree(N, lambda x,y: x if x >= y else y, int(-1))
    for i in range(N):
        st.update(i, a[i])
    st.dump()
    print(st.query(0,5))
    print(st.query(7,9))
    st.update(3,10000)
    st.dump()
    print(st.query(0,5))
    print(st.query(7,9))
    


if __name__ == "__main__":
    main()
