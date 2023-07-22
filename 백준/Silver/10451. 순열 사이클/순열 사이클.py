from sys import stdin
input = stdin.readline

# Depth-First-Search-Algorithm
def dfs(node):
    global visited
    visited[node] = True
    if not visited[permutation[node]]:      # 현재 노드와 연결된 노드를 아직 방문하지 않았다면, 방문
        dfs(permutation[node])

# 입력 및 그래프 생성
T = int(input())        # 테스트 케이스의 개수 T
for _ in range(T):
    N = int(input())        # 순열의 크기 N
    permutation = list(map(lambda x : int(x)-1, input().split()))
    visited = [False] * (N)
    number_of_cycle = 0     # 순열 사이클의 개수
    for i in range(N):
        if visited[i] == False:
            number_of_cycle = number_of_cycle + 1
            dfs(i)
    print(number_of_cycle)      # 결과 출력