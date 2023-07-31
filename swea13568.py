T = int(input())
for test_case in range(1, T + 1):
    max_ = 0
    min_ = 0
    sum_ = 0
    mid_ = []
   
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(N-M+1):
        midmid = 0
        for j in range(i,M+i):
            midmid += lst[j]
        mid_.append(midmid)
    mid_.sort()
    max_ = mid_[-1]
    min_ = mid_[0]
    sum_ = max_ - min_
    print(f'#{test_case} {sum_}')