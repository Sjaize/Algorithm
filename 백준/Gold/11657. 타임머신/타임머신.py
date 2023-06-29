from sys import stdin

input = stdin.readline
INF = int(1e9)

# 입력
N, M = map(int, input().split())
graph = []
distance = [INF] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A,B,C))

# 벨만포드 알고리즘
def BellmanFord(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            current_node, next_node, cost = graph[j]
            if distance[current_node] != INF and distance[next_node] > distance[current_node] + cost:
                distance[next_node] = distance[current_node] + cost      
                if i == N-1:
                    return True
    return False

# 결과 출력
negative_cycle = BellmanFord(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])