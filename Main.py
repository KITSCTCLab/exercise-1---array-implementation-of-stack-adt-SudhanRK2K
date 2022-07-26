class Stack:
    def _init_(self, size):
        self.items = [None]*size
        self.size = size
        self.top=-1

    def is_empty(self):
        if self.top==-1:
            return 1
        else:
            return 0

    def is_full(self):
        if self.top==size-1:
            return 1
        else:
            return 0

    def push(self, data):
        if self.is_full() ==1:
            pass
        else:
            self.top+=1
            self.items[self.top]=data
         
            

    def pop(self):
        if self.is_empty()==1:
            pass
        else:
            self.items[self.top]=""
            self.top-=1

    def status(self):
        for i in range(self.top+1):
            print(self.items[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status() 
