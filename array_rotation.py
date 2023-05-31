input = [2,7,11,4,-2]
for i in range(2):
    temp = input[0]
    for i in range(len(input)-1):
        input[i] = input[i+1]
    input[len(input)-1] = temp
print(input)