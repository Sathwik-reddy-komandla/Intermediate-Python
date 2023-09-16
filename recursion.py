
# n=7
# fact=1

# while n>0:
#     fact=fact*n
#     n=n-1
#     print(fact)
# print(fact)


# def factorial(n):
#     if n<1:
#         return 1
#     else:
#         number=n*factorial(n-1)
#         return number
    

# print(factorial(77))

# def fib(n):
#     a,b=0,1
#     for x in range(n):
#         a,b=b,a+b
#     return a

# print(fib(7))

# 0,
# 1,1,2,3,5,8,13
def extraLongFactorials(n):
    # Write your code here
    print(n)
    if n<1:
        return 1
    else:
        number=n*extraLongFactorials(n-1)
        print(number)
        return number
    
print(extraLongFactorials(25))