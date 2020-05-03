import sys
sys.setrecursionlimit(100000)
import random

def euler_tour_order_io(e, root):
    n = len(e)
    cnt = [0] * n
    euler = []
    stk = []
    stk.append(root)
    while len(stk) > 0:
        now = stk.pop()
        cnt[now] += 1
        euler.append(now)
        if cnt[now] == 1:
            stk.append(now)
            for nxt in e[now]:
                if cnt[nxt] == 0:
                    stk.append(nxt)
    
    return euler

def euler_tour_order_wandering(e, root):
    n = len(e)
    cnt = [0] * n
    parent = [-1] * n
    euler = []
    stk = []
    stk.append(root)
    while len(stk) > 0:
        now = stk.pop()
        cnt[now] += 1
        euler.append(now)
        if cnt[now] == 1:
            if parent[now] != -1: stk.append(parent[now])
            for nxt in e[now]:
                if cnt[nxt] == 0:
                    parent[nxt] = now
                    stk.append(nxt)
    
    return euler



def check():
    N = 12
    parent = [-1, 0, 1, 2, 3, 2, 5, 0, 7, 8, 0, 10]
	# 0 - 1 - 2 - 3 - 4
	#           - 5 - 6
	#   - 7 - 8 - 9
	#   - 10 - 11
    E = [[] for i in range(N)]
    for i in range(N):
        if parent[i] != -1:
            E[parent[i]].append(i)
            E[i].append(parent[i])
    root = 0

    euler_io = euler_tour_order_io(E, root)
    print(euler_io)
    # in and out only
    #   [0, 10, 11, 11, 10, 7, 8, 9, 9, 8, 7, 1, 2, 5, 6, 6, 5, 3, 4, 4, 3, 2, 1, 0]

    euler_wandering = euler_tour_order_wandering(E, root)
    print(euler_wandering)
    # wandering 1 by 1
    #   [0, 10, 11, 10, 0, 7, 8, 9, 8, 7, 0, 1, 2, 5, 6, 5, 2, 3, 4, 3, 2, 1, 0]

if __name__ == "__main__":
    check()
