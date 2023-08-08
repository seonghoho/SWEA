T = int(input())
for tc in range(1, T+1):
    num = input()
    print(f'#{tc}',end=' ')
    for i in range(len(num)-1,-1,-1):
        if num[i] == 'q':
            print('p',end='')
        elif num[i] == 'p':
            print('q',end='')
        elif num[i] == 'd':
            print('b',end='')
        elif num[i] == 'b':
            print('d',end='')
    print()
    
    
        