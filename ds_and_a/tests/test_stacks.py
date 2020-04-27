import pytest

from ds_and_a.stacks import string_reverser, balanced, Stack, TwoStacks, MinStack


@pytest.fixture
def stack():
    fixture_stack = Stack()
    fixture_stack.push(1)
    fixture_stack.push(2)
    fixture_stack.push(3)

    return fixture_stack


@pytest.fixture
def two_stacks():
    ts = TwoStacks(5)

    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    return ts


@pytest.fixture
def min_stack():
    stack = MinStack()

    stack.push(3)
    stack.push(5)

    return stack


def test_string_reverser():
    test_string = "abcdefg"
    result_string = string_reverser(test_string)
    assert test_string[::-1] == result_string


def test_string_reverser_empty_string():
    with pytest.raises(ValueError):
        string_reverser('')


def test_string_reverser_spaced_string():
    with pytest.raises(ValueError):
        string_reverser(' ')


@pytest.mark.parametrize(
    "expression",
    ["<>", "{}", "<{[]}>", "{123}"])
def test_balanced_true(expression):
    assert balanced(expression) == True


@pytest.mark.parametrize(
    "expression",
    ["<", "{>", "<{[}>", "{123)", ")"])
def test_balanced_false(expression):
    assert balanced(expression) == False


def test_stack_peek(stack):
    assert stack.peek() == 3


def test_stack_push(stack):
    stack.push(16)
    assert stack.peek() == 16


def test_stack_peek():
    stack = Stack()
    item = stack.peek()
    assert item is None


def test_stack_pop(stack):
    item = stack.pop()
    assert item == 3


def test_stack_pop():
    stack = Stack()
    item = stack.pop()
    assert item is None


def test_stack_is_empty(stack):
    assert stack.is_empty() == False


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True


def test_stack_string(stack):
    assert str(stack) == "<Stack: [3, 2, 1]>"


def test_stack_string_empty_stack():
    stack = Stack()
    assert str(stack) == "<Stack: []>"


def test_two_stacks(two_stacks):
    assert two_stacks.pop1() == 11
    assert two_stacks.pop2() == 7


def test_two_stacks_push2(two_stacks):
    # note: two_stacks is full coming in; need to pop
    two_stacks.pop1()
    two_stacks.push2(40)
    assert two_stacks.pop2() == 40


def test_two_stacks_push1(two_stacks):
    two_stacks.pop1()
    two_stacks.push1(12)
    assert two_stacks.pop1() == 12


def two_stacks_pop1(two_stacks):
    assert two_stacks.pop1() == 11


def two_stacks_is_full_1_and_2(two_stacks):
    assert two_stacks.is_full1()
    assert two_stacks.is_full2()


def two_stacks_is_empty_1_and_2():
    two_stacks = TwoStacks(5)

    assert two_stacks.is_empty1() == True
    assert two_stacks.is_empty2() == True


def two_stacks_cannot_pop1():
    two_stacks = TwoStacks(5)

    with pytest.raises(IndexError):
        assert two_stacks.pop1()


def two_stacks_cannot_pop1():
    two_stacks = TwoStacks(5)

    with pytest.raises(IndexError):
        assert two_stacks.pop2()


def two_stacks_cannot_push1(two_stacks):
    with pytest.raises(IndexError):
        assert two_stacks.push1(1)


def two_stacks_cannot_push2(two_stacks):
    with pytest.raises(IndexError):
        assert two_stacks.push2(1)


def test_min_stack(min_stack):
    assert min_stack.min() == 3


def test_min_stack_higher_value(min_stack):
    min_stack.push(5)
    assert min_stack.min() == 3


def test_min_stack_lower_value(min_stack):
    min_stack.push(1)
    assert min_stack.min() == 1


def test_min_stack_pop(min_stack):
    assert min_stack.pop() == 5


def test_pop_empty_min_stack_error():
    min_stack = MinStack()

    with pytest.raises(IndexError):
        min_stack.pop()


def tet_push_min_stack_empty():
    min_stack = MinStack()
    min_stack.push(666)

    assert min_stack.min() == 666
