# print nPr
N,R = map(int,input().split())

def do_something(perm):
    print(perm)

lst = list(range(N))

visited = [False] * N
result = []

def dfs_permutation(perm): #queue
    if len(perm) == R: # R개 모두 선택하여 종료
        result.append(list(perm))
        do_something(perm)
        return
    for i,val in enumerate(lst):
        if visited[i]: # 방문한 노드인 경우 제외
            continue
        # i번째 노드를 포함하여 재귀 호출
        perm.append(val)
        visited[i] = True
        dfs_permutation(perm)
        # i번째 노드 삭제
        perm.pop()
        visited[i] = False

dfs_permutation([])