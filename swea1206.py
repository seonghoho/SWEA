T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    sum_ = 0
    arr = []
    for i in range(2,N-2):
        arr = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]
        high = max(arr)
        if lst[i] - high > 0:
            sum_ += lst[i] - high
    print(f'#{test_case} {sum_}')