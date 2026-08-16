class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {
            '}': '{',
            ']': '[',
            ')': '('
        }   
        top = ''
        if s[0] in closetoopen:
            return False     
        for string in s:
            if string in closetoopen:
                if closetoopen[string] == top and len(stack) > 0:
                    stack.pop()
                    if len(stack) > 0:
                        top = stack[len(stack) - 1]
                else:
                    return False
            else:
                stack.append(string)
                top = string
        if len(stack) == 0:
            return True
        else:
            return False