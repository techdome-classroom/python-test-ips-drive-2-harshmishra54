class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or bracket_map[char] != stack.pop():
                    return False
            else:
                return False
        
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: true
print(solution.isValid("()[]{}"))    # Output: true
print(solution.isValid("(]"))        # Output: false