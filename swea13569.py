T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    N = int(input())
    lst = list(map(int, input().split()))
    arr = []
    for i in range(N):
        if lst[i] ==0:
            continue
        else:
            cnt = 0
            for j in range(i+1, N):
                if lst[i] <= lst[j]:
                    cnt += 1
        arr.append(N-cnt-i-1)
    arr.sort()
    min = arr[0]
    max = arr[-1]
    print(f'#{test_case} {max}')