T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    Max = -21e8
    for y in range(N):
        for x in range(M):
            Sum = lst[y][x]
            for k in range(4):
                dy = y+directy[k]
                dx = x+directx[k]
                if 0 <= dy < N and 0 <= dx < M:
                      Sum += lst[dy][dx]

            if Max < Sum:
                Max = Sum

    print(f'#{tc} {Max}')