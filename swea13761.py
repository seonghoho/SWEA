T = int(input())
for tc in range(1,T+1):
    words, word = map(str, input().split())
    cnt = words.count(word)
    rest = len(words)- cnt*(len(word)-1)

    print(f'#{tc} {rest}')
