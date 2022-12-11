"""
Programming 2
Nguyen Tan Anh - JC950881
"""

input_string = "?name=Bob&age=99&day=Wed"
special_word = '?'

for word in special_word:
    if word in special_word:
        input_string = input_string.replace(word, '')

data = input_string.split('&')

for i in range(len(data)):
    data[i] = data[i].split('=')
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            data[i][j] = int(data[i][j])
    data[i] = tuple(data[i])

print(data)

