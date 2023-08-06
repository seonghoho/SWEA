T = int(input())

def binary_search(s, e, target):
    cnt = 0
    while 1:
        cnt += 1
        mid = (s+e)//2
        if mid == target :
            return cnt
        elif mid < target :
            s = mid
        elif mid > target :
            e = mid
        if s > e:
            return 

for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    num_a = binary_search(1, p, a)
    num_b = binary_search(1, p, b)

    if num_a > num_b:
        print(f'#{tc} B')
    elif num_a < num_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')