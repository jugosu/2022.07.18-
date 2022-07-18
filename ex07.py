
#카운트의 위치가 for와 같은 위치선상에 있으므로 옮겨준다.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)
