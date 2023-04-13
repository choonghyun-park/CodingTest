heights = []
for _ in range(9):
    inp = int(input())
    heights.append(inp)

def combination(lst,r):

    results = []
    def combinate(c,index):
        if len(c)==r:
            results.append(c)
            return
        
        for idx,data in enumerate(lst):
            if idx>index:
                combinate(c+[data],idx)

    combinate([],-1)

    return results


# heigths, 7개를 뽑는 조합에서 합이 100인 경우 찾아서 오름차순 출력
for result in combination(heights,7):
    if sum(result)==100:
        result.sort()
        for v in result:
            print(v)
        break
