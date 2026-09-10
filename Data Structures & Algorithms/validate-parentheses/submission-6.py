class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = len(s) - 1
        if len(s) % 2 == 1:
            return False
        while (index >= 0):
            if s[index] == ")" or s[index] == "]" or s[index] == "}":
                stack.append(s[index])
            else:
                if len(stack) == 0:
                    return False
                if s[index] == "(":
                    if stack.pop() != ")":
                        return False
                elif s[index] == "{":
                    if stack.pop() != "}":
                        return False
                elif s[index] == "[":
                    if stack.pop() != "]":
                        return False
                else:
                    return False
            index -= 1
        if len(stack) > 0:
            return False
        return True
        