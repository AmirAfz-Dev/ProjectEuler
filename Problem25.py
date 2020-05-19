#Amir Afzali
#Problem 25 Project Euler

#Define Fibo

def fibo(n):

    x=1
    y=0
#Set up variables and uses fibonacci
    while n > 1:
    #Use of a loop
        x, y = x+y, x
        n = n - 1
    return x

#Print Fibo(1000)


    
 
