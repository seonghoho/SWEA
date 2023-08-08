T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    lst = str2.split(str1)
    

    print(f'#{tc}',end=' ')
    if lst[0] == str2:
        print(0)
    else:
        print(1)