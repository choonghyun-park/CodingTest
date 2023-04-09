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

lst = list(range(5))

for r in combination(lst,3):
    print(r)