#Amir Afzali
#Project Euler problem 48

def selfpowers():
#Define Self Powers
    total = 0
    for i in range(1, n + 1):
    #Use of for loop to find last 10 digits, might not be the most efficient way of doing things but atleast it works
        total += i ** i
    return str(total)[-10:]   
#Finds the last 10 digits of a given series