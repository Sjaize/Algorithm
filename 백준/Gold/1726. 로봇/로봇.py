from collections import deque
from sys import stdin
input = stdin.readline

# Breadth-First-Search-Algorithm
def bfs():
    global visited
    # 동,서,남,북 각각의 방향에서 이동 가능한 방향
    Turn_dir = [[3,2],[2,3],[0,1],[1,0]]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque([(start_x-1, start_y-1, start_direction-1)])
    visited[start_direction-1][start_x-1][start_y-1] = 0
    while queue:
        x, y, direction = queue.popleft()
        # 도착 지점에 도달 시, 최소 명령 횟수를 반환
        if x == end_x-1 and y == end_y-1 and direction == end_direction-1:
            return visited[direction][x][y]
        else:
            # Go K : K는 1,2 또는 3일 수 있다. 현재 향하고 있는 방향으로 K칸 만큼 움직인다. 
            for K in range(1,4):
                nx = x + dx[direction] * K
                ny = y + dy[direction] * K
                if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                    continue
                else:
                    # Go 1이 불가능하다면, Go 2,3도 불가능하다.
                    if graph[nx][ny] == 1:
                        break
                    if visited[direction][nx][ny] == -1:
                        visited[direction][nx][ny] = visited[direction][x][y] + 1
                        queue.append((nx,ny,direction))
            # Turn dir: dir은 left 또는 right만 가능하다.
            left = Turn_dir[direction][0]
            right = Turn_dir[direction][1]
            for new_direction in left, right:
                if visited[new_direction][x][y] == -1:
                    visited[new_direction][x][y] = visited[direction][x][y] + 1
                    queue.append((x,y,new_direction))

# 입력 및 그래프 생성
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[[-1] * N for _ in range(M)] for _ in range(4)]

# 출발지점, 도착지점 지정
start_x, start_y, start_direction = map(int, input().split())
end_x, end_y, end_direction = map(int, input().split())

# 결과 출력
result = bfs()
print(result)