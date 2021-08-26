n = int(input('Enter the num : '))

def sum_of_Natural(n):
    if(n==1):
        return 1
    else:
        return n+sum_of_Natural(n-1)

a = sum_of_Natural(n)
print(f"sum of first {n} numbers is : {a}")