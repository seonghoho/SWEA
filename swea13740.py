T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    word = ''
    found = False

    # 가로로 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            if lst[i][j:j+M] == lst[i][j:j+M][::-1]:
                word = ''.join(lst[i][j:j+M])
                found = True
                break
        if found:
            break

    if not found:
        # 세로로 회문 찾기
        for i in range(N - M + 1):
            for j in range(N):
                col = [lst[x][j] for x in range(i, i + M)]
                if col == col[::-1]:
                    word = ''.join(col)
                    found = True
                    break
            if found:
                break

    print(f'#{tc} {word}')