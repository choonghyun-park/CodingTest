N,M = map(int,input().split())

def combination(arr,r):
    result = []

    def combinate(c,index):
        if len(c)==r:
            result.append(c)
            return
        
        for idx,data in enumerate(arr):
            if idx>index:
                combinate(c+[data],idx)
        
    combinate([],-1)

    return result
    
lst = list(range(1,N+1))
for r in combination(lst,M):
    for v in r:
        print(v,end=' ')
    print()

