for tc in range(1, 11):  # 10회 test 반복
    n = int(input())  # 회문 길이 주어짐
    lst = [list(input()) for _ in range(8)]  # 8x8 배열 입력

    cntr = 0
    cntc = 0
    real_cnt = 0
    for i in range(8):  # 8개 행 반복 실행

        for j in range(8 - n + 1): # N-M+1 만큼 돌기 가능하다
            if lst[i][j:j + n] == lst[i][j:j + n][::-1]:
                cntr += 1 # n자리수 회문만큼을 비교하는 if문, 같으면 +1

        for j in range(8 - n + 1):
            col = [] # 세로, 열을 더할 col 리스트 생성
            for k in range(n): # n자릿수만큼 반복해서 lst[j+k][i] 를 추가,
                col.append(lst[j + k][i])

            if col == col[::-1]:  # 추가한 배열이 회문인지 확인
                cntc += 1

    real_cnt = cntc + cntr

    print(f'#{tc} {real_cnt}')
