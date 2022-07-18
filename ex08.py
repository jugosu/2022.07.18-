
#각 if문에 대해서 char를 넣어서 카운트될수있게한다. 
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)