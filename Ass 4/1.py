def mp(a,m,n):
        for i in range(m):
            for j in range(n):
                print(a[i][j] , end = ' ')
            print()
try:
    

    #m,n = map(int , input().split(' '))
    m = 5
    n = 5
    a = [[0]*n]*m
    for i in range(m):
        for j in range(n):
            a[i][j] = i*j
    mp(a,m,n)
except:
    print("Invalid Input")