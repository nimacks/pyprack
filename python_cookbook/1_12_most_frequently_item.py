# You have a sequence of items, and you’d like to determine the most frequently occurring items in the sequence.

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
            'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
            'look', 'into', 'my', 'eyes', "you're", 'under']

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
top_one = word_counts.most_common(1)
top_four = top_one + top_three
print(top_one)
print(top_one[0])
print(top_four)

# iterate over the top three words
for word, count in top_three:
    print(word, count)
