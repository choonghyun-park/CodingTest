import copy

def solution(grid, d, k):
    answer = 0
    
    '''
    격자 공간 : n x m
    d : 경사수열(1차원 정수배열)
    k : 경사수열 반복횟수
    경사 = 다음칸 - 현재칸 
    grid : 격자 칸의 높이를 담은 2차원 정수 배열
    
    return : 격자 내에서 조건을 만족하는 경로의 수
             단, 10^9+7로 나눈 나머지를 반환
    '''
    global n,m
    n = len(grid)       # row
    m = len(grid[0])    # column
    
    moves = [(-1,0),(1,0),(0,-1),(0,1)] # 상,하,좌,우 
    full_d = []
    for _ in range(k):
        full_d += d
        
    # dynamic programming
    global memory
    memory = []
    for _ in range(len(full_d)):
        memory.append({})
    '''
    memory[idx] : info
    info[pos] : case_num
    '''
    
        
    for r in range(n):
        for c in range(m):
            init_status = {"pos":(r,c),"idx":0,"path":[]}
            queue = []
            queue.append(init_status)
            paths = []        
            while(queue):
                status = queue.pop(0)
                pos = status["pos"]
                idx = status["idx"]
                
                # Use dynamic memory
                assert idx < len(memory)
                if pos in memory[idx]:
                    answer+=memory[idx][pos]
                    continue
                
                # end misison
                if idx==len(full_d)-2:
                    answer+=1
                    path_copy = copy.deepcopy(status["path"])
                    paths.append(path_copy)
                    continue
                
                for move in moves:
                    dr = move[0]
                    dc = move[1]
                    next_pos = (pos[0]+dr,pos[1]+dc)
                    # check out of range
                    if outOfRange(next_pos[0],next_pos[1]):
                        continue
                    
                    tilt = grid[next_pos[0]][next_pos[1]] - grid[pos[0]][pos[1]]
                    if tilt==full_d[idx]:
                        next_path = copy.deepcopy(status["path"])
                        next_path.append(next_pos)
                        next_status = {"pos":next_pos,"idx":idx+1,"path":next_path}
                        queue.append(next_status)
                
                recordPath(paths)        
    
    # 최종 나머지 반환
    answer = answer%(pow(10,9)+7)    
    return answer

def outOfRange(r,c):
    return r<0 or r>=n or c<0 or c>=m

def recordPath(paths):
    global memory
    # info = memory[idx]
    # case_num = info[pos]
    pos_flag = True
    for path in paths:
        for idx,pos in enumerate(path):
            assert idx < len(memory)
            info = memory[idx] # dict
            if pos not in info and pos_flag:
                info[pos]=0
                pos_flag = False
            elif pos in info and not pos_flag:
                info[pos]+=1                
    
    return
            
    
        
    
    