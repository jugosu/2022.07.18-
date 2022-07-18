# ()이 튜플형태이므로 값을 추가할수 없기때문에 list로 바꾸어준다.
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)