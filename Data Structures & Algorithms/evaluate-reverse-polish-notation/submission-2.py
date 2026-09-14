class Solution:

       
    def evalRPN(self, tokens: List[str]) -> int:
        operations = "+-*/"
        stack = []
        current_value = 0
        
        for item in tokens:
            if item not in operations:
                stack.append(item)
                continue;

            item1 = int(stack.pop())
            item2 = int(stack.pop())

            if(item == "+"):
                result = item2 + item1
            if(item == "*"):
                result = item2 * item1
            if(item == "/"):
                result = item2 / item1
            if(item == "-"):
                result = item2 - item1
            
            stack.append(result)
                

        return int(stack[-1])