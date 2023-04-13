# N : 세로, N >= 3
# M : 가로, M <= 10
N,M = map(int,input().split())

loc_R = None
loc_B = None
loc_O = None

memory = set()

def up(status):
    # current status
    map_cur = status["map"]
    loc_r_cur = status["loc_r"]
    loc_b_cur = status["loc_b"]
    statement = status["statement"] # "no-goal","R-goal","B-goal"
    moves = status["moves"]

    # next status
    map_next = map_cur.copy()
    loc_r_next = None
    loc_b_next = None
    moves_next = moves+1
    status_next = {}

    if loc_r_cur[0] < loc_b_cur[0]: # R이 먼저 움직임
        goal_r = loc_r_cur[0]-1
        while(goal_r>=0):
            next = map_cur[goal_r][loc_r_cur[1]]
            if next=='.':
                goal_r-=1
                continue
            elif next=='#' or next=='B':
                loc_r_next = (goal_r+1,loc_r_cur[1])
                line = map_next[loc_r_cur[0]]
                map_next[loc_r_cur[0]] = change_line(line,loc_r_cur[1],'.') # str, index, char
                line = map_next[loc_r_next[0]]
                map_next[loc_r_next[0]] = change_line(line,loc_r_next[1],'R')
            elif next=='O':
                loc_r_next = loc_r_cur
                map_next = map_cur
                get_O_r = True
            break
        assert loc_r_next is not None 
        goal_b = loc_b_cur[0]-1
        while(goal_b>=0):
            next = map_cur[goal_b][loc_b_cur[1]]
            if next=='.':
                goal_b-=1
                continue
            elif next=='#' or next=='R':
                loc_b_next = (goal_b+1,loc_b_cur[1])
                line = map_next[loc_b_cur[0]]
                map_next[loc_b_cur[0]] = change_line(line,loc_b_cur[1],'.') # str, index, char
                line = map_next[loc_b_next[0]]
                map_next[loc_b_next[0]] = change_line(line,loc_b_next[1],'B')
            elif next=='O':
                loc_b_next = loc_b_cur
                map_next = map_cur
                get_O_b = True
            break
        assert loc_b_next is not None 

        if get_O_b:
            statement_next = "B-goal"
        elif get_O_r:
            statement_next = "R-goal"
        else:
            statement_next = "no-goal"
            
        # Make status
        status_next["map"] = map_next
        status_next["loc_r"] = loc_r_next
        status_next["loc_b"] = loc_b_next
        status_next["statement"] = statement_next
        status_next["next_moves"] = moves_next
    
    else: # B가 먼저 움직임
        goal_b = loc_b_cur[0]-1
        while(goal_b>=0):
            next = map_cur[goal_b][loc_b_cur[1]]
            if next=='.':
                goal_b-=1
                continue
            elif next=='#' or next=='R':
                loc_b_next = (goal_b+1,loc_b_cur[1])
                line = map_next[loc_b_cur[0]]
                map_next[loc_b_cur[0]] = change_line(line,loc_b_cur[1],'.') # str, index, char
                line = map_next[loc_b_next[0]]
                map_next[loc_b_next[0]] = change_line(line,loc_b_next[1],'B')
            elif next=='O':
                # 어짜피 가지 못하는 경우이므로 기존 맵과 statement 를 반환하고 종료.
                statement_next = "B-goal"
                status_next['map']=map_cur
                status_next['loc_r']=loc_r_cur
                status_next['loc_b']=loc_r_cur
                status_next['statement']=statement_next
                status_next["next_moves"] = moves_next
                return status_next
            break
        assert loc_b_next is not None 
        goal_r = loc_r_cur[0]-1
        while(goal_r>=0):
            next = map_cur[goal_r][loc_r_cur[1]]
            if next=='.':
                goal_r-=1
                continue
            elif next=='#' or next=='B':
                loc_r_next = (goal_r+1,loc_r_cur[1])
                line = map_next[loc_r_cur[0]]
                map_next[loc_r_cur[0]] = change_line(line,loc_r_cur[1],'.') # str, index, char
                line = map_next[loc_r_next[0]]
                map_next[loc_r_next[0]] = change_line(line,loc_r_next[1],'R')
            elif next=='O':
                # 위에서 B가 먼저 움직였으므로, R만 goal에 도달하는 경우
                statement_next = "R-goal"
                status_next['map']=map_cur
                status_next['loc_r']=loc_r_cur
                status_next['loc_b']=loc_r_cur
                status_next['statement']=statement_next
                status_next["next_moves"] = moves_next
                return status_next
            break
        assert loc_r_next is not None 

        # Make status : R, B 모두 움직인 경우.
        statement_next = "no-goal"
        status_next['map']=map_next
        status_next['loc_r']=loc_r_next
        status_next['loc_b']=loc_b_next
        status_next['statement']=statement_next
        status_next["next_moves"] = moves_next
        return status_next
    
def move(status,direction):
    # current status
    map_cur = status["map"]
    loc_r_cur = status["loc_r"]
    loc_b_cur = status["loc_b"]
    statement = status["statement"] # "no-goal","R-goal","B-goal"
    moves = status["moves"]

    # next status
    map_next = map_cur.copy()
    loc_r_next = None
    loc_b_next = None
    moves_next = moves+1
    status_next = {}
    statement_next = "no-goal"

    # choose increment from direction
    incre = None
    first = 'B'
    if direction=="up": 
        incre = (-1,0)
        if loc_r_cur[0]<loc_b_cur[0]:
            first = 'R'
    elif direction=="down": 
        incre = (1,0)
        if loc_r_cur[0]>loc_b_cur[0]:
            first = 'R'

    elif direction=="left": 
        incre = (0,-1) 
        if loc_r_cur[1]<loc_b_cur[1]:
            first = 'R'
    elif direction=="right": 
        incre = (0,1)
        if loc_r_cur[1]>loc_b_cur[1]:
            first = 'R'
    assert incre is not None


    if first=='R': # R이 먼저 움직임
        goal_r = (loc_r_cur[0]+incre[0],loc_r_cur[1]+incre[1])
        while(in_map(goal_r)):
            next = map_next[goal_r[0]][goal_r[1]]
            if next=='.':
                goal_r = (goal_r[0]+incre[0],goal_r[1]+incre[1])
                continue
            elif next=='#' or next=='B':
                loc_r_next = (goal_r[0]-incre[0],goal_r[1]-incre[1])
                line = map_next[loc_r_cur[0]]
                map_next[loc_r_cur[0]] = change_line(line,loc_r_cur[1],'.') # str, index, char
                line = map_next[loc_r_next[0]]
                map_next[loc_r_next[0]] = change_line(line,loc_r_next[1],'R')
            elif next=='O':
                loc_r_next = loc_r_cur
                line = map_next[loc_r_cur[0]]
                map_next[loc_r_cur[0]] = change_line(line,loc_r_cur[1],'.') # str, index, char
                statement_next = "R-goal"
            break
        assert loc_r_next is not None 

        goal_b = (loc_b_cur[0]+incre[0],loc_b_cur[1]+incre[1])
        while(in_map(goal_b)):
            next = map_next[goal_b[0]][goal_b[1]]
            if next=='.':
                goal_b = (goal_b[0]+incre[0],goal_b[1]+incre[1])
                continue
                
            elif next=='#' or next=='R':
                loc_b_next = (goal_b[0]-incre[0],goal_b[1]-incre[1])
                line = map_next[loc_b_cur[0]]
                map_next[loc_b_cur[0]] = change_line(line,loc_b_cur[1],'.') # str, index, char
                line = map_next[loc_b_next[0]]
                map_next[loc_b_next[0]] = change_line(line,loc_b_next[1],'B')
            elif next=='O':
                
                loc_b_next = loc_b_cur
                line = map_next[loc_b_cur[0]]
                map_next[loc_b_cur[0]] = change_line(line,loc_b_cur[1],'.') # str, index, char
                statement_next='B-goal'
            break
        assert loc_b_next is not None 

        # Make status
        status_next["map"] = map_next
        status_next["loc_r"] = loc_r_next
        status_next["loc_b"] = loc_b_next
        status_next["statement"] = statement_next
        status_next["moves"] = moves_next
        return status_next

    
    else: # B가 먼저 움직임
        goal_b = (loc_b_cur[0]+incre[0],loc_b_cur[1]+incre[1])
        while(in_map(goal_b)):
            next = map_next[goal_b[0]][goal_b[1]]
            if next=='.':
                goal_b = (goal_b[0]+incre[0],goal_b[1]+incre[1])
                continue
            elif next=='#' or next=='R':
                loc_b_next = (goal_b[0]-incre[0],goal_b[1]-incre[1])
                line = map_next[loc_b_cur[0]]
                map_next[loc_b_cur[0]] = change_line(line,loc_b_cur[1],'.') # str, index, char
                line = map_next[loc_b_next[0]]
                map_next[loc_b_next[0]] = change_line(line,loc_b_next[1],'B')
            elif next=='O':
                # 어짜피 가지 못하는 경우이므로 기존 맵과 statement 를 반환하고 종료.
                statement_next = "B-goal"
                status_next['map']=map_cur
                status_next['loc_r']=loc_r_cur
                status_next['loc_b']=loc_r_cur
                status_next['statement']=statement_next
                status_next["moves"] = moves_next
                return status_next
            break
        assert loc_b_next is not None 

        goal_r = (loc_r_cur[0]+incre[0],loc_r_cur[1]+incre[1])
        while(in_map(goal_r)):
            next = map_next[goal_r[0]][goal_r[1]]
            if next=='.':
                goal_r = (goal_r[0]+incre[0],goal_r[1]+incre[1])
                continue
            elif next=='#' or next=='B':
                loc_r_next = (goal_r[0]-incre[0],goal_r[1]-incre[1])
                line = map_next[loc_r_cur[0]]
                map_next[loc_r_cur[0]] = change_line(line,loc_r_cur[1],'.') # str, index, char
                line = map_next[loc_r_next[0]]
                map_next[loc_r_next[0]] = change_line(line,loc_r_next[1],'R')
            elif next=='O':
                # 위에서 B가 먼저 움직였으므로, R만 goal에 도달하는 경우
                statement_next = "R-goal"
                status_next['map']=map_cur
                status_next['loc_r']=loc_r_cur
                status_next['loc_b']=loc_r_cur
                status_next['statement']=statement_next
                status_next["moves"] = moves_next
                return status_next
            break
        assert loc_r_next is not None 

        # Make status : R, B 모두 움직인 경우.
        statement_next = "no-goal"
        status_next['map']=map_next
        status_next['loc_r']=loc_r_next
        status_next['loc_b']=loc_b_next
        status_next['statement']=statement_next
        status_next["moves"] = moves_next
        return status_next

def down(map):
    pass

def left(map):
    pass

def right(map):
    pass

def check_movable(map,action):
    x_r = action[0]
    y_r = action[1]
    x_b = action[2]
    y_b = action[3]

    if x_r<0 or x_r>=N or y_r<0 or y_r>=M:
        return False
    if x_b<0 or x_b>=N or y_b<0 or y_b>=M:
        return False
    if map[x_r][y_r]=='#' and map[x_b][y_b]=='#':
        return False
    else:
        return True

def print_map(map):
    for line in map:
        print(line)
    print()

def change_line(str,index,char): # str, index, char
    str1 = str[:index]
    str2 = str[index+1:]
    ret = str1+char+str2
    return ret

def in_map(loc):
    x = loc[0]
    y = loc[1]

    if x<0 or x>=N or y<0 or y>=M:
        return False
    else:
        return True

map = []
init_status = {}
for n in range(N):
    line = input()  # str
    '''
    '.' : 빈칸 
    '#' : 공이 이동할 수 없는 장애물 또는 벽
    'O' : 구멍의 위치
    'R' : 빨간 구슬의 위치
    'B' : 파란 구슬의 위치
    '''
    map.append(line)
    if 'R' in line:
        init_status["loc_r"] = (n, line.index('R')) # index_row, index_column
    if 'B' in line:
        init_status["loc_b"] = (n, line.index('B')) # index_row, index_column
    if 'O' in line:
        init_status["loc_o"] = (n, line.index('O')) # index_row, index_column
init_status["map"]=map
init_status["statement"]="init" # no-goal, R-goal, B-goal
init_status["moves"]=0 # 몇 번 이동했는지.
# 갈 수 있는 방향이 상, 하, 좌, 우 중에 몇가지가 있을 것이고, 그 경우에 대해서 다음 경우의 수를 탐색한다.
# 이는 BFS로 탐색하다가, 가장 탐지 깊이가 낮은 상황에서 알고리즘을 중지시킨다.
# 상, 하, 좌, 우로 갔을 때 결과값이 나오는 함수를 각각 구현한다.
# B 의 경우도 따로 상태를 체크해서 만약 진행해서 B가 골에 들어가면 그 경우는 제외시킨다.

# test
# print_map(init_status['map'])
# print_map(up(init_status)["map"])
# print_map(move(init_status,"up")["map"])
# exit()

queue = []
queue.append(init_status)
final_moves = None
moves_round = 0

while(queue):
    status = queue.pop(0)
    actions = []
    pos_actions = []

    # pass same status
    check_status = (status['loc_r'][0],status['loc_r'][1],status['loc_b'][0],status['loc_b'][1])
    if check_status in memory:
        continue
    else:
        memory.add(check_status)

    # print_map(status['map'])
    # if status['moves']>moves_round:
    #     moves_round = status['moves']
    #     print("======================================")
    # max moves is 10
    if status["moves"]>10:
        continue

    # find possible states
    up_1 = (status["loc_r"][0]-1,status["loc_r"][1],status["loc_b"][0]-1,status["loc_b"][1],"up")
    down_1 = (status["loc_r"][0]+1,status["loc_r"][1],status["loc_b"][0]+1,status["loc_b"][1],"down")
    left_1 = (status["loc_r"][0],status["loc_r"][1]-1,status["loc_b"][0],status["loc_b"][1]-1,"left")
    right_1 = (status["loc_r"][0],status["loc_r"][1]+1,status["loc_b"][0],status["loc_b"][1]+1,"right")
    actions = [up_1,down_1,left_1,right_1]

    # 최소 한 칸은 이동할 수 있는 방향만 선택.
    for action in actions:
        if check_movable(status["map"],action):
            pos_actions.append(action)
    
    for action in pos_actions:
        status_next = move(status,action[4])

        if status_next["statement"] == "R-goal":
            final_moves = status_next["moves"]
            break
        elif status_next["statement"] == "B-goal":
            continue
        elif status_next["statement"] == "no-goal":
            queue.append(status_next)
    

    if final_moves is not None:
        break

if final_moves is None:
    print(-1)
else:
    if final_moves>10:
        print(-1)
    else:
        print(final_moves)    
    




