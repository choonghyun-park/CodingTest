def permutation(arr,r):
    result = []

    def permute(p,index):
        if len(p)==r:
            result.append(p)
            return
        
        for idx, data in enumerate(arr):
            if idx not in index:
                permute(p+[data],index+[idx])
    
    permute([],[])

    return result

lst = list(range(5))
result = permutation(lst,3)
for r in result:
    print(r)