from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs():
    global visited
    # 동,서,남,북 각각의 방향에서 이동 가능한 방향
    Turn_dir = [[],[4,3],[3,4],[1,2],[2,1]]
    queue = deque([(start_x-1, start_y-1, start_direction)])
    visited[start_direction][start_x-1][start_y-1] = 0
    while queue:
        x, y, direction = queue.popleft()
        # 도착 지점에 도달 시, 최소 명령 횟수를 반환
        if x == end_x-1 and y == end_y-1 and direction == end_direction:
            return visited[end_direction][x][y]
        else:
            # Turn dir: dir은 left 또는 right만 가능하다.
            left = Turn_dir[direction][0]
            right = Turn_dir[direction][1]
            for new_direction in left, right:
                if visited[new_direction][x][y] == -1:
                    visited[new_direction][x][y] = visited[direction][x][y] + 1
                    queue.append((x,y,new_direction))
            # 해당 방향으로 이동
            if direction == 1:
                for nx, ny in (x,y+1),(x,y+2),(x,y+3):
                    if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                        continue
                    else:
                        # Go 1이 불가능하다면, Go 3도 불가능하다.
                        if graph[nx][ny] == 1:
                            break
                        if visited[direction][nx][ny] == -1:
                            visited[direction][nx][ny] = visited[direction][x][y] + 1
                            queue.append((nx,ny,direction))
            elif direction == 2:
                for nx, ny in (x,y-1),(x,y-2),(x,y-3):
                    if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                        continue
                    else:
                        # Go 1이 불가능하다면, Go 3도 불가능하다.
                        if graph[nx][ny] == 1:
                            break
                        if visited[direction][nx][ny] == -1:
                            visited[direction][nx][ny] = visited[direction][x][y] + 1
                            queue.append((nx,ny,direction))
            elif direction == 3:
                for nx, ny in (x+1,y),(x+2,y),(x+3,y):
                    if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                        continue
                    else:
                        # Go 1이 불가능하다면, Go 3도 불가능하다.
                        if graph[nx][ny] == 1:
                            break
                        if visited[direction][nx][ny] == -1:
                            visited[direction][nx][ny] = visited[direction][x][y] + 1
                            queue.append((nx,ny,direction))
            elif direction == 4:
                for nx, ny in (x-1,y),(x-2,y),(x-3,y):
                    if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                        continue
                    else:
                        # Go 1이 불가능하다면, Go 3도 불가능하다.
                        if graph[nx][ny] == 1:
                            break
                        if visited[direction][nx][ny] == -1:
                            visited[direction][nx][ny] = visited[direction][x][y] + 1
                            queue.append((nx,ny,direction))

# 입력 및 그래프 생성
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[[-1] * N for _ in range(M)] for _ in range(5)]
Turn_dir = [1,3,2,4]

# 출발지점, 도착지점 지정
start_x, start_y, start_direction = map(int, input().split())
end_x, end_y, end_direction = map(int, input().split())

# 결과 출력
result = bfs()
print(result)