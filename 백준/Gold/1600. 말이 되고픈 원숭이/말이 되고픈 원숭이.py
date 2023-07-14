from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search Algorithm
def BFS():
    visited = [[[False] * W for _ in range(H)] for _ in range(K+1)]
    visited[0][0][0] = True
    queue = deque([(0,0,0,0)])
    while queue:
        x, y, jump, time = queue.popleft()      # 원숭이의 위치, 동작수, 말의 움직임 수
        if x == H-1 and y == W-1:       # 도착점 도달 시, 최솟값 반환
            return time
        else:
            # 말의 움직임
            for nx, ny in (x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y-2),(x+1,y+2),(x+2,y-1),(x+2,y+1):
                if nx < 0 or nx > H-1 or ny < 0 or ny > W-1:
                    continue
                if jump < K and graph[nx][ny] == 0 and visited[jump+1][nx][ny] == False:        # 원숭이는 총 K번만 말처럼 움직일 수 있다.
                    visited[jump+1][nx][ny] = True
                    queue.append((nx, ny, jump+1, time+1))
            # 인접한 네 방향 이동
            for nx, ny in (x-1,y), (x+1,y), (x, y+1), (x, y-1):
                if nx < 0 or nx > H-1 or ny < 0 or ny > W-1:
                    continue
                if graph[nx][ny] == 0 and visited[jump][nx][ny] == False:
                    visited[jump][nx][ny] = True
                    queue.append((nx, ny, jump, time+1))
    return -1

# 입력 및 그래프 생성
K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

# 결과 출력
minimum_movement = BFS()
print(minimum_movement)