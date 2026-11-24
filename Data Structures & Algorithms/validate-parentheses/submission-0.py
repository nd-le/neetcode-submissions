class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']':'[', ')':'(', '}':'{'}

        for c in s:
            if stack and c in closeToOpen:
                if stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()

            else:
                stack.append(c)

        return len(stack) == 0