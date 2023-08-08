T = int(input())
for tc in range(1, T+1):
    lst = [list(input())  for _ in range(5)] # 5개의 문자열 입력

    Max_len = -21e8
    for i in lst:                            # 문자열 최대길이 구하기
        if Max_len < len(i):
            Max_len = len(i)
    
    for i in lst:                            # 문자열 최대길이보다 짧으면 임시로 10 넣기
        if Max_len > len(i):
            blank = Max_len-len(i)
            for j in range(blank):
                i.append(10)

    print(f'#{tc}',end=' ')

    for i in range(Max_len):                 # 10이 아닌 곳 나란히 출력하기
        for j in range(5):
            if lst[j][i] != 10:
                print(lst[j][i], end='')
            else: continue
    print()