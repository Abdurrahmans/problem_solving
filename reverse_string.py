def reverse_words(input_string):
    words = input_string.split()  
    reversed_words = [word[::-1] for word in words]  
    output_string = ' '.join(reversed_words)  
    return output_string


input_string = 'this is python code'
output_string = reverse_words(input_string)
print(output_string)  