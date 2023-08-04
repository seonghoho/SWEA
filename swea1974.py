T = int(input())
for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0

    # 가로 비교
    for i in range(9):
        blank = [0] * 10
        for j in numbers[i]:  # 1~9
            blank[j] += 1
        if max(blank) != 1:
            cnt += 1
            break

    # 세로 비교
    for i in range(9):
        blank = [0] * 10
        for j in range(9):
            blank[numbers[j][i]] += 1
        if max(blank) != 1:
            cnt += 1
            break

    # 3x3 비교
    cnt1 = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blank = [0] * 10
            for k in range(3):
                for l in range(3):
                    blank[numbers[i + k][j + l]] += 1
            if max(blank) != 1:
                cnt1 += 1

    if cnt == 0 and cnt1 == 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
