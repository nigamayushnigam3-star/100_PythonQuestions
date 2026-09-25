#  Palindrome -->> 

#  first logic 

n = int(input("Enter the number: "))

original = n
result = 0

while n > 0:
    ld = n % 10
    result = (result * 10) + ld
    n = n // 10

if original == result:
    print("Yes, palindrome number")
else:
    print("No, not a palindrome number")
                                                                                     
# Second logic 

num = 121
n = num 
result = 0 
while n > 0 :
    ld = n % 10 
    result = (result*10)+ld
    n = n // 10  
n = num 
if n == result :
       print(f" Yes  palindrome number") 
else :
       print(f" No   palindrome number ") 