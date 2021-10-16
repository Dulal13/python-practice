def maximum(num1,num2,num3):
    
    if(num1>num2 and num1>num3):
        return num1
    elif num2>num3:
        return num2
    else:
        return num3

p = maximum(23,145,67)
print(f"The maximum value is {p}")