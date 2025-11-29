

text = input("Enter a word: ")

if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
