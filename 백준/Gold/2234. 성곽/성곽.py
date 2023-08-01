from sys import stdin
input = stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dfs(x,y):
    global size
    size = size + 1
    weight = graph[x][y]
    for direction in [3,2,1,0]:
        # 해당 방향 벽 존재.
        if weight >= 2 ** direction:
            weight = weight - 2 ** direction
        else:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx <= M-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx,ny)

N, M = map(int,input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if i == 0:
            graph[i][j] = graph[i][j] - 2
        elif i == M-1:
            graph[i][j] = graph[i][j] - 8
        if j == 0:
            graph[i][j] = graph[i][j] - 1
        elif j == N-1:
            graph[i][j] = graph[i][j] - 4

number_room = 0
maximum_size = 0
maximum_size_by_elimination = 0

visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            number_room = number_room + 1
            visited[i][j] = 1
            size = 0
            dfs(i,j)
            maximum_size = max(maximum_size,size)

for i in range(M):
    for j in range(N):
        weight = graph[i][j]
        for direction in [3,2,1,0]:
            if weight >= 2 ** direction:
                weight = weight - 2 ** direction
                graph[i][j] = graph[i][j] - 2 ** direction
                visited = [[0] * N for _ in range(M)]
                visited[i][j] = 1
                size = 0
                dfs(i,j)
                maximum_size_by_elimination = max(maximum_size_by_elimination,size)
                graph[i][j] = graph[i][j] + 2 ** direction

# 결과 출력
print(number_room)
print(maximum_size)
print(maximum_size_by_elimination)