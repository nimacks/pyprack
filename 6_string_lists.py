"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Please enter a word : ")

# solution 1
reversed_word = word[::-1]
print(reversed_word)

if word == reversed_word:
    print("The word you entered is a palindrome")
else:
    print("The word is not a palindrome")

# Solution 2

def reverse(wordd):
    x = ''
    for i in range(len(wordd)):
        x += word[len(wordd)-1-i]
    return x


wordd = input('give me a word:\n')
x = reverse(wordd)
if x == wordd:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')


