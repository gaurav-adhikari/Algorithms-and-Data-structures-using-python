# Implementation of binary searching techniques in python


# running time O(logn)
def binarySearch(mylist, searchItem):
    itemFoundBoolean = False
    firstItemCount = 0
    lastItemCount = len(mylist)-1

    while not itemFoundBoolean and firstItemCount<=lastItemCount:

        midPointIndex =(firstItemCount+lastItemCount)//2  # floor division because indexes must be in integers

        if mylist[midPointIndex] == searchItem: 
            itemFoundBoolean = True 

        if mylist[midPointIndex] < searchItem:
            firstItemCount=midPointIndex+1
        else:
            lastItemCount=midPointIndex-1
    
    if itemFoundBoolean:
         return 1 
    else:
        return -1


def main():
    a=[3,10,15,27,74,79,100]
    
    assert binarySearch(a,74) == 1
    assert binarySearch(a,25) == -1
    pass

if __name__=='__main__':
    main()

'''
 Conclusion
            -> Divide and conquer works like a charm
            
'''