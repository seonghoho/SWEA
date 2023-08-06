t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    Max = 1
    for i in range(n-1):
        if lst[i+1] ==lst[i]+1:
            cnt += 1
            if Max < cnt:
                Max = cnt
        else:
            cnt = 1
    print(f'#{tc} {Max}')