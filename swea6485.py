T = int(input())
for test_case in range(1, T + 1):
    bucket = [0]*5001

    N = int(input())
    for _ in range(N): # 테스트 케이스만큼 반복
        a, b = map(int, input().split())
        for i in range(a,b+1):
            bucket[i] += 1
    lst = []
    P = int(input())
    for i in range(P):
        ndx = int(input())
        lst.append(bucket[ndx])

    # result = " ".join(str(num) for num in lst)
    print(f'#{test_case}', end=' ')

    for num in lst:
        print(num, end=' ')
    print()