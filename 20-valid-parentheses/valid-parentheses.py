class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(':')',
            '[':']',
            '{':"}"
        }

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            elif not stack or mapping[stack.pop()] != ch:
                return False
        return not stack