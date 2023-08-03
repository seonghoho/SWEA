T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    lst = [(list(map(int, input().split()))) for _ in range(N)]

    def sumnum(a,b):
        sum_ = 0
        for i in range(M):
            for j in range(M):
                sum_ += lst[a+i][b+j]
        return sum_

    sum_list = []
    for i in range(N-M+1):                                                                                                                                                                                                                                                                                                                                                                
        for j in range(N-M+1):
            #네 개의 수를 더하는 함수
            sum_list.append(sumnum(i,j))

    result = max(sum_list)
    print(f'#{test_case} {result}')