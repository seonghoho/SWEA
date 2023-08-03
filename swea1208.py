T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        max_ = max(lst)
        min_ = min(lst)
        for k in range(100):
            if max_ == lst[k]:
                lst[k] -= 1
                
            elif min_ == lst[k]:
                lst[k] += 1
                
            else:
                continue

    last_max = max(lst)
    last_min = min(lst)
    result = last_max - last_min
    print(lst)
    print(f'#{test_case} {result}')