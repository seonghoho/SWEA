T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(input())
    ndx = [0]*10

    for i in range(10):
        for num in lst:
            if int(num) == i:
                ndx[i] +=1
    max_ndx = 0
    for j in range(10):
        if  ndx[j] == max(ndx):
            max_ndx = j

    print(f'#{test_case} {max_ndx} {ndx[max_ndx]}')