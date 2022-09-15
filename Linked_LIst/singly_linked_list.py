class Nodes:

    def __init__(self, data):
        self.data=data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head=None 
    
    

    def insertAtHead(self, new_data):
        new_node = Nodes(new_data)
         
        new_node.next = self.head
        self.head = new_node


    def insertAtend(self, new_data):
        new_node = Nodes(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last =last.next
        last.next = new_node

    def insertafter(self, prevnode, new_data):
        if prevnode is None:
            print("The given node does not exist")
            return

        new_node = Nodes(new_data)

        new_node.next = prevnode.next
        prevnode.next = new_node
    

    def insertAtPosition(self, position, new_data):
        new_node = Nodes(new_data)
        cnt =1
        temp = self.head
        if position == 1:
            self.insertAtHead(new_data)
            return
        while cnt<position-1:
            temp =temp.next
            cnt+=1
        new_node.next = temp.next
        temp.next = new_node

    

    def deletnode(self, position):
        cnt = 1
        curr =self.head
        prev = None
        if position == 1:
            self.head = self.head.next
        else:
            while cnt<position:
                prev = curr
                curr = curr.next
                cnt+=1
            prev.next = curr.next


    def printlist(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList() 

llist.head = Nodes(10)
second = Nodes(20)
third = Nodes(30)


llist.head.next = second
second.next = third

# llist.insertAtHead(112)
# llist.insertAtend(444)
# llist.insertafter(llist.head.next, 8)
# llist.insertAtPosition(1, 227)
print("Before")
llist.printlist()
print("After")
llist.deletnode(2)
llist.printlist()
