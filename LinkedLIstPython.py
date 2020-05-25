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



def main():
    mylist = LinkedListNode('A')
    mylist.setNextData('B')
    print(mylist.getHeadData())
    print(mylist.getNextData())
    pass

if __name__ == '__main__':
    main()
