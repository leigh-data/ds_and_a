import array as arr
from collections import Counter, defaultdict


def first_non_repeated(str1):
    str1 = str1.lower()
    char_dict = {ch: str1.count(ch) for ch in set(str1)}

    for char in str1:
        if char_dict[char] == 1:
            return char

    return None


def first_repeated(str1):
    char_set = set()

    for char in str1:
        if char in char_set:
            return char
        else:
            char_set.add(char)

    return None


def most_frequent(lyst):
    # make damn sure lyst is all integers
    nums = arr.array('i', lyst)

    frequencies = Counter(nums)

    if len(frequencies) > 0:
        return frequencies.most_common(1)[0][0]
    else:
        return None


def count_pairs_with_diff(nums, difference):
    number_set = set(nums)
    # note: need unique immutable iterable to work with
    nums = set(nums)
    count = 0

    for number in nums:
        if (number + difference) in number_set:
            count += 1
        if (number - difference) in number_set:
            count += 1
        number_set.remove(number)

    return count


def two_sum(nums, target):
    num_dict = {}
    n = len(nums)

    for i in range(n):
        val = target - nums[i]
        if val in num_dict:
            return [num_dict[val], i]
        else:
            num_dict[nums[i]] = i

    return None
