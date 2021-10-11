
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
    if n<0:
        return("Enter a value more than zero")
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n,x=0,y=1):
    """
    inputs for this function are three, one is required which is n and (x,y) which are optional
    if x=1 and y=2, it will return the n(th) value of fibonacci
    if x=2 and y=1, it will return the n(th) value of lucas
    if other values for the optional parameters, it will produce other series
    """
    if n<0:
        print('Enter a value more than zero')
    if x==0 and y==1:
        return fibonacci(n)
    if x==2 and y==1:
        return lucas(n)
    if not x==0 or x==2:
        return x
    if not y==1:
        return y

    return(sum_series(n-1,x,y)+sum_series(n-2,x,y))
    
    




if __name__=='__main__':
    n=int(input('enter a number > '))
    print("fibonacci value >",fibonacci(n))
    print("lucas value >",lucas(n))
    a=int(input('enter the first optional argument > '))
    b=int(input('enter the second optional argument > '))
    print(sum_series(n,a,b))
