class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            max_val = max(self.stack[-1][1], x)
            self.stack.append((x, max_val))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        reversed_buffer = []

        while self.stack and self.stack[-1][0] != max_val:
            reversed_buffer.append(self.stack.pop())

        self.stack.pop()

        for val, _ in reversed_buffer:
            self.push(val)

        return max_val


def test_max_stack():
    def assert_equal(actual, expected, message):
        if actual == expected:
            print(f"✅ PASS: {message}")
        else:
            print(f"❌ FAIL: {message} | Expected: {expected}, Got: {actual}")

    print("🔍 Starting MaxStack tests...\n")

    s = MaxStack()
    
    print("🧪 Test 1: Basic push/top")
    s.push(5)
    assert_equal(s.top(), 5, "top() after pushing 5")

    print("\n🧪 Test 2: push multiple, peekMax")
    s.push(1)
    s.push(3)
    assert_equal(s.peekMax(), 5, "peekMax() with [5, 1, 3]")

    print("\n🧪 Test 3: popMax with multiple max values")
    s.push(5)
    assert_equal(s.popMax(), 5, "popMax() should remove top-most 5")
    assert_equal(s.peekMax(), 5, "peekMax() after one 5 removed")

    print("\n🧪 Test 4: pop, then check top and max")
    assert_equal(s.pop(), 3, "pop() should return 3")
    assert_equal(s.top(), 1, "top() should return 1")
    assert_equal(s.peekMax(), 5, "peekMax() should still be 5")

    print("\n🧪 Test 5: popMax until empty")
    assert_equal(s.popMax(), 5, "popMax() removes last 5")
    assert_equal(s.pop(), 1, "pop() removes 1")

    print("\n🧪 Test 6: stack should be empty now")
    try:
        s.pop()
        print("❌ FAIL: pop() on empty stack should raise an exception")
    except:
        print("✅ PASS: pop() on empty stack raised an exception")

    try:
        s.peekMax()
        print("❌ FAIL: peekMax() on empty stack should raise an exception")
    except:
        print("✅ PASS: peekMax() on empty stack raised an exception")

    try:
        s.top()
        print("❌ FAIL: top() on empty stack should raise an exception")
    except:
        print("✅ PASS: top() on empty stack raised an exception")

    print("\n🎉 All tests finished.")

test_max_stack()