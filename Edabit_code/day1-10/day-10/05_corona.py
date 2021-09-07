import math
def end_corona(recovers, new_cases, active_cases):
    
    case = recovers - new_cases
    return math.ceil(active_cases/case)
      
res = end_corona(4000, 2000, 77000) 
print(res)