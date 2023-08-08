T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    big_lst = ''
    for i in lst:
        big_lst += (i[0] * int(i[1]))
    
    print(f'#{tc}')

    for i in range(0,len(big_lst)+1):
        if i == 0:
            print(big_lst[i], end='')
        elif i% 10==0:
            print()
            print(big_lst[i], end='')
        elif i == len(big_lst):
            break
        else:
            print(big_lst[i], end='')
    print()

