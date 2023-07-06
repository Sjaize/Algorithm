from sys import stdin
input = stdin.readline

# Depth-First-Search 알고리즘
def DFS(x, y, color):
    # 뭉쳐 있는 인원을 세기 위한 전역 변수 선언
    global count
    # Stop condition
    if x < 0 or y < 0 or x > M-1 or y > N-1:    # 전쟁터의 가로 크기가 N, 세로 크기가 M임을 주목하자.
        return
    # Stop condition
    if graph[x][y] != color:
        return
    else:
        graph[x][y] = 'O'
        count = count + 1
        DFS(x+1, y, color)
        DFS(x, y+1, color)
        DFS(x-1, y, color)
        DFS(x, y-1, color)

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
power_of_W = 0
power_of_B = 0

# 각 자리에서의 위력 계산
for i in range(M):                  # 전쟁터의 가로 크기가 N, 세로 크기가 M임을 주목하자.
    for j in range(N):
        if graph[i][j] == 'O':
            continue
        count = 0
        if graph[i][j] == 'W':
            DFS(i, j, 'W')
            power_of_W = power_of_W + count**2
        else:
            DFS(i, j, 'B')
            power_of_B = power_of_B + count**2    

# 결과 출력
print(power_of_W, power_of_B)