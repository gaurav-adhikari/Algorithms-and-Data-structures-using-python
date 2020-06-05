# Implentation of prime number in python

# 1st approach
# O(n)
def primeChecker1(a):

    if a>1:
        prime = True

        for i in range(2,a):
            if a%i==0:
                prime=False
                return prime 

        return prime

# Abit optimised approach to check prime
def primeChecker2(a):

    isPrime=True

    if a<=1:
        isPrime=False
        return isPrime

    if a<=3:
        isPrime=False
        return isPrime

    if a%2==0 and a%3==0:
        isPrime= False
        return isPrime
    
    return primeChecker1(a)


def main():

    assert primeChecker1(11)== True

    assert primeChecker1(10)== False

    assert primeChecker2(11)== True

    assert primeChecker2(10)== False


if __name__=='__main__':
    main()

'''
 Conclusion
            -> with some small tweaks in code, we an make the same algorithm alot efficient
'''
