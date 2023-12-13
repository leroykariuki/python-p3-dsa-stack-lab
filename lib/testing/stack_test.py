from lib.Stack import Stack


class TestStack:
    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert(expected[index] == stk.items[index])

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        expected = [1, 2, 3, 4, 5, 0]
        for index in range(0, len(expected)):
            assert(expected[index] == stk.items[index])

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert(expected[index] == stk.items[index])

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        assert(stk.size() == len(expected))

    def test_empty(self):
        '''Test Stack is_empty() method'''
        stk = Stack()
        assert(stk.is_empty())
        assert(stk.size() == 0)
        try:
            stk.pop()
            assert False, "Expected Exception"
        except Exception as e:
            assert str(e) == "Stack is empty"
        stk.push(1)
        assert(not stk.is_empty())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

    def test_full(self):
        '''Test Stack is_full() method'''
        stk = Stack(limit=1)
        assert(not stk.is_full())
        stk.push(1)
        assert(stk.is_full())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

        stk.push(1)
        try:
            stk.push(2)
            assert False, "Expected Exception"
        except Exception as e:
            assert str(e) == "Stack is full"

    def search(self, value):
        try:
         index = self.items.index(value)
         return len(self.items) - index
        except ValueError:
         return -1

        # Case with target not in Stack
        assert(stk.search(15) == -1)
