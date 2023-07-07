from collections import deque

# Breadth-First-Search 알고리즘
def BFS():
    queue = deque([(1,0,0)])        # 화면의 이모티콘 1개, time, 비어 있는 클립보드
    visited = [[False] * 8000 for _ in range(8000)]
    while queue:
        monitor, time, board = queue.popleft()
        if visited[monitor][board] == True:
            continue
        else:
            visited[monitor][board] = True
        if monitor == S:
            print(time)
            break
        else:
            queue.append((monitor, time + 1, monitor))      # 클립보드에 이모티콘을 복사하면, 이전의 클립보드 내용은 덮어쓰기 된다. 
            queue.append((monitor + board, time + 1, board))
            # 화면의 이모티콘 개수는 음수가 될 수 없다.
            if monitor >= 1:
                queue.append((monitor - 1, time + 1, board))
            
# 입력
S = int(input())

# 결과 출력
BFS()