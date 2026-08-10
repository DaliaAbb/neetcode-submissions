class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_brackets = {')':'(', ']':'[', '}' : '{'}

        for c in s:
            if c in pair_brackets:
                if stack and stack[-1] == pair_brackets[c]:
                    stack.pop()     
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False