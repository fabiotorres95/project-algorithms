def is_palindrome_iterative(word):
    if type(word) != str or word == '':
        return False

    high_index = len(word) - 1
    low_index = 0

    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1

    return True
