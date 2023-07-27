N,M = map(int, input().split())

def permutation(arr,r):
    result = []

    def permutate(p,index):
        if len(p)==r:
            result.append(p)
            return
    
        for idx,data in enumerate(arr):
            if idx not in index:
                permutate(p+[data],index+[idx])
            
    permutate([],[])

    return result

lst = list(range(1,N+1))
for r in permutation(lst,M):
    for v in r:
        print(v,end=' ')
    print()
