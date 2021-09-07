def calculate_losses(items):
    value = sum(list(items.values()))
    if value>0:
            return value
    else:
        return "Lucky you!"

res = calculate_losses({
 
})

print(res)

