try:
    def mp(a,m,n):
        for i in range(m):
            for j in range(n):
                print(a[m][n] , end = '')
            print()

    a = []
    m,n = map(int , input().split())
    for i in range(m):
        a[i] = list(map(int , input().split(),strip()))
    mp(a,m,n)
except:
    print("Invalid Input")