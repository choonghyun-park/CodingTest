'''
- NxN 지도
- 길 : 한쪽 끝에서 다른쪽 쯕까지(한 행 or 한 열)
- 경사로 : L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
    조건
        - 높이차이 1
        - L개의 연속된 바닥 보장(같은 높이)

경사로를 놓아서 가능한 길인지 판별하는 방법
- 높이차이는 0 or 1
- 0인 경우는 all_same
- 높이차이가 1인 경우만 고려하면 되는데,
- 높이차이가 존재하는 구역만 잘라서 경사로를 놓을 수 있는지 고려.
- 단, 경사로가 서로 겹치는 경우만 제외해주면 된다. -> 경사로를 관리하는 set 만들기. 


'''
def all_same(line):
    # if all same value, return True
    start = line[0]
    flag = True
    for value in line:
        if value!=start:
            flag = False
            break
    return flag

def diff(line):
    max_num = max(line)
    min_num = min(line)
    return max_num-min_num

def tilt_psb(line):
    for i in range(N-L):
        high = line[i]
        low1 = line[i+1]
        values = line[i+1:]
        if high-low1==1 and all_same(values):
            return True
    return False

def check_tilt(line):
    already_tilt = set()
    # 높이 차이가 존재하는 구간 탐색
    sections = [] # i만 저장. i와 i+1 사이에 차이 존재
    for i,v in enumerate(line):
        if i==len(line)-1:break
        if line[i]!=line[i+1]:
            sections.append(i)
    for i in sections:
        try:
            if line[i]>line[i+1]:
                high = line[i]
                low = line[i+1]
                # i+1:i+1+L 구역이 평평한지 확인
                if diff(line[i+1:i+1+L])==0:
                    for j in range(i+1,i+1+L):
                        if j in already_tilt: return False
                        already_tilt.add(j)

            else:
                high = line[i+1]
                low = line[i]
                # i-N:i 구역이 평평한지 확인
                if diff(line[i-N+1:i+1])==0:
                    for j in range(i-N+1,i+1):
                        if j in already_tilt: return False
                        already_tilt.add(j)
        except:
            return False
    print("tilt line",line)
    return True


N,L = map(int,input().split())
zido = []

for _ in range(N):
    line = list(map(int,input().split()))
    zido.append(line)

# 높이가 모두 같은 경우
# 경사로를 놓을 수 있는 경우

way_cnt_row = 0
# 열
tilt_psbs = []
for row in zido:
    height_diff = diff(row)

    if height_diff==0:
        way_cnt_row+=1
    else:
        tilt_psbs.append(row)

# 행
way_cnt_col = 0
for i in range(N):
    column = []
    for j in range(N):
        column.append(zido[j][i])
    height_diff = diff(column)

    if height_diff==0:
        way_cnt_col+=1
    else:
        tilt_psbs.append(column)

way_cnt_tilt = 0

for line in tilt_psbs:
    if check_tilt(line):
        way_cnt_tilt+=1


way_cnt = way_cnt_row + way_cnt_col + way_cnt_tilt
print("row",way_cnt_row)
print("col",way_cnt_col)
print("tilt",way_cnt_tilt)

print(way_cnt)