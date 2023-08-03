def isExist(numbers):
    for row in numbers:
        if len(set(row)) != 9:
            return False

    for col in range(9):
        if len(set(numbers[i][col] for i in range(9))) != 9:
            return False

    three = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            for x in range(i, i+3):
                for y in range(j, j+3):
                    three.append(numbers[x][y])

            if len(set(three)) != 9:
                return False
    
    return True


T = int(input())
for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split())) for _ in range(9)]

    if isExist(numbers):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
