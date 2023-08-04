from sys import stdin
input = stdin.readline

def bfs():
    count = 0
    q = [A]
    while q:
        tmp = []
        count = count + 1
        for i in q:
            for n in graph[i]:
                if n == B:
                    return count
                if not visited[n]:
                    visited[n] = True
                    tmp.append(n)
        q = tmp
    return -1

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
A, B = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
result = bfs()
print(result)