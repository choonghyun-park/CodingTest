N,R = map(int,input().split())
lst = list(range(N))

# print nCr
def do_something(comb):
    print(comb)


def dfs_combination(n,r,comb, depth): # queue, int
    if len(comb) == r: # N개를 모두 선택한 경우
        do_something(comb)
        return
    elif depth == n:
        return
    
    # 현재 depth의 값 포함 재귀 호출
    comb.append(lst[depth])
    dfs_combination(n,r,comb, depth+1)

    # 현재 depth의 값 미포함 재귀 호출
    comb.pop() # popleft 아니고, 방금 넣은걸 빼는 pop임.
    dfs_combination(n,r,comb, depth+1)

dfs_combination(N,R,[],0)


