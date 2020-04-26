import pytest

from ds_and_a.stacks import string_reverser, balanced, Stack


@pytest.fixture
def stack():
    fixture_stack = Stack()
    fixture_stack.push(1)
    fixture_stack.push(2)
    fixture_stack.push(3)

    return fixture_stack


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
