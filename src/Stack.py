"""
stack = Stack.Empty()
stack = stack.push("orange").push("banana")

note:
    "push" being duplicated across Empty and NonEmpty is fine
    I prefer them to be simple and decoupled.

    duplication is a sign that the design can be improved
    but naively creating a Base class with a push method
    that both Empty and NonEmpty inherits from
    introduces a layer of indirection for little gain from DRY-ing
"""


class Empty:
    def depth(self):
        return 0

    def top(self):
        raise EmptyStackError("Cannot read top element from an empty stack")

    def pop(self):
        raise EmptyStackError("Cannot pop an empty stack")

    def push(self, new_top):
        # O(1) time
        return NonEmpty(new_top, self)


class EmptyStackError(Exception):
    def __init__(self, error_message):
        # super(EmptyStackError, self).__init__()
        Exception.__init__(self, error_message)


class NonEmpty:
    def __init__(self, new_top, previous):
        self._top = new_top
        self._tail = previous

    def depth(self):
        # O(n) time
        return 1 + self._tail.depth()

    def top(self):
        # O(1) time
        return self._top

    def pop(self):
        # O(1) time
        return self._tail

    def push(self, new_top):
        # O(1) time
        return NonEmpty(new_top, self)
