from collections import deque
from sys import stdin
input = stdin.readline
INF = int(1e9)

# Depth-First-Search-Algorithm
def dfs(i, circuit, visited):
    global minimum_cost
    if i == N-1:        # 모든 노드를 순회하였다면, minimum_cost 갱신
        cost = 0
        for j in range(N-1):
            if graph[circuit[j]][circuit[j+1]] == 0:        # 해당 경로에 갈 수 없는 길이 포함돼 있다면, 결과에 반영하지 않는다.
                cost = INF
                break
            else:
                cost = cost + graph[circuit[j]][circuit[j+1]]
        if graph[circuit[N-1]][circuit[0]] == 0:
            cost = INF
        else:
            cost = cost + graph[circuit[N-1]][circuit[0]]
        if cost < minimum_cost:
            minimum_cost = cost
    else:
        for j in range(N):
            if visited[j] == False:     # 아직 방문하지 않은 노드를 방문 처리하고, DFS
                new_circuit = circuit[:]
                new_circuit[i+1] = j
                new_visited = visited[:]
                new_visited[j] = True
                dfs(i+1, new_circuit, new_visited)

# 입력 및 그래프 생성
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
circuit = [0] * N
minimum_cost = INF

# 각 노드를 출발지점으로 하는 경로 중 최소 경로를 찾는다.
for i in range(N):
    travel_visited = visited[:]
    travel_visited[i] = True
    travel_circuit = circuit[:]
    travel_circuit[0] = i
    dfs(0, travel_circuit, travel_visited)

# 결과 출력
print(minimum_cost)