class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClosed = {")": "(",
                        "}": "{",
                        "]": "["}

        for c in s:
            if c in openToClosed:
                if stack and stack[-1] == openToClosed[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False