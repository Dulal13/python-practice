num = int(input('Enter your factorial number : '))

# def factorial(num):

#     product = 1
#     for i in range(1,num+1):
#         product *= i
#     return product

# print(factorial(num))

def factorial_recursive(num):
    if(num==0):
        return 1
    else:
        return num*factorial_recursive(num-1)

print(factorial_recursive(num))
