class CircularQueue:
    def __init__(self, limit):
        self.Q = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.limit == self.front
    
    def enqueue(self, data):
        if self.is_full():
            return -1 
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.limit
        self.Q[self.rear] = data
    
    def dequeue(self):
        if self.is_empty():
            return -1
        removed = self.Q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.limit
        return removed
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Circular Queue:")
        i = self.front
        while True:
            print(self.Q[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.limit
            print()