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

