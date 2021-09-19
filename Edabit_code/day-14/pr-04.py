def dis(price, discount):
    after_discount = round(price-((price*discount)/100) , 2)
    return after_discount

res  = dis(1693,80)
print(res)