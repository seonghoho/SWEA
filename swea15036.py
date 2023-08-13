def dfs(now):
    global path
    path.append(now)
    if now == end:                        # 시작점이 끝점으로 도달하면 리턴
        return

    for k in lst[now]:
        if not used[k]:
            used[k] = 1
            dfs(k)

T = int(input())                         # 반복 케이스 입력
for tc in range(1, T + 1):
    V, E = map(int, input().split())     # 노드 갯수 V, 연결선 E
    lst = [[] for _ in range(V)]         # VxV 빈 배열 생성
    used = [0] * V                       # 중복 금지
    for _ in range(E):                   # E번 반복해서 연결선 입력
        a, b = map(int, input().split())
        lst[a - 1].append(b - 1)         # a-1인덱스에 b-1 숫자 입력

    path = []
    start, end = map(int, input().split())
    dfs(start - 1)

    if end - 1 in path:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
