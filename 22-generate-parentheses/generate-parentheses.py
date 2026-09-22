class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        def backtrack(current, open, close):

            # A complete valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '('
            if open < n:
                backtrack(current + "(", open + 1, close)

            # Add ')'
            if close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)

        return result