# # 첫 번째 풀이 방법
# T = int(input())
# for tc in range(1, T+1): #T번 반복 실행
#     word = list(input()) #단어 입력받기
#     Len = len(word)
#     while Len >0:
#         for i in range(Len):
#             if i>0:
#                 if word[i] == word[i-1]:
#                     word.pop(i-1)
#                     word.pop(i-1)
#                     break
#         Len -= 2
#
#     print(f'#{tc} {len(word)}')

# 두 번째 풀이 방법
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    lst = []
    for i in range(len(word)):
        lst.append(word[i])
        if len(lst)>1 and lst[-1] == lst[-2]:
            lst.pop()
            lst.pop()
    print(f'{tc} {len(lst)}')