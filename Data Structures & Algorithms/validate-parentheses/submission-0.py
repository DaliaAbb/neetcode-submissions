class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_brackets = {'(':')', '[':']', '{': '}'}
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if len(stack) == 0:
                    return False
                if pair_brackets[stack[-1]] != i:
                    return False
                stack.pop()
        return len(stack) == 0       