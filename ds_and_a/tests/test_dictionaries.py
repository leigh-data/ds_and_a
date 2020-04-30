import pytest

from ds_and_a.dictionaries import (
    first_non_repeated,
    first_repeated,
    most_frequent,
    count_pairs_with_diff,
    two_sum)
from ds_and_a.hashtable import Hashtable


@pytest.fixture
def hashtable():
    ht = Hashtable()
    ht.put(1, "Ronnie Wood")
    ht.put(7, "Keith Richards")

    return ht


@pytest.mark.parametrize("str1, expected", [
    ("a green apple", 'g'),
    ("AAAAAAAAA", None),
    (" AAAAAAAAA", ' ')
])
def test_first_non_repeated(str1, expected):
    assert first_non_repeated(str1) == expected


def test_first_repeated():
    str1 = "a green apple"
    assert first_repeated(str1) == 'e'


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 4, 4, 4], 4),
    ([1, 2, 3], 1),
])
def test_most_frequent(nums, expected):
    assert most_frequent(nums) == expected


def test_most_frequent_bad_inout():
    nums = ['a', 'b', 'c']

    with pytest.raises(TypeError):
        most_frequent(nums)


@pytest.mark.parametrize("lyst, k, expected", [
    ([1, 7, 5, 9, 2, 12, 3], 2, 4),
    ([3, 1, 4, 1, 5], 2, 2)
])
def test_cpwd(lyst, k, expected):
    assert count_pairs_with_diff(lyst, k) == expected


@pytest.mark.parametrize("lyst, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1])
])
def test_two_sum(lyst, target, expected):
    assert two_sum(lyst, target) == expected


def test_hashtable_get(hashtable):
    assert hashtable.get(7) == "Keith Richards"


def test_hashtable_put(hashtable):
    hashtable.put(69, "Mick Jagger")
    assert hashtable.get(69) == "Mick Jagger"


def test_hashtable_put_chained(hashtable):
    hashtable.put(6, "Mick Taylor")
    assert hashtable.get(6) == "Mick Taylor"


def test_hashtable_remove(hashtable):
    hashtable.put(67, "Brian Jones")
    assert hashtable.remove(67) == "Brian Jones"
    assert hashtable.get(67) is None


def test_hashtable_remove(hashtable):
    assert hashtable.remove(54) == None
