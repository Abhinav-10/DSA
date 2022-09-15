# WAP to reverse a linked list 

from dataclasses import dataclass


class Nodes :
    def __init__(self, data) -> None:
        self.data = data
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


    def reverseLL(self):
        ## Reversing a linked List 

        # iterative approach
        # time comnplexity = O(n)
        # space complexity = O(1)

        prev = None
        curr = self.head

        while curr != None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        self.head = prev

    def getlength(self):
        temp = self.head
        lenll = 0
        while temp:
            lenll+=1
            temp = temp.next
        return lenll

    def middle(self):

        ### Middle of linked List 

        # Approach 1:  traverse linked list and the length of linked list 
        # mid  = Len/2 +1
        # temp =  head 

        len=self.getlength()
        mid = len/2
        cnt = 0
        temp = self.head
        while cnt<mid:
            temp = temp.next
            cnt+=1

        print("Middle element ===>", temp.data)


    def middle2(self):
        if not self.head:
            print("No element")
        if self.head == None:
            print(self.head.data)

        second = self.head
        first = self.head.next

        while first != None:
            first = first.next
            if first:
                first = first.next
            
            second = second.next
        print("Middle element  is ", second.data)

# 10 20 30 40 
L1 =  LinkedList()
L1.insertAtHead(10)
L1.insertAtend(20)
L1.insertAtend(30)
L1.insertAtend(40)

print("Original Linked List ")
L1.printlist()

L1.reverseLL()

print("Reversed Linked List ")
L1.printlist()

# Middle of LL

L1.middle()
L1.middle2()