from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs(start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    cabin_bacon = [0] * (N+1)
    while queue:
        node = queue.popleft()
        # 모든 사람은 친구 관계로 연결되어져 있다.
        for friend in graph[node]:
            if not visited[friend]:
                cabin_bacon[friend] = cabin_bacon[node] + 1
                visited[friend] = True
                queue.append(friend)
    return sum(cabin_bacon)     # 케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이다.

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)      # A와 B가 친구이면, B와 A도 친구이다.
    graph[B].append(A)

# 케빈 베이컨의 수가 가장 작은 사람 구하기
minimum_index, minimum_number = 1, bfs(1)
for i in range(2,N+1):
    cabin_bacon = bfs(i)
    if cabin_bacon < minimum_number:
        minimum_number = cabin_bacon
        minimum_index = i

# 결과 출력
print(minimum_index)