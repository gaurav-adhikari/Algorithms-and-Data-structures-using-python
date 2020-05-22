# A basic implementation of Queues in python using abstract datatype


# Creating basic Stack Operations from python lists
class Queue:
    def __init__(self):
        self.queueItems=[]
    
    def isEmpty(self):
        if len(self.queueItems)==0:
            return True
        else:
            return False
    
    def enqueue(self,item):
        self.queueItems.insert(0,item)
    
    def deque(self):
        return self.queueItems.pop()

    def size(self):
        return len(self.queueItems)

    # Returns the first elements but doesnt remove it
    def front(self):
        return self.queueItems[0]


def main():
     myQueue=Queue()

     print(myQueue.isEmpty())
     print(myQueue.size())
     myQueue.enqueue('worm holes')
     myQueue.enqueue('blackholes')
     print(myQueue.front())
     print(myQueue.deque())
     print(myQueue.deque())
     print(myQueue.isEmpty())


if __name__=="__main__":
    main()


'''
 Conclusion
            -> Explored different operations of Queue
            -> OOP is beautiful
'''

