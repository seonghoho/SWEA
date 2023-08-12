T = int(input())
for tc in range(1, T + 1):
    lst = input()
    lst1 = []

    for i in lst:
        if i == '(' or i == ')' or i == '{' or i == '}':
            lst1.append(i)
        if len(lst1) > 1:
            if lst1[-2] == '(' and lst1[-1] == ')':
                lst1.pop()
                lst1.pop()
            elif lst1[-2] == '{' and lst1[-1] == '}':
                lst1.pop()
                lst1.pop()

    if len(lst1) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
