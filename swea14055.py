from collections import deque

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    S, G = map(int, input().split())
    used = [0] * (V + 1)

    def bfs(start, target):
        q = deque()
        q.append([start, 0])
        while q:
            now, level = q.popleft()
            if used[now] == 1: continue
            if now == target:
                return level
            used[now] = 1
            for i in lst[now]:
                q.append([i, level + 1])

        return 0

    cnt = bfs(S,G)
    print(f'#{tc} {cnt}')


