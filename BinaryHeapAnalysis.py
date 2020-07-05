# Playing with binary heap

class BinaryHeap:

    def __init__(self):
        self.myHeapList = [0]
        self.myHeapCount = 0
    
    # compare child and the root 
    def locateUp(self, i):

        while i//2 > 0:
            if self.myHeapList[i] > self.myHeapList[i//2]:
                self.myHeapList[i], self.myHeapList[i // 2] = self.myHeapList[i//2], self.myHeapList[i]

            i = i//2

    # Insertion in heap
    def insert(self, myItem):
        self.myHeapList.append(myItem)
        self.myHeapCount += 1
        self.locateUp(self.myHeapCount)


    # Function to find the minimum child
    def minChild(self, i):

        # compare if the right child is there
        if i*2+1 > self.myHeapCount:
            return i*2  # returns the parent itself
        else:
            # compare parent and the right child
            if self.myHeapList[i*2] < self.myHeapList[i*2+1]:
                return i*2

            else:
                # return the right child
                return i*2+1


    def locateDown(self, i):
        while i*2 <= self.myHeapCount:

            # get minimum child
            myMinChildIndex = self.minChild(i)

            # compare with the root and swap them
            if self.myHeapList[i] > self.myHeapList[myMinChildIndex]:
                self.myHeapList[i], self.myHeapList[myMinChildIndex] = self.myHeapList[myMinChildIndex], self.myHeapList[i]

            i = myMinChildIndex


    def deleteMinimum(self):
        initialVal= self.myHeapList[1]

        # set the root to be the highest value
        self.myHeapList[1]=self.myHeapList[self.myHeapCount]
        self.myHeapCount-=1
        
        # Remove the last element as it is not needed
        self.myHeapList.pop()

        # locate the actual position
        self.locateDown(1)

        return initialVal


    def myHeapBuilder(self, mylist):
        
        i = len(mylist) // 2

        self.myHeapCount=len(mylist)

        # Add the 0 on the first of the list
        self.myHeapList=[0] + mylist[:] 

        # loop through elements with heap property
        while(i>0):
            self.locateDown(i)
            i-=1


def main():

    myheap=BinaryHeap()
    myheap.myHeapBuilder([9,5,6,2,3])

    assert myheap.deleteMinimum() == 2
    assert myheap.deleteMinimum() == 3 
    assert myheap.deleteMinimum() == 5
    assert myheap.deleteMinimum() == 6
    assert myheap.deleteMinimum() == 9


if __name__=='__main__':
    main()


'''
Conclusion
            -> the complexity is shorter than O(logn)
            -> the smallest element is always on the root node
            -> trees are awesome
            -> OOPS is very beautiful 
'''
