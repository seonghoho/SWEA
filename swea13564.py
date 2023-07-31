T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_ = lst[0]
    min_ = lst[0]
    sum_ = 0
    for i in range(len(lst)):
        if max_ <= lst[i]:
            max_ = lst[i]
        if min_ >= lst[i]:
            min_ = lst[i]
    sum_ = max_ - min_
    print(f'#{test_case} {sum_}')