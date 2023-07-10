from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search
def BFS():
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1     # 토마토가 익는 데 필요한 일 수 계산
                queue.append((nx, ny))      # 유망한 child node만, queue에 삽입

# 입력 및 그래프 생성
M, N = map(int, input().split())
graph = []
queue = deque([])       # BFS를 이용하기 위한 queue 생성
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))     # queue에 익은 토마토들의 위치 저장

# BFS 시행
BFS()

# 결과 출력
minimum_time = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:        # 만일 익을 수 없는 토마토가 존재한다면, -1을 출력하고 종료
            print(-1)
            exit(0)
        if graph[i][j] > minimum_time:
            minimum_time = graph[i][j]

# 모든 토마토가 익는 데 필요한 최소 일수 출력
print(minimum_time - 1)