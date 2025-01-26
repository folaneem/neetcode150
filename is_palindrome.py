def is_valid_palindrome(word):
    clean_word = ''
    for w in word:
        l_c_w = w.lower()
        if l_c_w.isalnum():
            clean_word += l_c_w
    return clean_word == clean_word[::-1]


if __name__ == '__main__':
    print(is_valid_palindrome(word="Was it a car or a cat I saw?"))
