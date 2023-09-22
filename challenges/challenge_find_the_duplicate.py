def find_duplicate(nums):
    check = check_list(nums)
    if not check:
        return False

    nums.sort()
    index = 0
    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            return nums[index]
        index += 1

    return False


def check_list(nums):
    if nums is None or type(nums) is not list or len(nums) <= 1:
        return False

    for num in nums:
        if type(num) is not int or num < 0:
            return False

    return True
