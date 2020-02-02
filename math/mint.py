class mint:
    mod = int(1e9 + 7)
    def __init__(self, v = 0):
        if not ((v >= 0) and (v < mint.mod)):
            v %= mint.mod
            if v < 0: v += mint.mod
        self.V = v
    def __add__(self, other):
        v = self.V + (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __sub__(self, other):
        v = self.V - (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __mul__(self, other):
        v = self.V * (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __floordiv__(self, other):
        v = self.V * mint.inv((other.V if isinstance(other, mint) else other))
        return mint(v)
    def __truediv__(self, other):
        v = self.V * mint.inv((other.V if isinstance(other, mint) else other))
        return mint(v)
    
    def __eq__(self, other):
        return self.V == (other.V if isinstance(other, mint) else mint(other).V)
    def __ne__(self, other):
        return self.V != (other.V if isinstance(other, mint) else other)
    def __int__(self): return self.V
    # right operand
    def __radd__(self, other):
        v = (other.V if isinstance(other, mint) else other) + self.V
        return mint(v)
    def __rsub__(self, other):
        v = (other.V if isinstance(other, mint) else other) - self.V
        return mint(v)
    def __rmul__(self, other):
        v = (other.V if isinstance(other, mint) else other) * self.V
        return mint(v)
    def __rfloordiv__(self, other):
        v = (other.V if isinstance(other, mint) else other) * mint.inv(self.V)
        return mint(v)
    def __rtruediv__(self, other):
        v = (other.V if isinstance(other, mint) else other) * mint.inv(self.V)
        return mint(v)

    @staticmethod
    def inv(x):
        a, _, _ = mint.extGCD(x, mint.mod)
        return (a + mint.mod) % mint.mod
    @staticmethod
    def extGCD(x, y):
        r0 = x
        r1 = y
        a0 = 1
        a1 = 0
        b0 = 0
        b1 = 1
        while(r1 > 0):
            q1 = r0 // r1
            r2 = r0 % r1
            a2 = a0 - q1 * a1
            b2 = b0 - q1 * b1
            r0 = r1; r1 = r2
            a0 = a1; a1 = a2
            b0 = b1; b1 = b2
        c = r0
        a = a0
        b = b0       
        return a, b, c
    @staticmethod
    def pow(x, k):
        x = x.V if isinstance(x, mint) else x
        return pow(x, k, mint.mod)

    
    def __str__(self):
        return str(self.V)
    def __repr__(self):
        return str(self.V)


def main():
    x = mint(-2)
    y = mint(-1)
    z = mint(-2)
    print(x + y)
    print(x * y)
    print(x - y)
    print(x / y)
    print(x == y)
    print(x != y)
    print(x == z)
    print(x != z)
    print(int(x))
    print(x == mint(-2))
    print(x == -2)
    print(1 / mint(2))
    print(mint(1) / 2)
    

if __name__ == "__main__":
    main()
