t = int(input())
for ts in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    bucket = [0]*101
    for i in lst:
        bucket[i] += 1
    for i in range(1,len(bucket)):
        bucket[i] += bucket[i-1]
    new_ = [0]*(len(lst))
    Max = max(lst)
    for i in lst:
        new_[bucket[i]-1] = i
        bucket[i] -= 1
    
    print(f'#{ts}', end=' ')
    for i in range(5):
        print(f'{new_[-1-i]} {new_[i]}', end=' ')
    print()



