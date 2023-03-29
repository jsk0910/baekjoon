import sys
sys.setrecursionlimit(10**9)

tree = []

while 1:
    try:
        num = int(input())
        tree.append(num)
    except:
        break

def postorder(lo, hi):
    if lo > hi:
        return
    mid = hi + 1

    for i in range(lo+1, hi+1):
        if tree[lo] < tree[i]:
            mid = i
            break

    postorder(lo + 1, mid - 1)
    postorder(mid, hi)
    print(tree[lo])

postorder(0, len(tree) - 1)