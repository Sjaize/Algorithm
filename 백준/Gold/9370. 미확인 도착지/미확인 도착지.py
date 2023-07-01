import heapq
from sys import stdin

input = stdin.readline
INF = int(1e9)

# 개선된 다익스트라 알고리즘
def dijkstra(start, distance):
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

# T. testcase의 개수 
T = int(input())

# 각가의 testcase에 대하여
for _ in range(T):
    # n. 교차로의 개수, m. 도로의 개수, t. 목적지 후보의 개수 
    n, m, t = map(int, input().split())
    # s. 출발지, g,h. 경유지
    s, g, h = map(int, input().split())

    # graph 생성
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    # 목적지 후보지 입력
    destination_candidate = []
    for i in range(t):
        candidate = int(input())
        destination_candidate.append(candidate)
    
    # 각 후보에 대하여 다익스트라 수행
    distance_from_s = [INF] * (n+1)  
    dijkstra(s, distance_from_s)
    distance_from_g = [INF] * (n+1)  
    dijkstra(g, distance_from_g)
    distance_from_h = [INF] * (n+1)  
    dijkstra(h, distance_from_h)
    answer = []
    for candidate in destination_candidate:
        if (distance_from_s[candidate] == distance_from_s[g] + distance_from_g[h] + distance_from_h[candidate]) or (distance_from_s[candidate] == distance_from_s[h]+distance_from_h[g]+distance_from_g[candidate]):
            answer.append(candidate)

    # 정답 출력
    answer.sort()
    for destination in answer:
        print(destination, end = ' ')
    print()