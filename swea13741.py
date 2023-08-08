T = int(input())
for tc in range(1,T+1):
    str1 = set(input())
    str2 = input()
     
    Max = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if Max < cnt:
            Max = cnt
     
    print(f'#{tc} {Max}')