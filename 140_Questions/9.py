#  Factorial of a number 

n = int(input("Enter the number ")) 
factorial = 1 
if n < 0 :
    print("Factorial is not exist for negative numbers ")  
elif n == 0 and n == 1:
    print(f"Factorial of  {n} will be 1  ")
else :
    for i in range(1,n+1):
        factorial = factorial * i 
    print(f"factorial of {n} will be {factorial }") 



