from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs(x,y):
    global visited
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if graph[nx][ny] <= rain or visited[nx][ny] == True:
                continue
            else:
                visited[nx][ny] = True
                queue.append((nx,ny))

# 입력 및 그래프 생성
N = int(input())
max_height = 0
answer = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max_height:
            max_height = graph[i][j]        # 가장 높은 높이 저장

# 각 높이에 대하여, bfs를 시행하여 반복하여 안전한 영역의 개수 count
for rain in range(max_height+1):
    safe_area = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > rain and visited[i][j] == False:
                bfs(i, j)
                safe_area = safe_area + 1
    # 물에 잠기지 않는 안전한 영역의 최대 개수 갱신
    if safe_area > answer:
        answer = safe_area

# 결과 출력
print(answer)