#Amir Afzali
#Project Euler Problem 1


#Find the sum of all the multiples of 3 or 5 below 1000
#the Sum function should help with this
#Establish the Range 

x = sum(i for i in range(1000) if i % 3 == 0 or i % 5 ==0)
#Checks if it's divisible by 3 or 5 then takes the sum (If it's divisible by 3 there would be no remainder thats why it's equal to 0 and same with 5)

print(x)

#print statement


