

class LinkedListCell():

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    
    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def get_data(self):
        return self.data


class LinkedList():

    def __init__(self):
        self.tail = None
        self.head = None


    def add_first(self,data):
        if self.head == None and self.tail == None:
            self.head = LinkedListCell(data)
            self.tail = self.head
        else:
            tmp = self.head
            self.head = LinkedListCell(data)
            self.head.next = tmp
            tmp.previous = self.head

    def add_last(self,data):
        if self.tail == None and self.head == None:
            self.add_first(data)
        else:
            tmp = self.tail
            self.tail = LinkedListCell(data)
            self.tail.previous = tmp
            tmp.next = self.tail

    def remove_first(self):
        if self.head == None and self.tail == None:
            return None
        elif self.tail == self.head:
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp
        else:
            tmp = self.head
            self.head = tmp.next
            self.head.previous = None
            tmp.next = None
            return tmp

    def remove(self,data):
        if self.head.data == data:
            return self.remove_first()
        else:
            tmp = self.head.next
            while tmp != None:
                if tmp.data == data and tmp != self.tail:
                    tmp.previous.next = tmp.next
                    tmp.next.previous = tmp.previous
                    tmp.previous = None
                    tmp.next = None
                    return tmp 
                elif tmp.data == data and tmp == self.tail:
                    tmp.previous.next = tmp.next
                    self.tail = tmp.previous
                    tmp.previous = None
                    return tmp
                tmp = tmp.next
            return None
            
