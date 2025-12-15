class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '({[':          # opening bracket
                stack.append(ch)
            else:                     # closing bracket
                if not stack or stack[-1] != bracket_map[ch]:
                    return False
                stack.pop()

        return len(stack) == 0


# --------- Testing in VS ----------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))        # True
    print(sol.isValid("()[]{}"))    # True
    print(sol.isValid("(]"))        # False
    print(sol.isValid("([)]"))      # False
