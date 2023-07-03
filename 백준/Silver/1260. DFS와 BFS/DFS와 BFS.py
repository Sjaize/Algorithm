from sys import stdin
from collections import deque

input = stdin.readline

# Depth-First-Search 알고리즘
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# Breadth-First-Search 알고리즘
def bfs(graph, start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력
N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

# 그래프 생성
for i in range(M):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)
    
for i in range(N+1):
    graph[i].sort()

# 결과 출력
visited = [False] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V)