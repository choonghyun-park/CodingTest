'''
- NxN 체스판
- 사용하는 말의 개수 : k개
- 체스판 색 : 흰색, 빨간색, 파란색 중 하나
- K개의 말은 1 ~ K 번까지 번호가 매겨져 있음
- 이동방향 : 위, 아래, 왼, 오 중 하나로 FIx

칸의 색에 따라서
- 흰색 : 그대로 쌓음
- 빨간 : 굴러온 돌만 순서 뒤집고, 그대로 쌓기
- 파랑 : 이동방향 반대로 해서 이동. 양쪽 다 파랑이면 그냥 정지. 체스판 바깥은 다 파란색

입력(결론적으로 주어진 것)
- 체스판의 크기 : N
- 말의 개수 : K
- 말의 위치 : 행, 열 이동방향
    행, 열 : 1부터 시작
    이동방향
        1 : 오른
        2 : 왼
        3 : 위
        4 : 아래
- 칸의 색 : 
    0 : 흰색
    1 : 빨강
    2 : 파랑


출력
- 게임이 종료되는 턴의 번호

종료 조건 : 말이 4개 이상 쌓이면 종료

'''
import copy

N, K = map(int, input().split())

def reverse_dir(dir):
    if dir==1:return 2
    elif dir==2:return 1
    elif dir==3:return 4
    elif dir==4:return 3

def check_finish(metadata):
    for horse_list in metadata.values():
        if len(horse_list)>=4:
            return True
    return False

def reversed_list(lst):
    ret = []
    while(lst):
        ret.append(lst.pop())
    return ret

# 체스판 정보
board = [] # blue를 포함하기 위해서 그대로 사용.
board.append([2] * (N+2))

for i in range(N):
    line = list(map(int,input().split()))
    line = [2]+line
    line.append(2)
    board.append(line)

board.append([2] * (N+2))

# 말 정보
horses = []
metadata = {}
for i in range(K):
    row, col, dir = map(int,input().split())
    horse = {"row":row, "col":col, "dir":dir}
    horses.append(horse)

    metadata[(row,col)]=[i+1] # 말의 번호임. idx 아님. 1~K

directions = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} # 오른, 왼, 위, 아래

turns = 0
while(turns<=1000):
    turns+=1
    # horse 순서대로 이동
    for i,horse in enumerate(horses):
        # 현재 horse의 정보
        row = horse["row"]
        col = horse["col"]
        dir = horse["dir"]
        dir_tuple = directions[dir]
        cur_color = board[row][col]
        horse_num = i+1
        
        # 다음 이동할 위치
        next_row = row+dir_tuple[0]
        next_col = col+dir_tuple[1]

        # 다음 이동할 색상
        next_color = board[next_row][next_col]

        if next_color==2: # 파랑
            rev_dir = reverse_dir(dir)              # 반대 방향 dir
            rev_row = row-dir_tuple[0]              # 반대 방향 row, col
            rev_col = col-dir_tuple[1]
            rev_color = board[rev_row][rev_col]
            horse["dir"]=rev_dir
            if rev_color==2: continue               # stop
            else:
                next_row = rev_row                  # go backward
                next_col = rev_col
                next_color = rev_color
        cur_stack = copy.deepcopy(metadata[(row,col)])  # 말이 쌓인 상태 확인
        left_stack = []                                 # 남겨진 말
        for h in cur_stack:
            if h==horse_num:
                break
            else:
                left_stack.append(cur_stack.pop(0))     # 남겨질 말 결정
        moved_stack = copy.deepcopy(cur_stack)          # 이동할 말 결정
        
        if next_color == 1:
            moved_stack = reversed_list(moved_stack)    # 움직일 말의 순서 거꾸로 하기

        if len(left_stack)==0:                          # 현재 칸에 남은 말이 없는 경우
            del(metadata[(row,col)])
        else:
            metadata[(row,col)] = left_stack            # 현재 칸에 남은 말이 있는 경우

        if (next_row,next_col) in metadata:             # 이동할 말을 metadata에 담기
            metadata[(next_row,next_col)] += moved_stack
        else:
            metadata[(next_row,next_col)] = moved_stack

        for h in moved_stack:
            horses[h-1]["row"] = next_row               # 이동한 말들의 row, col 정보 업데이트.
            horses[h-1]["col"] = next_col

        # if turns<10:
        #     print("metadata in turns",turns,"horse",horse_num,"dir",dir,":")
        #     print(metadata)
        if check_finish(metadata):break

    # if turns<10:
    #     print(turns,":",metadata)
    #     print()
    
    if check_finish(metadata):break


if turns>1000:
    print(-1)
else:
    print(turns)
        
        

       

