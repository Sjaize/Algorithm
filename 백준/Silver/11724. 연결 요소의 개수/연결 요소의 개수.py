from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs():
    number = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if visited[i] == False:     # 아직 방문하지 않은 노드가 있을 경우, 새로운 연결 요소로 count
            number = number + 1
            queue = deque([i])      # 해당 노드와 연결된 노드들 방문 처리
            while queue:
                node = queue.popleft()
                if visited[node] == True:
                    continue
                else:
                    visited[node] = True
                for connected_node in graph[node]:
                    queue.append(connected_node)
    return number

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 결과 출력
connected_component = bfs()
print(connected_component)