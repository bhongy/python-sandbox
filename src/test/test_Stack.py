from src import Stack

def set_up_non_empty_stack():
    return Stack.Empty().push("orange").push("banana")


# def test_top_of_empty_stack():
#     stack = Stack.Empty()
#     with raises(ValueError):
#       stack.top()
      

def test_top_of_non_empty_stack():
    stack = set_up_non_empty_stack()
    assert stack.top() == "banana"
