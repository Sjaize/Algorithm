from collections import deque
from sys import stdin
input = stdin.readline

# 입력 및 그래프 생성
R, C = map(int, input().split())
graph = []
queue = deque([])
for i in range(R):
    graph.append(list(input().strip()))
    for j in range(C):
        if graph[i][j] == '*':
            queue.append((i, j, False, 0))      # 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없으므로, 홍수의 위치를 먼저 push
            continue
        if graph[i][j] == 'S':
            start = (i, j, True, 0)

# Breadth-First-Search Algorithm
queue.append(start)
found = False
while not found and queue:
    x, y, hedgehog, minute = queue.popleft()
    for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if nx < 0 or nx > R-1 or ny < 0 or ny > C-1:
            continue
        if hedgehog:        # 고슴도치의 이동
            if graph[nx][ny] == '.':
                graph[nx][ny] = 'S'
                queue.append((nx, ny, True, minute+1))
                continue
            if graph[nx][ny] == 'D':
                minimum_time = minute + 1
                found = True
        else:       # 홍수의 이동
            if graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                queue.append((nx, ny, False, minute+1))

# 결과 출력
if found:
    print(minimum_time)
else:
    print("KAKTUS")