from collections import deque
from sys import stdin
input = stdin.readline
INF = int(1e9)

# BFS 알고리즘을 이용하여, 서로 다른 섬을 구별
def island_distinction(x,y):
    global number
    number = number + 1
    graph[x][y] = number
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for nx, ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = number
                queue.append((nx,ny))

# BFS 알고리즘을 이용하여, 서로 다른 두 섬을 잇는 다리 길이 계산
def bridge_construction(island):
    global visited
    global count
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if graph[i][j] == island:
                queue.append((i,j,0))
                visited[i][j] = 0
    while queue:
        x, y, length = queue.popleft()
        for nx, ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] != island:
                return length
            if graph[nx][ny] == 0 and length+1 < visited[nx][ny] :
                visited[nx][ny] = length+1
                queue.append((nx,ny,length+1))
    return INF

# 입력 및 그래프 생성
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 섬을 구분하기
number = 1      # 섬의 number은 2부터 시작한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:        # 번호가 안매겨진 섬에 대해서만 bfs 시행
            island_distinction(i,j)

# 서로 다른 두 섬을 잇는 다리 길이 계산
minimum_length = INF
visited = [[INF] * N for _ in range(N)]
for island in range(2,number+1):
    length = bridge_construction(island)
    minimum_length = min(minimum_length, length)

# 결과 출력
print(minimum_length)