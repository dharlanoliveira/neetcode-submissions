class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        startMarkers = "{[("
        endMarkers = "}])"
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        for i in s:
            if(i in startMarkers):
                stack.append(i)
            elif(i in endMarkers):
                if not stack or pairs[stack.pop()] != i:
                    return False

        return len(stack) == 0
               


        