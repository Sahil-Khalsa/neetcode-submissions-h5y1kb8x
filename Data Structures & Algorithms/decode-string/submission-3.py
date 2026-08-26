class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                # Get the substring inside brackets
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()  # remove "["

                # Get the repeat count
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(substr * int(k))

        return "".join(stack)