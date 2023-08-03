T = int(input())
for test_case in range(1, T + 1):

    N = int(input())

    lst = list(map(int, input().split()))
    bucket = [0]*(max(lst)+1)

    for i in lst:
        bucket[i] += 1


    for i in range(1, len(bucket)):
        bucket[i] +=bucket[i-1]
        
    new_lst = [0]*len(lst)    

    for i in lst:
        new_lst[bucket[i]-1] = i
        bucket[i] -= 1

    result = " ".join(str(num) for num in new_lst)
    print(f'#{test_case} {result}')
