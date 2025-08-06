def isValid(s: str) -> bool:
        stack = []
        hashmap = {'}':'{', ']':'[', ')':'('}
        for c in s:
            if stack and (c in hashmap and hashmap[c] == stack[-1]):
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0