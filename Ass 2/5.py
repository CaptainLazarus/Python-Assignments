try:
    def f(n):
        if n == 0:
            return 0
        f(n-1)
        print(3*n)
    
    n = 5
    f(n)
except:
    print("Invalid")