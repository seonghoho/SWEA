for test_case in range(1, 11):

    T = int(input())

    lst = [(list(map(int, input().split()))) for _ in range(100)]

    row_max_ = -21e8
    col_max_ = -21e8
    dae_max_ = -21e8
    dae2_max_ = 0
    dae1 = 0
    #row, col max

    for i in range(100):
        sum_r = 0 
        sum_c = 0
        for j in range(100):
            sum_r += lst[i][j]
            sum_c += lst[j][i]
            
            
            if i == j:
                dae1 += lst[i][j]
            
        if row_max_ < sum_r:
            row_max_ = sum_r
        if col_max_ < sum_c:
            col_max_ = sum_c
        dae2_max_ += lst[i][99-i]
    if dae_max_ < dae1:
        dae_max_ = dae1

    result = [row_max_, col_max_, dae_max_, dae2_max_]
    result1 = max(result)
    print(f'#{T} {result1}')
