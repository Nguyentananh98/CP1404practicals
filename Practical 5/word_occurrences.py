"""
Programming 2 - Practical 5
NGUYEN TAN ANH - JC950881


Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes


"""

sentence = input('Text: ')

words = sentence.split(' ')
counts = {}
for word in words:
    if word in counts.keys():
        counts[word] += 1
    else:
        counts[word] = 1

count_words = counts.keys()
count_words = sorted(count_words)
max_words = max([len(word) for word in counts.keys()])

for word in count_words:
    print(f'{word:{max_words}} : {counts[word]}')

