input = [5,7,9,11,15,17]
output = [13]
for i in range(len(input)):
    current = input[i]
    next = current+2
    if input[i+1] != next:
        print(next)
        break