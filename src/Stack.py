"""
stack = Stack.Empty()
stack = stack.push("orange").push("banana")

note: I don't care for "push" being duplicated (duplication of something simple is fine)
      because I prefer them to be simple, decoupled
      creating Base class with push method that both Empty and NonEmpty inherits from
      introduces a big amount of indirection for little gain in DRY
"""


class Empty:
    def depth(self):
        return 0

    def top(self):
        raise ValueError("Cannot read top element from an empty stack")

    def pop(self):
        raise ValueError("Cannot pop an empty stack")

    def push(self, new_top):
        # O(1) time
        return NonEmpty(new_top, self)


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
