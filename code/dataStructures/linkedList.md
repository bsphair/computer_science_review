# Linked Lists

```python
class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        newNode = Node(data)
        
        if self.head:
            currentNode = self.head
            while currentNode.nextNode:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode
        else:
            self.head = newNode

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.nextNode

newList = LinkedList()
newList.add_node(1)
newList.add_node(2)

newList.printList()




```
