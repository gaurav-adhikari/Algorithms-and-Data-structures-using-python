# A basic implementation of DeQueues in python using abstract datatypes


class DeQueue:
    def __init__(self):
        self.deQueueItems=[]
    
    def addFront(self,item):
        self.deQueueItems.insert(0,item)

    def addRear(self,item):
        self.deQueueItems.insert(len(self.deQueueItems),item)
    
    # Removes the front item from the dequeue
    def removeFront(self):
        return self.deQueueItems.pop(0)
    
    # Removes the last item from the dequeue
    def removeRear(self):
        return self.deQueueItems.pop()
    
    def isEmpty(self):
        return self.deQueueItems == []
    
    def size(self):
        return len(self.deQueueItems)

    #   Returns the whole dequeue   
    def peek(self):
        return self.deQueueItems



# Main Function implementaion
def main():

    myDeQueue=DeQueue()

    print(myDeQueue.isEmpty())
    print(myDeQueue.size())

    myDeQueue.addFront('universe')
    myDeQueue.addFront('multiverse')
    myDeQueue.addRear('omniverse')
    
    print(myDeQueue.isEmpty())
    print(myDeQueue.size())
    print(myDeQueue.peek())


if __name__=="__main__":
    main()


'''
 Conclusion
            -> Explored different operations of DeQueue
            -> Will be exploring their applications next
            -> OOP is beautiful
'''