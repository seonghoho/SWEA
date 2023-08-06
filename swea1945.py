T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    def soinsoo(n, so):
        cnt = 0
        while n % so ==0:
            n //= so
            cnt += 1
        return cnt
    
    nums = [2,3,5,7,11]
    print(f'#{tc}',end=' ')
    for i in nums:
        result = soinsoo(N,i)
        print(result, end=' ')
    print()