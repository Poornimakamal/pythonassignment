def factorial(n):
 fact=1
 for i in range(1,n+1):
  fact=fact*i
n=int(input("enter the no"))
print("factorial of n integer is",factorial(n))