from collections import deque

def slide_max_index(a, K, cmp, right_preffered=True):
    # arr:List[T], cmp: T,T -> [-1,0,1]
    # returns idx of max in [i - K + 1, i] (closed-closed) fpr each i in [0, N)
    N = len(a)
    max_idx = [0] * N # until N-1 th member's entrance.
    deq = deque()

    for i in range(0,N):
        while len(deq) > 0 and deq[0] <= i - K : deq.popleft()
        while len(deq) > 0 and cmp(a[deq[-1]], a[i]) < 0 : deq.pop()
        if right_preffered:
            while len(deq) > 0 and cmp(a[deq[-1]], a[i]) <= 0 : deq.pop()
        deq.append(i)
        max_idx[i] = deq[0]
    
    return max_idx

def naive(a, K, cmp, right_preffered=True):
    N = len(a)
    max_idx = [0] * N
    for i in range(N):
        ma = None
        idx = -1
        for j in range(i-K+1, i+1):
            if j < 0: continue
            if (ma is None) or cmp(ma, a[j]) < 0 or (right_preffered and cmp(ma, a[j]) == 0):
                ma = a[j]
                idx = j
        max_idx[i] = idx
    return max_idx

def main():
    a = [6,5,4,4,3,2,3,4,4,5,7,2,2]
    yn = [True, False]
    ks = [1,3,6]
    cmp = lambda x,y: 0 if x == y else (1 if x > y else -1)
    for right_preffered in yn:
        for K in ks:
            res = slide_max_index(a, K, cmp, right_preffered)
            gt = naive(a, K, cmp, right_preffered)
            print("K:{0}, right_preffered:{1}, assert:{2}, res:{3}".format(K, right_preffered, res == gt, res))

if __name__ == "__main__":
    main()
