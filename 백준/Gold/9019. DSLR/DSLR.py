from sys import stdin
input = stdin.readline

order_name = ['D','S','L','R']
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [""] * 10000
    visited[A] = "."
    found = False
    q = [A]
    while q:
        tmp= []
        for n in q:
            if n == B:
                found = True
                break
            for order, nn in enumerate([2 * n % 10000, n-1 if n != 0 else 9999, n % 1000 * 10 + n // 1000, n // 10 + n % 10 * 1000]):
                if visited[nn] == "":
                    visited[nn] = visited[n] + order_name[order]
                    tmp.append(nn)
        if found == True:
            break
        q = tmp
    print(visited[B][1:])