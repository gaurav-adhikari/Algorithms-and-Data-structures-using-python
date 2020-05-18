# Here, we will be implementing a function to find a minumum number from the list

from random import randrange
import time

# Approach1
def minimumFinder1(inputList):
    globalMinimum=inputList[0]
    
    for x in inputList:
        if globalMinimum>x:
            globalMinimum=x
    
    return globalMinimum


# Testing the minimum finder on hardcoded list
# print("The minimum is ",minimumFinder([234,24,4556,1000]))


# Testing the mimum finder on large lists

for listSize in range(1000,10001,1000):
    
    testList=[randrange(100000) for x in range(listSize)]
    
    tic=time.time()
    print(minimumFinder1(testList))
    toc=time.time()

    print("The size of the list is %d and time taken is  %f"%(listSize,(toc-tic)*1000))



'''
 Conclusion
            -> This min finding algorithm finishes in Linear time and the complexity is O(n)
            -> As the list size (n) grows, it takes more time as the algorithm iterates over n

'''