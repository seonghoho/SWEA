T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    real_cnt = 0
    for i in range(N):
        cnt_r = 0
        cnt_c = 0
        for j in range(N):
            if lst[i][j] == 1:
                cnt_r += 1
            if lst[i][j] == 0 or j == N - 1:
                if cnt_r == K:
                    real_cnt += 1
                if lst[i][j] == 0:
                    cnt_r = 0

            if lst[j][i] == 1:
                cnt_c += 1
            if lst[j][i] == 0 or j == N - 1:
                if cnt_c == K:
                    real_cnt += 1
                if lst[j][i] == 0:
                    cnt_c = 0

    print(f'#{tc} {real_cnt}')