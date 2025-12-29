class node: 
    def __init__ (self, d):
        self.data = d
        self.next = None

class linked_list :
    def __init__ (self): 
        self.head = None

    def insert_first (self, x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            a.next = self.head
            self.head = a

    def insert_last (self, x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            c = self.head
            while c.next : 
                c = c.next
            c.next = a

    def insert_after (self,x ,y ):
        if self.head == None:
            print("list is empty")
            return
        else:
            c = self.head
            while c:
                if c.data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                    return
                c = c.next 
            print("not found")

    def insert_befor (self, x, y):
        if self.head == None:
            print("list is empty")
            return
        else:
            c = self.head
            if self.head.data == x:
                self.insert_first(y)
                return
            while c.next :
                if c.data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                    return
                c = c.next
            print("not found")
        
    def del_first (self):
        if self.head == None:
            print("error 0")
            return
        c = self.head
        self.head = c.next
        del c

    def del_last (self):
        if self.head == None:
            print("error 0")
            return
        if self.head.next is None:
           self.del_first()
           return
        c = self.head
        while c.next.next :
            c = c.next 
        del c.next
        c.next = None

    def del_after (self, x):
        if self.head is None:
            print("error 0")
            return
        if self.head.next is None:
            print("error 1")
            return
        c = self.head
        while c.next.next:
            if c.data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
        print("not found")

    def del_befor (self, x):
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x: 
            print("print x1")
            return
        if self.head.next is None:
            print("error 1")
            return
        if self.head.next.data == x:
            self.del_first()
            return
        if self.head.next.next is None:
            print("error 2")
            return
        c = self.head
        while c.next.next.next :
            if c.next.next.data == x:
                a= c.next
                c.next = a.next
                del a
                return
            c = c.next
        print ("not found")

    def del_x (self, x):
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x:
            self.del_first()
            return
        c = self.head
        while c.next :
            if c.next.data == x:
                a = c.next 
                c.next = a.next 
                del a
                return
            c = c.next
        print ("not found")

    def del_all (self):
        while self.head :
            self.del_first()
        
    def print_primes (self):
        c = self.head
        while c:
            n = c.data
            if n > 1:
                is_Prime = True
                for i in range (2, int(n**0.5) + 1):
                    if n % i == 0 :
                        is_Prime = False
                        break
                    if is_Prime :
                        print(n)
            c = c.next


doom = linked_list()
doom.insert_first(1)
doom.insert_last(3)
doom.insert_last(6)
doom.insert_last(8)
doom.insert_last(13)
doom.insert_last(17)
doom.insert_last(19)


doom.print_primes()

