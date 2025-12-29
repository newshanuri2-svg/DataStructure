class Queue:

    def __init__(self, max):
        self.list = [None] * max
        self.front = -1
        self.rear = -1
    def ins(self, x):
        if (self.rear + 1) % len(self.list) == self.front:
            print('Queue is full')
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear = (self.rear + 1) % len(self.list)
        self.list[self.rear] = x
    def Delete(self):
        if self.front == -1:
            print('Queue is empty')
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)
        return k
    def is_Full(self):
        if (self.rear + 1) % len(self.list) == self.front :
            print('Your list is Full')
            return 
        print("Your queue is not full yet")
    def is_Empty(self):
        if self.front == -1:
            print('Your list is Empty')
            return 
        print("Your queue is not empty yet")


#Creating a queue with a capacity of 3
test = Queue(3)

#Inserting numbers
test.ins(10)
print(test.list)
test.ins(20)
print(test.list)
test.ins(30)
print(test.list)

#Testing if the queue is full
test.is_Full()

#Deleting an element from the queue
test.Delete()

#Testing if the queue is full
test.is_Full()

#Checking rear and front
print(test.list)
print("Front is =", test.front)
print("Rear is =", test.rear)