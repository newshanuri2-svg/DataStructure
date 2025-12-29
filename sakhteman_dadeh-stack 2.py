class Stack :
    def __init__(self, limit = 1000):
        self.st = []
        self.lim = limit

    def push (self, x) :
        if len (self.st) >= self.lim :
            print('stack is full')
            return -1
        self.st.append(x)
        
    def pop (self):
        if len (self.st) == 0 :
            print('stack is empty')
            return -1
        return self.st.pop()
    
    def peek (self):
        if len (self.st) == 0:
            print('stack hs empty')
            return -1
        return self.st[-1]
    

test = Stack(10)
test.push(23)
test.push(15)
test.push(47)
print(test.st)

k = test.pop()
print(k)

k = test.peek()
print(k)