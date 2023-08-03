T = int(input())
for test_case in range(1, T + 1):
    arr = [['']*10 for i in range(10)]
    N = int(input())

    for i in range(N):
        x1,y1,x2,y2,a = map(int, input().split())
        if a == 1:
            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    arr[i][j] += 'r'

        else:
            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    arr[i][j] += 'b'
    cnt = 0
    for _ in arr:
        for num in _:
            if 'r' in num and 'b' in num:
                cnt +=1         

    print(f'#{test_case} {cnt}')