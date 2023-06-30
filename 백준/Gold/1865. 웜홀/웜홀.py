from sys import stdin

input = stdin.readline
INF = int(1e9)

# 벨만포드 알고리즘
def BellmanFord(start):
    distance[start] = 0
    for i in range(N):
        for edge in graph:
            current_node, next_node, cost = edge
            if distance[next_node] > distance[current_node] + cost:
                distance[next_node] = distance[current_node] + cost      
                if i == N-1:
                    return True
    return False

# 입력
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    distance = [INF] * (N+1)
    for i in range(M):
        S, E, T = map(int, input().split())
        graph.append((S,E,T))
        graph.append((E,S,T))
    for j in range(W):
        S, E, T = map(int, input().split())
        graph.append((S,E,-T))
    
    # 결과 출력
    negative_cycle = BellmanFord(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")