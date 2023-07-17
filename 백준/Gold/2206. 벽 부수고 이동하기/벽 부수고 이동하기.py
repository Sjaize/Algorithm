from sys import stdin
from collections import deque
input = stdin.readline

# Breadth-First-Search Algorithm
def bfs():
    queue = deque([(0,0,0,1)])
    visited[0][0][0] = True
    while queue:
        x, y, jump, distance = queue.popleft()
        # (N, M) 도달 시, 최단 경로 반환
        if x == N-1 and y == M-1:
            return distance
        else:
            for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                    continue
                else:
                    # 벽 부수고 이동
                    if jump < 1 and graph[nx][ny] == 1 and visited[jump+1][nx][ny] == False:
                        visited[jump+1][nx][ny] = True
                        queue.append((nx, ny, jump+1, distance+1))
                    # 그냥 이동
                    if visited[jump][nx][ny] == False and graph[nx][ny] == 0:
                        visited[jump][nx][ny] = True
                        queue.append((nx, ny, jump, distance+1))
    return -1

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False] * M for _ in range(N)] for _ in range(2)]

# 결과 출력
minimum_distance = bfs()
print(minimum_distance)