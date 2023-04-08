# Notion
삼성 SW 역량 테스트 기초 유형별로 핵심만 정리해보려 한다.

## 빈출 유형 정리
* 2차원 배열을 이용한 구현
* 완전 탐색(브루트 포스)
* BFS
* DFS
* 순열
* 조합

## 참고 포스팅
[포스팅 1](https://kimjingo.tistory.com/205)


## BFS
삼성 코테에서 가장 빈출 유형이라고 하며, 일반적으로 dx, dy 를 따로 튜플로 정하는 경우가 많은데, 나는 (dx,dy)로 묶은 후에 for문을 사용해서 하나씩 하는 방법이 더 익숙하다. \
deque를 사용해서 구현할 수도 있고, 삼성 코테도 deque는 사용할 수 있다지만, list를 사용하는 것이 더 깔끔한 것 같아서, 이 방법으로 구현해본다.
```py
neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
N = int(input())
init_x, init_y = map(int,input().split())

def out_of_range(x,y):
    # x, y 모두 range(N)에 들어오는지 확인
    return x<0 or y<0 or x>=N or y>=N

def do_something(x,y,order):
    print("Visiting {}: ({},{})".format(order,x,y))

def bfs(x,y):
    queue = []
    queue.append((x,y))
    visited = [[False] * N for _ in range(N)] # NxN 격자의 경우
    visited[x][y] = True
    order = 0

    while queue:
        x,y = queue.pop(0)
        # 만약 최초 노드에서도 해아하는 것이 있다면.
        if order==0:
            order+=1
            do_something(x,y,order)
        # search neightbors and append to queue
        for n in neighbors:
            nx = x+n[0]
            ny = y+n[1]

            if out_of_range(nx,ny) or visited[nx][ny]: # 격자에서 벗어났거나, 방문한 위치.
                continue
            else: # 처음 방문한 위치
                order += 1
                do_something(nx,ny,order)
                queue.append((nx,ny))
                visited[nx][ny] = True

bfs(init_x,init_y)
```

## DFS
TODO 이다. 왜냐하면 DFS 자체를 다루기 보다는 DFS로 순열 혹은 조합을 구현하는 문제가 더 빈출이라서 나중으로 미룬다. 구현하라고 하면 할 수는 있으니.

## DFS를 이용한 조합 구현
nCr(조합) = 서로 다른 n개 중에서 중복을 허용하지 않으며, 순서를 고려하지 않고 r개 선택. \
DFS 기반의 재귀와 deque를 사용하면 되는데, 여기서도 deque 대신에 list를 사용해서 구현해본다.
```py
N,R = map(int,input().split())
lst = list(range(N))

# print nCr
def do_something(comb):
    print(comb)


def dfs_combination(n,r,comb, depth): # queue, int
    if len(comb) == r: # N개를 모두 선택한 경우
        do_something(comb)
        return
    elif depth == n:
        return
    
    # 현재 depth의 값 포함 재귀 호출
    comb.append(lst[depth])
    dfs_combination(n,r,comb, depth+1)

    # 현재 depth의 값 미포함 재귀 호출
    comb.pop() # popleft 아니고, 방금 넣은걸 빼는 pop임.
    dfs_combination(n,r,comb, depth+1)

dfs_combination(N,R,[],0)

```
함수 구현 내용을 보면 lst는 전역변수를 사용한다. bfs 과정에서 얻은 케이스들을 모으려면 역시 전역변수를 사용해야 할 것이다. 추가적으로, 위에서는 n,r을 매개변수로 넣어주었고, 근데 오히려 지저분하다 싶으면 이것도 전역변수로 빼주어도 된다.

## DFS를 이용한 순열 구현
nPr(순열) = 서로 다른 n개 중에서 중복을 허용하지 않으며, 순서를 고려하여 r개 선택.
```py
# print nPr
N,R = map(int,input().split())

def do_something(perm):
    print(perm)

lst = list(range(N))

visited = [False] * N
result = []

def dfs_permutation(perm): #queue
    if len(perm) == R: # R개 모두 선택하여 종료
        result.append(list(perm))
        do_something(perm)
        return
    for i,val in enumerate(lst):
        if visited[i]: # 방문한 노드인 경우 제외
            continue
        # i번째 노드를 포함하여 재귀 호출
        perm.append(val)
        visited[i] = True
        dfs_permutation(perm)
        # i번째 노드 삭제
        perm.pop()
        visited[i] = False

dfs_permutation([])
```

## 순열, 조합 (더 간단히 구현)
위에 DFS를 사용하는 경우는 global 변수를 사용해야 전체 결과값을 확인할 수 있는 한계점이 존재했다. 그러나 하나의 함수에 순열 또는 조합의 대상이 되는 list와 몇개를 뽑을지를 넣으면 계산해주는 알고리즘을 찾아서, 다시 작성해본다. 참고 포스팅은 [여기](https://buyandpray.tistory.com/52)
### 순열
```py
def permutation(arr, r):
    
    # 순열을 저장할 배열
    result = []
    
    # 실제 순열을 구하는 함수
    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return

        for idx, data in enumerate(arr):
            if idx not in index: 
				# list는 mutable이기 때문에 새로운 리스트를 넘겨준다.
            	permute(p + [data], index + [idx])
				
    permute([], [])
    
    return result

for r in permutation(['A', 'B', 'C', 'D'], 2):
    print(r)


# --- Result ---
'''
['A', 'B']
['A', 'C']
['A', 'D']
['B', 'A']
['B', 'C']
['B', 'D']
['C', 'A']
['C', 'B']
['C', 'D']
['D', 'A']
['D', 'B']
['D', 'C']
'''
```
### 순열 - itertools
삼성 코테에서 itertools를 만약 사용 가능하다면 아래 방법으로 더 쉽게 구할 수 있다.
```py
from itertools import permutations

# permutations(iterable, r)
# iterable의 원소들을 이용해 길이가 r인 순열을 생성한다.
# 리턴값은 순열 튜플의 이터레이터다.

data = "ABCD"
result = permutations(data, 2) # <itertools.permutations object at 0x7ff96110ee90>

for r in result:
    print(r)
    
# --- Result ---
'''
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
```

### 조합
```py
# 재귀적으로 조합 구현

def combination(arr, r):
    
    # 조합을 저장할 배열
    result = []
    
    # 실제 조합을 구하는 함수
    def combinate(c, index):
        if len(c) == r:
            result.append(c)
            return 
        
        for idx, data in enumerate(arr):
            # 중복되는 조합이 생성되지 않게 마지막으로 들어온 원소의 인덱스보다
            # 새로 추가하는 원소의 인덱스가 큰 경우만 조합을 생성한다.
            if idx > index:
                combinate(c + [data], idx)
    
    combinate([], -1)
    
    return result

for r in combination(['A', 'B', 'C', 'D'], 2):
    print(r)
    
# --- Result ---
'''
['A', 'B']
['A', 'C']
['A', 'D']
['B', 'C']
['B', 'D']
['C', 'D']
'''
```

### 조합 - itertools
```py
from itertools import combinations

# combinations(iterable, r)
# iterable의 원소들을 이용해 길이가 r인 조합을 생성한다.
# 리턴값은 조합 튜플의 이터레이터다.

data = "ABCD"
result = combinations(data, 2) # <itertools.combinations object at 0x7f603bdc5e90>

for r in result:
    print(r)
    
# --- Result ---
'''
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
'''
```


## 2차원 배열의 나선형 알고리즘
2번 움직일 때마다 이동거리가 1씩 증가하는 것만 기억하자. 구체적인 내용은 [포스팅](https://kimjingo.tistory.com/205) 참고.
```py
N = 5
board = [[0] * N for _ in range(N)]
 
#      ←   ↓   →   ↑ (4방향, 시작방향: 서쪽)
dy = ( 0,  1,  0, -1)
dx = (-1,  0,  1,  0)
 
 
def init_grid():
    y = x = int(N / 2) # 배열의 중앙 좌표
    direction = move_count = number = 0
    dist = 1
 
    while True:
        move_count += 1 # 움직인 횟수
        for _ in range(dist): # dist만큼 direction 방향으로 이동
            ny = y + dy[direction]
            nx = x + dx[direction]
 
            # 종료 조건 : 이동한 좌표가 (0, -1)인 경우(배열의 길이가 홀수면 항상 마지막 좌표는 (0, -1), 방향은 서쪽
            if (ny, nx) == (0, -1):
                return
            # 번호 증가 및 기록
            number += 1
            board[ny][nx] = number
 
            # (y, x) 갱신
            y = ny
            x = nx
 
        if move_count == 2: # 어떠한 방향으로든 2번 이동한 경우
            dist += 1 # 이동거리 1 증가
            move_count = 0 # 초기화
        direction = (direction + 1) % 4 # 방향 변경
 
init_grid()
for row in board:
    print(row)
```
### 출력
```
[24, 23, 22, 21, 20]
[9, 8, 7, 6, 19]
[10, 1, 0, 5, 18]
[11, 2, 3, 4, 17]
[12, 13, 14, 15, 16]
```
## 배열 돌리기
90, 180, ... 만큼 각도로 배열 회전시키는 문제도 꽤 나온다고 한다. 빈 배열을 만들고, 기존 배열에서의 index와의 관계만 잘 써주면 된다. 아래 `rotate45()` 함수 참고. 포스팅에서는 45도라고 하는데, 45도가 아니라 90도를 회전하는 함수라고 봐야할 것 같다. 
```py
N = 5
board = [[i * N + j for j in range(N)] for i in range(N)]
 
 
def rotate45():
    # 시계방향으로 배열을 45도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[N - j - 1][i]
    return new_board
 
 
print("원본")
for row in board:
    print(row)
print()
 
print("시계방향 45도 회전")
rotated = rotate45()
for row in rotated:
    print(row)
 
```
### 출력
```
원본
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

시계방향 45도 회전
[20, 15, 10, 5, 0]
[21, 16, 11, 6, 1]
[22, 17, 12, 7, 2]
[23, 18, 13, 8, 3]
[24, 19, 14, 9, 4]
```