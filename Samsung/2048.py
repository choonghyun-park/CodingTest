import copy

N = int(input()) # 보드의 크기 (1 <= N <= 20)

board = [] # 2차원 배열
for _ in range(N):
    line = list(map(int,input().split()))
    board.append(line)


def move(status,direction):
    status_next = {}
    board_next = []
    round_next = status["round"]+1
    board_now = status["board"]

    # 대칭이동
    lines = copy.deepcopy(board_now)
    if direction=="up":
        # 우하향 대각선 대칭
        for r in range(N):
            for c in range(N):
                if r<=c:
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[c][r]
                lines[r][c] = pos_2
                lines[c][r] = pos_1
    elif direction=="down":
        # 좌하양 대각선 대칭
        for r in range(N):
            for c in range(N):
                if r+c>=N-1:
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[N-1-c][N-1-r]
                lines[r][c] = pos_2
                lines[N-1-c][N-1-r] = pos_1
    elif direction=="left":
        pass
    elif direction=="right":
        for r in range(N):
            for c in range(N):
                if c>=int(N/2):
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[r][N-1-c]
                lines[r][c] = pos_2
                lines[r][N-1-c] = pos_1
    # left 상황이라고 가정
    for line in lines:
        first = None
        second = None
        # line을 queue로 사용하여, 2개 수를 뽑고, 만약 2개 수가 연속으로 같은 값이면 더하기.
        line_result = []
        while(line):
            first = line.pop(0)
            if first==0: 
                continue
            else:
                if len(line)==0:
                    line_result.append(first)
                while(line):
                    second = line.pop(0)
                    if second==0:
                        if len(line)==0:
                            line_result.append(first)
                        continue
                    else:
                        if first==second:
                            line_result.append(first+second)
                            break
                        else:
                            line_result.append(first)
                            if len(line)==0:
                                line_result.append(second)
                            first = second
                            continue
        zeros = N-len(line_result)
        for _ in range(zeros):
            line_result.append(0)
        assert len(line_result)==N
        board_next.append(line_result)
    assert len(board_next)==N
    
    # 다시 대칭이동
    lines = copy.deepcopy(board_next)
    if direction=="up":
        # 우하향 대각선 대칭
        for r in range(N):
            for c in range(N):
                if r<=c:
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[c][r]
                lines[r][c] = pos_2
                lines[c][r] = pos_1
    elif direction=="down":
        # 좌하양 대각선 대칭
        for r in range(N):
            for c in range(N):
                if r+c>=N-1:
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[N-1-c][N-1-r]
                lines[r][c] = pos_2
                lines[N-1-c][N-1-r] = pos_1
    elif direction=="left":
        pass
    elif direction=="right":
        for r in range(N):
            for c in range(N):
                if c>=int(N/2):
                    continue
                pos_1 = lines[r][c]
                pos_2 = lines[r][N-1-c]
                lines[r][c] = pos_2
                lines[r][N-1-c] = pos_1
    board_next = copy.deepcopy(lines)

    status_next["board"] = board_next
    status_next["max_block"] = board_max(board_next)
    status_next["round"] = round_next

    return status_next

def board_max(board):
    max_num = 0
    for line in board:
        max_line = max(line)
        if max_line>max_num:
            max_num = max_line
    return max_num

def print_board(board):
    for line in board:
        print(line)
    print()

queue = []
init_status = {}
init_status["board"] = copy.deepcopy(board)
init_status["max_block"] = board_max(board)
init_status["round"] = 0

# test
# print("======test line======")
# print_board(init_status['board'])
# print_board(move(init_status,"up")['board'])
# exit()

queue.append(init_status)

max_block = 0
round_cnt = -1

while(queue):
    # status in now
    status_now = queue.pop(0)
    if status_now['round']>round_cnt:
        round_cnt=status_now['round']
    #     print("=========== round : {} ===========".format(round_cnt))
    # print_board(status_now['board'])

    # possible directions
    directions = ["up","down","left","right"]

    for direction in directions:
        status_now_copy = copy.deepcopy(status_now)
        # status in next
        status_next = {}
        status_next = move(status_now_copy,direction)
        
        if status_next["round"] >= 5:
            if status_next["max_block"] > max_block:
                max_block = status_next["max_block"]
        else:
            queue.append(status_next)

print(max_block)


