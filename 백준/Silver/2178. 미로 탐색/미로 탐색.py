from sys import stdin
from collections import deque

input = stdin.readline

# Breadth-First-Search 알고리즘
def BFS(X, Y):
    queue = deque()
    queue.append((X,Y))
    while queue:
        X, Y = queue.popleft()
        for i in range(4):
            NX = X + dX[i]
            NY = Y + dY[i]
            if NX < 0 or NY < 0 or NX >= N or NY >= M:
                continue
            if graph[NX][NY] == 0:
                continue
            if graph[NX][NY] == 1:
                graph[NX][NY] = graph[X][Y] + 1
                queue.append((NX, NY))
    return graph[N-1][M-1]

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
dX = [1, 0, -1, 0]
dY = [0, 1, 0, -1]

# 결과 출력
print(BFS(0, 0)) 