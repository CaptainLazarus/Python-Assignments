def recurSum(n): 
    if n <= 1: 
        return n 
    return n + recurSum(n - 1) 

n = 6
print(recurSum(n)) 