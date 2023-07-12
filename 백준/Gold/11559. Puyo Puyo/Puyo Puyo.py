from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search Algorithm
def Counting(x, y, color):       # 모여있는 뿌요들의 개수를 계산
    queue = deque([])
    graph[x][y] = '#'
    count = 1
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == color:
                graph[nx][ny] = '#'
                count = count + 1
                queue.append((nx, ny))
    return count

# Breadth-First-Search Algorithm
def Coloring(x, y, color):       # 모여있는 뿌요들의 개수가 4개 미만이라면, 색 복원
    queue = deque([])
    graph[x][y] = color
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == '#':
                graph[nx][ny] = color
                queue.append((nx, ny))

# Breadth-First-Search Algorithm
def Eliminating(x, y):       # 모여있는 뿌요들의 개수가 4개 이상이라면, 제거
    queue = deque([])
    graph[x][y] = 'x'
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == '#':
                graph[nx][ny] = 'x'
                queue.append((nx, ny))

# block 내리기
def lay_down():
    for j in range(6):
        i = 11
        index = 11
        while i >= 0:
            if graph[i][j] != '.' and graph[i][j] != 'x':
                graph[index][j] = graph[i][j]
                index = index - 1
            i = i - 1
        while index >= 0:
            graph[index][j] = '.'
            index = index - 1

# 입력 및 그래프 생성
graph = [list(input().strip()) for _ in range(12)]
consecutive_times = -1
boom = True

# 뿌요가 터졌다면, 내려온 뿌요에 대해서 반복
while boom:
    consecutive_times = consecutive_times + 1
    # block 내리기
    lay_down()
    # 뿌요 터트리기
    boom = False
    for j in range(6):
        i = 11
        while i >= 0 and graph[i][j] != '.':
            if graph[i][j] == 'x':
                i = i - 1
                continue
            else:
                color = graph[i][j]
                if Counting(i, j, color) < 4:
                    Coloring(i, j, color)
                else:
                    boom = True
                    Eliminating(i, j)
                i = i - 1

# 결과 출력
print(consecutive_times)