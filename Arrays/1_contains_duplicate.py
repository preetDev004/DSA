def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False


def contains_duplicate_2(nums):
    return len(nums) != len(set(nums))

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate_2([1, 2, 3, 1]))
