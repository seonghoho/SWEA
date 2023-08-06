T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(input())
    cnt = 1
    max_lst = []
    for i in range(N-1):
        if lst[i] == '1' and lst[i+1] == '1':
            cnt += 1
            max_lst.append(cnt)
        else:
            cnt = 1
            max_lst.append(cnt)
    max_lst.sort()
    Max = max_lst[-1]
    print(f'#{tc} {Max}')