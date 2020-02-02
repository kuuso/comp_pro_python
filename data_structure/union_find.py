class union_find:
    def __init__(self, n):
        self.N = n
        self._parent = [i for i in range(self.N)]
        self._mem = [1] * self.N
        self.compo = self.N

    def parent(self, a):
        if self._parent[a] == a:
            return a
        self._parent[a] = self.parent(self._parent[a])
        return self._parent[a]

    def united(self,a, b):
        return self.parent(a) == self.parent(b)
    
    def unite(self,a, b):
        a = self.parent(a)
        b = self.parent(b)
        if(a == b): return False
        if self._mem[a] > self._mem[b]: a, b = b, a
        self._parent[a] = b
        self._mem[b] += self._mem[a]
        self.compo -= 1
        return True
    
    def is_root(self,a):
        return a == self._parent[a]
    def mem_cnt(self,a):
        return self._mem[self.parent(a)]
    def dump(self):
        print(self._parent)
    
        

def main():
    N = 10
    uf = union_find(N)
    print("{0} and {1} unite:{2}, compo:{3}".format(1,3,uf.unite(1,3),uf.compo))
    print("{0} and {1} unite:{2}, compo:{3}".format(4,2,uf.unite(4,2),uf.compo))
    print("{0} and {1} unite:{2}, compo:{3}".format(6,4,uf.unite(6,4),uf.compo))
    print("{0} and {1} unite:{2}, compo:{3}".format(2,4,uf.unite(2,4),uf.compo))


if __name__ == "__main__":
    main()
