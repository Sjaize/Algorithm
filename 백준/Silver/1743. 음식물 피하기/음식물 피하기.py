import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# Depth-First-Search Algorithm
def DFS(x, y):
    if graph[x][y] == '.':
        return 0
    else:
        graph[x][y] = '.'
        return DFS(x+1, y) + DFS(x, y+1) + DFS(x-1, y) + DFS(x, y-1) + 1

# 입력 및 그래프 생성
N, M, K = map(int, input().split())
graph = [['.'] * (M+2) for _ in range(N+2)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r][c] = '#'

# DFS 시행
biggest = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        garbage = DFS(i, j)
        if garbage > biggest:
            biggest = garbage

# 결과 출력
print(biggest)