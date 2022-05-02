def is_palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()
    return word == word[::-1]


is_palindrome(input("Type a word"))

if is_palindrome == True:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
