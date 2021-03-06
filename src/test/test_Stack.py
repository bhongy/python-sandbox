import pytest
from src import Stack


class TestEmptyStack:
    def setup_method(self, method):
        self.empty_stack = Stack.Empty()

    def test_depth_should_be_zero(self):
        assert self.empty_stack.depth() == 0

    def test_top_empty_should_raise(self):
        with pytest.raises(Stack.EmptyStackError):
            self.empty_stack.top()

    def test_pop_empty_should_raise(self):
        with pytest.raises(Stack.EmptyStackError):
            self.empty_stack.pop()

    def test_push_empty_should_not_raise(self):
        try:
            self.empty_stack.push(1)
            self.empty_stack.push("foo")
            self.empty_stack.push({"foo": "bar"})
            self.empty_stack.push(("raspberry", "sorbet"))
        except:
            pytest.fail("Push to an empty stack should not raise an error")


class TestNonEmptyStack:
    def setup_method(self, method):
        self.stack = Stack.Empty().push("orange").push("banana")

    def test_depth(self):
        assert self.stack.depth() == 2

    def test_top(self):
        assert self.stack.top() == "banana"

    def test_pop_returns_new_stack_without_previous_top(self):
        new_stack = self.stack.pop()
        assert new_stack.depth() == 1
        assert new_stack.top() == "orange"

    def test_pop_is_immutable(self):
        self.stack.pop()
        old_stack = self.stack
        assert old_stack.depth() == 2
        assert old_stack.top() == "banana"

    def test_push_returns_new_stack_with_new_element_on_top(self):
        new_stack = self.stack.push("raspberry")
        assert new_stack.depth() == 3
        assert new_stack.top() == "raspberry"

    def test_push_is_immutable(self):
        self.stack.push("raspberry")
        old_stack = self.stack
        assert old_stack.depth() == 2
        assert old_stack.top() == "banana"
