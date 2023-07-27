N,M = map(int,input().split())

def harmonic(arr,r):
    result = []

    def harmo(h,index):
        if len(h)==r:
            result.append(h)
            return
        
        for idx,data in enumerate(arr):
            if idx>=index:
                harmo(h+[data],idx)
    
    harmo([],-1)

    return result

lst = list(range(1,N+1))

for r in harmonic(lst,M):
    for v in r:
        print(v,end=' ')
    print()
