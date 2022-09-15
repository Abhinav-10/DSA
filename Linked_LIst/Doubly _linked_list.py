class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None 
    


    def insertAtHead(self, newdata):
        new_node = Node(newdata)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head=new_node
    

    def insertAtposition(self, position, data):
        if position == 1:
           self.insertAtHead(data)
           return
        
        new_node = Node(data)
        cnt =1
        temp = self.head
        while cnt<position-1:
            temp =temp.next
            cnt+=1
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
    


    def getlength(self):
        temp = self.head
        cnt=0
        while(temp):
            cnt+=1
            temp = temp.next
            return cnt


    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



dlist = DoublyLinkedList()

n1 = Node(10)
dlist.head = n1
dlist.insertAtHead(20)
dlist.insertAtposition(3, 220)
dlist.printlist()