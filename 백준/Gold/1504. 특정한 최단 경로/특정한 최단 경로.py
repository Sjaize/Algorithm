# 1504

from sys import stdin
import heapq
input = stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(E): 
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

distance = [INF] * (N+1)
dijkstra(1)
path_1 = distance[v1]
path_2 = distance[v2]

distance = [INF] * (N+1)
dijkstra(v1)
path_1 = path_1 + distance[v2]
path_2 = path_2 + distance[N]

distance = [INF] * (N+1)
dijkstra(v2)
path_1 = path_1 + distance[N]
path_2 = path_2 + distance[v1]

min_distance = min(path_1, path_2)
if min_distance < INF:
    print(min_distance)
else:
    print(-1)