class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        if len(s) == 1:
            return False

        for i in s:
            if i == "(":
                stack.append(")")
            if i == "{":
                stack.append("}")
            if i == "[":
                stack.append("]")
            if i == ")":
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if e!=")":
                    return False
            if i == "]":
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if e!="]":
                    return False
            if i == "}":
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if e!="}":
                    return False
        if len(stack) != 0:
            return False
        return True
