def is_palindrome_recursive(word, low_index=0, high_index=None):
    if type(word) != str or word == '':
        return False

    if high_index is None:
        high_index = len(word) - 1

    if low_index >= high_index:
        return True
    elif word[low_index] == word[high_index]:
        result = is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return result
    else:
        return False
