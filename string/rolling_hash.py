import sys
sys.setrecursionlimit(100000)
import random

class rolling_hash:
    def __init__(self, s, b=2525, mod=int(1e9+7)):
        N = len(s)

        self.mod = mod
        self.S = s
        self.N = N
        self.hash = [0] * (N + 1)

        self.b = b
        self.bs = [0] * (N + 1)

        self.bs[0] = 1
        for i in range(N):
            self.bs[i + 1] = self.bs[i] * self.b
            if self.bs[i + 1] >= mod: self.bs[i + 1] %= mod

        self.hash[0] = 0
        for i in range(N):
            self.hash[i + 1] = self.hash[i] * self.b + ord(s[i])
            if self.hash[i + 1] >= mod: self.hash[i + 1] %= mod

    def get_hash(self, start, length):
        if length == 0: return 0
        if(start + length >= self.N): length = self.N - start
        ret = self.hash[start + length] - self.hash[start] * self.bs[length]
        if(ret >= self.mod or ret < 0): ret %= self.mod
        if(ret < 0): ret += self.mod
        return ret


def check():

    N = 50
    random.seed(2525)
    s = "".join([chr(random.randrange(ord('a'), ord('e'))) for _ in range(N)])
    N = len(s)
    cnt = 0
    ff = 0
    tt = 0
    ft = 0 
    tf = 0

    print("s:{0}".format(s))
    rh = rolling_hash(s)

    for i1 in range(N):
        for i2 in range(N):
            for l1 in range(N-i1):
                for l2 in range(N-i2):
                    cnt += 1
                    s1 = s[i1:(i1+l1)]
                    s2 = s[i2:(i2+l2)]
                    naive = s1 == s2
                    hashed = rh.get_hash(i1, l1) == rh.get_hash(i2, l2)

                    if naive == hashed:
                        if naive and hashed: tt += 1
                        if (not naive) and (not hashed): ff += 1
                    else:
                        if naive and (not hashed): tf += 1
                        if (not naive) and hashed: ft += 1
                        print("s1:{0}, s2:{1}, naive_judge:{2}".format(s1, s2, naive))
                        print("h1:{0}, h2:{1}, hashed_judge:{2}".format(rh.get_hash(i1, l1), rh.get_hash(i2, l2), hashed))
    print("total count: {0}".format(cnt))
    print("pass       : {0}".format(tt + ff))
    print(" t/t       : {0}".format(tt))
    print(" f/f       : {0}".format(ff))
    print("fail       : {0}".format(tf + ft))
    print(" t/f       : {0}".format(tf))
    print(" f/t       : {0}".format(ft))

if __name__ == "__main__":
    check()
