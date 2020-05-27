# Implemention of a node of Linked List


class LinkedListNode:

    def __init__(self, headData):
        self.headData = headData
        self.nextData = None

    def getHeadData(self):
        return self.headData

    def getNextData(self):
        return self.nextData

    def setNextData(self, myNewNextData):
        self.nextData = myNewNextData

    def setNewHeadData(self, myNewHeadData):
        self.headData = myNewHeadData


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        tempNode = LinkedListNode(item)
        tempNode.setNextData(self.head)
        self.head = tempNode

    def getListSize(self):
        currentNode = self.head
        nodeCount = 0

        while currentNode != None:
            nodeCount += 1
            currentNode = currentNode.getNextData()

        return nodeCount

    def isEmpty(self):
        return self.head == None

    def searchList(self, searchItem):

        currentNode = self.head
        traversalPosition = 0

        while currentNode != None:

            traversalPosition += 1

            if currentNode.getHeadData() == searchItem:
                return traversalPosition

            currentNode = currentNode.getNextData()

        return -1

    def removeNode(self, removeItem):

        currentNode = self.head
        isItemFound = False
        previousNode = None

        # Considering the fact that no two datas are repeated in a list
        while not isItemFound:

            if removeItem == currentNode.getHeadData():
                isItemFound = True

            else:
                previousNode = currentNode
                currentNode = currentNode.getNextData()

        if previousNode == None:
            self.head = currentNode.getNextData()
        else:
            previousNode.setNextData(currentNode.getNextData())


def main():

    myLinkedList = UnorderedList()

    myLinkedList.add('A')
    myLinkedList.add('B')
    myLinkedList.add('C')
    myLinkedList.add('D')
    myLinkedList.add('E')
    myLinkedList.add('F')

    assert myLinkedList.isEmpty() != None

    assert myLinkedList.getListSize() == 6

    # As new nodes gets added on the precceeding node so A is the last element
    assert myLinkedList.searchList('A') == 6
    assert myLinkedList.searchList('G') == -1

    myLinkedList.removeNode('C')
    myLinkedList.removeNode('B')

    assert myLinkedList.searchList('B') == -1
    assert myLinkedList.searchList('C') == -1

    assert myLinkedList.getListSize() == 4
    pass



if __name__ == '__main__':
    main()
