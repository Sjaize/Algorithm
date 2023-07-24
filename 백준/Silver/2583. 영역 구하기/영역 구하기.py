from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs(x,y):
    global area_of_area
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            continue
        else:
            graph[x][y] = 1
            area_of_area = area_of_area + 1
            for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                    continue
                if graph[nx][ny] != 1:
                    queue.append((nx,ny))

# 입력 및 그래프 생성
M, N, K = map(int, input().split())
graph = [[0] * (N) for _ in range(M)]
number_of_areas = 0
result = []
for _ in range(K):
    rectangle = list(map(int, input().split()))
    left_x, left_y = M-1-rectangle[1], rectangle[0]
    width, height = rectangle[2]-rectangle[0], rectangle[3]-rectangle[1]
    for i in range(height):
        for j in range(width):
                graph[left_x-i][left_y+j] = 1

# 그래프 탐색
for i in range(M):
    for j in range(N):
        if graph[i][j] != 1:
            number_of_areas = number_of_areas + 1
            area_of_area = 0
            bfs(i,j)
            result.append(area_of_area)

# 결과 출력
print(number_of_areas)
result.sort()
for i in range(number_of_areas):
    print(result[i], end = ' ')