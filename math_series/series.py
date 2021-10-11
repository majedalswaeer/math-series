
def fibonacci(n: int):
    """
    for number 0 return the(n)th value which is 0
    for number 1 return the(n)th value which is 1
    for other nums will return the sum of the two numbers that precede it
    """
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def lucas(n: int):
    """
    for number 0 return the (n)th value which is 1 a lucas number
    for number 1 return the (n)th value which is 2 a lucas number
    for other nums will return the sum of the two numbers that precede it
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(x,*args):
    return fibonacci(x)+lucas(x)




if __name__=='__main__':
    n=int(input('enter a number > '))
    print(fibonacci(n))
    print(lucas(n))
