N = int(input()) # 3<=N<=20
queue = []
seats = [[0]*N for _ in range(N)]
for _ in range(N*N):
    inp = list(map(int,input().split()))
    queue.append(inp)

def out_of_range(r,c):
    return r<0 or c<0 or r>=N or c>=N

def print_seats(seats):
    for r in range(N):
        for c in range(N):
            print(seats[r][c]['st'], end=' ')
        print()
# 조건 1, 2, 3의 순서로 가능한 자리를 추린다.

# 처음 자리배정은 무조건 (1,1)  
# 주의 : 문제에서 설명은 index+1이지만, 구현은 index 기준.
init_st_info = queue.pop(0)
init_st = init_st_info.pop(0)
init_student = {"st":init_st,"favor":init_st_info} # {"st":4,"favor":[2,5,1,7]}
seats[1][1]=init_student


neighbors = [(-1,0),(1,0),(0,-1),(0,1)]

while(queue):
    st_info = queue.pop(0)
    st = st_info.pop(0)
    student = {"st":st,"favor":st_info} 

    score_1_max = 0
    score_2_max = 0
    pos_seats = []

    for r in range(N):
        for c in range(N):
            # 이미 채워져있는 자리인 경우 패스
            if seats[r][c]!=0:
                continue
            score_1 = 0
            score_2 = 0

            # 인접한 자리에서 score_1 조사
            for n in neighbors:
                nr = r+n[0]
                nc = c+n[1]
                if out_of_range(nr,nc):
                    continue
                if seats[nr][nc]==0:
                    score_2 += 1
                    continue

                n_student = seats[nr][nc]
                if n_student['st'] in student["favor"]:
                    score_1 += 1
            if score_1 == score_1_max:
                if len(pos_seats)==0:
                    pos_seats.append((r,c))
                    score_2_max = score_2
                # score_1이 동률인 경우, score_2가 높은지로 결정
                elif len(pos_seats)>0:
                    if score_2 == score_2_max:
                        pos_seats.append((r,c))
                    elif score_2 > score_2_max:
                        pos_seats = []
                        pos_seats.append((r,c))
                        score_2_max = score_2
                    else: # score_1은 같지만, score_2가 낮아서 제외.
                        pass
            elif score_1 > score_1_max:
                pos_seats = [] # 비워주기
                pos_seats.append((r,c)) # 자리 추가
                score_1_max = score_1
                score_2_max = score_2
    


    if len(pos_seats)==1:
        pos_seat = pos_seats.pop(0)
    elif len(pos_seats)>1:
        # 3번 : r,c가 가장 작은 값 선택 
        min_pos_seat = pos_seats.pop(0)
        while(pos_seats):
            pos_seat = pos_seats.pop(0)
            if pos_seat[0] < min_pos_seat[0]:
                min_pos_seat = pos_seat
            elif pos_seat[0] == min_pos_seat[0]:
                if pos_seat[1] < min_pos_seat[1]:
                    min_pos_seat = pos_seat
        # finally
        pos_seat = min_pos_seat
    # 자리 배정 완료.
    seats[pos_seat[0]][pos_seat[1]] = student

# 만족도 조사
satisfy = 0
for r in range(N):
    for c in range(N):
        satisfy_local = 0
        student = seats[r][c]
        for n in neighbors:
            nr = r+n[0]
            nc = c+n[1]
            if out_of_range(nr,nc):
                continue
            assert seats[nr][nc]!=0
            n_student = seats[nr][nc]
            if n_student['st'] in student['favor']:
                satisfy_local+=1

        # 최종 만족도 합산
        if satisfy_local==1:
            satisfy+=1
        elif satisfy_local==2:
            satisfy+=10
        elif satisfy_local==3:
            satisfy+=100
        elif satisfy_local==4:
            satisfy+=1000

        '''만족도
        인접 학생수 : 만족도
        0 : 0
        1 : 1
        2 : 10
        3 : 100
        4 : 1000
        '''

# print_seats(seats)

print(satisfy)