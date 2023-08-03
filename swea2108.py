T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        max_cnt = 0
        min_cnt = 0
        max_ = max(lst)
        min_ = min(lst)
        if max_ - min_ > 1:
            for k in range(100):
                if min_ == lst[k]:
                    min_cnt = k
                elif max_ == lst[k]:
                    max_cnt = k
            lst[max_cnt] -= 1
            lst[min_cnt] += 1
        else:
            print(1)  
    last_max = max(lst)
    last_min = min(lst)
    result = last_max - last_min
    print(f'#{test_case} {result}')