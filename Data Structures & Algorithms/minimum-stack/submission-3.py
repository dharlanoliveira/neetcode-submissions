class MinStack:

    def __init__(self):
        self.max_item = float("-inf")
        self.min_item = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.max_item = max(self.max_item,val)
        self.min_item = min(self.min_item,val)
        

    def pop(self) -> None:
        item = self.stack.pop()
        self.max_item = float("-inf")
        self.min_item = float("inf")
        for i in self.stack:
            self.max_item = max(self.max_item,i)
            self.min_item = min(self.min_item,i)
        

    def top(self) -> int:
        if(len(self.stack) > 0):
            return self.stack[-1]
        else:
            return 0    

    def getMin(self) -> int:        
        return self.min_item
        
