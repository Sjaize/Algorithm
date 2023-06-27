from sys import stdin
import heapq
input = stdin.readline

N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


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
dijkstra(X)
time = distance[:]
for i in range(N+1):
    distance = [INF] * (N+1)
    dijkstra(i)
    time[i] = time[i] + distance[X]

max_time = max(time[1:])
print(max_time)