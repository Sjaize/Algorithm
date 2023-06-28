from sys import stdin
input = stdin.readline

INF = int(1e9)
t = int(input())

# 각 테스트케이스에 대하여
for _ in range(t):
    n = int(input())
    location = []

    # 좌표 저장
    for i in range(n+2):
        x, y = map(int, input().split())
        location.append((x,y))

    # 좌표를 그래프로 만들기
    graph = [[INF] * (n+3) for _ in range(n+3)]
    for i in range(1, n+3):
        for j in range(1, n+3):
            if i == j:
                graph[i][j] = 0
            else:
                if abs(location[i-1][0]-location[j-1][0]) + abs(location[i-1][1]-location[j-1][1]) <= 1000:
                    graph[i][j] = 1

    # 플로이드 워셜 알고리즘
    for k in range(1, n+3):
        for a in range(1, n+3):
            if k == a: continue
            for b in range(1, n+3):
                if b == k or a == b: continue
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 결과 출력
    print("sad" if graph[1][n+2] >= INF else "happy")