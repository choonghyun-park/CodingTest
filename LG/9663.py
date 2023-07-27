N = int(input())

# 세로, 가로 각각 겹치는 queen이 있으면 안됨.
# 대각선으로도 겹치는 queen이 있으면 안됨.
def print_chess(p):
    line = [0]*N
    for q in p:
        line[q]=1
        print(line)
        line[q]=0
    print()

def permutation(arr,r):
    # result = []

    def is_promising(p,queen):
    
        for i,data in enumerate(p):
            q = (i,data)
            # assert q[0]!=queen[0]
            # assert q[1]!=queen[1]
            if abs(q[0]-queen[0])==abs(q[1]-queen[1]):
                return False
        return True


    def permute(p,index):
        if len(p)==r:
            global cnt
            cnt+=1
            # result.append(p)
            # print_chess(p)
            return
        
        for idx,data in enumerate(arr):
            if idx not in index:
                queen = (len(p),data)
                if is_promising(p,queen):
                    permute(p+[data],index+[idx])

    permute([],[])

    return 

lst = list(range(N))

cnt = 0
permutation(lst,N)

# print(len(res))
print(cnt)