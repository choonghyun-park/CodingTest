N,M = map(int,input().split())

def pi(arr,r):
    result = []

    def pi_operate(p,index):
        if len(p)==r:
            result.append(p)
            return

        for idx,data in enumerate(arr):
            pi_operate(p+[data],index+[idx]) # 순열에 있던 if문만 빼줌.
        
    pi_operate([],[])

    return result

lst = list(range(1,N+1))

for r in pi(lst,M):
    for v in r:
        print(v,end=' ')
    print()
