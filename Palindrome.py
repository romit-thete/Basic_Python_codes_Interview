"""
A word, verse, or sentence (such as "Able was I ere I saw Elba") or a number (such as 1881) that reads the same backward or forward.
"""


def palindrome(word_to_check):
    # print(word_to_check, word_to_check[::-1])
    if word_to_check.lower() != word_to_check[::-1].lower():        # ex: Madam would make this go False
        return False
    return True


word = input("Enter the word: ")
print("Palindrome") if palindrome(word) == 1 else print("Not a Palindrome")
