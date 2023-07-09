from sys import stdin
input = stdin.readline

# Depth-First-Search. Back-tracking
def DFS(i, selected_number):        # visited 배열의 i번째 index에는 선택된 i번째 숫자 저장
    if i == 6:      # 6개의 숫자가 모두 선택됐다면, 결과를 출력
        for j in range(1,7):
            print(selected_number[j], end = ' ')
        print()
    else:
        for j in range(1, testcase[0] + 1):     # testcase에서 i번째로 선택할 숫자를 고른다.
            insertion = True
            for k in range(1, 7):   
                if selected_number[k] >= testcase[j]:        # testcase의 j번째 숫자가 이미 포함된 숫자들보다 크지 않다면, 삽입하지 않는다.
                    insertion = False
                    break
            if insertion == True:       # testcase의 j번째 숫자가 이미 포함된 숫자들보다 크다면, 해당 숫자를 고르고 DFS
                new_selected = selected_number[:]
                new_selected[i+1] = testcase[j]
                DFS(i+1, new_selected)

testcase = list(map(int, input().split()))  
while (testcase[0] != 0):       # input이 0이 아니라면,
    for i in range(1, testcase[0] + 1):     # 선택된 번호를 저장하기 위한 1차원 배열 생성
        start_number = [0] * 7
        start_number[1] = testcase[i]
        DFS(1, start_number)        # 집합 S에서 숫자를 고른 후, 그 숫자를 포함하는 6개의 숫자 선택
    print()
    testcase = list(map(int, input().split()))