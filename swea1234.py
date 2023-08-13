for tc in range(1,11):
    num1, word1 = input().split()
    num = int(num1)
    word = list(word1)
    while num > 1:
        for i in range(1,num):
            if word[i] == word[i-1]:
                word.pop(i-1)
                word.pop(i-1)
                break
        num -=2
    result = ''.join(word)

    print(f'#{tc} {result}')