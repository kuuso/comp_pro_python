def first_exceeder(arr_, cmp_, strict_exceed=True, left=False):
    # arr:List[T], cmp: T,T -> [-1,0,1]
    N = len(arr_)
    cmp = lambda x,y: cmp_(x,y)
    if not strict_exceed:
        cmp = lambda x,y : -1 if cmp_(x, y) == 0 else cmp_(x, y)
    a = arr_
    if left:
        a = [arr_[N-1-i] for i in range(N)]
    exceeder = [0] * N
    stk = []
    stk.append(0)
    for i in range(1,N):
        while len(stk) > 0:
            top = stk[-1]
            if cmp(a[top],a[i]) < 0:
                exceeder[top] = i
                stk.pop()
                continue
            break
        stk.append(i)
    for i in stk:
        exceeder[i] = N
    
    if left:
        exceeder = [N - 1 - exceeder[N - 1 - i] for i in range(N)]
    
    return exceeder



def naive(arr_, cmp_, strict_exceed=True, left=False):
    N = len(arr_)
    if not left:
        exceeder = [N] * N
        for i in range(N):
            for j in range(i+1,N):
                if strict_exceed and cmp_(arr_[i], arr_[j]) < 0:
                    exceeder[i] = j
                    break
                if (not strict_exceed) and cmp_(arr_[i], arr_[j]) <= 0:
                    exceeder[i] = j
                    break
        return exceeder
    else:
        exceeder = [-1] * N
        for i in range(N):
            for j in reversed(range(0,i)):
                if strict_exceed and cmp_(arr_[i], arr_[j]) < 0:
                    exceeder[i] = j
                    break
                if (not strict_exceed) and cmp_(arr_[i], arr_[j]) <= 0:
                    exceeder[i] = j
                    break
        return exceeder



def main():
    a = [6,5,4,4,3,2,3,4,4,5,7,2,2]
    yn = [True, False]
    for left in yn:
        for strict_exceed in yn:
            res = first_exceeder(a, lambda x,y: 0 if x == y else (1 if x > y else -1), strict_exceed, left)
            gt = naive(a, lambda x,y: 0 if x == y else (1 if x > y else -1), strict_exceed, left)
            print("strict_exceed:{0}, left:{1}, assert:{2}".format(strict_exceed, left, res == gt))

if __name__ == "__main__":
    main()
