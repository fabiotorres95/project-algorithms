def is_anagram(first_string: str, second_string: str):
    first_lower = first_string.lower()
    second_lower = second_string.lower()
    first_list = []
    second_list = []
    first_list[:0] = first_lower
    second_list[:0] = second_lower

    first_result = ''.join(merge_sort(first_list))
    second_result = ''.join(merge_sort(second_list))

    if first_result == '' or second_result == '':
        return (first_result, second_result, False)

    is_equal = first_result == second_result
    return (first_result, second_result, is_equal)


def merge_sort(letters_list: list) -> list:
    if len(letters_list) < 2:
        return letters_list

    midpoint = len(letters_list) // 2

    left_list = letters_list[:midpoint]
    right_list = letters_list[midpoint:]

    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return premerge(left, right)


def premerge(left: list, right: list) -> list:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    index_left = 0
    index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result


print(is_anagram('banana', 'ananab'))
print(is_anagram('BanaNa', 'ANAnaB'))
