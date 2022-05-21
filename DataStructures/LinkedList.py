''' 
Creating node like below 
{
    "value":5,
    "node":None
}
'''
class node:
    def __init__(self,value):
        self.value=value
        self.next=None

''' 
Creating linkedlist like below 
head/tail={
    "value":5,
    "node":None
}
'''
class LinkedList:
    def __init__(self,value):
        Node = node(value)
        self.head=Node
        self.tail=Node
        self.length=1

    def append(self,value):
        Node=node(value)
        if(self.length==0):
            self.head=Node
            self.tail=Node
            self.length=1
        else:
            print("inside")
            self.tail.next=Node
            self.tail=Node
        self.length=self.length+1
        return True

    def prepend(self,value):
        NewNode=node(value)
        if(self.length==0):
            self.head=Node
            self.tail=Node
        else:
            NewNode.next=self.head
            self.head=NewNode
        self.length=self.length+1
        return True

        


    def print_all(self):
        allNodes=self.head
        while allNodes is not None:
            print(allNodes.value)
            allNodes=allNodes.next

    def pop(self):
        if(self.length==0):
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length=self.length-1
        if(self.length==0):
            self.head=None
            self.tail=None
        return temp

    def popFirst(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            temp=self.head.next=None
            self.head=None
            self.tail=None
            return temp
        else:
            temp=self.head.next
            self.head=temp
            temp.next=None#this is for just to return no use
            self.length=self.length-1
            return temp

    def getValue(self,index):
        count=self.length
        temp=self.head
        if(count>=0 and index<=count):
            for _ in range(index):
                temp=temp.next
        return temp

    def setValue(self,index,value):
        count=self.length
        if(count>=0 and index<=count):
            tempvalue=self.getValue(index)
            tempvalue.value=value
            return True
        else:
            return False

    def insert(self,index,value):
        if(index<0 or index>self.length+1):
            return False
        else if(index==0):
            self.prepend(value)
        else if(index==self.length+1):
            self.append(value)
        else:
            NewNode=node(value)
            idxBefore=self.getValue(index-1)
            idxBefore.next=NewNode
            NewNode.next=idxBefore.next
        self.length=self.length+1
        return True
           




            
                    







    
            

linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.prepend(4)
linked_list.print_all()
#linked_list.popFirst()
#linked_list.pop()
#print(linked_list.head.value)
print("get Value-->",linked_list.getValue(0))
linked_list.setValue(0,3)
linked_list.print_all()
